# NI DOCUMENT BUNDLE: ni-daqmx-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-labview-api-ref start=1251 end=1500 -->
<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1645.html language=enus -->
## TOPIC 01251: Triggers:Advance Trigger:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1645.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1645.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Advance Trigger. Remarks The following table lists the characteristics of this property. Short Name AdvTrig.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time En

### Triggers:Advance Trigger:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Advance Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvTrig.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1646.html language=enus -->
## TOPIC 01252: Triggers:Advance Trigger:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1646.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1646.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the polarity of the exported Advance Trigger. Remarks The following table lists the characteristics of this property. Short Name AdvTrig.Pulse.Polarity Data type ci32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Triggers:Advance Trigger:Pulse:Polarity

Indicates the polarity of the exported Advance Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvTrig.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1647.html language=enus -->
## TOPIC 01253: Triggers:Advance Trigger:Pulse:Width Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1647.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1647.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AdvTrig.Pulse.Width . Remarks The following table lists the characteristics of this property. Short Name AdvTrig.Pulse.WidthUnits Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Seconds

### Triggers:Advance Trigger:Pulse:Width Units

Specifies the units of 
 [AdvTrig.Pulse.Width](/csh?context=nidaqmx_daqmxprop_attr1648)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvTrig.Pulse.WidthUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Seconds | 10364 | Seconds. |
| --- | --- | --- |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1648.html language=enus -->
## TOPIC 01254: Triggers:Advance Trigger:Pulse:Width Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1648.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1648.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with AdvTrig.Pulse.WidthUnits . Remarks The following table lists the characteristics of this property. Short Name AdvTrig.Pulse.Width Data type cdbl.png Permissions Read/Write Resettable True Setta

### Triggers:Advance Trigger:Pulse:Width Value

Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with 
 [AdvTrig.Pulse.WidthUnits](/csh?context=nidaqmx_daqmxprop_attr1647)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvTrig.Pulse.Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1651.html language=enus -->
## TOPIC 01255: Events:Advance Complete Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1651.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1651.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Advance Complete Event. Remarks The following table lists the characteristics of this property. Short Name AdvCmpltEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available i

### Events:Advance Complete Event:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Advance Complete Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvCmpltEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1652.html language=enus -->
## TOPIC 01256: Events:Advance Complete Event:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1652.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1652.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Advance Complete Event. Remarks The following table lists the characteristics of this property. Short Name AdvCmpltEvent.Pulse.Polarity Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### Events:Advance Complete Event:Pulse:Polarity

Specifies the polarity of the exported Advance Complete Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvCmpltEvent.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1654.html language=enus -->
## TOPIC 01257: Events:Advance Complete Event:Pulse:Width Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1654.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1654.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the exported Advance Complete Event pulse. Remarks The following table lists the characteristics of this property. Short Name AdvCmpltEvent.Pulse.Width Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Tim

### Events:Advance Complete Event:Pulse:Width Value

Specifies the width of the exported Advance Complete Event pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvCmpltEvent.Pulse.Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1657.html language=enus -->
## TOPIC 01258: Clocks:20MHz Timebase:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1657.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1657.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the 20MHz Timebase. Remarks The following table lists the characteristics of this property. Short Name 20MHzTimebase.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Ti

### Clocks:20MHz Timebase:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the 20MHz Timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 20MHzTimebase.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1663.html language=enus -->
## TOPIC 01259: Clocks:Sample Clock:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1663.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1663.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Sample Clock. Remarks The following table lists the characteristics of this property. Short Name SampClk.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engin

### Clocks:Sample Clock:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Sample Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1664.html language=enus -->
## TOPIC 01260: Clocks:Sample Clock:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1664.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1664.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Sample Clock if SampClk.OutputBehavior is Pulse. Remarks The following table lists the characteristics of this property. Short Name SampClk.Pulse.Polarity Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific A

### Clocks:Sample Clock:Pulse:Polarity

Specifies the polarity of the exported Sample Clock if 
 [SampClk.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr186b)
 is Pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1687.html language=enus -->
## TOPIC 01261: Clocks:AI Convert Clock:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1687.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1687.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the AI Convert Clock. Remarks The following table lists the characteristics of this property. Short Name AIConvClk.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### Clocks:AI Convert Clock:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the AI Convert Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConvClk.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1688.html language=enus -->
## TOPIC 01262: Clocks:AI Convert Clock:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1688.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1688.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock. Remarks The following table lists the characteristics of this property. Short Name AIConvClk.Pulse.Polarity Data type ci32.png Permissions Read Onl

### Clocks:AI Convert Clock:Pulse:Polarity

Indicates the polarity of the exported AI Convert Clock. The polarity is fixed and independent of the active edge of the source of the AI Convert Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIConvClk.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1717.html language=enus -->
## TOPIC 01263: Events:Counter Output Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1717.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1717.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Counter Output Event. Remarks The following table lists the characteristics of this property. Short Name CtrOutEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Ru

### Events:Counter Output Event:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Counter Output Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CtrOutEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1718.html language=enus -->
## TOPIC 01264: Events:Counter Output Event:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1718.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1718.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the pulses at the output terminal of the counter when CtrOutEvent.OutputBehavior is Pulse. NI-DAQmx ignores this property if CtrOutEvent.OutputBehavior is Toggle. Remarks The following table lists the characteristics of this property. Short Name CtrOutEvent.Pulse.Polarity D

### Events:Counter Output Event:Pulse:Polarity

Specifies the polarity of the pulses at the output terminal of the counter when 
 [CtrOutEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr174f)
 is Pulse. NI-DAQmx ignores this property if 
 [CtrOutEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr174f)
 is Toggle.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CtrOutEvent.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr174f.html language=enus -->
## TOPIC 01265: Events:Counter Output Event:Output Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr174f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr174f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count. Upon reaching terminal count, the counter can issue a pulse. Use CtrOutEvent.Pulse.Polarity to select a high or low pulse. Upon reaching terminal count, the outp

### Events:Counter Output Event:Output Behavior

Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.

Upon reaching terminal count, the counter can issue a pulse. Use 
 [CtrOutEvent.Pulse.Polarity](/csh?context=nidaqmx_daqmxprop_attr1718)
 to select a high or low pulse.

Upon reaching terminal count, the output terminal of the counter can change state, or toggle. For example, if the terminal is initially at a low state, 
it changes to high state and stays at the high state until the next terminal count. The terminal then changes to low state. Use 
 [CtrOutEvent.Toggle.IdleState](/csh?context=nidaqmx_daqmxprop_attr186a)
 to select the initial state of the terminal.

When counting up, a counter reaches terminal count when it reaches the maximum value (2^24 - 1 for a 24-bit counter). When counting 
down, a counter reaches terminal count when it reaches 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CtrOutEvent.OutputBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Pulse | 10265 | Send a pulse to the terminal. |
| --- | --- | --- |
| Toggle | 10307 | Toggle the state of the terminal from low to high or from high to low. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1751.html language=enus -->
## TOPIC 01266: Events:Ready For Start Event:Level:Active Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1751.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1751.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Ready for Start Event. Remarks The following table lists the characteristics of this property. Short Name RdyForStartEvent.Lvl.ActiveLvl Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Ti

### Events:Ready For Start Event:Level:Active Level

Specifies the polarity of the exported Ready for Start Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RdyForStartEvent.Lvl.ActiveLvl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr1757.html language=enus -->
## TOPIC 01267: Events:Advance Complete Event:Delay Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr1757.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr1757.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output signal delay in periods of the sample clock. Remarks The following table lists the characteristics of this property. Short Name AdvCmpltEvent.Delay Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engi

### Events:Advance Complete Event:Delay Value

Specifies the output signal delay in periods of the sample clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AdvCmpltEvent.Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr186a.html language=enus -->
## TOPIC 01268: Events:Counter Output Event:Toggle:Idle State

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr186a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr186a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the output terminal of the counter when CtrOutEvent.OutputBehavior is Toggle. The terminal enters this state when NI-DAQmx commits the task. The initial state of the terminal affects whether the first toggle is from low state to high state or from high state to low sta

### Events:Counter Output Event:Toggle:Idle State

Specifies the initial state of the output terminal of the counter when 
 [CtrOutEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr174f)
 is Toggle. The terminal enters this state when NI-DAQmx 
 [commits](/csh?context=nidaqmx_mxcncpts_committedstate)
 the task.

The initial state of the terminal affects whether the first toggle is from low state to high state or from high state to low state.

NI-DAQmx ignores this property if 
 [CtrOutEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr174f)
 is Pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CtrOutEvent.Toggle.IdleState |
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

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr186b.html language=enus -->
## TOPIC 01269: Clocks:Sample Clock:Output Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr186b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr186b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample. E Series devices might require many AI Convert Clock pulses to acquire one sample. Each pulse of the Sample Clock initiates the acquisition of one sample

### Clocks:Sample Clock:Output Behavior

Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample.

E Series devices might require many AI Convert Clock pulses to acquire one sample. Each pulse of the Sample Clock initiates the acquisition of one 
sample per channel in the task. Each sample per channel requires a pulse from the AI Convert Clock.

This property is valid for the AI Sample Clock only.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.OutputBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Pulse | 10265 | The exported Sample Clock pulses at the beginning of each sample. |
| --- | --- | --- |
| Level | 10210 | The exported Sample Clock goes high at the beginning of the sample and goes low when the last AI Convert begins. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr18ed.html language=enus -->
## TOPIC 01270: Events:AI Hold Complete Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr18ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr18ed.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the AI Hold Complete Event. Remarks The following table lists the characteristics of this property. Short Name AIHoldCmpltEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availabl

### Events:AI Hold Complete Event:Output Terminal

Specifies the terminal to which to route the AI Hold Complete Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIHoldCmpltEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr18ee.html language=enus -->
## TOPIC 01271: Events:AI Hold Complete Event:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr18ee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr18ee.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of an exported AI Hold Complete Event pulse. Remarks The following table lists the characteristics of this property. Short Name AIHoldCmpltEvent.Pulse.Polarity Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Events:AI Hold Complete Event:Pulse:Polarity

Specifies the polarity of an exported AI Hold Complete Event pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AIHoldCmpltEvent.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr18f9.html language=enus -->
## TOPIC 01272: Clocks:Sample Clock Timebase:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr18f9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr18f9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Sample Clock Timebase. Remarks The following table lists the characteristics of this property. Short Name SampClkTimebase.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available

### Clocks:Sample Clock Timebase:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Sample Clock Timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClkTimebase.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr2197.html language=enus -->
## TOPIC 01273: Events:Change Detection Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr2197.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr2197.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Change Detection Event. Remarks The following table lists the characteristics of this property. Short Name ChangeDetectEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Events:Change Detection Event:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Change Detection Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ChangeDetectEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr21a1.html language=enus -->
## TOPIC 01274: Clocks:Divided Sample Clock Timebase:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr21a1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr21a1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Divided Sample Clock Timebase. Remarks The following table lists the characteristics of this property. Short Name DividedSampClkTimebase.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-spec

### Clocks:Divided Sample Clock Timebase:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Divided Sample Clock Timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DividedSampClkTimebase.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr21aa.html language=enus -->
## TOPIC 01275: Events:Watchdog Timer Expired Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr21aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr21aa.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Watchdog Timer Expired Event. Remarks The following table lists the characteristics of this property. Short Name WatchdogExpiredEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specifi

### Events:Watchdog Timer Expired Event:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Watchdog Timer Expired Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WatchdogExpiredEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr21c4.html language=enus -->
## TOPIC 01276: Clocks:Sample Clock:Delay Offset

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr21c4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr21c4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to offset the exported Sample clock. Refer to timing diagrams for generation applications in the device documentation for more information about this value. Remarks The following table lists the characteristics of this property. Short Name SampClk.DelayOffset

### Clocks:Sample Clock:Delay Offset

Specifies in seconds the amount of time to offset the exported Sample clock. Refer to timing diagrams for generation applications in the device documentation for more information about this value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.DelayOffset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr223c.html language=enus -->
## TOPIC 01277: Events:Synchronization Pulse Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr223c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr223c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Synchronization Pulse Event. Remarks The following table lists the characteristics of this property. Short Name SyncPulseEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Avail

### Events:Synchronization Pulse Event:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Synchronization Pulse Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SyncPulseEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr226e.html language=enus -->
## TOPIC 01278: Clocks:10MHz Reference Clock:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr226e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr226e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the 10MHz Clock. Remarks The following table lists the characteristics of this property. Short Name 10MHzRefClk.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time En

### Clocks:10MHz Reference Clock:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the 10MHz Clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 10MHzRefClk.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22b5.html language=enus -->
## TOPIC 01279: Events:Ready For Transfer Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22b5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22b5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Ready for Transfer Event. Remarks The following table lists the characteristics of this property. Short Name RdyForXferEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Availab

### Events:Ready For Transfer Event:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Ready for Transfer Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RdyForXferEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22b6.html language=enus -->
## TOPIC 01280: Events:Ready For Transfer Event:Level:Active Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22b6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22b6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active level of the exported Ready for Transfer Event. Remarks The following table lists the characteristics of this property. Short Name RdyForXferEvent.Lvl.ActiveLvl Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in

### Events:Ready For Transfer Event:Level:Active Level

Specifies the active level of the exported Ready for Transfer Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RdyForXferEvent.Lvl.ActiveLvl |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22ba.html language=enus -->
## TOPIC 01281: Events:Handshake Event:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22ba.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22ba.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Handshake Event. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### Events:Handshake Event:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Handshake Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bb.html language=enus -->
## TOPIC 01282: Events:Handshake Event:Output Behavior

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output behavior of the Handshake Event. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.OutputBehavior Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Events:Handshake Event:Output Behavior

Specifies the output behavior of the Handshake Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.OutputBehavior |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Interlocked | 12549 | Handshake Event deasserts after the Handshake Trigger asserts, plus the amount of time specified with HshkEvent.Interlocked.DeassertDelay . |
| --- | --- | --- |
| Pulse | 10265 | Handshake Event pulses with the pulse width specified in HshkEvent.Pulse.Width . |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bc.html language=enus -->
## TOPIC 01283: Events:Handshake Event:Delay Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of seconds to delay after the Handshake Trigger deasserts before asserting the Handshake Event. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.Delay Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Run

### Events:Handshake Event:Delay Value

Specifies the number of seconds to delay after the Handshake Trigger deasserts before asserting the Handshake Event.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.Delay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bd.html language=enus -->
## TOPIC 01284: Events:Handshake Event:Interlocked:Asserted Level

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the asserted level of the exported Handshake Event if HshkEvent.OutputBehavior is Interlocked. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.Interlocked.AssertedLvl Data type ci32.png Permissions Read/Write Resettable True Settable While Task

### Events:Handshake Event:Interlocked:Asserted Level

Specifies the asserted level of the exported Handshake Event if 
 [HshkEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr22bb)
 is Interlocked.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.Interlocked.AssertedLvl |
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

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22be.html language=enus -->
## TOPIC 01285: Events:Handshake Event:Interlocked:Assert on Start

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22be.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22be.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to assert the Handshake Event when the task starts if HshkEvent.OutputBehavior is Interlocked. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.Interlocked.AssertOnStart Data type cbool.png Permissions Read/Write Resettable True Settable While Ta

### Events:Handshake Event:Interlocked:Assert on Start

Specifies to assert the Handshake Event when the task starts if 
 [HshkEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr22bb)
 is Interlocked.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.Interlocked.AssertOnStart |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bf.html language=enus -->
## TOPIC 01286: Events:Handshake Event:Interlocked:Deassert Delay Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22bf.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to wait after the Handshake Trigger asserts before deasserting the Handshake Event if HshkEvent.OutputBehavior is Interlocked. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.Interlocked.DeassertDelay Data type cdbl

### Events:Handshake Event:Interlocked:Deassert Delay Value

Specifies in seconds the amount of time to wait after the Handshake Trigger asserts before deasserting the Handshake Event if 
 [HshkEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr22bb)
 is Interlocked.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.Interlocked.DeassertDelay |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22c0.html language=enus -->
## TOPIC 01287: Events:Handshake Event:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22c0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22c0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Handshake Event if HshkEvent.OutputBehavior is Pulse. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.Pulse.Polarity Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-spe

### Events:Handshake Event:Pulse:Polarity

Specifies the polarity of the exported Handshake Event if 
 [HshkEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr22bb)
 is Pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr22c1.html language=enus -->
## TOPIC 01288: Events:Handshake Event:Pulse:Width Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr22c1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr22c1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the pulse width of the exported Handshake Event if HshkEvent.OutputBehavior is Pulse. Remarks The following table lists the characteristics of this property. Short Name HshkEvent.Pulse.Width Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running

### Events:Handshake Event:Pulse:Width Value

Specifies in seconds the pulse width of the exported Handshake Event if 
 [HshkEvent.OutputBehavior](/csh?context=nidaqmx_daqmxprop_attr22bb)
 is Pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | HshkEvent.Pulse.Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr2303.html language=enus -->
## TOPIC 01289: Events:Change Detection Event:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr2303.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr2303.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of an exported Change Detection Event pulse. Remarks The following table lists the characteristics of this property. Short Name ChangeDetectEvent.Pulse.Polarity Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available i

### Events:Change Detection Event:Pulse:Polarity

Specifies the polarity of an exported Change Detection Event pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ChangeDetectEvent.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr2963.html language=enus -->
## TOPIC 01290: Events:Ready For Transfer Event:Deassert Condition

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr2963.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr2963.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies when the ready for transfer event deasserts. Remarks The following table lists the characteristics of this property. Short Name RdyForXferEvent.DeassertCond Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine

### Events:Ready For Transfer Event:Deassert Condition

Specifies when the ready for transfer event deasserts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RdyForXferEvent.DeassertCond |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Onboard Memory More than Half Full | 10237 | Deassert the signal when more than half of the onboard memory of the device fills. |
| --- | --- | --- |
| Onboard Memory Full | 10236 | Deassert the signal when the onboard memory fills. |
| Onboard Memory Custom Threshold | 12577 | Deassert the signal when the amount of space available in the onboard memory is below the value specified with RdyForXferEvent.DeassertCondCustomThreshold . |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr2964.html language=enus -->
## TOPIC 01291: Events:Ready For Transfer Event:Deassert Condition Custom Threshold

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr2964.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr2964.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in samples the threshold below which the Ready for Transfer Event deasserts. This threshold is an amount of space available in the onboard memory of the device. RdyForXferEvent.DeassertCond must be Onboard Memory Custom Threshold to use a custom threshold. Remarks The following table lists

### Events:Ready For Transfer Event:Deassert Condition Custom Threshold

Specifies in samples the threshold below which the Ready for Transfer Event deasserts. This threshold is an amount of space available in the onboard memory of the device. 
 [RdyForXferEvent.DeassertCond](/csh?context=nidaqmx_daqmxprop_attr2963)
 must be Onboard Memory Custom Threshold to use a custom threshold.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RdyForXferEvent.DeassertCondCustomThreshold |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr584.html language=enus -->
## TOPIC 01292: Triggers:Start Trigger:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr584.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr584.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Start Trigger. Remarks The following table lists the characteristics of this property. Short Name StartTrig.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time En

### Triggers:Start Trigger:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Start Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | StartTrig.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr585.html language=enus -->
## TOPIC 01293: Triggers:Start Trigger:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr585.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr585.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Start Trigger. Remarks The following table lists the characteristics of this property. Short Name StartTrig.Pulse.Polarity Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True

### Triggers:Start Trigger:Pulse:Polarity

Specifies the polarity of the exported Start Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | StartTrig.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr590.html language=enus -->
## TOPIC 01294: Triggers:Reference Trigger:Output Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr590.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr590.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which to route the Reference Trigger. Remarks The following table lists the characteristics of this property. Short Name RefTrig.OutputTerm Data type cdaqmxscale.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### Triggers:Reference Trigger:Output Terminal

Specifies the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which to route the Reference Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RefTrig.OutputTerm |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-export-signal/attr591.html language=enus -->
## TOPIC 01295: Triggers:Reference Trigger:Pulse:Polarity

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-export-signal/attr591.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-export-signal/attr591.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Reference Trigger. Remarks The following table lists the characteristics of this property. Short Name RefTrig.Pulse.Polarity Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tr

### Triggers:Reference Trigger:Pulse:Polarity

Specifies the polarity of the exported Reference Trigger.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RefTrig.Pulse.Polarity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Active High | 10095 | High state is the active state. |
| --- | --- | --- |
| Active Low | 10096 | Low state is the active state. |

Parent topic:

DAQmx Export Signal Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-channel-p.html language=enus -->
## TOPIC 01296: DAQmx Persisted Channel Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-channel-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-channel-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Persisted Channel properties to query information about programmatically saved global channels.

### DAQmx Persisted Channel Properties

Use the DAQmx Persisted Channel properties to query information about programmatically saved global channels.

- [Active Channel](../../../resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22cf.html) Specifies the saved global channel to which subsequent properties apply.
- [Allow Interactive Deletion?](../../../resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d2.html) Indicates whether the global channel can be deleted through MAX.
- [Allow Interactive Editing?](../../../resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d1.html) Indicates whether the global channel can be edited in the DAQ Assistant.
- [Author](../../../resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d0.html) Indicates the author of the global channel.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22cf.html language=enus -->
## TOPIC 01297: Active Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22cf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22cf.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the saved global channel to which subsequent properties apply. Remarks The following table lists the characteristics of this property. Short Name ActiveChan Data type cgenclassrntag.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run-

### Active Channel

Specifies the saved global channel to which subsequent properties apply.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveChan |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d0.html language=enus -->
## TOPIC 01298: Author

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the author of the global channel. Remarks The following table lists the characteristics of this property. Short Name Author Data type cstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Author

Indicates the author of the global channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Author |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d1.html language=enus -->
## TOPIC 01299: Allow Interactive Editing?

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the global channel can be edited in the DAQ Assistant. Remarks The following table lists the characteristics of this property. Short Name AllowInteractiveEditing Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in R

### Allow Interactive Editing?

Indicates whether the global channel can be edited in the DAQ Assistant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AllowInteractiveEditing |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d2.html language=enus -->
## TOPIC 01300: Allow Interactive Deletion?

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-channel/attr22d2.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the global channel can be deleted through MAX. Remarks The following table lists the characteristics of this property. Short Name AllowInteractiveDeletion Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time

### Allow Interactive Deletion?

Indicates whether the global channel can be deleted through MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AllowInteractiveDeletion |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-scale-p.html language=enus -->
## TOPIC 01301: DAQmx Persisted Scale Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-scale-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-scale-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Persisted Scale properties to query information about programmatically saved custom scales.

### DAQmx Persisted Scale Properties

Use the DAQmx Persisted Scale properties to query information about programmatically saved custom scales.

- [Active Scale](../../../resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d3.html) Specifies the saved custom scale to which subsequent properties apply.
- [Allow Interactive Deletion?](../../../resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d6.html) Indicates whether the custom scale can be deleted through MAX.
- [Allow Interactive Editing?](../../../resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d5.html) Indicates whether the custom scale can be edited in the DAQ Assistant.
- [Author](../../../resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d4.html) Indicates the author of the custom scale.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d3.html language=enus -->
## TOPIC 01302: Active Scale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the saved custom scale to which subsequent properties apply. Remarks The following table lists the characteristics of this property. Short Name ActiveScale Data type cdaqmxscale.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run-Time

### Active Scale

Specifies the saved custom scale to which subsequent properties apply.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveScale |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d4.html language=enus -->
## TOPIC 01303: Author

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the author of the custom scale. Remarks The following table lists the characteristics of this property. Short Name Author Data type cstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Author

Indicates the author of the custom scale.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Author |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d5.html language=enus -->
## TOPIC 01304: Allow Interactive Editing?

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the custom scale can be edited in the DAQ Assistant. Remarks The following table lists the characteristics of this property. Short Name AllowInteractiveEditing Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run

### Allow Interactive Editing?

Indicates whether the custom scale can be edited in the DAQ Assistant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AllowInteractiveEditing |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d6.html language=enus -->
## TOPIC 01305: Allow Interactive Deletion?

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-scale/attr22d6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the custom scale can be deleted through MAX. Remarks The following table lists the characteristics of this property. Short Name AllowInteractiveDeletion Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time E

### Allow Interactive Deletion?

Indicates whether the custom scale can be deleted through MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AllowInteractiveDeletion |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-task-p.html language=enus -->
## TOPIC 01306: DAQmx Persisted Task Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-task-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-task-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Persisted Task properties to query information about programmatically saved tasks.

### DAQmx Persisted Task Properties

Use the DAQmx Persisted Task properties to query information about programmatically saved tasks.

- [Active Task](../../../resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cb.html) Specifies the saved task to which subsequent properties apply.
- [Allow Interactive Deletion?](../../../resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22ce.html) Indicates whether the task can be deleted through MAX.
- [Allow Interactive Editing?](../../../resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cd.html) Indicates whether the task can be edited in the DAQ Assistant.
- [Author](../../../resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cc.html) Indicates the author of the task.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cb.html language=enus -->
## TOPIC 01307: Active Task

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the saved task to which subsequent properties apply. Remarks The following table lists the characteristics of this property. Short Name ActiveTask Data type cgenclassrntag.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engin

### Active Task

Specifies the saved task to which subsequent properties apply.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveTask |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cc.html language=enus -->
## TOPIC 01308: Author

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the author of the task. Remarks The following table lists the characteristics of this property. Short Name Author Data type cstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Author

Indicates the author of the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Author |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cd.html language=enus -->
## TOPIC 01309: Allow Interactive Editing?

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22cd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the task can be edited in the DAQ Assistant. Remarks The following table lists the characteristics of this property. Short Name AllowInteractiveEditing Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time En

### Allow Interactive Editing?

Indicates whether the task can be edited in the DAQ Assistant.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AllowInteractiveEditing |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22ce.html language=enus -->
## TOPIC 01310: Allow Interactive Deletion?

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22ce.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-persisted-task/attr22ce.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the task can be deleted through MAX. Remarks The following table lists the characteristics of this property. Short Name AllowInteractiveDeletion Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine Tr

### Allow Interactive Deletion?

Indicates whether the task can be deleted through MAX.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AllowInteractiveDeletion |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Persisted Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel-p.html language=enus -->
## TOPIC 01311: DAQmx Physical Channel Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Physical Channel properties to query information about physical channels. Use the DAQmx Channel properties to configure virtual channels.

### DAQmx Physical Channel Properties

Use the DAQmx Physical Channel properties to query information about physical channels. Use the 
 [DAQmx Channel](/csh?context=nidaqmx_daqmxprop_daqmxchannel)
 properties to configure virtual channels.

- [Active Physical Channels](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21d9.html) Specifies the physical channel from which to retrieve properties.
- [Analog Input:Input Configuration:Input Sources](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd8.html) Indicates the list of input sources supported by the channel. Channels may support using the signal from the I/O connector or one of several calibration signals.
- [Analog Input:Input Configuration:Terminal Configurations](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2342.html) Indicates the list of terminal configurations supported by the channel.
- [Analog Input:Measurement Types](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd7.html) Indicates the measurement types supported by the channel.
- [Analog Input:Signal Conditioning:Sensor Power:Power Control:Enable](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316d.html) Specifies whether to turn on the sensor's power supply.
- [Analog Input:Signal Conditioning:Sensor Power:Power Control:Type](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316e.html) Specifies the type of power supplied to the sensor.
- [Analog Input:Signal Conditioning:Sensor Power:Power Control:Voltage](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316c.html) Specifies the voltage level for the sensor's power supply.
- [Analog Input:Signal Conditioning:Sensor Power:Status:Open Channel](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317c.html) Indicates whether there is an open channel or undercurrent condition on the channel.
- [Analog Input:Signal Conditioning:Sensor Power:Status:Overcurrent](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317d.html) Indicates whether there is an overcurrent condition on the channel.
- [Analog Input:Signal Conditioning:Sensor Power:Types](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3179.html) Indicates the types of power supplied to the sensor supported by this channel.
- [Analog Input:Signal Conditioning:Sensor Power:Voltage Range Values](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317a.html) Indicates pairs of sensor power voltage ranges supported by this channel. Each pair consists of the low value followed by the high value.
- [Analog Output:Advanced:Manual Control:Amplitude](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1f.html) Indicates the current value of the front panel amplitude control for the physical channel in volts.
- [Analog Output:Advanced:Manual Control:Enable](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1e.html) Specifies if you can control the physical channel externally via a manual control located on the device. You cannot simultaneously control a channel manually and with NI-DAQmx.
- [Analog Output:Advanced:Manual Control:Frequency](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a20.html) Indicates the current value of the front panel frequency control for the physical channel in hertz.
- [Analog Output:Advanced:Manual Control:Short Detected](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2ec3.html) Indicates whether the physical channel is currently disabled due to a short detected on the channel.
- [Analog Output:Advanced:Power Amplifier:Calibration:Gain](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3065.html) Indicates the calibrated gain of the channel.
- [Analog Output:Advanced:Power Amplifier:Calibration:Offset](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3066.html) Indicates the calibrated offset of the channel in volts.
- [Analog Output:Advanced:Power Amplifier:Channel Enable](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3062.html) Specifies whether to enable or disable a channel for amplification. This property can also be used to check if a channel is enabled.
- [Analog Output:Advanced:Power Amplifier:Overcurrent](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3064.html) Indicates if the channel detected an overcurrent condition .
- [Analog Output:Advanced:Power Amplifier:Scaling Coefficients](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3063.html) Indicates the coefficients of a polynomial equation used to scale from pre-amplified values.
- [Analog Output:Output Configuration:Terminal Configurations](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a3.html) Indicates the list of terminal configurations supported by the channel.
- [Analog Output:Output Types](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd9.html) Indicates the output types supported by the channel.
- [Analog Output:Power Up Output Types](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr304e.html) Indicates the power up output types supported by the channel.
- [Counter Input:Measurement Types](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fda.html) Indicates the measurement types supported by the channel.
- [Counter Output:Output Types](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fdb.html) Indicates the output types supported by the channel.
- [Digital Input:Port Width](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a4.html) Indicates in bits the width of digital input port.
- [Digital Input:Timing:Change Detection Supported](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a6.html) Indicates if the change detection timing type is supported for the digital input physical channel.
- [Digital Input:Timing:Sample Clock Supported](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a5.html) Indicates if the sample clock timing type is supported for the digital input physical channel.
- [Digital Input:Timing:Sample Modes](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe0.html) Indicates the sample modes supported by devices that support sample clocked digital input.
- [Digital Output:Port Width](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a7.html) Indicates in bits the width of digital output port.
- [Digital Output:Timing:Sample Clock Supported](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a8.html) Indicates if the sample clock timing type is supported for the digital output physical channel.
- [Digital Output:Timing:Sample Modes](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe1.html) Indicates the sample modes supported by devices that support sample clocked digital output.
- [Digital:Port Logic Family](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr31eb.html) Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.
- [TEDS:BitStream](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21df.html) Indicates the TEDS binary bitstream without checksums.
- [TEDS:ManufacturerID](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21da.html) Indicates the manufacturer ID of the sensor.
- [TEDS:Model Number](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21db.html) Indicates the model number of the sensor.
- [TEDS:Serial Number](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dc.html) Indicates the serial number of the sensor.
- [TEDS:TemplateIDs](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr228f.html) Indicates the IDs of the templates in the bitstream in TEDS.BitStream .
- [TEDS:Version Letter](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21de.html) Indicates the version letter of the sensor.
- [TEDS:Version Number](../../../resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dd.html) Indicates the version number of the sensor.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21d9.html language=enus -->
## TOPIC 01312: Active Physical Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21d9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21d9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical channel from which to retrieve properties. Remarks The following table lists the characteristics of this property. Short Name ActivePhysicalChans Data type cdaqmxscale.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run-T

### Active Physical Channels

Specifies the 
 [physical channel](/csh?context=nidaqmx_mxcncpts_chans)
 from which to retrieve properties.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActivePhysicalChans |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21da.html language=enus -->
## TOPIC 01313: TEDS:ManufacturerID

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21da.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21da.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the manufacturer ID of the sensor. Remarks The following table lists the characteristics of this property. Short Name TEDS.MfgID Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### TEDS:ManufacturerID

Indicates the manufacturer ID of the sensor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TEDS.MfgID |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21db.html language=enus -->
## TOPIC 01314: TEDS:Model Number

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21db.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21db.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the model number of the sensor. Remarks The following table lists the characteristics of this property. Short Name TEDS.ModelNum Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### TEDS:Model Number

Indicates the model number of the sensor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TEDS.ModelNum |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dc.html language=enus -->
## TOPIC 01315: TEDS:Serial Number

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the serial number of the sensor. Remarks The following table lists the characteristics of this property. Short Name TEDS.SerialNum Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### TEDS:Serial Number

Indicates the serial number of the sensor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TEDS.SerialNum |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dd.html language=enus -->
## TOPIC 01316: TEDS:Version Number

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21dd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the version number of the sensor. Remarks The following table lists the characteristics of this property. Short Name TEDS.VersionNum Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### TEDS:Version Number

Indicates the version number of the sensor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TEDS.VersionNum |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21de.html language=enus -->
## TOPIC 01317: TEDS:Version Letter

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21de.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21de.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the version letter of the sensor. Remarks The following table lists the characteristics of this property. Short Name TEDS.VersionLetter Data type cstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### TEDS:Version Letter

Indicates the version letter of the sensor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TEDS.VersionLetter |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21df.html language=enus -->
## TOPIC 01318: TEDS:BitStream

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21df.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr21df.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the TEDS binary bitstream without checksums. Remarks The following table lists the characteristics of this property. Short Name TEDS.BitStream Data type c1du8.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### TEDS:BitStream

Indicates the TEDS binary bitstream without checksums.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TEDS.BitStream |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr228f.html language=enus -->
## TOPIC 01319: TEDS:TemplateIDs

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr228f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr228f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the IDs of the templates in the bitstream in TEDS.BitStream . Remarks The following table lists the characteristics of this property. Short Name TEDS.TemplateIDs Data type c1du32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time

### TEDS:TemplateIDs

Indicates the IDs of the templates in the bitstream in 
 [TEDS.BitStream](/csh?context=nidaqmx_daqmxprop_attr21df)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TEDS.TemplateIDs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2342.html language=enus -->
## TOPIC 01320: Analog Input:Input Configuration:Terminal Configurations

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2342.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2342.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the list of terminal configurations supported by the channel. Remarks The following table lists the characteristics of this property. Short Name AI.TermCfgs Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engi

### Analog Input:Input Configuration:Terminal Configurations

Indicates the list of terminal configurations supported by the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.TermCfgs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| RSE | 10083 | Referenced Single-Ended. |
| --- | --- | --- |
| NRSE | 10078 | Non-Referenced Single-Ended. |
| Differential | 10106 | Differential. |
| Pseudodifferential | 12529 | Pseudodifferential. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a3.html language=enus -->
## TOPIC 01321: Analog Output:Output Configuration:Terminal Configurations

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the list of terminal configurations supported by the channel. Remarks The following table lists the characteristics of this property. Short Name AO.TermCfgs Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engi

### Analog Output:Output Configuration:Terminal Configurations

Indicates the list of terminal configurations supported by the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.TermCfgs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| RSE | 10083 | Referenced Single-Ended. |
| --- | --- | --- |
| Differential | 10106 | Differential. |
| Pseudodifferential | 12529 | Pseudodifferential. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a4.html language=enus -->
## TOPIC 01322: Digital Input:Port Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bits the width of digital input port. Remarks The following table lists the characteristics of this property. Short Name DI.PortWidth Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Digital Input:Port Width

Indicates in bits the width of digital input port.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.PortWidth |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a5.html language=enus -->
## TOPIC 01323: Digital Input:Timing:Sample Clock Supported

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the sample clock timing type is supported for the digital input physical channel. Remarks The following table lists the characteristics of this property. Short Name DI.SampClkSupported Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-speci

### Digital Input:Timing:Sample Clock Supported

Indicates if the sample clock timing type is supported for the digital input physical channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.SampClkSupported |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a6.html language=enus -->
## TOPIC 01324: Digital Input:Timing:Change Detection Supported

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the change detection timing type is supported for the digital input physical channel. Remarks The following table lists the characteristics of this property. Short Name DI.ChangeDetectSupported Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running dev

### Digital Input:Timing:Change Detection Supported

Indicates if the change detection timing type is supported for the digital input physical channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.ChangeDetectSupported |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a7.html language=enus -->
## TOPIC 01325: Digital Output:Port Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bits the width of digital output port. Remarks The following table lists the characteristics of this property. Short Name DO.PortWidth Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Digital Output:Port Width

Indicates in bits the width of digital output port.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.PortWidth |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a8.html language=enus -->
## TOPIC 01326: Digital Output:Timing:Sample Clock Supported

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr29a8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the sample clock timing type is supported for the digital output physical channel. Remarks The following table lists the characteristics of this property. Short Name DO.SampClkSupported Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-spec

### Digital Output:Timing:Sample Clock Supported

Indicates if the sample clock timing type is supported for the digital output physical channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.SampClkSupported |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1e.html language=enus -->
## TOPIC 01327: Analog Output:Advanced:Manual Control:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if you can control the physical channel externally via a manual control located on the device. You cannot simultaneously control a channel manually and with NI-DAQmx. Remarks The following table lists the characteristics of this property. Short Name AO.ManualControl.Enable Data type cbool.

### Analog Output:Advanced:Manual Control:Enable

Specifies if you can control the physical channel externally via a manual control located on the device. You cannot simultaneously control a channel manually and with NI-DAQmx.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.ManualControl.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1f.html language=enus -->
## TOPIC 01328: Analog Output:Advanced:Manual Control:Amplitude

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a1f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current value of the front panel amplitude control for the physical channel in volts. Remarks The following table lists the characteristics of this property. Short Name AO.ManualControl.Amplitude Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running d

### Analog Output:Advanced:Manual Control:Amplitude

Indicates the current value of the front panel amplitude control for the physical channel in volts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.ManualControl.Amplitude |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a20.html language=enus -->
## TOPIC 01329: Analog Output:Advanced:Manual Control:Frequency

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a20.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2a20.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current value of the front panel frequency control for the physical channel in hertz. Remarks The following table lists the characteristics of this property. Short Name AO.ManualControl.Freq Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device

### Analog Output:Advanced:Manual Control:Frequency

Indicates the current value of the front panel frequency control for the physical channel in hertz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.ManualControl.Freq |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2ec3.html language=enus -->
## TOPIC 01330: Analog Output:Advanced:Manual Control:Short Detected

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2ec3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2ec3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the physical channel is currently disabled due to a short detected on the channel. Remarks The following table lists the characteristics of this property. Short Name AO.ManualControl.ShortDetected Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Run

### Analog Output:Advanced:Manual Control:Short Detected

Indicates whether the physical channel is currently disabled due to a short detected on the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.ManualControl.ShortDetected |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd7.html language=enus -->
## TOPIC 01331: Analog Input:Measurement Types

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement types supported by the channel. Remarks The following table lists the characteristics of this property. Short Name AI.MeasTypes Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Volta

### Analog Input:Measurement Types

Indicates the measurement types supported by the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.MeasTypes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Voltage | 10322 | Voltage measurement. |
| --- | --- | --- |
| Voltage RMS | 10350 | Voltage RMS measurement. |
| Current | 10134 | Current measurement. |
| Current RMS | 10351 | Current RMS measurement. |
| More:Voltage:Custom with Excitation | 10323 | Voltage measurement with an excitation source. You can use this measurement type for custom sensors that require excitation, but you must use a custom scale to scale the measured voltage. |
| More:Bridge (V/V) | 15908 | Measure voltage ratios from a Wheatstone bridge. |
| Frequency | 10181 | Frequency measurement using a frequency to voltage converter. |
| Resistance | 10278 | Resistance measurement. |
| Temperature:Thermocouple | 10303 | Temperature measurement using a thermocouple. |
| Temperature:Thermistor | 10302 | Temperature measurement using a thermistor. |
| Temperature:RTD | 10301 | Temperature measurement using an RTD. |
| Temperature:Built-in Sensor | 10311 | Temperature measurement using a built-in sensor on a terminal block or device. On SCXI modules, for example, this could be the CJC sensor. |
| Strain Gage | 10300 | Strain measurement. |
| Rosette Strain Gage | 15980 | Strain measurement using a rosette strain gage. |
| Position:LVDT | 10352 | Position measurement using an LVDT. |
| Position:RVDT | 10353 | Position measurement using an RVDT. |
| Position:Eddy Current Proximity Probe | 14835 | Position measurement using an eddy current proximity probe. |
| Accelerometer | 10356 | Acceleration measurement using an accelerometer. |
| Acceleration:Charge | 16104 | Acceleration measurement using a charge-based sensor. |
| Acceleration:4 Wire DC Voltage | 16106 | Acceleration measurement using a 4 wire DC voltage based sensor. |
| Velocity:IEPE Sensor | 15966 | Velocity measurement using an IEPE Sensor. |
| Force:Bridge | 15899 | Force measurement using a bridge-based sensor. |
| Force:IEPE Sensor | 15895 | Force measurement using an IEPE Sensor. |
| Pressure:Bridge | 15902 | Pressure measurement using a bridge-based sensor. |
| Sound Pressure:Microphone | 10354 | Sound pressure measurement using a microphone. |
| Torque:Bridge | 15905 | Torque measurement using a bridge-based sensor. |
| TEDS Sensor | 12531 | Measurement type defined by TEDS. |
| Charge | 16105 | Charge measurement. |
| Power | 16201 | Power source and measurement. |
| CalculatedPower | 16204 | Calculated power measurement. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd8.html language=enus -->
## TOPIC 01332: Analog Input:Input Configuration:Input Sources

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the list of input sources supported by the channel. Channels may support using the signal from the I/O connector or one of several calibration signals. Remarks The following table lists the characteristics of this property. Short Name AI.InputSrcs Data type c1dstr.png Permissions Read Only

### Analog Input:Input Configuration:Input Sources

Indicates the list of input sources supported by the channel. Channels may support using the signal from the I/O connector or one of several calibration signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.InputSrcs |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd9.html language=enus -->
## TOPIC 01333: Analog Output:Output Types

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fd9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the output types supported by the channel. Remarks The following table lists the characteristics of this property. Short Name AO.OutputTypes Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Voltage

### Analog Output:Output Types

Indicates the output types supported by the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.OutputTypes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Voltage | 10322 | Voltage generation. |
| --- | --- | --- |
| Current | 10134 | Current generation. |
| Function Generation | 14750 | Function generation. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fda.html language=enus -->
## TOPIC 01334: Counter Input:Measurement Types

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fda.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fda.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement types supported by the channel. Remarks The following table lists the characteristics of this property. Short Name CI.MeasTypes Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Count

### Counter Input:Measurement Types

Indicates the measurement types supported by the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CI.MeasTypes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Count Edges | 10125 | Count edges of a digital signal. |
| --- | --- | --- |
| Frequency | 10179 | Measure the frequency of a digital signal. |
| Period | 10256 | Measure the period of a digital signal. |
| Pulse Width | 10359 | Measure the width of a pulse of a digital signal. |
| Semi Period | 10289 | Measure the time between state transitions of a digital signal. |
| Pulse Frequency | 15864 | Pulse measurement, returning the result as frequency and duty cycle. |
| Pulse Time | 15865 | Pulse measurement, returning the result as high time and low time. |
| Pulse Ticks | 15866 | Pulse measurement, returning the result as high ticks and low ticks. |
| Duty Cycle | 16070 | Measure the duty cycle of a digital signal. |
| Position:Angular Encoder | 10360 | Angular position measurement using an angular encoder. |
| Position:Linear Encoder | 10361 | Linear position measurement using a linear encoder. |
| Velocity:Angular Encoder | 16078 | Angular velocity measurement using an angular encoder. |
| Velocity:Linear Encoder | 16079 | Linear velocity measurement using a linear encoder. |
| Two Edge Separation | 10267 | Measure time between edges of two digital signals. |
| GPS Timestamp | 10362 | Timestamp measurement, synchronizing the counter to a GPS receiver. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fdb.html language=enus -->
## TOPIC 01335: Counter Output:Output Types

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fdb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the output types supported by the channel. Remarks The following table lists the characteristics of this property. Short Name CO.OutputTypes Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Pulse:Ti

### Counter Output:Output Types

Indicates the output types supported by the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CO.OutputTypes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Pulse:Time | 10269 | Generate pulses defined by the time the pulse is at a low state and the time the pulse is at a high state. |
| --- | --- | --- |
| Pulse:Frequency | 10119 | Generate digital pulses defined by frequency and duty cycle. |
| Pulse:Ticks | 10268 | Generate digital pulses defined by the number of timebase ticks that the pulse is at a low state and the number of timebase ticks that the pulse is at a high state. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe0.html language=enus -->
## TOPIC 01336: Digital Input:Timing:Sample Modes

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the sample modes supported by devices that support sample clocked digital input. Remarks The following table lists the characteristics of this property. Short Name DI.SampModes Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Availa

### Digital Input:Timing:Sample Modes

Indicates the sample modes supported by devices that support sample clocked digital input.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.SampModes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Finite Samples | 10178 | Acquire or generate a finite number of samples. |
| --- | --- | --- |
| Continuous Samples | 10123 | Acquire or generate samples until you stop the task. |
| Hardware Timed Single Point | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe1.html language=enus -->
## TOPIC 01337: Digital Output:Timing:Sample Modes

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr2fe1.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the sample modes supported by devices that support sample clocked digital output. Remarks The following table lists the characteristics of this property. Short Name DO.SampModes Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Avail

### Digital Output:Timing:Sample Modes

Indicates the sample modes supported by devices that support sample clocked digital output.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DO.SampModes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Finite Samples | 10178 | Acquire or generate a finite number of samples. |
| --- | --- | --- |
| Continuous Samples | 10123 | Acquire or generate samples until you stop the task. |
| Hardware Timed Single Point | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr304e.html language=enus -->
## TOPIC 01338: Analog Output:Power Up Output Types

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr304e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr304e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the power up output types supported by the channel. Remarks The following table lists the characteristics of this property. Short Name AO.PowerUpOutputTypes Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engi

### Analog Output:Power Up Output Types

Indicates the power up output types supported by the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.PowerUpOutputTypes |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Voltage | 10322 | Voltage output. |
| --- | --- | --- |
| Current | 10134 | Current output. |
| High-Impedance | 12527 | High-impedance state. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3062.html language=enus -->
## TOPIC 01339: Analog Output:Advanced:Power Amplifier:Channel Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3062.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3062.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable or disable a channel for amplification. This property can also be used to check if a channel is enabled. Remarks The following table lists the characteristics of this property. Short Name AO.PowerAmp.ChannelEnable Data type cbool.png Permissions Read/Write Resettable True

### Analog Output:Advanced:Power Amplifier:Channel Enable

Specifies whether to enable or disable a channel for amplification. This property can also be used to check if a channel is enabled.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.PowerAmp.ChannelEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3063.html language=enus -->
## TOPIC 01340: Analog Output:Advanced:Power Amplifier:Scaling Coefficients

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3063.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3063.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the coefficients of a polynomial equation used to scale from pre-amplified values. Remarks The following table lists the characteristics of this property. Short Name AO.PowerAmp.ScalingCoeff Data type c1ddbl.png Permissions Read Only Resettable False Settable While Task Is Running device-s

### Analog Output:Advanced:Power Amplifier:Scaling Coefficients

Indicates the coefficients of a polynomial equation used to scale from pre-amplified values.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.PowerAmp.ScalingCoeff |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3064.html language=enus -->
## TOPIC 01341: Analog Output:Advanced:Power Amplifier:Overcurrent

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3064.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3064.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the channel detected an overcurrent condition . Remarks The following table lists the characteristics of this property. Short Name AO.PowerAmp.Overcurrent Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engi

### Analog Output:Advanced:Power Amplifier:Overcurrent

Indicates if the channel detected an 
 [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.PowerAmp.Overcurrent |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3065.html language=enus -->
## TOPIC 01342: Analog Output:Advanced:Power Amplifier:Calibration:Gain

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3065.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3065.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the calibrated gain of the channel. Remarks The following table lists the characteristics of this property. Short Name AO.PowerAmp.Gain Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Analog Output:Advanced:Power Amplifier:Calibration:Gain

Indicates the calibrated gain of the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.PowerAmp.Gain |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3066.html language=enus -->
## TOPIC 01343: Analog Output:Advanced:Power Amplifier:Calibration:Offset

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3066.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3066.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the calibrated offset of the channel in volts. Remarks The following table lists the characteristics of this property. Short Name AO.PowerAmp.Offset Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Analog Output:Advanced:Power Amplifier:Calibration:Offset

Indicates the calibrated offset of the channel in volts.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AO.PowerAmp.Offset |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316c.html language=enus -->
## TOPIC 01344: Analog Input:Signal Conditioning:Sensor Power:Power Control:Voltage

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level for the sensor's power supply. Remarks The following table lists the characteristics of this property. Short Name AI.PowerControl.Voltage Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine

### Analog Input:Signal Conditioning:Sensor Power:Power Control:Voltage

Specifies the voltage level for the sensor's power supply.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.PowerControl.Voltage |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316d.html language=enus -->
## TOPIC 01345: Analog Input:Signal Conditioning:Sensor Power:Power Control:Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to turn on the sensor's power supply. Remarks The following table lists the characteristics of this property. Short Name AI.PowerControl.Enable Data type cbool.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine Tru

### Analog Input:Signal Conditioning:Sensor Power:Power Control:Enable

Specifies whether to turn on the sensor's power supply.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.PowerControl.Enable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316e.html language=enus -->
## TOPIC 01346: Analog Input:Signal Conditioning:Sensor Power:Power Control:Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr316e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of power supplied to the sensor. Remarks The following table lists the characteristics of this property. Short Name AI.PowerControl.Type Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True DC 10

### Analog Input:Signal Conditioning:Sensor Power:Power Control:Type

Specifies the type of power supplied to the sensor.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.PowerControl.Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| DC | 10050 | Sensor power supply generates a single DC voltage level. |
| --- | --- | --- |
| AC | 10045 | Sensor power supply generates an AC voltage. |
| BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3179.html language=enus -->
## TOPIC 01347: Analog Input:Signal Conditioning:Sensor Power:Types

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3179.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr3179.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the types of power supplied to the sensor supported by this channel. Remarks The following table lists the characteristics of this property. Short Name AI.SensorPower.Types Data type c1di32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available

### Analog Input:Signal Conditioning:Sensor Power:Types

Indicates the types of power supplied to the sensor supported by this channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.SensorPower.Types |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| DC | 10050 | Sensor power supply generates a single DC voltage level. |
| --- | --- | --- |
| AC | 10045 | Sensor power supply generates an AC voltage. |
| BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317a.html language=enus -->
## TOPIC 01348: Analog Input:Signal Conditioning:Sensor Power:Voltage Range Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates pairs of sensor power voltage ranges supported by this channel. Each pair consists of the low value followed by the high value. Remarks The following table lists the characteristics of this property. Short Name AI.SensorPower.VoltageRangeVals Data type c1ddbl.png Permissions Read Only Rese

### Analog Input:Signal Conditioning:Sensor Power:Voltage Range Values

Indicates pairs of sensor power voltage ranges supported by this channel. Each pair consists of the low value followed by the high value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.SensorPower.VoltageRangeVals |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317c.html language=enus -->
## TOPIC 01349: Analog Input:Signal Conditioning:Sensor Power:Status:Open Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether there is an open channel or undercurrent condition on the channel. Remarks The following table lists the characteristics of this property. Short Name AI.SensorPower.OpenChan Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Av

### Analog Input:Signal Conditioning:Sensor Power:Status:Open Channel

Indicates whether there is an open channel or undercurrent condition on the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.SensorPower.OpenChan |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317d.html language=enus -->
## TOPIC 01350: Analog Input:Signal Conditioning:Sensor Power:Status:Overcurrent

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr317d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether there is an overcurrent condition on the channel. Remarks The following table lists the characteristics of this property. Short Name AI.SensorPower.Overcurrent Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run

### Analog Input:Signal Conditioning:Sensor Power:Status:Overcurrent

Indicates whether there is an overcurrent condition on the channel.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AI.SensorPower.Overcurrent |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-physical-channel/attr31eb.html language=enus -->
## TOPIC 01351: Digital:Port Logic Family

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-physical-channel/attr31eb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-physical-channel/attr31eb.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

### Digital:Port Logic Family

Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Dig.PortLogicFamily |
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

DAQmx Physical Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read-p.html language=enus -->
## TOPIC 01352: DAQmx Read Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Read properties to configure read operations, such as from what position in a buffer you want to read, and to query the current status of read operations.

### DAQmx Read Properties

Use the DAQmx Read properties to configure read operations, such as from what 
 [position in a buffer](/csh?context=nidaqmx_mxcncpts_controlwherebufferread)
 you want to read, and to 
 [query the current status](/csh?context=nidaqmx_mxcncpts_readstatus)
 of read operations.

- [Advanced:Digital Input:Number of Booleans Per Channel](../../../resource/objmgr/daqmx-rc/daqmx-read/attr217c.html) Indicates the number of Booleans per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra Booleans are FALSE.
- [Advanced:Number of Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr217b.html) Indicates the number of channels that DAQmx Read reads from the task. This value is the number of channels in the task or the number of channels you specify with ChannelsToRead .
- [Advanced:Raw Data Width](../../../resource/objmgr/daqmx-rc/daqmx-read/attr217a.html) Indicates in bytes the size of a raw sample from the task.
- [Advanced:Sleep Time](../../../resource/objmgr/daqmx-rc/daqmx-read/attr22b0.html) Specifies in seconds the amount of time to sleep after checking for available samples if WaitMode is Sleep.
- [Advanced:Wait Mode](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2232.html) Specifies how DAQmx Read waits for samples to become available.
- [Auto Start](../../../resource/objmgr/daqmx-rc/daqmx-read/attr1826.html) Specifies if DAQmx Read automatically starts the task if you did not start the task explicitly by using DAQmx Start Task . The default value is TRUE. When DAQmx Read starts a finite acquisition task, it also stops the task after reading the last sample.
- [Channels to Read](../../../resource/objmgr/daqmx-rc/daqmx-read/attr1823.html) Specifies a subset of channels in the task from which to read.
- [Logging:File Path](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2ec4.html) Specifies the path to the TDMS file to which you want to log data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when DAQmx Start New File is called. New file paths can be specified by ending with "\" or "/". Files created after specifying a new file path retain the same name and numbering sequence.
- [Logging:File Pre-allocation Size](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2fc6.html) Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you configure the task to acquire.
- [Logging:File Write Size](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2fc3.html) Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes.
- [Logging:Mode](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2ec5.html) Specifies whether to enable logging and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode.
- [Logging:Pause](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2fe3.html) Specifies whether logging is paused while a task is executing. If Logging.Mode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If Logging.Mode is set to Log Only mode, this value is taken into consideration the next time that data is written to disk. A new TDMS group is written when logging is resumed from a paused state.
- [Logging:Samples Per File](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2fe4.html) Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of <filename>_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\data.tdms, the next file name used is C:\data_0001.tdms. To disable file spanning behavior, set this attribute to 0. If Logging.FilePath is changed while this attribute is set, the new file path takes effect on the next file created.
- [Logging:TDMS:Group Name](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2ec6.html) Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist. For example, if you specify a group name of Voltage Task, and that group already exists, NI-DAQmx assigns the group name Voltage Task #1, then Voltage Task #2.
- [Logging:TDMS:Operation](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2ec7.html) Specifies how to open the TDMS file.
- [Offset](../../../resource/objmgr/daqmx-rc/daqmx-read/attr190b.html) Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with RelativeTo .
- [OverWrite Mode](../../../resource/objmgr/daqmx-rc/daqmx-read/attr1211.html) Specifies whether to overwrite samples in the buffer that you have not yet read.
- [Read All Available Samples](../../../resource/objmgr/daqmx-rc/daqmx-read/attr1215.html) Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of samples to read is -1, a read operation always reads all samples currently available in the buffer.
- [RelativeTo](../../../resource/objmgr/daqmx-rc/daqmx-read/attr190a.html) Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with Offset , the read operation begins at that offset relative to the point you select with this property. The default value is Current Read Position unless you configure a Reference Trigger for the task. If you configure a Reference Trigger, the default value is First Pretrigger Sample.
- [Status:Accessory:Accessory Insertion or Removal Detected](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2f70.html) Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevsWithInsertedOrRemovedAccessories . Otherwise, you will receive an error.
- [Status:Accessory:Devices with Inserted or Removed Accessories](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2f71.html) Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error.
- [Status:Advanced:ChangeDetection:Overflowed](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2194.html) Indicates if samples were missed because change detection events occurred faster than the device could handle them. Some devices detect overflows differently than others.
- [Status:Aux Power Error:Aux Power Error Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr31e0.html) Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Otherwise, you will receive an error.
- [Status:Aux Power Error:Aux Power Error Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr31df.html) Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Aux Power Error Channels property. Otherwise, you will receive an error.
- [Status:Available Samples Per Channel](../../../resource/objmgr/daqmx-rc/daqmx-read/attr1223.html) Indicates the number of samples available to read per channel. This value is the same for all channels in the task.
- [Status:Common Mode Range Error:Common Mode Range Error Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2a99.html) Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read CommonModeRangeErrorChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Common Mode Range Error:Common Mode Range Error Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2a98.html) Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation status for all channels in the task. You must read this property before you read CommonModeRangeErrorChans . Otherwise, you will receive an error.
- [Status:Current Read Position](../../../resource/objmgr/daqmx-rc/daqmx-read/attr1221.html) Indicates in samples per channel the current position in the buffer.
- [Status:Excitation Fault:Excitation Fault Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3089.html) Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition . You must read ExcitFaultChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Excitation Fault:Excitation Fault Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3088.html) Indicates if the device(s) detected an excitation fault condition for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read ExcitFaultChans . Otherwise, you will receive an error.
- [Status:Input Limits Fault:Input Limits Fault Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3190.html) Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read InputLimitsFaultChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Input Limits Fault:Input Limits Fault Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr318f.html) Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read InputLimitsFaultChans . Otherwise, you will receive an error. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA.
- [Status:Open Channels:Open Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3101.html) Indicates a list of names of any open virtual channels. You must read OpenChansExist before you read this property. Otherwise you will receive an error.
- [Status:Open Channels:Open Channels Details](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3102.html) Indicates a list of details of any open virtual channels. You must read OpenChansExist before you read this property. Otherwise you will receive an error.
- [Status:Open Channels:Open Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3100.html) Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before you read OpenChans . Otherwise, you will receive an error.
- [Status:Open Current Loop:Open Current Loop Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2a0a.html) Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop . You must read OpenCurrentLoopChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Open Current Loop:Open Current Loop Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2a09.html) Indicates if the device(s) detected an open current loop for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read OpenCurrentLoopChans . Otherwise, you will receive an error.
- [Status:Open Thermocouple:Open Thermocouple Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2a97.html) Indicates a list of names of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read OpenThrmcplChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Open Thermocouple:Open Thermocouple Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2a96.html) Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read OpenThrmcplChans . Otherwise, you will receive an error.
- [Status:Overcurrent:Overcurrent Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr29e7.html) Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition . You must read OvercurrentChansExist before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels to recover.
- [Status:Overcurrent:Overcurrent Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr29e6.html) Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read OvercurrentChans . Otherwise, you will receive an error.
- [Status:Overload:Overloaded Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2175.html) Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Overload:Overloaded Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr2174.html) Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedChans . Otherwise, you will receive an error.
- [Status:Overtemperature:Overtemperature Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3082.html) Indicates a list of names of any overtemperature virtual channels. You must read OvertemperatureChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Overtemperature:Overtemperature Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3081.html) Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read OvertemperatureChans . Otherwise, you will receive an error.
- [Status:Phase-Locked Loop:Unlocked Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3119.html) Indicates the channels that had their PLLs unlock.
- [Status:Phase-Locked Loop:Unlocked Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3118.html) Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition.
- [Status:Power Supply Fault:Power Supply Fault Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3193.html) Indicates the virtual channels that have detected a power supply fault. You must read PowerSupplyFaultChansExist before you read this property. Otherwise, you will receive an error.
- [Status:Power Supply Fault:Power Supply Fault Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr3192.html) Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read PowerSupplyFaultChans . Otherwise, you will receive an error.
- [Status:Remote Sense Error:Remote Sense Error Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr31de.html) Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise, you will receive an error.
- [Status:Remote Sense Error:Remote Sense Error Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr31dd.html) Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. You must read this property before you read the Remote Sense Error Channels property. Otherwise, you will receive an error.
- [Status:Reverse Voltage Error:Reverse Voltage Error Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr31e7.html) Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Otherwise, you will receive an error.
- [Status:Reverse Voltage Error:Reverse Voltage Error Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr31e6.html) Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Reverse Voltage Error Channels property. Otherwise, you will receive an error.
- [Status:Synchronization:Unlocked Channels](../../../resource/objmgr/daqmx-rc/daqmx-read/attr313e.html) Indicates the channels from devices in an unlocked target.
- [Status:Synchronization:Unlocked Channels Exist](../../../resource/objmgr/daqmx-rc/daqmx-read/attr313d.html) Indicates whether the target is currently locked to the grand master. Devices may report PLL Unlock either during acquisition or after acquisition.
- [Status:Total Samples Per Channel Acquired](../../../resource/objmgr/daqmx-rc/daqmx-read/attr192a.html) Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions.
- [Waveform Attributes](../../../resource/objmgr/daqmx-rc/daqmx-read/attr1225.html) Specifies the waveform data type attributes to return. Returning fewer attributes increases performance.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr1211.html language=enus -->
## TOPIC 01353: OverWrite Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr1211.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr1211.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to overwrite samples in the buffer that you have not yet read. Remarks The following table lists the characteristics of this property. Short Name OverWrite Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time

### OverWrite Mode

Specifies whether to overwrite samples in the buffer that you have not yet read.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OverWrite |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Overwrite Unread Samples | 10252 | When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting RelativeTo to Most Recent Sample and setting Offset to the appropriate number of samples. |
| --- | --- | --- |
| Do Not Overwrite Unread Samples | 10159 | The acquisition stops when it encounters a sample in the buffer that you have not read. |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr1215.html language=enus -->
## TOPIC 01354: Read All Available Samples

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr1215.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr1215.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of s

### Read All Available Samples

Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of samples to read is -1, a read operation always reads all samples currently available in the buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ReadAllAvailSamp |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr1221.html language=enus -->
## TOPIC 01355: Status:Current Read Position

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr1221.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr1221.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in samples per channel the current position in the buffer. Remarks The following table lists the characteristics of this property. Short Name CurrReadPos Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine Tr

### Status:Current Read Position

Indicates in samples per channel the current position in the buffer.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CurrReadPos |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr1223.html language=enus -->
## TOPIC 01356: Status:Available Samples Per Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr1223.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr1223.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of samples available to read per channel. This value is the same for all channels in the task. Remarks The following table lists the characteristics of this property. Short Name AvailSampPerChan Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Run

### Status:Available Samples Per Channel

Indicates the number of samples available to read per channel. This value is the same for all channels in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AvailSampPerChan |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr1225.html language=enus -->
## TOPIC 01357: Waveform Attributes

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr1225.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr1225.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the waveform data type attributes to return. Returning fewer attributes increases performance. Remarks The following table lists the characteristics of this property. Short Name WfmAttr Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific

### Waveform Attributes

Specifies the waveform data type attributes to return. Returning fewer attributes increases performance.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WfmAttr |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Samples | 10287 | Return only samples. |
| --- | --- | --- |
| Samples and Timing | 10140 | Return the samples and timing information. |
| Samples, Timing, and Attributes | 10141 | Return the samples, timing information, and other attributes, such as the name of the channel. |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr1823.html language=enus -->
## TOPIC 01358: Channels to Read

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr1823.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr1823.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a subset of channels in the task from which to read. Remarks The following table lists the characteristics of this property. Short Name ChannelsToRead Data type cgenclassrntag.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time En

### Channels to Read

Specifies a subset of channels in the task from which to read.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ChannelsToRead |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr1826.html language=enus -->
## TOPIC 01359: Auto Start

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr1826.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr1826.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if DAQmx Read automatically starts the task if you did not start the task explicitly by using DAQmx Start Task . The default value is TRUE. When DAQmx Read starts a finite acquisition task, it also stops the task after reading the last sample. Remarks The following table lists the characte

### Auto Start

Specifies if 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 automatically starts the task if you did not start the task explicitly by using 
 [DAQmx Start Task](/csh?context=nidaqmx_lvdaqmx_mxstart)
 . The default value is TRUE. When 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 starts a finite acquisition task, it also stops the task after reading the last sample.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AutoStart |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr190a.html language=enus -->
## TOPIC 01360: RelativeTo

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr190a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr190a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with Offset , the read operation begins at that offset relative to the point you select with this property. The default value is Current Read Position unless you configure a Reference Trigger for the

### RelativeTo

Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with 
 [Offset](/csh?context=nidaqmx_daqmxprop_attr190b)
 , the read operation begins at that offset relative to the point you select with this property. The default value is Current Read Position unless you configure a 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 for the task. If you configure a Reference Trigger, the default value is First Pretrigger Sample.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RelativeTo |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| First Sample | 10424 | Start reading samples relative to the first sample acquired. |
| --- | --- | --- |
| Current Read Position | 10425 | Start reading samples relative to the last sample returned by the previous read. For the first read operation, this position is the first sample acquired or the first pretrigger sample if you configured a reference trigger for the task. |
| Reference Trigger | 10426 | Start reading samples relative to the first sample after the reference trigger occurred. |
| First Pretrigger Sample | 10427 | Start reading samples relative to the first pretrigger sample. You specify the number of pretrigger samples to acquire when you configure a reference trigger. |
| Most Recent Sample | 10428 | Start reading samples relative to the next sample acquired. For example, use this value and set Offset to -1 to read the last sample acquired. |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr190b.html language=enus -->
## TOPIC 01361: Offset

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr190b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr190b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with RelativeTo . Remarks The following table lists the characteristics of this property. Short Name Offset Data type ci32.png Permissions Read/Write Resettable True Set

### Offset

Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with 
 [RelativeTo](/csh?context=nidaqmx_daqmxprop_attr190a)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr192a.html language=enus -->
## TOPIC 01362: Status:Total Samples Per Channel Acquired

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr192a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr192a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions. Remarks The following table lists the cha

### Status:Total Samples Per Channel Acquired

Indicates the total number of samples acquired by each channel. NI-DAQmx returns a single value because this value is the same for all channels. For retriggered acquisitions, this value is the cumulative number of samples across all retriggered acquisitions.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TotalSampPerChanAcquired |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2174.html language=enus -->
## TOPIC 01363: Status:Overload:Overloaded Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2174.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2174.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedChans . Otherwise, you will receive an error. Remarks The following table lists the

### Status:Overload:Overloaded Channels Exist

Indicates if the device(s) detected an 
 [overload](/csh?context=nidaqmx_mxdevconsid_overloaddetection)
 in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read 
 [OverloadedChans](/csh?context=nidaqmx_daqmxprop_attr2175)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2175.html language=enus -->
## TOPIC 01364: Status:Overload:Overloaded Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2175.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2175.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. Short Name OverloadedChans Data type c1dstr.png Pe

### Status:Overload:Overloaded Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any 
 [overloaded](/csh?context=nidaqmx_mxdevconsid_overloaddetection)
 virtual channels in the task. You must read 
 [OverloadedChansExist](/csh?context=nidaqmx_daqmxprop_attr2174)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr217a.html language=enus -->
## TOPIC 01365: Advanced:Raw Data Width

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr217a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr217a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bytes the size of a raw sample from the task. Remarks The following table lists the characteristics of this property. Short Name RawDataWidth Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Advanced:Raw Data Width

Indicates in bytes the size of a raw sample from the task.

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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr217b.html language=enus -->
## TOPIC 01366: Advanced:Number of Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr217b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr217b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of channels that DAQmx Read reads from the task. This value is the number of channels in the task or the number of channels you specify with ChannelsToRead . Remarks The following table lists the characteristics of this property. Short Name NumChans Data type cu32.png Permission

### Advanced:Number of Channels

Indicates the number of channels that 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 reads from the task. This value is the number of channels in the task or the number of channels you specify with 
 [ChannelsToRead](/csh?context=nidaqmx_daqmxprop_attr1823)
 .

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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr217c.html language=enus -->
## TOPIC 01367: Advanced:Digital Input:Number of Booleans Per Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr217c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr217c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Booleans per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra Booleans are FALSE. Remarks The following table lists the characteristics of this property. Short Name DI.NumBooleansPerChan Data type cu32.pn

### Advanced:Digital Input:Number of Booleans Per Channel

Indicates the number of Booleans per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra Booleans are FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DI.NumBooleansPerChan |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2194.html language=enus -->
## TOPIC 01368: Status:Advanced:ChangeDetection:Overflowed

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2194.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2194.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if samples were missed because change detection events occurred faster than the device could handle them. Some devices detect overflows differently than others. Remarks The following table lists the characteristics of this property. Short Name ChangeDetect.Overflowed Data type cbool.png Pe

### Status:Advanced:ChangeDetection:Overflowed

Indicates if samples were missed because change detection events occurred faster than the device could handle them. 
 [Some devices](/csh?context=nidaqmx_mxdevconsid_changedetstaticdio)
 detect overflows differently than others.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ChangeDetect.Overflowed |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2232.html language=enus -->
## TOPIC 01369: Advanced:Wait Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2232.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2232.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how DAQmx Read waits for samples to become available. Remarks The following table lists the characteristics of this property. Short Name WaitMode Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Wait

### Advanced:Wait Mode

Specifies how 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 waits for samples to become available.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WaitMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Wait For Interrupt | 12523 | Check for available samples when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates. |
| --- | --- | --- |
| Poll | 12524 | Repeatedly check for available samples as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |
| Yield | 12525 | Repeatedly check for available samples, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency. |
| Sleep | 12547 | Check for available samples once per the amount of time specified in SleepTime . |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr22b0.html language=enus -->
## TOPIC 01370: Advanced:Sleep Time

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr22b0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr22b0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the amount of time to sleep after checking for available samples if WaitMode is Sleep. Remarks The following table lists the characteristics of this property. Short Name SleepTime Data type cdbl.png Permissions Read/Write Resettable True Settable While Task Is Running device-spe

### Advanced:Sleep Time

Specifies in seconds the amount of time to sleep after checking for available samples if 
 [WaitMode](/csh?context=nidaqmx_daqmxprop_attr2232)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr29e6.html language=enus -->
## TOPIC 01371: Status:Overcurrent:Overcurrent Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr29e6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr29e6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read OvercurrentChans . Otherwise, you will receive an error. Remarks The followi

### Status:Overcurrent:Overcurrent Channels Exist

Indicates if the device(s) detected an 
 [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet)
 for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read 
 [OvercurrentChans](/csh?context=nidaqmx_daqmxprop_attr29e7)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr29e7.html language=enus -->
## TOPIC 01372: Status:Overcurrent:Overcurrent Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr29e7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr29e7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition . You must read OvercurrentChansExist before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels t

### Status:Overcurrent:Overcurrent Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any virtual channels in the task for which the device(s) detected an 
 [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet)
 . You must read 
 [OvercurrentChansExist](/csh?context=nidaqmx_daqmxprop_attr29e6)
 before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels to recover.

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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2a09.html language=enus -->
## TOPIC 01373: Status:Open Current Loop:Open Current Loop Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2a09.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2a09.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an open current loop for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read OpenCurrentLoopChans . Otherwise, you will receive an error. Remarks The f

### Status:Open Current Loop:Open Current Loop Channels Exist

Indicates if the device(s) detected an 
 [open current loop](/csh?context=nidaqmx_mxdevconsid_opencurrent)
 for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read 
 [OpenCurrentLoopChans](/csh?context=nidaqmx_daqmxprop_attr2a0a)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2a0a.html language=enus -->
## TOPIC 01374: Status:Open Current Loop:Open Current Loop Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2a0a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2a0a.html
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
 [OpenCurrentLoopChansExist](/csh?context=nidaqmx_daqmxprop_attr2a09)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2a96.html language=enus -->
## TOPIC 01375: Status:Open Thermocouple:Open Thermocouple Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2a96.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2a96.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read OpenThrmcplChans . Otherwise, you will receive an error. Remarks

### Status:Open Thermocouple:Open Thermocouple Channels Exist

Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read 
 [OpenThrmcplChans](/csh?context=nidaqmx_daqmxprop_attr2a97)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OpenThrmcplChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2a97.html language=enus -->
## TOPIC 01376: Status:Open Thermocouple:Open Thermocouple Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2a97.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2a97.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read OpenThrmcplChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. Short N

### Status:Open Thermocouple:Open Thermocouple Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read 
 [OpenThrmcplChansExist](/csh?context=nidaqmx_daqmxprop_attr2a96)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OpenThrmcplChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2a98.html language=enus -->
## TOPIC 01377: Status:Common Mode Range Error:Common Mode Range Error Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2a98.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2a98.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation sta

### Status:Common Mode Range Error:Common Mode Range Error Channels Exist

Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation status for all channels in the task. You must read this property before you read 
 [CommonModeRangeErrorChans](/csh?context=nidaqmx_daqmxprop_attr2a99)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CommonModeRangeErrorChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2a99.html language=enus -->
## TOPIC 01378: Status:Common Mode Range Error:Common Mode Range Error Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2a99.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2a99.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read CommonModeRangeErrorChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of thi

### Status:Common Mode Range Error:Common Mode Range Error Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read 
 [CommonModeRangeErrorChansExist](/csh?context=nidaqmx_daqmxprop_attr2a98)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CommonModeRangeErrorChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2ec4.html language=enus -->
## TOPIC 01379: Logging:File Path

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2ec4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2ec4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the path to the TDMS file to which you want to log data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when DAQmx Start New File is called. New file paths can be specified by ending with "\" or

### Logging:File Path

Specifies the path to the TDMS file to which you want to 
 [log](/csh?context=nidaqmx_mxcncpts_datalogging)
 data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when DAQmx Start New File is called. New file paths can be specified by ending with "\" or "/". Files created after specifying a new file path retain the same name and numbering sequence.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.FilePath |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2ec5.html language=enus -->
## TOPIC 01380: Logging:Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2ec5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2ec5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable logging and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode. Remarks The following table lists th

### Logging:Mode

Specifies whether to enable 
 [logging](/csh?context=nidaqmx_mxcncpts_datalogging)
 and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Off | 10231 | Disable logging for the task. |
| --- | --- | --- |
| Log | 15844 | Enable logging for the task. You cannot read data using DAQmx Read when using this mode. If you require access to the data, read from the TDMS file. |
| Log and Read | 15842 | Enable both logging and reading data for the task. You must use DAQmx Read to read samples for NI-DAQmx to stream them to disk. |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2ec6.html language=enus -->
## TOPIC 01381: Logging:TDMS:Group Name

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2ec6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2ec6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not ex

### Logging:TDMS:Group Name

Specifies the name of the group to create within the 
 [TDMS](/csh?context=nidaqmx_mxcncpts_datalogging)
 file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist. For example, if you specify a group name of Voltage Task, and that group already exists, NI-DAQmx assigns the group name Voltage Task #1, then Voltage Task #2.

For digital input tasks, NI-DAQmx creates a group for each virtual channel in the task. For each created group, NI-DAQmx appends a hyphen and the virtual channel name to the group name.

If you query this property, NI-DAQmx returns the original value specified without any suffixes appended by NI-DAQmx for digital input tasks or for existing groups.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.TDMS.GroupName |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2ec7.html language=enus -->
## TOPIC 01382: Logging:TDMS:Operation

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2ec7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2ec7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to open the TDMS file. Remarks The following table lists the characteristics of this property. Short Name Logging.TDMS.Operation Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Engine True Open 10437 Open an

### Logging:TDMS:Operation

Specifies how to open the 
 [TDMS](/csh?context=nidaqmx_mxcncpts_datalogging)
 file.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.TDMS.Operation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Open | 10437 | Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx returns an error. |
| --- | --- | --- |
| Open or Create | 15846 | Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx creates a new TDMS file. |
| Create or Replace | 15847 | Create a new TDMS file, or replace an existing TDMS file. |
| Create | 15848 | Create a new TDMS file. If the file already exists, NI-DAQmx returns an error. |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2f70.html language=enus -->
## TOPIC 01383: Status:Accessory:Accessory Insertion or Removal Detected

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2f70.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2f70.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevsWithInsertedOrRemovedAccessories . Otherwise, you wi

### Status:Accessory:Accessory Insertion or Removal Detected

Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read 
 [DevsWithInsertedOrRemovedAccessories](/csh?context=nidaqmx_daqmxprop_attr2f71)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2f71.html language=enus -->
## TOPIC 01384: Status:Accessory:Devices with Inserted or Removed Accessories

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2f71.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2f71.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this prope

### Status:Accessory:Devices with Inserted or Removed Accessories

Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read 
 [AccessoryInsertionOrRemovalDetected](/csh?context=nidaqmx_daqmxprop_attr2f70)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2fc3.html language=enus -->
## TOPIC 01385: Logging:File Write Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2fc3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2fc3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes. Remarks The following table lists the characteristics of this property. Short Name Logging.FileWriteSize Data type cu32.png Permissions Read/Write Resettable

### Logging:File Write Size

Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.FileWriteSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2fc6.html language=enus -->
## TOPIC 01386: Logging:File Pre-allocation Size

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2fc6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2fc6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you config

### Logging:File Pre-allocation Size

Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you configure the task to acquire.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.FilePreallocationSize |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2fe3.html language=enus -->
## TOPIC 01387: Logging:Pause

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2fe3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2fe3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether logging is paused while a task is executing. If Logging.Mode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If Logging.Mode is set to Log Only mode, this value is taken into consideration the next t

### Logging:Pause

Specifies whether logging is paused while a task is executing. If 
 [Logging.Mode](/csh?context=nidaqmx_daqmxprop_attr2ec5)
 is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If 
 [Logging.Mode](/csh?context=nidaqmx_daqmxprop_attr2ec5)
 is set to Log Only mode, this value is taken into consideration the next time that data is written to disk. A new TDMS group is written when logging is resumed from a paused state.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.Pause |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr2fe4.html language=enus -->
## TOPIC 01388: Logging:Samples Per File

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr2fe4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr2fe4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of <filename>_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is

### Logging:Samples Per File

Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of &#60;filename&#62;_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\data.tdms, the next file name used is C:\data_0001.tdms. To disable file spanning behavior, set this attribute to 0. If 
 [Logging.FilePath](/csh?context=nidaqmx_daqmxprop_attr2ec4)
 is changed while this attribute is set, the new file path takes effect on the next file created.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Logging.SampsPerFile |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3081.html language=enus -->
## TOPIC 01389: Status:Overtemperature:Overtemperature Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3081.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3081.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read OvertemperatureChans . Otherwise, you will receive an error. Remarks

### Status:Overtemperature:Overtemperature Channels Exist

Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read 
 [OvertemperatureChans](/csh?context=nidaqmx_daqmxprop_attr3082)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3082.html language=enus -->
## TOPIC 01390: Status:Overtemperature:Overtemperature Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3082.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3082.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overtemperature virtual channels. You must read OvertemperatureChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. Short Name OvertemperatureChans Data type c1dstr.png

### Status:Overtemperature:Overtemperature Channels

Indicates a list of names of any overtemperature virtual channels. You must read 
 [OvertemperatureChansExist](/csh?context=nidaqmx_daqmxprop_attr3081)
 before you read this property. Otherwise, you will receive an error.

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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3088.html language=enus -->
## TOPIC 01391: Status:Excitation Fault:Excitation Fault Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3088.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3088.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an excitation fault condition for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read ExcitFaultChans . Otherwise, you will receive an error. Remarks Th

### Status:Excitation Fault:Excitation Fault Channels Exist

Indicates if the device(s) detected an 
 [excitation fault condition](/csh?context=nidaqmx_mxdevconsid_excitationfaultdetection)
 for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read 
 [ExcitFaultChans](/csh?context=nidaqmx_daqmxprop_attr3089)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExcitFaultChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3089.html language=enus -->
## TOPIC 01392: Status:Excitation Fault:Excitation Fault Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3089.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3089.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition . You must read ExcitFaultChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this propert

### Status:Excitation Fault:Excitation Fault Channels

Indicates a 
 [list of names](/csh?context=nidaqmx_mxcncpts_physchannames)
 of any virtual channels in the task for which the device(s) detected an 
 [excitation fault condition](/csh?context=nidaqmx_mxdevconsid_excitationfaultdetection)
 . You must read 
 [ExcitFaultChansExist](/csh?context=nidaqmx_daqmxprop_attr3088)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ExcitFaultChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3100.html language=enus -->
## TOPIC 01393: Status:Open Channels:Open Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3100.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3100.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before you read OpenChans . Otherwise, you will receive an error. Remarks The foll

### Status:Open Channels:Open Channels Exist

Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before you read 
 [OpenChans](/csh?context=nidaqmx_daqmxprop_attr3101)
 . Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OpenChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3101.html language=enus -->
## TOPIC 01394: Status:Open Channels:Open Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3101.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3101.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any open virtual channels. You must read OpenChansExist before you read this property. Otherwise you will receive an error. Remarks The following table lists the characteristics of this property. Short Name OpenChans Data type c1dstr.png Permissions Read Only Resettable

### Status:Open Channels:Open Channels

Indicates a list of names of any open virtual channels. You must read 
 [OpenChansExist](/csh?context=nidaqmx_daqmxprop_attr3100)
 before you read this property. Otherwise you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OpenChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3102.html language=enus -->
## TOPIC 01395: Status:Open Channels:Open Channels Details

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3102.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3102.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of details of any open virtual channels. You must read OpenChansExist before you read this property. Otherwise you will receive an error. Remarks The following table lists the characteristics of this property. Short Name OpenChansDetails Data type c1dstr.png Permissions Read Only Re

### Status:Open Channels:Open Channels Details

Indicates a list of details of any open virtual channels. You must read 
 [OpenChansExist](/csh?context=nidaqmx_daqmxprop_attr3100)
 before you read this property. Otherwise you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OpenChansDetails |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3118.html language=enus -->
## TOPIC 01396: Status:Phase-Locked Loop:Unlocked Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3118.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3118.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition. Remarks The following table lists the characteristics of this property. Short Name PLL.UnlockedChansExist Data t

### Status:Phase-Locked Loop:Unlocked Channels Exist

Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PLL.UnlockedChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3119.html language=enus -->
## TOPIC 01397: Status:Phase-Locked Loop:Unlocked Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3119.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3119.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the channels that had their PLLs unlock. Remarks The following table lists the characteristics of this property. Short Name PLL.UnlockedChans Data type c1dstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Status:Phase-Locked Loop:Unlocked Channels

Indicates the channels that had their PLLs unlock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PLL.UnlockedChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr313d.html language=enus -->
## TOPIC 01398: Status:Synchronization:Unlocked Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr313d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr313d.html
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr313e.html language=enus -->
## TOPIC 01399: Status:Synchronization:Unlocked Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr313e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr313e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the channels from devices in an unlocked target. Remarks The following table lists the characteristics of this property. Short Name Sync.UnlockedChans Data type c1dstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine Tru

### Status:Synchronization:Unlocked Channels

Indicates the channels from devices in an unlocked target.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sync.UnlockedChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr318f.html language=enus -->
## TOPIC 01400: Status:Input Limits Fault:Input Limits Fault Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr318f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr318f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read InputLimitsFaultChans

### Status:Input Limits Fault:Input Limits Fault Channels Exist

Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read 
 [InputLimitsFaultChans](/csh?context=nidaqmx_daqmxprop_attr3190)
 . Otherwise, you will receive an error. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | InputLimitsFaultChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3190.html language=enus -->
## TOPIC 01401: Status:Input Limits Fault:Input Limits Fault Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3190.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3190.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read InputLimitsFaultChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of

### Status:Input Limits Fault:Input Limits Fault Channels

Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read 
 [InputLimitsFaultChansExist](/csh?context=nidaqmx_daqmxprop_attr318f)
 before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | InputLimitsFaultChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3192.html language=enus -->
## TOPIC 01402: Status:Power Supply Fault:Power Supply Fault Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3192.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3192.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read PowerSupplyFaultChans . Otherwise, you will receive an

### Status:Power Supply Fault:Power Supply Fault Channels Exist

Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read 
 [PowerSupplyFaultChans](/csh?context=nidaqmx_daqmxprop_attr3193)
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr3193.html language=enus -->
## TOPIC 01403: Status:Power Supply Fault:Power Supply Fault Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr3193.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr3193.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the virtual channels that have detected a power supply fault. You must read PowerSupplyFaultChansExist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characteristics of this property. Short Name PowerSupplyFaultChans Data type c1d

### Status:Power Supply Fault:Power Supply Fault Channels

Indicates the virtual channels that have detected a power supply fault. You must read 
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

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr31dd.html language=enus -->
## TOPIC 01404: Status:Remote Sense Error:Remote Sense Error Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr31dd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr31dd.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. You must read this property before you read the Remote Sense Error Channels property.

### Status:Remote Sense Error:Remote Sense Error Channels Exist

Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. You must read this property before you read the Remote Sense Error Channels property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RemoteSenseErrorChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr31de.html language=enus -->
## TOPIC 01405: Status:Remote Sense Error:Remote Sense Error Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr31de.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr31de.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise, you will receive an error. Remarks The following table lists the characterist

### Status:Remote Sense Error:Remote Sense Error Channels

Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RemoteSenseErrorChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr31df.html language=enus -->
## TOPIC 01406: Status:Aux Power Error:Aux Power Error Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr31df.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr31df.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Aux Power Error Channels property. Otherwise, you will rece

### Status:Aux Power Error:Aux Power Error Channels Exist

Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Aux Power Error Channels property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AuxPowerErrorChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr31e0.html language=enus -->
## TOPIC 01407: Status:Aux Power Error:Aux Power Error Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr31e0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr31e0.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Otherwise, you will receive an error. Remarks The following table lists the ch

### Status:Aux Power Error:Aux Power Error Channels

Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AuxPowerErrorChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr31e6.html language=enus -->
## TOPIC 01408: Status:Reverse Voltage Error:Reverse Voltage Error Channels Exist

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr31e6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr31e6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property clears the error condition status for all channels in the task. You must read this proper

### Status:Reverse Voltage Error:Reverse Voltage Error Channels Exist

Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Reverse Voltage Error Channels property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ReverseVoltageErrorChansExist |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-read/attr31e7.html language=enus -->
## TOPIC 01409: Status:Reverse Voltage Error:Reverse Voltage Error Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-read/attr31e7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-read/attr31e7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Otherwise, you will receive an error. Remarks The following table lists the charac

### Status:Reverse Voltage Error:Reverse Voltage Error Channels

Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Otherwise, you will receive an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ReverseVoltageErrorChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Read Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-real-time-p.html language=enus -->
## TOPIC 01410: DAQmx Real-Time Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-real-time-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-real-time-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Real-Time properties to configure error reporting and recovery options for deterministic applications.

### DAQmx Real-Time Properties

Use the DAQmx Real-Time properties to configure error reporting and recovery options for deterministic applications.

- [Convert Late Errors To Warnings](../../../resource/objmgr/daqmx-rc/daqmx-real-time/attr22ee.html) Specifies if DAQmx Wait for Next Sample Clock , DAQmx Read , and DAQmx Write convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with NumOfWarmupIters execute.
- [Number Of Warmup Iterations](../../../resource/objmgr/daqmx-rc/daqmx-real-time/attr22ed.html) Specifies the number of loop iterations that must occur before DAQmx Wait for Next Sample Clock and DAQmx Read return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system.
- [Report Missed Samples](../../../resource/objmgr/daqmx-rc/daqmx-real-time/attr2319.html) Specifies whether DAQmx Read returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect DAQmx Wait for Next Sample Clock . Set this property to TRUE for applications that need to detect lateness without using DAQmx Wait for Next Sample Clock .
- [Wait For Next Sample Clock Wait Mode](../../../resource/objmgr/daqmx-rc/daqmx-real-time/attr22ef.html) Specifies how DAQmx Wait for Next Sample Clock waits for the next Sample Clock pulse.
- [Write Recovery Mode](../../../resource/objmgr/daqmx-rc/daqmx-real-time/attr231a.html) Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-real-time/attr22ed.html language=enus -->
## TOPIC 01411: Number Of Warmup Iterations

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-real-time/attr22ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-real-time/attr22ed.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of loop iterations that must occur before DAQmx Wait for Next Sample Clock and DAQmx Read return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be lat

### Number Of Warmup Iterations

Specifies the number of loop iterations that must occur before 
 [DAQmx Wait for Next Sample Clock](/csh?context=nidaqmx_lvdaqmx_mxwaitforsc)
 and 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumOfWarmupIters |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Real-Time Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-real-time/attr22ee.html language=enus -->
## TOPIC 01412: Convert Late Errors To Warnings

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-real-time/attr22ee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-real-time/attr22ee.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if DAQmx Wait for Next Sample Clock , DAQmx Read , and DAQmx Write convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with NumOfWarmupIters execute. Remarks The following table lists the characteristics of this pro

### Convert Late Errors To Warnings

Specifies if 
 [DAQmx Wait for Next Sample Clock](/csh?context=nidaqmx_lvdaqmx_mxwaitforsc)
 , 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 , and 
 [DAQmx Write](/csh?context=nidaqmx_lvdaqmx_mxwrite)
 convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with 
 [NumOfWarmupIters](/csh?context=nidaqmx_daqmxprop_attr22ed)
 execute.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ConvLateErrorsToWarnings |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Real-Time Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-real-time/attr22ef.html language=enus -->
## TOPIC 01413: Wait For Next Sample Clock Wait Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-real-time/attr22ef.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-real-time/attr22ef.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how DAQmx Wait for Next Sample Clock waits for the next Sample Clock pulse. Remarks The following table lists the characteristics of this property. Short Name WaitForNextSampClkWaitMode Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific

### Wait For Next Sample Clock Wait Mode

Specifies how 
 [DAQmx Wait for Next Sample Clock](/csh?context=nidaqmx_lvdaqmx_mxwaitforsc)
 waits for the next Sample Clock pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WaitForNextSampClkWaitMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Wait For Interrupt | 12523 | Check for Sample Clock pulses when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates. |
| --- | --- | --- |
| Poll | 12524 | Repeatedly check for Sample Clock pulses as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |

Parent topic:

DAQmx Real-Time Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-real-time/attr2319.html language=enus -->
## TOPIC 01414: Report Missed Samples

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-real-time/attr2319.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-real-time/attr2319.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether DAQmx Read returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect DAQmx Wait for Next Sample Clock . Set this property to TRUE for applications that need to detect lateness without using DAQmx Wait for Next Sample Clock . Remark

### Report Missed Samples

Specifies whether 
 [DAQmx Read](/csh?context=nidaqmx_lvdaqmx_mxread)
 returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect 
 [DAQmx Wait for Next Sample Clock](/csh?context=nidaqmx_lvdaqmx_mxwaitforsc)
 . Set this property to TRUE for 
 [applications](/csh?context=nidaqmx_mxcncpts_readwritelate)
 that need to detect lateness without using 
 [DAQmx Wait for Next Sample Clock](/csh?context=nidaqmx_lvdaqmx_mxwaitforsc)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ReportMissedSamp |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Real-Time Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-real-time/attr231a.html language=enus -->
## TOPIC 01415: Write Recovery Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-real-time/attr231a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-real-time/attr231a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. Remarks The following table lists the characteristics of this property. Short Name WriteRecoveryMode Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running

### Write Recovery Mode

Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WriteRecoveryMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Wait For Interrupt | 12523 | Attempt to recover when the system receives an interrupt service request. This mode is the most CPU efficient and best suited for recovery at lower pulse train frequencies. |
| --- | --- | --- |
| Poll | 12524 | Repeatedly attempt to recover as fast as possible. This mode has the highest probability of recovery success at the expense of CPU efficiency. |

Parent topic:

DAQmx Real-Time Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale-p.html language=enus -->
## TOPIC 01416: DAQmx Scale Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Scale properties to configure custom scales .

### DAQmx Scale Properties

Use the DAQmx Scale properties to configure 
 [custom scales](/csh?context=nidaqmx_mxcncpts_customscales)
 .

- [Active Scale](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr175c.html) Specifies the name of the custom scale to modify.
- [Description](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1226.html) Specifies a description for the scale.
- [Linear:Slope](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1227.html) Specifies the slope, m, in the equation y=mx+b.
- [Linear:Y-Intercept](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1228.html) Specifies the y-intercept, b, in the equation y=mx+b.
- [Map:Pre-Scaled Maximum Value](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1231.html) Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to Map.ScaledMax .
- [Map:Pre-Scaled Minimum Value](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1232.html) Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to Map.ScaledMin .
- [Map:Scaled Maximum Value](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1229.html) Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to Map.PreScaledMax . Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value.
- [Map:Scaled Minimum Value](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1230.html) Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to Map.PreScaledMin . Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value.
- [Polynomial:Forward Coefficients](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1234.html) Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.
- [Polynomial:Reverse Coefficients](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1235.html) Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y^3.
- [Pre-Scaled Units](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr18f7.html) Specifies the units of the values that you want to scale.
- [Scale Type](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1929.html) Indicates the method or equation form that the custom scale uses.
- [Scaled Units](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr191b.html) Specifies the units to use for scaled values. You can use an arbitrary string.
- [Table:Pre-Scaled Values](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1237.html) Specifies an array of pre-scaled values. These values map directly to the values in Table.ScaledVals .
- [Table:Scaled Values](../../../resource/objmgr/daqmx-rc/daqmx-scale/attr1236.html) Specifies an array of scaled values. These values map directly to the values in Table.PreScaledVals .

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1226.html language=enus -->
## TOPIC 01417: Description

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1226.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1226.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a description for the scale. Remarks The following table lists the characteristics of this property. Short Name Descr Data type cstr.png Permissions Read/Write Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Description

Specifies a description for the scale.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Descr |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1227.html language=enus -->
## TOPIC 01418: Linear:Slope

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1227.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1227.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the slope, m, in the equation y=mx+b. Remarks The following table lists the characteristics of this property. Short Name Lin.Slope Data type cdbl.png Permissions Read/Write Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Linear:Slope

Specifies the slope, m, in the equation y=mx+b.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Lin.Slope |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1228.html language=enus -->
## TOPIC 01419: Linear:Y-Intercept

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1228.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1228.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the y-intercept, b, in the equation y=mx+b. Remarks The following table lists the characteristics of this property. Short Name Lin.YIntercept Data type cdbl.png Permissions Read/Write Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Linear:Y-Intercept

Specifies the y-intercept, b, in the equation y=mx+b.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Lin.YIntercept |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1229.html language=enus -->
## TOPIC 01420: Map:Scaled Maximum Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1229.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1229.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to Map.PreScaledMax . Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value. Remarks The following table lists the characteristic

### Map:Scaled Maximum Value

Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to 
 [Map.PreScaledMax](/csh?context=nidaqmx_daqmxprop_attr1231)
 . Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Map.ScaledMax |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1230.html language=enus -->
## TOPIC 01421: Map:Scaled Minimum Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1230.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1230.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to Map.PreScaledMin . Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value. Remarks The following table lists the characteris

### Map:Scaled Minimum Value

Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to 
 [Map.PreScaledMin](/csh?context=nidaqmx_daqmxprop_attr1232)
 . Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Map.ScaledMin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1231.html language=enus -->
## TOPIC 01422: Map:Pre-Scaled Maximum Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1231.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1231.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to Map.ScaledMax . Remarks The following table lists the characteristics of this property. Short Name Map.PreScaledMax Data type cdbl.png Permissions Read/Write Resettable False Settable While Task Is Running dev

### Map:Pre-Scaled Maximum Value

Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to 
 [Map.ScaledMax](/csh?context=nidaqmx_daqmxprop_attr1229)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Map.PreScaledMax |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1232.html language=enus -->
## TOPIC 01423: Map:Pre-Scaled Minimum Value

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1232.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1232.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to Map.ScaledMin . Remarks The following table lists the characteristics of this property. Short Name Map.PreScaledMin Data type cdbl.png Permissions Read/Write Resettable False Settable While Task Is Running de

### Map:Pre-Scaled Minimum Value

Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to 
 [Map.ScaledMin](/csh?context=nidaqmx_daqmxprop_attr1230)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Map.PreScaledMin |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1234.html language=enus -->
## TOPIC 01424: Polynomial:Forward Coefficients

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1234.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1234.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. Remarks The following table lists the chara

### Polynomial:Forward Coefficients

Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Poly.ForwardCoeff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1235.html language=enus -->
## TOPIC 01425: Polynomial:Reverse Coefficients

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1235.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1235.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y^3. Remarks The following table lists the chara

### Polynomial:Reverse Coefficients

Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y^3.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Poly.ReverseCoeff |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1236.html language=enus -->
## TOPIC 01426: Table:Scaled Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1236.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1236.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of scaled values. These values map directly to the values in Table.PreScaledVals . Remarks The following table lists the characteristics of this property. Short Name Table.ScaledVals Data type c1ddbl.png Permissions Read/Write Resettable False Settable While Task Is Running device

### Table:Scaled Values

Specifies an array of scaled values. These values map directly to the values in 
 [Table.PreScaledVals](/csh?context=nidaqmx_daqmxprop_attr1237)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Table.ScaledVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1237.html language=enus -->
## TOPIC 01427: Table:Pre-Scaled Values

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1237.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1237.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of pre-scaled values. These values map directly to the values in Table.ScaledVals . Remarks The following table lists the characteristics of this property. Short Name Table.PreScaledVals Data type c1ddbl.png Permissions Read/Write Resettable False Settable While Task Is Running de

### Table:Pre-Scaled Values

Specifies an array of pre-scaled values. These values map directly to the values in 
 [Table.ScaledVals](/csh?context=nidaqmx_daqmxprop_attr1236)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Table.PreScaledVals |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr175c.html language=enus -->
## TOPIC 01428: Active Scale

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr175c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr175c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the custom scale to modify. Remarks The following table lists the characteristics of this property. Short Name ActiveScale Data type cdaqmxscale.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Active Scale

Specifies the name of the 
 [custom scale](/csh?context=nidaqmx_mxcncpts_customscales)
 to modify.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveScale |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr18f7.html language=enus -->
## TOPIC 01429: Pre-Scaled Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr18f7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr18f7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the values that you want to scale. Remarks The following table lists the characteristics of this property. Short Name PreScaledUnits Data type ci32.png Permissions Read/Write Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Volt

### Pre-Scaled Units

Specifies the units of the values that you want to scale.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PreScaledUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Volts | 10348 | Volts. |
| --- | --- | --- |
| Amps | 10342 | Amperes. |
| Watts | 16203 | Watts. |
| Deg F | 10144 | Degrees Fahrenheit. |
| Deg C | 10143 | Degrees Celsius. |
| Deg R | 10145 | Degrees Rankine. |
| Kelvins | 10325 | Kelvins. |
| Strain | 10299 | Strain. |
| Ohms | 10384 | Ohms. |
| Hz | 10373 | Hertz. |
| Seconds | 10364 | Seconds. |
| Meters | 10219 | Meters. |
| Inches | 10379 | Inches. |
| Degrees | 10146 | Degrees. |
| Radians | 10273 | Radians. |
| Ticks | 10304 | Ticks. |
| RPM | 16080 | Revolutions per minute. |
| Radians/s | 16081 | Radians per second. |
| Degrees/s | 16082 | Degrees per second. |
| g | 10186 | 1 g is approximately equal to 9.81 m/s/s. |
| m/s^2 | 12470 | Meters per second per second. |
| in/s^2 | 12471 | Inches per second per second. |
| m/s | 15959 | Meters per second. |
| in/s | 15960 | Inches per second. |
| Pascals | 10081 | Pascals. |
| Newtons | 15875 | Newtons. |
| Pounds | 15876 | Pounds. |
| kgf | 15877 | Kilograms-force. |
| psi | 15879 | Pounds per square inch. |
| bar | 15880 | Bar. |
| Nm | 15881 | Newton meters. |
| oz-in | 15882 | Ounce-inches. |
| lb-in | 15883 | Pound-inches. |
| lb-ft | 15884 | Pound-feet. |
| Volts/Volt | 15896 | Volts per volt. |
| mVolts/Volt | 15897 | Millivolts per volt. |
| Coulombs | 16102 | Coulombs. |
| PicoCoulombs | 16103 | PicoCoulombs. |
| From TEDS | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr191b.html language=enus -->
## TOPIC 01430: Scaled Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr191b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr191b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use for scaled values. You can use an arbitrary string. Remarks The following table lists the characteristics of this property. Short Name ScaledUnits Data type cstr.png Permissions Read/Write Resettable False Settable While Task Is Running device-specific Available in Run-Tim

### Scaled Units

Specifies the units to use for scaled values. You can use an arbitrary string.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ScaledUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-scale/attr1929.html language=enus -->
## TOPIC 01431: Scale Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-scale/attr1929.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-scale/attr1929.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the method or equation form that the custom scale uses. Remarks The following table lists the characteristics of this property. Short Name ScaleType Data type ci32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Li

### Scale Type

Indicates the method or equation form that the 
 [custom scale](/csh?context=nidaqmx_mxcncpts_customscales)
 uses.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ScaleType |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Linear | 10447 | Scale values by using the equation y=mx+b, where x is a prescaled value and y is a scaled value. |
| --- | --- | --- |
| Map Ranges | 10448 | Scale values proportionally from a range of pre-scaled values to a range of scaled values. |
| Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |
| Table | 10450 | Map an array of pre-scaled values to an array of corresponding scaled values, with all other values scaled proportionally. |

Parent topic:

DAQmx Scale Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel-p.html language=enus -->
## TOPIC 01432: DAQmx Switch Channel Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Switch Channel properties to modify the usage of a switch channel and to query the capabilities of a switch channel.

### DAQmx Switch Channel Properties

Use the DAQmx Switch Channel properties to modify the usage of a switch channel and to query the capabilities of a switch channel.

- [Active Switch Channel](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e3.html) Specifies the switch channel to which the subsequent properties apply.
- [Deprecated:Analog Bus Sharing Enable](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr2f9e.html) (Deprecated) Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to TRUE to enable sharing on the channel that connects to the analog bus line. Analog bus sharing is disabled by default.
- [Deprecated:Capability:Bandwidth](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr640.html) (Deprecated) Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration.
- [Deprecated:Capability:Impedance](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr641.html) (Deprecated) Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads.
- [Deprecated:Capability:Max AC Carry Current](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr648.html) (Deprecated) Indicates in amperes the maximum AC current that the device can carry.
- [Deprecated:Capability:Max AC Carry Power](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr642.html) (Deprecated) Indicates in watts the maximum AC power that the device can carry.
- [Deprecated:Capability:Max AC Switching Current](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr646.html) (Deprecated) Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level.
- [Deprecated:Capability:Max AC Switching Power](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr644.html) (Deprecated) Indicates in watts the maximum AC power that the device can switch.
- [Deprecated:Capability:Max AC Voltage](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr651.html) (Deprecated) Indicates in volts the maximum AC RMS voltage that the device can switch.
- [Deprecated:Capability:Max DC Carry Current](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr647.html) (Deprecated) Indicates in amperes the maximum DC current that the device can carry.
- [Deprecated:Capability:Max DC Carry Power](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr643.html) (Deprecated) Indicates in watts the maximum DC power that the device can carry.
- [Deprecated:Capability:Max DC Switching Current](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr645.html) (Deprecated) Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level.
- [Deprecated:Capability:Max DC Switching Power](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr649.html) (Deprecated) Indicates in watts the maximum DC power that the device can switch.
- [Deprecated:Capability:Max DC Voltage](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr650.html) (Deprecated) Indicates in volts the maximum DC voltage that the device can switch.
- [Deprecated:Capability:Wire Mode](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e5.html) (Deprecated) Indicates the number of wires that the channel switches.
- [Deprecated:Usage](../../../resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e4.html) (Deprecated) Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e3.html language=enus -->
## TOPIC 01433: Active Switch Channel

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e3.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the switch channel to which the subsequent properties apply. Remarks The following table lists the characteristics of this property. Short Name ActiveSwitchChan Data type cdaqmxscale.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run

### Active Switch Channel

Specifies the switch channel to which the subsequent properties apply.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveSwitchChan |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e4.html language=enus -->
## TOPIC 01434: Deprecated:Usage

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e4.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. Remarks The following table lists the characteristics of this property. Short Name Usage Data type ci32.png Permissions Read/Write Reset

### Deprecated:Usage

(Deprecated) Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Usage |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Source | 10439 | You can use the channel only as an input for a signal. |
| --- | --- | --- |
| Load | 10440 | You can use the channel only as the output for a signal passing through the switch. |
| Reserved for Routing | 10441 | You can use the channel only to complete routes within a switch. |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e5.html language=enus -->
## TOPIC 01435: Deprecated:Capability:Wire Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr18e5.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates the number of wires that the channel switches. Remarks The following table lists the characteristics of this property. Short Name WireMode Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Deprecated:Capability:Wire Mode

(Deprecated) Indicates the number of wires that the channel switches.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WireMode |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr2f9e.html language=enus -->
## TOPIC 01436: Deprecated:Analog Bus Sharing Enable

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr2f9e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr2f9e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to TRUE to enable sharing on the channel that connects to the analog bus line. Analog bus sh

### Deprecated:Analog Bus Sharing Enable

(Deprecated) Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to TRUE to enable sharing on the channel that connects to the analog bus line. Analog bus sharing is disabled by default.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AnlgBusSharingEnable |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr640.html language=enus -->
## TOPIC 01437: Deprecated:Capability:Bandwidth

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr640.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr640.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration. Remarks The following table lists the characteristics of this property. Short Name Bandwidth Data type cdbl.png Permissions Read Only Resettable False Settable While

### Deprecated:Capability:Bandwidth

(Deprecated) Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Bandwidth |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr641.html language=enus -->
## TOPIC 01438: Deprecated:Capability:Impedance

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr641.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr641.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads. Remarks The following table lists the characteristics of this property. Short Name Impedance Data type cdbl.png Permissions Read Only Resettable Fals

### Deprecated:Capability:Impedance

(Deprecated) Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Impedance |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr642.html language=enus -->
## TOPIC 01439: Deprecated:Capability:Max AC Carry Power

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr642.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr642.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in watts the maximum AC power that the device can carry. Remarks The following table lists the characteristics of this property. Short Name MaxACCarryPwr Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-T

### Deprecated:Capability:Max AC Carry Power

(Deprecated) Indicates in watts the maximum AC power that the device can carry.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxACCarryPwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr643.html language=enus -->
## TOPIC 01440: Deprecated:Capability:Max DC Carry Power

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr643.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr643.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in watts the maximum DC power that the device can carry. Remarks The following table lists the characteristics of this property. Short Name MaxDCCarryPwr Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-T

### Deprecated:Capability:Max DC Carry Power

(Deprecated) Indicates in watts the maximum DC power that the device can carry.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxDCCarryPwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr644.html language=enus -->
## TOPIC 01441: Deprecated:Capability:Max AC Switching Power

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr644.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr644.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in watts the maximum AC power that the device can switch. Remarks The following table lists the characteristics of this property. Short Name MaxACSwitchPwr Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run

### Deprecated:Capability:Max AC Switching Power

(Deprecated) Indicates in watts the maximum AC power that the device can switch.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxACSwitchPwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr645.html language=enus -->
## TOPIC 01442: Deprecated:Capability:Max DC Switching Current

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr645.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr645.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level. Remarks The following table lists the characteristics of this property. Short Name MaxDCSwitchCurrent Data type cdbl.png Permissions Read Only Resettable False Sett

### Deprecated:Capability:Max DC Switching Current

(Deprecated) Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxDCSwitchCurrent |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr646.html language=enus -->
## TOPIC 01443: Deprecated:Capability:Max AC Switching Current

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr646.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr646.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level. Remarks The following table lists the characteristics of this property. Short Name MaxACSwitchCurrent Data type cdbl.png Permissions Read Only Resettable False Se

### Deprecated:Capability:Max AC Switching Current

(Deprecated) Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxACSwitchCurrent |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr647.html language=enus -->
## TOPIC 01444: Deprecated:Capability:Max DC Carry Current

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr647.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr647.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in amperes the maximum DC current that the device can carry. Remarks The following table lists the characteristics of this property. Short Name MaxDCCarryCurrent Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available

### Deprecated:Capability:Max DC Carry Current

(Deprecated) Indicates in amperes the maximum DC current that the device can carry.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxDCCarryCurrent |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr648.html language=enus -->
## TOPIC 01445: Deprecated:Capability:Max AC Carry Current

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr648.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr648.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in amperes the maximum AC current that the device can carry. Remarks The following table lists the characteristics of this property. Short Name MaxACCarryCurrent Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available

### Deprecated:Capability:Max AC Carry Current

(Deprecated) Indicates in amperes the maximum AC current that the device can carry.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxACCarryCurrent |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr649.html language=enus -->
## TOPIC 01446: Deprecated:Capability:Max DC Switching Power

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr649.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr649.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in watts the maximum DC power that the device can switch. Remarks The following table lists the characteristics of this property. Short Name MaxDCSwitchPwr Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run

### Deprecated:Capability:Max DC Switching Power

(Deprecated) Indicates in watts the maximum DC power that the device can switch.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxDCSwitchPwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr650.html language=enus -->
## TOPIC 01447: Deprecated:Capability:Max DC Voltage

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr650.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr650.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in volts the maximum DC voltage that the device can switch. Remarks The following table lists the characteristics of this property. Short Name MaxDCVoltage Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run

### Deprecated:Capability:Max DC Voltage

(Deprecated) Indicates in volts the maximum DC voltage that the device can switch.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxDCVoltage |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-channel/attr651.html language=enus -->
## TOPIC 01448: Deprecated:Capability:Max AC Voltage

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-channel/attr651.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-channel/attr651.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates in volts the maximum AC RMS voltage that the device can switch. Remarks The following table lists the characteristics of this property. Short Name MaxACVoltage Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in

### Deprecated:Capability:Max AC Voltage

(Deprecated) Indicates in volts the maximum AC RMS voltage that the device can switch.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MaxACVoltage |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Channel Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device-p.html language=enus -->
## TOPIC 01449: DAQmx Switch Device Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Switch Device properties to configure and query the capabilities of switch devices.

### DAQmx Switch Device Properties

Use the DAQmx Switch Device properties to configure and query the capabilities of switch devices.

- [Active Device](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr1869.html) Specifies the switch device to which the subsequent properties apply.
- [Deprecated:Auto Connect Analog Bus](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr17da.html) (Deprecated) Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property.
- [Deprecated:Capability:Number of Columns](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr18ea.html) (Deprecated) Indicates the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology.
- [Deprecated:Capability:Number of Relays](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e6.html) (Deprecated) Indicates the number of relays on the device. This value matches the number of relay names in RelayList .
- [Deprecated:Capability:Number of Rows](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e9.html) (Deprecated) Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology.
- [Deprecated:Capability:Number of Switch Channels](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e8.html) (Deprecated) Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in SwitchChanList .
- [Deprecated:Capability:Relay List](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr17dc.html) (Deprecated) Indicates a comma-delimited list of relay names.
- [Deprecated:Capability:Switch Channel List](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e7.html) (Deprecated) Indicates a comma-delimited list of channel names for the current topology of the device.
- [Deprecated:Is Settled](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr1243.html) (Deprecated) Indicates when SettlingTime expires.
- [Deprecated:Power Down Latching Relays After Settling](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr22db.html) (Deprecated) Specifies if DAQmx Switch Wait for Settling powers down latching relays after waiting for the device to settle.
- [Deprecated:Settling Time](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr1244.html) (Deprecated) Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times.
- [Deprecated:Temperature](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr301a.html) (Deprecated) Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information.
- [Deprecated:Topology](../../../resource/objmgr/daqmx-rc/daqmx-switch-device/attr193d.html) (Deprecated) Indicates the current topology of the device. This value is one of the topology options in DAQmx Switch Set Topology and Reset .

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr1243.html language=enus -->
## TOPIC 01450: Deprecated:Is Settled

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr1243.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr1243.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates when SettlingTime expires. Remarks The following table lists the characteristics of this property. Short Name Settled Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Deprecated:Is Settled

(Deprecated) Indicates when 
 [SettlingTime](/csh?context=nidaqmx_daqmxprop_attr1244)
 expires.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Settled |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr1244.html language=enus -->
## TOPIC 01451: Deprecated:Settling Time

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr1244.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr1244.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for

### Deprecated:Settling Time

(Deprecated) Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SettlingTime |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr17da.html language=enus -->
## TOPIC 01452: Deprecated:Auto Connect Analog Bus

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr17da.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr17da.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property. Remarks The following table lists the characteristics of this property. Short Name AutoConnAnlgBus Data type cbool.png Permissions Read/Write Resettable

### Deprecated:Auto Connect Analog Bus

(Deprecated) Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AutoConnAnlgBus |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr17dc.html language=enus -->
## TOPIC 01453: Deprecated:Capability:Relay List

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr17dc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr17dc.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates a comma-delimited list of relay names. Remarks The following table lists the characteristics of this property. Short Name RelayList Data type cstr.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Deprecated:Capability:Relay List

(Deprecated) Indicates a comma-delimited list of relay names.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RelayList |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr1869.html language=enus -->
## TOPIC 01454: Active Device

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr1869.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr1869.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the switch device to which the subsequent properties apply. Remarks The following table lists the characteristics of this property. Short Name ActiveDev Data type cdaqmxscale.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run-Time En

### Active Device

Specifies the switch device to which the subsequent properties apply.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveDev |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e6.html language=enus -->
## TOPIC 01455: Deprecated:Capability:Number of Relays

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e6.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates the number of relays on the device. This value matches the number of relay names in RelayList . Remarks The following table lists the characteristics of this property. Short Name NumRelays Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running

### Deprecated:Capability:Number of Relays

(Deprecated) Indicates the number of relays on the device. This value matches the number of relay names in 
 [RelayList](/csh?context=nidaqmx_daqmxprop_attr17dc)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumRelays |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e7.html language=enus -->
## TOPIC 01456: Deprecated:Capability:Switch Channel List

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e7.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates a comma-delimited list of channel names for the current topology of the device. Remarks The following table lists the characteristics of this property. Short Name SwitchChanList Data type cstr.png Permissions Read Only Resettable False Settable While Task Is Running device-spe

### Deprecated:Capability:Switch Channel List

(Deprecated) Indicates a comma-delimited list of channel names for the current topology of the device.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SwitchChanList |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e8.html language=enus -->
## TOPIC 01457: Deprecated:Capability:Number of Switch Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e8.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in SwitchChanList . Remarks The following table lists the characteristics of this property. Short Name NumSwitchChans Data type cu32.png Permissions Read Only R

### Deprecated:Capability:Number of Switch Channels

(Deprecated) Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in 
 [SwitchChanList](/csh?context=nidaqmx_daqmxprop_attr18e7)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumSwitchChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e9.html language=enus -->
## TOPIC 01458: Deprecated:Capability:Number of Rows

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr18e9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology. Remarks The following table lists the characteristics of this property. Short Name NumRows Data type cu32.png Permissions Read Only Resettabl

### Deprecated:Capability:Number of Rows

(Deprecated) Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumRows |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr18ea.html language=enus -->
## TOPIC 01459: Deprecated:Capability:Number of Columns

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr18ea.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr18ea.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology. Remarks The following table lists the characteristics of this property. Short Name NumColumns Data type cu32.png Permissions Read Only Resettable False Set

### Deprecated:Capability:Number of Columns

(Deprecated) Indicates the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumColumns |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr193d.html language=enus -->
## TOPIC 01460: Deprecated:Topology

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr193d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr193d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates the current topology of the device. This value is one of the topology options in DAQmx Switch Set Topology and Reset . Remarks The following table lists the characteristics of this property. Short Name Topology Data type cstr.png Permissions Read Only Resettable False Settable

### Deprecated:Topology

(Deprecated) Indicates the current topology of the device. This value is one of the topology options in 
 [DAQmx Switch Set Topology and Reset](/csh?context=nidaqmx_lvdaqmx_mxswitchsettopologyandreset)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Topology |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr22db.html language=enus -->
## TOPIC 01461: Deprecated:Power Down Latching Relays After Settling

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr22db.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr22db.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies if DAQmx Switch Wait for Settling powers down latching relays after waiting for the device to settle. Remarks The following table lists the characteristics of this property. Short Name PwrDownLatchRelaysAfterSettling Data type cbool.png Permissions Read/Write Resettable False

### Deprecated:Power Down Latching Relays After Settling

(Deprecated) Specifies if 
 [DAQmx Switch Wait for Settling](/csh?context=nidaqmx_lvdaqmx_mxswitchwaitforsettling)
 powers down latching relays after waiting for the device to settle.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PwrDownLatchRelaysAfterSettling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-device/attr301a.html language=enus -->
## TOPIC 01462: Deprecated:Temperature

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-device/attr301a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-device/attr301a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information. Remarks The following table lists the characteristics of this property. Short Name Temp Data type cdbl.png Permissions Read Only Resettable False S

### Deprecated:Temperature

(Deprecated) Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Temp |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Device Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-scan-p.html language=enus -->
## TOPIC 01463: DAQmx Switch Scan Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-scan-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-scan-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Switch Scan properties to configure the behavior of a switch scanning task.

### DAQmx Switch Scan Properties

Use the DAQmx Switch Scan properties to configure the behavior of a switch scanning task.

- [Deprecated:Break Mode](../../../resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1247.html) (Deprecated) Specifies the action to take between each entry in a scan list.
- [Deprecated:Is Waiting For Advance](../../../resource/objmgr/daqmx-rc/daqmx-switch-scan/attr17d9.html) (Deprecated) Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list.
- [Deprecated:Repeat Mode](../../../resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1248.html) (Deprecated) Specifies if the task advances through the scan list multiple times.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1247.html language=enus -->
## TOPIC 01464: Deprecated:Break Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1247.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1247.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies the action to take between each entry in a scan list. Remarks The following table lists the characteristics of this property. Short Name BreakMode Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Time Eng

### Deprecated:Break Mode

(Deprecated) Specifies the action to take between each entry in a scan list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | BreakMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| No Action | 10227 | When advancing to the next entry in the scan list, leave all previous connections intact. |
| --- | --- | --- |
| Break Before Make | 10110 | When advancing to the next entry in the scan list, disconnect all previous connections before making any new connections. |

Parent topic:

DAQmx Switch Scan Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1248.html language=enus -->
## TOPIC 01465: Deprecated:Repeat Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1248.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-scan/attr1248.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Specifies if the task advances through the scan list multiple times. Remarks The following table lists the characteristics of this property. Short Name RepeatMode Data type ci32.png Permissions Read/Write Resettable True Settable While Task Is Running device-specific Available in Run-Ti

### Deprecated:Repeat Mode

(Deprecated) Specifies if the task advances through the scan list multiple times.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RepeatMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Finite | 10172 | The task advances through the scan list one time only. NI-DAQmx ignores any Advance Triggers after completing the scan list. |
| --- | --- | --- |
| Continuous | 10117 | The task returns to the beginning of the scan list when it reaches the end of the scan list. |

Parent topic:

DAQmx Switch Scan Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-switch-scan/attr17d9.html language=enus -->
## TOPIC 01466: Deprecated:Is Waiting For Advance

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-switch-scan/attr17d9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-switch-scan/attr17d9.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: (Deprecated) Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list. Remarks The following table lists the characteristics of this property. Short Name WaitingForAdv Data type cbool.png Permissions Read Only Re

### Deprecated:Is Waiting For Advance

(Deprecated) Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | WaitingForAdv |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Switch Scan Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system-p.html language=enus -->
## TOPIC 01467: DAQmx System Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DAQmx System properties return information about the NI-DAQmx software configuration on your system, including version number and the names of saved virtual channels and tasks.

### DAQmx System Properties

The DAQmx System properties return information about the NI-DAQmx software configuration on your system, including version number and the names of saved virtual channels and tasks.

- [Device Names](../../../resource/objmgr/daqmx-rc/daqmx-system/attr193b.html) Indicates the names of all devices installed in the system.
- [Global Channels](../../../resource/objmgr/daqmx-rc/daqmx-system/attr1265.html) Indicates an array that contains the names of all global channels saved on the system.
- [Scales](../../../resource/objmgr/daqmx-rc/daqmx-system/attr1266.html) Indicates an array that contains the names of all custom scales saved on the system.
- [System:NI-DAQ Version:Major](../../../resource/objmgr/daqmx-rc/daqmx-system/attr1272.html) Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0.
- [System:NI-DAQ Version:Minor](../../../resource/objmgr/daqmx-rc/daqmx-system/attr1923.html) Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0.
- [System:NI-DAQ Version:Update](../../../resource/objmgr/daqmx-rc/daqmx-system/attr2f22.html) Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1.
- [Tasks](../../../resource/objmgr/daqmx-rc/daqmx-system/attr1267.html) Indicates an array that contains the names of all tasks saved on the system.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system/attr1265.html language=enus -->
## TOPIC 01468: Global Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system/attr1265.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system/attr1265.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array that contains the names of all global channels saved on the system. Remarks The following table lists the characteristics of this property. Short Name GlobalChans Data type c1dgenclassrntag.png Permissions Read Only Resettable False Settable While Task Is Running device-specific A

### Global Channels

Indicates an array that contains the names of all global channels saved on the system.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | GlobalChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx System Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system/attr1266.html language=enus -->
## TOPIC 01469: Scales

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system/attr1266.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system/attr1266.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array that contains the names of all custom scales saved on the system. Remarks The following table lists the characteristics of this property. Short Name Scales Data type c1ddaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available i

### Scales

Indicates an array that contains the names of all custom scales saved on the system.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Scales |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx System Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system/attr1267.html language=enus -->
## TOPIC 01470: Tasks

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system/attr1267.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system/attr1267.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array that contains the names of all tasks saved on the system. Remarks The following table lists the characteristics of this property. Short Name Tasks Data type c1dgenclassrntag.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-

### Tasks

Indicates an array that contains the names of all tasks saved on the system.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Tasks |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx System Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system/attr1272.html language=enus -->
## TOPIC 01471: System:NI-DAQ Version:Major

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system/attr1272.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system/attr1272.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0. Remarks The following table lists the characteristics of this property. Short Name MajorVersion Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Availa

### System:NI-DAQ Version:Major

Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MajorVersion |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx System Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system/attr1923.html language=enus -->
## TOPIC 01472: System:NI-DAQ Version:Minor

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system/attr1923.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system/attr1923.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0. Remarks The following table lists the characteristics of this property. Short Name MinorVersion Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Availa

### System:NI-DAQ Version:Minor

Indicates the minor portion of the installed version of NI-DAQmx, such as 0 for version 7.0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MinorVersion |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx System Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system/attr193b.html language=enus -->
## TOPIC 01473: Device Names

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system/attr193b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system/attr193b.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of all devices installed in the system. Remarks The following table lists the characteristics of this property. Short Name DevNames Data type c1ddaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Device Names

Indicates the names of all devices installed in the system.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DevNames |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx System Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-system/attr2f22.html language=enus -->
## TOPIC 01474: System:NI-DAQ Version:Update

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-system/attr2f22.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-system/attr2f22.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1. Remarks The following table lists the characteristics of this property. Short Name UpdateVersion Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Av

### System:NI-DAQ Version:Update

Indicates the update portion of the installed version of NI-DAQmx, such as 1 for version 9.0.1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | UpdateVersion |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx System Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-task-p.html language=enus -->
## TOPIC 01475: DAQmx Task Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-task-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-task-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DAQmx Task properties return information about a specified task.

### DAQmx Task Properties

The DAQmx Task properties return information about a specified task.

- [Channels](../../../resource/objmgr/daqmx-rc/daqmx-task/attr1273.html) Indicates the names of all virtual channels in the task.
- [Devices](../../../resource/objmgr/daqmx-rc/daqmx-task/attr230e.html) Indicates an array containing the names of all devices in the task.
- [Name](../../../resource/objmgr/daqmx-rc/daqmx-task/attr1276.html) Indicates the name of the task.
- [Number of Channels](../../../resource/objmgr/daqmx-rc/daqmx-task/attr2181.html) Indicates the number of virtual channels in the task.
- [Number of Devices](../../../resource/objmgr/daqmx-rc/daqmx-task/attr29ba.html) Indicates the number of devices in the task.
- [Task Done](../../../resource/objmgr/daqmx-rc/daqmx-task/attr1274.html) Indicates whether the task completed execution .

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-task/attr1273.html language=enus -->
## TOPIC 01476: Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-task/attr1273.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-task/attr1273.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of all virtual channels in the task. Remarks The following table lists the characteristics of this property. Short Name Channels Data type c1dgenclassrntag.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Channels

Indicates the names of all virtual channels in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channels |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-task/attr1274.html language=enus -->
## TOPIC 01477: Task Done

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-task/attr1274.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-task/attr1274.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the task completed execution . Remarks The following table lists the characteristics of this property. Short Name Done Data type cbool.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Task Done

Indicates whether the task 
 [completed execution](/csh?context=nidaqmx_mxcncpts_whentaskdone)
 .

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-task/attr1276.html language=enus -->
## TOPIC 01478: Name

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-task/attr1276.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-task/attr1276.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the task. Remarks The following table lists the characteristics of this property. Short Name Name Data type cgenclassrntag.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Name

Indicates the name of the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-task/attr2181.html language=enus -->
## TOPIC 01479: Number of Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-task/attr2181.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-task/attr2181.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of virtual channels in the task. Remarks The following table lists the characteristics of this property. Short Name NumChans Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Number of Channels

Indicates the number of virtual channels in the task.

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

DAQmx Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-task/attr230e.html language=enus -->
## TOPIC 01480: Devices

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-task/attr230e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-task/attr230e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates an array containing the names of all devices in the task. Remarks The following table lists the characteristics of this property. Short Name Devices Data type c1ddaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engin

### Devices

Indicates an array containing the names of all devices in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Devices |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-task/attr29ba.html language=enus -->
## TOPIC 01481: Number of Devices

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-task/attr29ba.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-task/attr29ba.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of devices in the task. Remarks The following table lists the characteristics of this property. Short Name NumDevices Data type cu32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Number of Devices

Indicates the number of devices in the task.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NumDevices |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Task Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-p.html language=enus -->
## TOPIC 01482: DAQmx Timing Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Timing properties to configure the sample timing and duration of a task.

### DAQmx Timing Properties

Use the DAQmx Timing properties to configure the sample timing and duration of a task.

- [Advanced:First Sample Clock Time:Offset](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr31aa.html) Specifies, in seconds, the offset to apply to the FirstSampClk.When value. This offset modifies when the first sample clock occurs and is used to account for known delays in the signal path.
- [Advanced:First Sample Clock Time:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr3183.html) Specifies the timescale to be used for the value of FirstSampClk.When .
- [Advanced:First Sample Clock Time:When](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr3182.html) Specifies the time of the first sample clock pulse.
- [Advanced:First Sample Timestamp:Enable](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr3139.html) Specifies whether to enable the first sample timestamp.
- [Advanced:First Sample Timestamp:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr313b.html) Specifies the timescale to be used for the first sample timestamp.
- [Advanced:First Sample Timestamp:Value](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr313a.html) Indicates the timestamp of the first sample.
- [Advanced:Sample Timing Engine](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2a26.html) Specifies which timing engine to use for the task.
- [Change Detection:Digital Input:Falling Edge Physical Channels](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2196.html) Specifies the names of the digital lines or ports on which to detect falling edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports.
- [Change Detection:Digital Input:Rising Edge Physical Channels](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2195.html) Specifies the names of the digital lines or ports on which to detect rising edges. The lines or ports must be used by virtual channels in the task. You also can specify a string that contains a list or range of digital lines or ports.
- [Change Detection:Digital Input:Tristate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2efa.html) Specifies whether to tristate lines specified with ChangeDetect.DI.RisingEdgePhysicalChans and ChangeDetect.DI.FallingEdgePhysicalChans that are not in a virtual channel in the task. If you set this property to TRUE, NI-DAQmx tristates rising/falling edge lines that are not in a virtual channel in the task. If you set this property to FALSE, NI-DAQmx does not modify the configuration of rising/falling edge lines that are not in a virtual channel in the task, even if the lines were previously tristated. Set this property to FALSE to detect changes on lines in other tasks or to detect changes on output-only lines.
- [Handshake:Delay After Transfer](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr22c2.html) Specifies the number of seconds to wait after a handshake cycle before starting a new handshake cycle.
- [Handshake:Sample Input Data When](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr22c4.html) Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device.
- [Handshake:Start Condition](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr22c3.html) Specifies the point in the handshake cycle that the device is in when the task starts.
- [Implicit:Underflow Behavior](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2efd.html) Specifies the action to take when the onboard memory of the device becomes empty.
- [More:AI Convert:Active Devices](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2970.html) Specifies a subset of devices in the task to configure. NI-DAQmx configures all devices in the task if you do not set this property.
- [More:AI Convert:Active Edge](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1853.html) Specifies on which edge of the clock pulse an analog-to-digital conversion takes place.
- [More:AI Convert:Delay From Sample Clock:Delay](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1317.html) Specifies the amount of time to wait after receiving a Sample Clock edge before beginning to acquire the sample. This value is in the units you specify with DelayFromSampClk.DelayUnits .
- [More:AI Convert:Delay From Sample Clock:Delay Units](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1304.html) Specifies the units of DelayFromSampClk.Delay .
- [More:AI Convert:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2edc.html) Specifies whether to apply a digital filter to the AI Convert Clock.
- [More:AI Convert:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2edd.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [More:AI Convert:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2edf.html) Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [More:AI Convert:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2ede.html) Specifies the terminal of the signal to use as the timebase of the digital filter.
- [More:AI Convert:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2ee0.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [More:AI Convert:Maximum Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr22c9.html) Indicates the maximum convert rate supported by the task, given the current devices and channel count.
- [More:AI Convert:Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1848.html) Specifies in Hertz the rate at which to clock the analog-to-digital converter. This clock is specific to the analog input section of multiplexed devices .
- [More:AI Convert:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1502.html) Specifies the terminal of the signal to use as the AI Convert Clock.
- [More:AI Convert:Timebase Divisor](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1335.html) Specifies the number of AI Convert Clock Timebase pulses needed to produce a single AI Convert Clock pulse.
- [More:AI Convert:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1339.html) Specifies the terminal of the signal to use as the AI Convert Clock Timebase.
- [More:Master Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1495.html) Specifies the rate of the Master Timebase.
- [More:Master Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1343.html) Specifies the terminal of the signal to use as the Master Timebase. On an E Series device, you can choose only between the onboard 20MHz Timebase or the RTSI7 terminal.
- [More:Reference Clock:Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1315.html) Specifies the frequency of the Reference Clock.
- [More:Reference Clock:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1316.html) Specifies the terminal of the signal to use as the Reference Clock.
- [More:Synchronization Clock:Interval](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2f7e.html) Specifies the interval, in Sample Clock periods, between each internal Synchronization Clock pulse. NI-DAQmx uses this pulse for synchronization of triggers between multiple devices at different rates. Refer to device documentation for information about how to calculate this value.
- [More:Synchronization Pulse:Digital Edge:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr223d.html) Specifies the terminal of the signal to use as the synchronization pulse. The synchronization pulse resets the clock dividers and the ADCs/DACs on the device.
- [More:Synchronization Pulse:Minimum Delay To Start](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr223f.html) Specifies in seconds the amount of time that elapses after the master device issues the synchronization pulse before the task starts.
- [More:Synchronization Pulse:Reset Delay](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2f7d.html) Specifies in seconds the amount of time to wait after the Synchronization Pulse before resetting the ADCs or DACs on the device. When synchronizing devices, query SyncPulse.ResetTime on all devices and note the largest reset time. Then, for each device, subtract the reset time from the largest reset time and set this property to the resulting value.
- [More:Synchronization Pulse:Reset Time](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2f7c.html) Indicates in seconds the amount of time required for the ADCs or DACs on the device to reset. When synchronizing devices, query this property on all devices and note the largest reset time. Then, for each device, subtract the value of this property from the largest reset time and set SyncPulse.ResetDelay to the resulting value.
- [More:Synchronization Pulse:Synchronization Time](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr223e.html) Indicates in seconds the delay required to reset the ADCs/DACs after the device receives the synchronization pulse.
- [More:Synchronization Pulse:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2f85.html) Indicates the name of the internal Synchronization Pulse terminal for the task. This property does not return the name of the source terminal.
- [More:Synchronization Pulse:Time:Timescale](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr3138.html) Specifies the timescale to be used for timestamps for a sync pulse.
- [More:Synchronization Pulse:Time:When](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr3137.html) Specifies the start time of the sync pulse.
- [More:Synchronization Pulse:Type](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr3136.html) Specifies the type of sync pulse used in the task.
- [On Demand:Simultaneous Analog Output Enable](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr21a0.html) Specifies whether to update all channels in the task simultaneously, rather than updating channels independently when you write a sample to that channel.
- [Sample Clock:Active Edge](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1301.html) Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock.
- [Sample Clock:Digital Filter:Enable](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr221e.html) Specifies whether to apply the pulse width filter to the signal.
- [Sample Clock:Digital Filter:Minimum Pulse Width](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr221f.html) Specifies in seconds the minimum pulse width the filter recognizes.
- [Sample Clock:Digital Filter:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2221.html) Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.
- [Sample Clock:Digital Filter:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2220.html) Specifies the input terminal of the signal to use as the timebase of the pulse width filter.
- [Sample Clock:Digital Synchronization:Enable](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2222.html) Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.
- [Sample Clock:Maximum Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr22c8.html) Indicates the maximum Sample Clock rate supported by the task, based on other timing settings. For output tasks, the maximum Sample Clock rate is the maximum rate of the DAC. For input tasks, NI-DAQmx calculates the maximum sampling rate differently for multiplexed devices than simultaneous sampling devices .
- [Sample Clock:Overrun Behavior](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2efc.html) Specifies the action to take if Sample Clock edges occur faster than the device can handle them.
- [Sample Clock:Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1344.html) Specifies the sampling rate in samples per channel per second. If you use an external source for the Sample Clock, set this input to the maximum expected rate of that clock.
- [Sample Clock:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1852.html) Specifies the terminal of the signal to use as the Sample Clock.
- [Sample Clock:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2f1b.html) Indicates the name of the internal Sample Clock terminal for the task. This property does not return the name of the Sample Clock source terminal specified with SampClk.Src .
- [Sample Clock:Timebase Divisor](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr18eb.html) Specifies the number of Sample Clock Timebase pulses needed to produce a single Sample Clock pulse.
- [Sample Clock:Timebase:Active Edge](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr18ec.html) Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.
- [Sample Clock:Timebase:Master Timebase Divisor](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1305.html) Specifies the number of pulses of the Master Timebase needed to produce a single pulse of the Sample Clock Timebase.
- [Sample Clock:Timebase:Rate](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1303.html) Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters.
- [Sample Clock:Timebase:Source](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1308.html) Specifies the terminal of the signal to use as the Sample Clock Timebase.
- [Sample Clock:Timebase:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2f1c.html) Indicates the name of the internal Sample Clock Timebase terminal for the task. This property does not return the name of the Sample Clock Timebase source terminal specified with SampClk.Timebase.Src .
- [Sample Clock:Underflow Behavior](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr2961.html) Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop.
- [Sample Clock:Write Waveform:Use Initial Waveform dt](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr30fc.html) Specifies that the value of SampClk.Rate will be determined by the dt component of the initial DAQmx Write waveform input for Output tasks.
- [Sample Quantity:Sample Mode](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1300.html) Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples.
- [Sample Quantity:Samples Per Channel](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1310.html) Specifies the number of samples to acquire or generate for each channel if SampQuant.SampMode is Finite Samples. If SampQuant.SampMode is Continuous Samples, NI-DAQmx uses this value to determine the buffer size .
- [Sample Timing Type](../../../resource/objmgr/daqmx-rc/daqmx-timing/attr1347.html) Specifies the type of sample timing to use for the task.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source-p.html language=enus -->
## TOPIC 01483: DAQmx Timing Source Properties

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source-p.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source-p.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the DAQmx Timing Source properties to retrieve information about timing sources for Timed Loops.

### DAQmx Timing Source Properties

Use the DAQmx Timing Source properties to retrieve information about timing sources for Timed Loops.

- [Active Timing Source](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr2249.html) Specifies the timing source from which to retrieve properties.
- [Control Loop From Task:Sleep Time](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr2554.html) Indicates in microseconds the amount of time the Timed Loop sleeps after each sample clock pulse.
- [Digital Change Detection:Falling Edge Physical Channels](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr2270.html) Indicates the names of the digital lines or ports on which to detect falling edges.
- [Digital Change Detection:Rising Edge Physical Channels](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr226f.html) Indicates the names of the digital lines or ports on which to detect rising edges.
- [Digital Edge using Counter:Counter](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr226c.html) Indicates the counter the timing source uses.
- [Digital Edge using Counter:Edge](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr224c.html) Indicates on which edges of the digital signal each iteration of the Timed Loop executes.
- [Digital Edge using Counter:Edge Count](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr224d.html) Indicates the number of edges of the digital signal that must occur for each iteration of the Timed Loop to execute.
- [Digital Edge using Counter:Terminal](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr224e.html) Indicates the terminal to which you connect the digital signal you want to use for the timing source.
- [Frequency:Counter](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr226a.html) Indicates the counter the timing source uses.
- [Frequency:Frequency](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr224a.html) Indicates the frequency of the timing source.
- [Signal From Task:Signal](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr224f.html) Indicates the signal the timing source uses.
- [Timing Source Type](../../../resource/objmgr/daqmx-rc/daqmx-timing-source/attr2269.html) Indicates the type of timing source.

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr2249.html language=enus -->
## TOPIC 01484: Active Timing Source

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr2249.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr2249.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timing source from which to retrieve properties. Remarks The following table lists the characteristics of this property. Short Name ActiveTimingSrc Data type cstr.png Permissions Write Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine Tru

### Active Timing Source

Specifies the timing source from which to retrieve properties.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ActiveTimingSrc |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr224a.html language=enus -->
## TOPIC 01485: Frequency:Frequency

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr224a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr224a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the frequency of the timing source. Remarks The following table lists the characteristics of this property. Short Name Freq.Freq Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Frequency:Frequency

Indicates the frequency of the timing source.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Freq.Freq |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr224c.html language=enus -->
## TOPIC 01486: Digital Edge using Counter:Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr224c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr224c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates on which edges of the digital signal each iteration of the Timed Loop executes. Remarks The following table lists the characteristics of this property. Short Name DigitalEdgeCtr.Edge Data type ci32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Av

### Digital Edge using Counter:Edge

Indicates on which edges of the digital signal each iteration of the Timed Loop executes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DigitalEdgeCtr.Edge |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Rising | 10280 | Rising edge(s). |
| --- | --- | --- |
| Falling | 10171 | Falling edge(s). |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr224d.html language=enus -->
## TOPIC 01487: Digital Edge using Counter:Edge Count

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr224d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr224d.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of edges of the digital signal that must occur for each iteration of the Timed Loop to execute. Remarks The following table lists the characteristics of this property. Short Name DigitalEdgeCtr.EdgeCount Data type cu32.png Permissions Read Only Resettable False Settable While Ta

### Digital Edge using Counter:Edge Count

Indicates the number of edges of the digital signal that must occur for each iteration of the Timed Loop to execute.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DigitalEdgeCtr.EdgeCount |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr224e.html language=enus -->
## TOPIC 01488: Digital Edge using Counter:Terminal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr224e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr224e.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the terminal to which you connect the digital signal you want to use for the timing source. Remarks The following table lists the characteristics of this property. Short Name DigitalEdgeCtr.Term Data type cdaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Running

### Digital Edge using Counter:Terminal

Indicates the 
 [terminal](/csh?context=nidaqmx_mxcncpts_terminal)
 to which you connect the digital signal you want to use for the timing source.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DigitalEdgeCtr.Term |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr224f.html language=enus -->
## TOPIC 01489: Signal From Task:Signal

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr224f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr224f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the signal the timing source uses. Remarks The following table lists the characteristics of this property. Short Name SignalFromTask.Signal Data type ci32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Sample Comp

### Signal From Task:Signal

Indicates the signal the timing source uses.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SignalFromTask.Signal |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Sample Complete Event | 12530 | Timed Loop executes each time the Sample Complete Event occurs. |
| --- | --- | --- |
| Counter Output Event | 12494 | Timed Loop executes each time the Counter Output Event occurs. |
| Change Detection Event | 12511 | Timed Loop executes each time the Change Detection Event occurs. |
| Sample Clock | 12487 | Timed Loop executes on each active edge of the Sample Clock. |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr2269.html language=enus -->
## TOPIC 01490: Timing Source Type

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr2269.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr2269.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the type of timing source. Remarks The following table lists the characteristics of this property. Short Name TimingSrcType Data type ci32.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True Frequency 12532 Causes the

### Timing Source Type

Indicates the type of timing source.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TimingSrcType |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Frequency | 12532 | Causes the Timed Loop to execute at a constant frequency. |
| --- | --- | --- |
| Digital Change Detection | 12533 | Causes the Timed Loop to execute on rising and/or falling edges of one or more digital lines. |
| Digital Edge using Counter | 12534 | Causes the Timed Loop to execute on rising or falling edges of a digital signal. |
| Signal From Task | 12535 | Use the signal indicated by SignalFromTask.Signal to determine when the Timed Loop executes. |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr226a.html language=enus -->
## TOPIC 01491: Frequency:Counter

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr226a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr226a.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the counter the timing source uses. Remarks The following table lists the characteristics of this property. Short Name Freq.Counter Data type cdaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Frequency:Counter

Indicates the counter the timing source uses.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Freq.Counter |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr226c.html language=enus -->
## TOPIC 01492: Digital Edge using Counter:Counter

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr226c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr226c.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the counter the timing source uses. Remarks The following table lists the characteristics of this property. Short Name DigitalEdgeCtr.Counter Data type cdaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Running device-specific Available in Run-Time Engine True

### Digital Edge using Counter:Counter

Indicates the counter the timing source uses.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DigitalEdgeCtr.Counter |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr226f.html language=enus -->
## TOPIC 01493: Digital Change Detection:Rising Edge Physical Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr226f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr226f.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of the digital lines or ports on which to detect rising edges. Remarks The following table lists the characteristics of this property. Short Name DigChangeDetect.RisingEdgePhysicalChans Data type cdaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Runnin

### Digital Change Detection:Rising Edge Physical Channels

Indicates the names of the digital lines or ports on which to detect rising edges.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DigChangeDetect.RisingEdgePhysicalChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr2270.html language=enus -->
## TOPIC 01494: Digital Change Detection:Falling Edge Physical Channels

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr2270.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr2270.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of the digital lines or ports on which to detect falling edges. Remarks The following table lists the characteristics of this property. Short Name DigChangeDetect.FallingEdgePhysicalChans Data type cdaqmxscale.png Permissions Read Only Resettable False Settable While Task Is Runn

### Digital Change Detection:Falling Edge Physical Channels

Indicates the names of the digital lines or ports on which to detect falling edges.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DigChangeDetect.FallingEdgePhysicalChans |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing-source/attr2554.html language=enus -->
## TOPIC 01495: Control Loop From Task:Sleep Time

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing-source/attr2554.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing-source/attr2554.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in microseconds the amount of time the Timed Loop sleeps after each sample clock pulse. Remarks The following table lists the characteristics of this property. Short Name ControlLoopFromTask.SleepTime Data type cdbl.png Permissions Read Only Resettable False Settable While Task Is Running

### Control Loop From Task:Sleep Time

Indicates in microseconds the amount of time the Timed Loop sleeps after each sample clock pulse.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ControlLoopFromTask.SleepTime |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| Resettable | False |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Source Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1300.html language=enus -->
## TOPIC 01496: Sample Quantity:Sample Mode

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1300.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1300.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples. For an analog input task with a Reference Trigger , you must set this property to Finite Samples even though the task runs continuously until the Reference Trigger occurs. Remark

### Sample Quantity:Sample Mode

Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples.

For an analog input task with a 
 [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger)
 , you must set this property to Finite Samples even though the task runs continuously until the Reference Trigger occurs.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampQuant.SampMode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Finite Samples | 10178 | Acquire or generate a finite number of samples. |
| --- | --- | --- |
| Continuous Samples | 10123 | Acquire or generate samples until you stop the task. |
| Hardware Timed Single Point | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1301.html language=enus -->
## TOPIC 01497: Sample Clock:Active Edge

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1301.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1301.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock. Remarks The following table lists the characteristics of this property. Short Name SampClk.ActiveEdge Data type ci32.png Permissions R

### Sample Clock:Active Edge

Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.ActiveEdge |
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

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1303.html language=enus -->
## TOPIC 01498: Sample Clock:Timebase:Rate

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1303.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1303.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters. Remarks The following table lists the characteristics of this pro

### Sample Clock:Timebase:Rate

Specifies the rate of the Sample Clock Timebase. Some applications require that you specify a rate when you use any signal other than the onboard Sample Clock Timebase. NI-DAQmx requires this rate to calculate other timing parameters.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Timebase.Rate |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1304.html language=enus -->
## TOPIC 01499: More:AI Convert:Delay From Sample Clock:Delay Units

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1304.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1304.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of DelayFromSampClk.Delay . NI-DAQmx uses the AI Convert Clock timebase to produce the delay. If you set this property to Ticks and N is the value of DelayFromSampClk.Delay , N pulses of the AI Convert Clock Timebase occur after receiving a Sample Clock pulse before the acquisiti

### More:AI Convert:Delay From Sample Clock:Delay Units

Specifies the units of 
 [DelayFromSampClk.Delay](/csh?context=nidaqmx_daqmxprop_attr1317)
 .

NI-DAQmx uses the AI Convert Clock timebase to produce the delay.

If you set this property to Ticks and N is the value of 
 [DelayFromSampClk.Delay](/csh?context=nidaqmx_daqmxprop_attr1317)
 , N pulses of the AI Convert Clock Timebase 
occur after receiving a Sample Clock pulse before the acquisition of the sample begins.

If you set this property to Seconds, that number of seconds elapses after receiving a Sample Clock pulse before the acquisition of the 
sample begins.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DelayFromSampClk.DelayUnits |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

| Seconds | 10364 | Seconds. |
| --- | --- | --- |
| Ticks | 10304 | Timebase ticks. |

Parent topic:

DAQmx Timing Properties

<!--NI_TOPIC bundle=ni-daqmx-labview-api-ref path=resource/objmgr/daqmx-rc/daqmx-timing/attr1305.html language=enus -->
## TOPIC 01500: Sample Clock:Timebase:Master Timebase Divisor

- bundle_id: `ni-daqmx-labview-api-ref`
- source_path: `resource/objmgr/daqmx-rc/daqmx-timing/attr1305.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-labview-api-ref/raw/resource/enus/resource/objmgr/daqmx-rc/daqmx-timing/attr1305.html
- document_id: `ni-daqmx-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of pulses of the Master Timebase needed to produce a single pulse of the Sample Clock Timebase. The rate of the Sample Clock Timebase is equal to (frequency of Master Timebase) / (value of this property). The only valid values for this property are 1 and 200. Setting this proper

### Sample Clock:Timebase:Master Timebase Divisor

Specifies the number of pulses of the Master Timebase needed to produce a single pulse of the Sample Clock Timebase.

The rate of the Sample Clock Timebase is equal to (frequency of Master Timebase) / (value of this property). The only valid values for this property are 1 and 200.

Setting this property has a similar effect to setting 
 [SampClk.Timebase.Rate](/csh?context=nidaqmx_daqmxprop_attr1303)
 . Use 
 [SampClk.Timebase.Rate](/csh?context=nidaqmx_daqmxprop_attr1303)
 when you know the rate of the Master Timebase 
and you want to produce a Sample Clock Timebase at the specified rate. Use this property when you have an external Master Timebase that 
you want to divide down and use as the Sample Clock Timebase, but you do not know rate of that external Master Timebase.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SampClk.Timebase.MasterTimebaseDiv |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| Resettable | True |
| Settable While Task Is Running | device-specific |
| Available in Run-Time Engine | True |

Parent topic:

DAQmx Timing Properties
