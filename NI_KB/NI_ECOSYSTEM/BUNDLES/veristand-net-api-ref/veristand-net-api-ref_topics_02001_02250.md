# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=2001 end=2250 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-rowdimensions.html language=enus -->
## TOPIC 02001: RowDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-rowdimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-rowdimensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of rows in the channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int RowDimensions { get; }ReturnsThe number of rows.

### RowDimensions

Gets the number of rows in the channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int RowDimensions { get; }

#### Returns

The number of rows.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-scale.html language=enus -->
## TOPIC 02002: Scale

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-scale.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-scale.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the value of the scale property on the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale Scale { get; set; }

### Scale

Gets or sets the value of the scale property on the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) Scale { get; set; }

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-scaleunits.html language=enus -->
## TOPIC 02003: ScaleUnits

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-scaleunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-scaleunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units of the scale associated with the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ScaleUnits { get; }RemarksThe units of the scale can be any arbitrary string. If no scale exists, then this property returns the units of the channel. ReturnsRetur

### ScaleUnits

Gets the units of the scale associated with the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ScaleUnits { get; }

#### Remarks

The units of the scale can be any arbitrary string. If no scale exists, then this property returns the units of the channel.

#### Returns

Returns a string that indicates the units of the scale associated with the channel.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-units.html language=enus -->
## TOPIC 02004: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the units associated with the channel. This can be any arbitrary string. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Units { get; set; }ReturnsThe units.

### Units

Gets or sets the units associated with the channel. This can be any arbitrary string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Units { get; set; }

#### Returns

The units.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel.html language=enus -->
## TOPIC 02005: Channel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a channel in the system definition. This is a base class for more specific channel classes, including hardware channels, system channels, user channels, calculated channels, and so on. Derives fromBaseNodeIChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic cla

### Channel Class

Represents a channel in the system definition. This is a base class for more specific channel classes, including hardware channels, system channels, user channels, calculated channels, and so on.

#### Derives from

- BaseNode
- IChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Channel : BaseNode, IChannel

#### Remarks

Use the members of this class to get and set basic properties of a channel, including its data source, default value, and associated units.

**Accessing this Class**

You cannot explicitly construct a Channel object. Use an object of a type that inherits this class to access its members.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Channel(ChannelType) | Initializes a new instance of Channel with the object that you specify. |
| Channel(BaseNodeType) | Initializes a new instance of Channel with the object that you specify. Returns an exception if the object is not of type Channel. |

#### Fields

| Name | Description |
| --- | --- |
| K_FAULTABLE | A bit flag mask specifying that the channel can be faulted. |
| K_READABLE | A bit flag mask specifying that the channel can be read from. |
| K_SCALABLE | A bit flag mask specifying that the channel can be scaled. |
| K_WRITABLE | A bit flag mask specifying that the channel can be written to. |

#### Properties

| Name | Description |
| --- | --- |
| BitFields | Gets a bitfield mask that is set on the channel. |
| ColumnDimensions | Gets the number of columns in the channel value. |
| DataSource | Gets or sets the source channel that maps to the current channel and provides it data. |
| DefaultValue | Gets the default value of the channel. |
| IsReadable | Gets a value indicating whether the channel is readable. |
| IsWritable | Gets a value indicating whether the channel is writable. |
| RowDimensions | Gets the number of rows in the channel value. |
| Scale | Gets or sets the value of the scale property on the channel. |
| ScaleUnits | Gets the units of the scale associated with the channel. |
| Units | Gets or sets the units associated with the channel. This can be any arbitrary string. |

#### Methods

| Name | Description |
| --- | --- |
| GetValueTable(out string[], out double[]) | Gets the value table for the channel. |
| RemoveDataSource() | Removes the source channel that maps to the current channel and provides it data. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channelnames.html language=enus -->
## TOPIC 02006: ChannelNames Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channelnames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channelnames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the names of DAQ channels appear in log files this task creates and in the list of available triggers. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ChannelNamesMembersNameValueDescriptionPhysicalChannel0Name channels based on their physical addresses, s

### ChannelNames Enumeration

Specifies how the names of DAQ channels appear in log files this task creates and in the list of available triggers.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ChannelNames

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PhysicalChannel | 0 | Name channels based on their physical addresses, such as Dev1/ai0. |
| SystemDefinition | 1 | Name channels based on their names in the system definition file, such as MyVoltageChannel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-chassis__string.html language=enus -->
## TOPIC 02007: Chassis(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-chassis__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-chassis__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Chassis with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Chassis(string Name)ParametersNameTypeDescriptionNamestringThe name of the Chassis.

### Chassis(string)

Initializes a new instance of [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Chassis(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Chassis. |

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-clearchassismasterdevice.html language=enus -->
## TOPIC 02008: ClearChassisMasterDevice()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-clearchassismasterdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-clearchassismasterdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the chassis master hardware synchronization device setting. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ClearChassisMasterDevice()

### ClearChassisMasterDevice()

Clears the chassis master hardware synchronization device setting.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ClearChassisMasterDevice()

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-getdaq.html language=enus -->
## TOPIC 02009: GetDAQ()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-getdaq.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-getdaq.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQ section under the current Chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQ GetDAQ()ReturnsA DAQ object.

### GetDAQ()

Gets the [DAQ](nationalinstruments-veristand-systemdefinitionapi-daq.html) section under the current [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQ](nationalinstruments-veristand-systemdefinitionapi-daq.html) GetDAQ()

#### Returns

A [DAQ](nationalinstruments-veristand-systemdefinitionapi-daq.html) object.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-getdatasharing.html language=enus -->
## TOPIC 02010: GetDataSharing()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-getdatasharing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-getdatasharing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DataSharing section under the current Chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataSharing GetDataSharing()ReturnsA DataSharing object.

### GetDataSharing()

Gets the [DataSharing](nationalinstruments-veristand-systemdefinitionapi-datasharing.html) section under the current [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataSharing](nationalinstruments-veristand-systemdefinitionapi-datasharing.html) GetDataSharing()

#### Returns

A [DataSharing](nationalinstruments-veristand-systemdefinitionapi-datasharing.html) object.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-getfpga.html language=enus -->
## TOPIC 02011: GetFPGA()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-getfpga.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-getfpga.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FPGA section under the current Chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGA GetFPGA()ReturnsAn FPGA object.

### GetFPGA()

Gets the [FPGA](nationalinstruments-veristand-systemdefinitionapi-fpga.html) section under the current [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FPGA](nationalinstruments-veristand-systemdefinitionapi-fpga.html) GetFPGA()

#### Returns

An [FPGA](nationalinstruments-veristand-systemdefinitionapi-fpga.html) object.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-gettimingandsync.html language=enus -->
## TOPIC 02012: GetTimingAndSync()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-gettimingandsync.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-gettimingandsync.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the TimingAndSync section under the current Chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TimingAndSync GetTimingAndSync()ReturnsA TimingAndSync object.

### GetTimingAndSync()

Gets the [TimingAndSync](nationalinstruments-veristand-systemdefinitionapi-timingandsync.html) section under the current [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TimingAndSync](nationalinstruments-veristand-systemdefinitionapi-timingandsync.html) GetTimingAndSync()

#### Returns

A [TimingAndSync](nationalinstruments-veristand-systemdefinitionapi-timingandsync.html) object.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-getxnet.html language=enus -->
## TOPIC 02013: GetXNET()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-getxnet.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-getxnet.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the XNET section under the current Chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic XNET GetXNET()RemarksFor example code and more information about this method, refer to one of the following help topics: LabVIEW Walkthrough: Modifying a System Definition FileC#

### GetXNET()

Gets the [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) section under the current [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) GetXNET()

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

An [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) object.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertodaq__string-daqcm_clock_source-daqcm_active_edge-daqcm_export_sample_clock-daqcm_export_clk_on_line-daqcm_tri...d2015e194.html language=enus -->
## TOPIC 02014: SetChassisMasterToDAQ(string, DAQCM_Clock_Source, DAQCM_Active_Edge, DAQCM_Export_Sample_Clock, DAQCM_Export_Clk_On_Line, DAQCM_Trigger_Line, DAQCM_Slope, DAQCM_Export_Start_Trigger, DAQCM_Export_StartTrigger_On_Line)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertodaq__string-daqcm_clock_source-daqcm_active_edge-daqcm_export_sample_clock-daqcm_export_clk_on_line-daqcm_tri...d2015e194.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertodaq__string-daqcm_clock_source-daqcm_active_edge-daqcm_export_sample_clock-daqcm_export_clk_on_line-daqcm_tri...d2015e194.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the chassis master hardware synchronization device to the DAQ device you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetChassisMasterToDAQ(string DAQName, DAQCM_Clock_Source clkSrc, DAQCM_Active_Edge activeEdge, DAQCM_Export_Sample_Clock exportClk, DAQ

### SetChassisMasterToDAQ(string, DAQCM_Clock_Source, DAQCM_Active_Edge, DAQCM_Export_Sample_Clock, DAQCM_Export_Clk_On_Line, DAQCM_Trigger_Line, DAQCM_Slope, DAQCM_Export_Start_Trigger, DAQCM_Export_StartTrigger_On_Line)

Sets the chassis master hardware synchronization device to the DAQ device you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetChassisMasterToDAQ(string DAQName, DAQCM_Clock_Source clkSrc, DAQCM_Active_Edge activeEdge, DAQCM_Export_Sample_Clock exportClk, DAQCM_Export_Clk_On_Line exportClkToLine, DAQCM_Trigger_Line triggerLine, DAQCM_Slope triggerSlope, DAQCM_Export_Start_Trigger startTrigger, DAQCM_Export_StartTrigger_On_Line startTriggerLine)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| DAQName | string | The name of the DAQ device. |
| clkSrc | DAQCM_Clock_Source | The source for the sample clock. |
| activeEdge | DAQCM_Active_Edge | The edge on which the sample clock pulses to acquire or generate samples. |
| exportClk | DAQCM_Export_Sample_Clock | The sample clock to export. |
| exportClkToLine | DAQCM_Export_Clk_On_Line | The line that receives the pulse from the sample clock. |
| triggerLine | DAQCM_Trigger_Line | The line that triggers the acquisition or generation of samples. |
| triggerSlope | DAQCM_Slope | The edge on which to trigger the device. |
| startTrigger | DAQCM_Export_Start_Trigger | The start trigger to export. |
| startTriggerLine | DAQCM_Export_StartTrigger_On_Line | The line that exports the startTrigger . |

#### Returns

true if the chassis master hardware synchronization device is set successfully.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertodaq__string-daqcm_clock_source-daqcm_active_edge-daqcm_export_sample_clock-daqcm_export_clk_on_line-daqcm_tri...d2015e304.html language=enus -->
## TOPIC 02015: SetChassisMasterToDAQ(string, DAQCM_Clock_Source, DAQCM_Active_Edge, DAQCM_Export_Sample_Clock, DAQCM_Export_Clk_On_Line, DAQCM_Trigger_Line, DAQCM_Slope, DAQCM_Export_Start_Trigger, DAQCM_Export_StartTrigger_On_Line, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertodaq__string-daqcm_clock_source-daqcm_active_edge-daqcm_export_sample_clock-daqcm_export_clk_on_line-daqcm_tri...d2015e304.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertodaq__string-daqcm_clock_source-daqcm_active_edge-daqcm_export_sample_clock-daqcm_export_clk_on_line-daqcm_tri...d2015e304.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the chassis master hardware synchronization device to the DAQ device you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetChassisMasterToDAQ(string DAQName, DAQCM_Clock_Source clkSrc, DAQCM_Active_Edge activeEdge, DAQCM_Export_Sample_Clock exportClk, DAQ

### SetChassisMasterToDAQ(string, DAQCM_Clock_Source, DAQCM_Active_Edge, DAQCM_Export_Sample_Clock, DAQCM_Export_Clk_On_Line, DAQCM_Trigger_Line, DAQCM_Slope, DAQCM_Export_Start_Trigger, DAQCM_Export_StartTrigger_On_Line, out Error)

Sets the chassis master hardware synchronization device to the DAQ device you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetChassisMasterToDAQ(string DAQName, DAQCM_Clock_Source clkSrc, DAQCM_Active_Edge activeEdge, DAQCM_Export_Sample_Clock exportClk, DAQCM_Export_Clk_On_Line exportClkToLine, DAQCM_Trigger_Line triggerLine, DAQCM_Slope triggerSlope, DAQCM_Export_Start_Trigger startTrigger, DAQCM_Export_StartTrigger_On_Line startTriggerLine, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| DAQName | string | The name of the DAQ device. |
| clkSrc | DAQCM_Clock_Source | The source for the sample clock. |
| activeEdge | DAQCM_Active_Edge | The edge on which the sample clock pulses to acquire or generate samples. |
| exportClk | DAQCM_Export_Sample_Clock | The sample clock to export. |
| exportClkToLine | DAQCM_Export_Clk_On_Line | The line that receives the pulse from the sample clock. |
| triggerLine | DAQCM_Trigger_Line | The line that triggers the acquisition or generation of samples. |
| triggerSlope | DAQCM_Slope | The edge on which to trigger the device. |
| startTrigger | DAQCM_Export_Start_Trigger | The start trigger to export. |
| startTriggerLine | DAQCM_Export_StartTrigger_On_Line | The line that exports the startTrigger . |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the chassis master hardware synchronization device is set successfully.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertofpga__string-out.html language=enus -->
## TOPIC 02016: SetChassisMasterToFPGA(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertofpga__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertofpga__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the chassis master hardware synchronization device to the FPGA target you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetChassisMasterToFPGA(string FPGAName, out Error error)ParametersNameTypeDescriptionFPGANamestringThe name of the FPGA target.errorou

### SetChassisMasterToFPGA(string, out Error)

Sets the chassis master hardware synchronization device to the FPGA target you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetChassisMasterToFPGA(string FPGAName, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| FPGAName | string | The name of the FPGA target. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the chassis master hardware synchronization device is set successfully.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertofpga__string.html language=enus -->
## TOPIC 02017: SetChassisMasterToFPGA(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertofpga__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertofpga__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the chassis master hardware synchronization device to the FPGA target you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetChassisMasterToFPGA(string FPGAName)ParametersNameTypeDescriptionFPGANamestringThe name of the FPGA target.Returnstrue if the chass

### SetChassisMasterToFPGA(string)

Sets the chassis master hardware synchronization device to the FPGA target you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetChassisMasterToFPGA(string FPGAName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| FPGAName | string | The name of the FPGA target. |

#### Returns

true if the chassis master hardware synchronization device is set successfully.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertotimingandsync__string-out.html language=enus -->
## TOPIC 02018: SetChassisMasterToTimingAndSync(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertotimingandsync__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertotimingandsync__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the chassis master hardware synchronization device to the timing and sync device you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetChassisMasterToTimingAndSync(string TimingAndSyncName, out Error error)ParametersNameTypeDescriptionTimingAndSyncNamestr

### SetChassisMasterToTimingAndSync(string, out Error)

Sets the chassis master hardware synchronization device to the timing and sync device you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetChassisMasterToTimingAndSync(string TimingAndSyncName, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| TimingAndSyncName | string | The name of the timing and sync device. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the chassis master hardware synchronization device is set successfully.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertotimingandsync__string.html language=enus -->
## TOPIC 02019: SetChassisMasterToTimingAndSync(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertotimingandsync__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis-setchassismastertotimingandsync__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the chassis master hardware synchronization device to the timing and sync device you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetChassisMasterToTimingAndSync(string TimingAndSyncName)ParametersNameTypeDescriptionTimingAndSyncNamestringThe name of th

### SetChassisMasterToTimingAndSync(string)

Sets the chassis master hardware synchronization device to the timing and sync device you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetChassisMasterToTimingAndSync(string TimingAndSyncName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| TimingAndSyncName | string | The name of the timing and sync device. |

#### Returns

true if the chassis master hardware synchronization device is set successfully.

Parent topic:

Chassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-chassis.html language=enus -->
## TOPIC 02020: Chassis Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-chassis.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-chassis.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a chassis, which contains any NI-DAQ devices, reflective memory devices, NI FPGA targets, NI-XNET devices, and timing and sync devices you add. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Chassis : SectionRemarksUse the members of this

### Chassis Class

Represents a chassis, which contains any NI-DAQ devices, reflective memory devices, NI FPGA targets, NI-XNET devices, and timing and sync devices you add.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Chassis : Section

#### Remarks

Use the members of this class to access hardware in the chassis and to set or clear the master hardware synchronization device.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Hardware.GetChassisList
- Chassis Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Chassis(string) | Initializes a new instance of Chassis with the specified name. |

#### Methods

| Name | Description |
| --- | --- |
| ClearChassisMasterDevice() | Clears the chassis master hardware synchronization device setting. |
| GetDAQ() | Gets the DAQ section under the current Chassis. |
| GetDataSharing() | Gets the DataSharing section under the current Chassis. |
| GetFPGA() | Gets the FPGA section under the current Chassis. |
| GetTimingAndSync() | Gets the TimingAndSync section under the current Chassis. |
| GetXNET() | Gets the XNET section under the current Chassis. |
| SetChassisMasterToDAQ(string, DAQCM_Clock_Source, DAQCM_Active_Edge, DAQCM_Export_Sample_Clock, DAQCM_Export_Clk_On_Line, DAQCM_Trigger_Line, DAQCM_Slope, DAQCM_Export_Start_Trigger, DAQCM_Export_StartTrigger_On_Line) | Sets the chassis master hardware synchronization device to the DAQ device you specify. |
| SetChassisMasterToDAQ(string, DAQCM_Clock_Source, DAQCM_Active_Edge, DAQCM_Export_Sample_Clock, DAQCM_Export_Clk_On_Line, DAQCM_Trigger_Line, DAQCM_Slope, DAQCM_Export_Start_Trigger, DAQCM_Export_StartTrigger_On_Line, out Error) | Sets the chassis master hardware synchronization device to the DAQ device you specify. |
| SetChassisMasterToFPGA(string) | Sets the chassis master hardware synchronization device to the FPGA target you specify. |
| SetChassisMasterToFPGA(string, out Error) | Sets the chassis master hardware synchronization device to the FPGA target you specify. |
| SetChassisMasterToTimingAndSync(string, out Error) | Sets the chassis master hardware synchronization device to the timing and sync device you specify. |
| SetChassisMasterToTimingAndSync(string) | Sets the chassis master hardware synchronization device to the timing and sync device you specify. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-command.html language=enus -->
## TOPIC 02021: Command Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-command.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-command.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a parent class for the different Procedure command types. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Command : SectionRemarksAccessing this ClassM:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure.GetCommandList Thread Safet

### Command Class

Represents a parent class for the different [Procedure](nationalinstruments-veristand-systemdefinitionapi-procedure.html) command types.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Command : Section

#### Remarks

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure.GetCommandList

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html language=enus -->
## TOPIC 02022: CommunicationProtocol Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Protocol used by the virtual ECU Network Cluster to communicate with the real ECU network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum CommunicationProtocolMembersNameValueDescriptionCAN0Controller Area Network (CAN). LIN2Local Interconnect Network (LIN). Ethernet3E

### CommunicationProtocol Enumeration

Protocol used by the virtual ECU Network Cluster to communicate with the real ECU network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CommunicationProtocol

#### Members

| Name | Value | Description |
| --- | --- | --- |
| CAN | 0 | Controller Area Network (CAN). |
| LIN | 2 | Local Interconnect Network (LIN). |
| Ethernet | 3 | Ethernet. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-comparison.html language=enus -->
## TOPIC 02023: Comparison

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-comparison.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-comparison.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the condition to use when comparing Variable and Value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ConditionStepComparison Comparison { get; set; }ReturnsAn enumeration value of ConditionStepComparison.

### Comparison

Gets or sets the condition to use when comparing *Variable* and *Value*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ConditionStepComparison](nationalinstruments-veristand-systemdefinitionapi-conditionstepcomparison.html) Comparison { get; set; }

#### Returns

An enumeration value of [ConditionStepComparison](nationalinstruments-veristand-systemdefinitionapi-conditionstepcomparison.html).

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-condition__string-string-basenode-conditionstepcomparison-basenode-command.html language=enus -->
## TOPIC 02024: Condition(string, string, BaseNode, ConditionStepComparison, BaseNode, Command)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-condition__string-string-basenode-conditionstepcomparison-basenode-command.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-condition__string-string-basenode-conditionstepcomparison-basenode-command.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Condition that compares a channel to another channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Condition(string Name, string Description, BaseNode Variable, ConditionStepComparison Comparison, BaseNode Value, Command GotoLabel)ParametersN

### Condition(string, string, BaseNode, ConditionStepComparison, BaseNode, Command)

Initializes a new instance of [Condition](nationalinstruments-veristand-systemdefinitionapi-condition.html) that compares a channel to another channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Condition(string Name, string Description, BaseNode Variable, ConditionStepComparison Comparison, BaseNode Value, Command GotoLabel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Condition step. |
| Description | string | The description of the Condition step. |
| Variable | BaseNode | The channel in the system against which to test the condition. |
| Comparison | ConditionStepComparison | The condition to use when comparing Variable and Value. |
| Value | BaseNode | The channel to compare with Variable. |
| GotoLabel | Command | The procedure step to execute when the condition is met. |

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-condition__string-string-basenode-conditionstepcomparison-double-command.html language=enus -->
## TOPIC 02025: Condition(string, string, BaseNode, ConditionStepComparison, double, Command)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-condition__string-string-basenode-conditionstepcomparison-double-command.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-condition__string-string-basenode-conditionstepcomparison-double-command.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Condition that compares a channel to a constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Condition(string Name, string Description, BaseNode Variable, ConditionStepComparison Comparison, double Value, Command GotoLabel)ParametersNa

### Condition(string, string, BaseNode, ConditionStepComparison, double, Command)

Initializes a new instance of [Condition](nationalinstruments-veristand-systemdefinitionapi-condition.html) that compares a channel to a constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Condition(string Name, string Description, BaseNode Variable, ConditionStepComparison Comparison, double Value, Command GotoLabel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Condition step. |
| Description | string | The description of the Condition step. |
| Variable | BaseNode | The channel in the system against which to test the condition. |
| Comparison | ConditionStepComparison | The condition to use when comparing Variable and Value. |
| Value | double | The constant value to compare with Variable. |
| GotoLabel | Command | The procedure step to execute when the condition is met. |

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-gotolabel.html language=enus -->
## TOPIC 02026: GotoLabel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-gotolabel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-gotolabel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the procedure step to go to if the condition is met. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode GotoLabel { get; set; }ReturnsA BaseNode reference to the procedure step to go to.

### GotoLabel

Gets or sets the procedure step to go to if the condition is met.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) GotoLabel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the procedure step to go to.

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-setvalue__basenode.html language=enus -->
## TOPIC 02027: SetValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-setvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-setvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the channel to compare with the Variable channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetValue(BaseNode Value)ParametersNameTypeDescriptionValueBaseNodeThe channel to compare with Variable.

### SetValue(BaseNode)

Sets the channel to compare with the [Variable](nationalinstruments-veristand-systemdefinitionapi-condition-variable.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetValue(BaseNode Value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Value | BaseNode | The channel to compare with Variable. |

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-setvalue__double.html language=enus -->
## TOPIC 02028: SetValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-setvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-setvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the constant value to compare with the Variable channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetValue(double Value)ParametersNameTypeDescriptionValuedoubleThe constant value to compare with Variable.

### SetValue(double)

Sets the constant value to compare with the [Variable](nationalinstruments-veristand-systemdefinitionapi-condition-variable.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetValue(double Value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Value | double | The constant value to compare with Variable. |

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-valuechannel.html language=enus -->
## TOPIC 02029: ValueChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-valuechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-valuechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value that is compared to Variable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode ValueChannel { get; }ReturnsA BaseNode reference to the value channel.

### ValueChannel

Gets the channel that specifies the value that is compared to [Variable](nationalinstruments-veristand-systemdefinitionapi-condition-variable.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) ValueChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the value channel.

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-valueconstant.html language=enus -->
## TOPIC 02030: ValueConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-valueconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-valueconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value that is compared to Variable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double ValueConstant { get; }ReturnsThe constant value.

### ValueConstant

Gets the constant value that is compared to [Variable](nationalinstruments-veristand-systemdefinitionapi-condition-variable.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double ValueConstant { get; }

#### Returns

The constant value.

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-valueisconstant.html language=enus -->
## TOPIC 02031: ValueIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-valueisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-valueisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value compared to Variable is determined by a channel or by a constant. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ValueIsConstant { get; }Returnstrue if the value is a constant. false if it is a channel value.

### ValueIsConstant

Gets whether the value compared to [Variable](nationalinstruments-veristand-systemdefinitionapi-condition-variable.html) is determined by a channel or by a constant.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ValueIsConstant { get; }

#### Returns

true if the value is a constant. false if it is a channel value.

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition-variable.html language=enus -->
## TOPIC 02032: Variable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition-variable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel against which to test the condition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Variable { get; set; }ReturnsA BaseNode reference to the channel.

### Variable

Gets or sets the channel against which to test the condition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Variable { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Condition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-condition.html language=enus -->
## TOPIC 02033: Condition Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-condition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-condition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Condition step that you can add to a procedure. The Condition step executes a GotoLabel step based on the comparison of a constant value or channel value. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Condition : CommandRemarksUse the

### Condition Class

Represents a **Condition** step that you can add to a procedure. The **Condition** step executes a [GotoLabel](nationalinstruments-veristand-systemdefinitionapi-gotolabel.html) step based on the comparison of a constant value or channel value.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Condition : Command

#### Remarks

Use the members of this class to get or set the comparison condition and the [GotoLabel](nationalinstruments-veristand-systemdefinitionapi-gotolabel.html) step to execute.

**Accessing this Class**

- Condition Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Condition(string, string, BaseNode, ConditionStepComparison, double, Command) | Initializes a new instance of Condition that compares a channel to a constant value. |
| Condition(string, string, BaseNode, ConditionStepComparison, BaseNode, Command) | Initializes a new instance of Condition that compares a channel to another channel. |

#### Properties

| Name | Description |
| --- | --- |
| Comparison | Gets or sets the condition to use when comparing Variable and Value. |
| GotoLabel | Gets or sets the procedure step to go to if the condition is met. |
| ValueChannel | Gets the channel that specifies the value that is compared to Variable. |
| ValueConstant | Gets the constant value that is compared to Variable. |
| ValueIsConstant | Gets whether the value compared to Variable is determined by a channel or by a constant. |
| Variable | Gets or sets the channel against which to test the condition. |

#### Methods

| Name | Description |
| --- | --- |
| SetValue(double) | Sets the constant value to compare with the Variable channel. |
| SetValue(BaseNode) | Sets the channel to compare with the Variable channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-and.html language=enus -->
## TOPIC 02034: AND

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-and.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-and.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI VeriStand converts the values of the double data type to the I32 data type and then performs the AND operation on the values bitwise. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort AND

### AND

NI VeriStand converts the values of the double data type to the I32 data type and then performs the AND operation on the values bitwise.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort AND

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-comparisonmode.html language=enus -->
## TOPIC 02035: ComparisonMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-comparisonmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-comparisonmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of comparison to use for the condition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ushort ComparisonMode { get; set; }RemarksValueComparison Type0Greater than1Less than2Equal to3Not equal to4Greater than or equal to5Less than or equal to ReturnsThe

### ComparisonMode

Gets or sets the type of comparison to use for the condition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ushort ComparisonMode { get; set; }

#### Remarks

| Value | Comparison Type |
| --- | --- |
| 0 | Greater than |
| 1 | Less than |
| 2 | Equal to |
| 3 | Not equal to |
| 4 | Greater than or equal to |
| 5 | Less than or equal to |

#### Returns

The comparison type. The following values are valid:

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-basenode-basenode.html language=enus -->
## TOPIC 02036: Conditional(string, string, ushort, BaseNode, BaseNode, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y, W, and Z are all channel values. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue

### Conditional(string, string, ushort, BaseNode, BaseNode, BaseNode, BaseNode)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y*, *W*, and *Z* are all channel values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, BaseNode YValue, BaseNode WValue, BaseNode ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | BaseNode | The channel value to which X is compared. |
| WValue | BaseNode | The channel that determines the value of W. |
| ZValue | BaseNode | The channel that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-basenode-double.html language=enus -->
## TOPIC 02037: Conditional(string, string, ushort, BaseNode, BaseNode, BaseNode, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-basenode-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-basenode-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and W are channel values, and Z is a constant. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMode, Ba

### Conditional(string, string, ushort, BaseNode, BaseNode, BaseNode, double)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y* and *W* are channel values, and *Z* is a constant.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, BaseNode YValue, BaseNode WValue, double ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | BaseNode | The channel value to which X is compared. |
| WValue | BaseNode | The channel that determines the value of W. |
| ZValue | double | The constant that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-double-basenode.html language=enus -->
## TOPIC 02038: Conditional(string, string, ushort, BaseNode, BaseNode, double, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-double-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-double-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and Z are both channel values, and W is a constant. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMod

### Conditional(string, string, ushort, BaseNode, BaseNode, double, BaseNode)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y* and *Z* are both channel values, and *W* is a constant.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, BaseNode YValue, double WValue, BaseNode ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | BaseNode | The channel value to which X is compared. |
| WValue | double | The constant that determines the value of W. |
| ZValue | BaseNode | The channel that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-double-double.html language=enus -->
## TOPIC 02039: Conditional(string, string, ushort, BaseNode, BaseNode, double, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-double-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-basenode-double-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y is a channel value, and W and Z are both constants. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMod

### Conditional(string, string, ushort, BaseNode, BaseNode, double, double)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y* is a channel value, and *W* and *Z* are both constants.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, BaseNode YValue, double WValue, double ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | BaseNode | The channel value to which X is compared. |
| WValue | double | The constant that determines the value of W. |
| ZValue | double | The constant that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-basenode-basenode.html language=enus -->
## TOPIC 02040: Conditional(string, string, ushort, BaseNode, double, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y is a constant, and W and Z are both channel values. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMod

### Conditional(string, string, ushort, BaseNode, double, BaseNode, BaseNode)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y* is a constant, and *W* and *Z* are both channel values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, double YValue, BaseNode WValue, BaseNode ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | double | The constant that determines the value of Y. |
| WValue | BaseNode | The channel that determines the value of W. |
| ZValue | BaseNode | The channel that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-basenode-double.html language=enus -->
## TOPIC 02041: Conditional(string, string, ushort, BaseNode, double, BaseNode, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-basenode-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-basenode-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and Z are both constants, and W is a channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMod

### Conditional(string, string, ushort, BaseNode, double, BaseNode, double)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y* and *Z* are both constants, and *W* is a channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, double YValue, BaseNode WValue, double ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | double | The constant that determines the value of Y. |
| WValue | BaseNode | The channel that determines the value of W. |
| ZValue | double | The constant that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-double-basenode.html language=enus -->
## TOPIC 02042: Conditional(string, string, ushort, BaseNode, double, double, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-double-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-double-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and W are constants, and Z is a channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMode, Ba

### Conditional(string, string, ushort, BaseNode, double, double, BaseNode)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y* and *W* are constants, and *Z* is a channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, double YValue, double WValue, BaseNode ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | double | The constant that determines the value of Y. |
| WValue | double | The constant that determines the value of W. |
| ZValue | BaseNode | The channel that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-double-double.html language=enus -->
## TOPIC 02043: Conditional(string, string, ushort, BaseNode, double, double, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-conditional__string-string-ushort-basenode-double-double-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y, W, and Z are all constants. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, dou

### Conditional(string, string, ushort, BaseNode, double, double, double)

Initializes a new instance of [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html). In the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), *Y*, *W*, and *Z* are all constants.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Conditional(string Name, string Description, ushort ComparisonMode, BaseNode XValue, double YValue, double WValue, double ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Conditional calculated channel. |
| Description | string | The description of the Conditional calculated channel. |
| ComparisonMode | ushort | The comparison condition. Use class constants such as Greater. |
| XValue | BaseNode | The channel to be compared. |
| YValue | double | The constant that determines the value of Y. |
| WValue | double | The constant that determines the value of W. |
| ZValue | double | The constant that determines the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-equal.html language=enus -->
## TOPIC 02044: Equal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-equal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-equal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Equal to operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Equal

### Equal

Equal to operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Equal

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-greater.html language=enus -->
## TOPIC 02045: Greater

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-greater.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-greater.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Greater than operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Greater

### Greater

Greater than operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Greater

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-greaterorequal.html language=enus -->
## TOPIC 02046: GreaterOrEqual

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-greaterorequal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-greaterorequal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Greater than or equal to operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort GreaterOrEqual

### GreaterOrEqual

Greater than or equal to operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort GreaterOrEqual

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-less.html language=enus -->
## TOPIC 02047: Less

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-less.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-less.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Less than operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Less

### Less

Less than operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Less

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-lessorequal.html language=enus -->
## TOPIC 02048: LessOrEqual

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-lessorequal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-lessorequal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Less than or equal to operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort LessOrEqual

### LessOrEqual

Less than or equal to operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort LessOrEqual

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-notequal.html language=enus -->
## TOPIC 02049: NotEqual

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-notequal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-notequal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Not equal operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort NotEqual

### NotEqual

Not equal operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort NotEqual

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-or.html language=enus -->
## TOPIC 02050: OR

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-or.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-or.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI VeriStand converts the values of the double data type to the I32 data type and then performs the OR operation on the values bitwise. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort OR

### OR

NI VeriStand converts the values of the double data type to the I32 data type and then performs the OR operation on the values bitwise.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort OR

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-setwvalue__basenode.html language=enus -->
## TOPIC 02051: SetWValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-setwvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-setwvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets W in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetWValue(BaseNode WValue)ParametersNameTypeDescriptionWValueBaseNodeThe channel that specifies the value of W.

### SetWValue(BaseNode)

Sets *W* in the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), to the specified channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetWValue(BaseNode WValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| WValue | BaseNode | The channel that specifies the value of W. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-setwvalue__double.html language=enus -->
## TOPIC 02052: SetWValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-setwvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-setwvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets W in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetWValue(double WValue)ParametersNameTypeDescriptionWValuedoubleThe value of W.

### SetWValue(double)

Sets *W* in the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), to the specified constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetWValue(double WValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| WValue | double | The value of W. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-setyvalue__basenode.html language=enus -->
## TOPIC 02053: SetYValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-setyvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-setyvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Y in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetYValue(BaseNode YValue)ParametersNameTypeDescriptionYValueBaseNodeThe channel that specifies the value of Y.

### SetYValue(BaseNode)

Sets *Y* in the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), to the specified channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetYValue(BaseNode YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| YValue | BaseNode | The channel that specifies the value of Y. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-setyvalue__double.html language=enus -->
## TOPIC 02054: SetYValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-setyvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-setyvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Y in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetYValue(double YValue)ParametersNameTypeDescriptionYValuedoubleThe value of Y.

### SetYValue(double)

Sets *Y* in the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), to the specified constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetYValue(double YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| YValue | double | The value of Y. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-setzvalue__basenode.html language=enus -->
## TOPIC 02055: SetZValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-setzvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-setzvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Z in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetZValue(BaseNode ZValue)ParametersNameTypeDescriptionZValueBaseNodeThe channel that specifies the value of Z.

### SetZValue(BaseNode)

Sets *Z* in the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), to the specified channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetZValue(BaseNode ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ZValue | BaseNode | The channel that specifies the value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-setzvalue__double.html language=enus -->
## TOPIC 02056: SetZValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-setzvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-setzvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Z in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetZValue(double ZValue)ParametersNameTypeDescriptionZValuedoubleThe value of Z.

### SetZValue(double)

Sets *Z* in the conditional formula (If (*X* compare *Y*), then *W*. Else, *Z*.), to the specified constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetZValue(double ZValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ZValue | double | The value of Z. |

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-wchannelvalue.html language=enus -->
## TOPIC 02057: WChannelValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-wchannelvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-wchannelvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value of W in the formula: If (X compare Y), then W. Else, Z. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode WChannelValue { get; }ReturnsA BaseNode reference to the channel, or null if W is a constant.

### WChannelValue

Gets the channel that specifies the value of *W* in the formula: If (*X* compare *Y*), then *W*. Else, *Z*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) WChannelValue { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel, or null if *W* is a constant.

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-wconstantvalue.html language=enus -->
## TOPIC 02058: WConstantValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-wconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-wconstantvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of W in the formula: If (X compare Y), then W. Else, Z. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double WConstantValue { get; }ReturnsThe value of W. This property gets a constant value regardless of whether the data source of W is a constant o

### WConstantValue

Gets the constant value of *W* in the formula: If (*X* compare *Y*), then *W*. Else, *Z*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double WConstantValue { get; }

#### Returns

The value of *W*. This property gets a constant value regardless of whether the data source of *W* is a constant or a channel.

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-xchannel.html language=enus -->
## TOPIC 02059: XChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-xchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-xchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel to check for the comparison condition. This channel is the value of X in the formula: If (X compare Y), then W. Else, Z. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode XChannel { get; set; }ReturnsA BaseNode reference to the channel.

### XChannel

Gets or sets the channel to check for the comparison condition. This channel is the value of *X* in the formula: If (*X* compare *Y*), then *W*. Else, *Z*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) XChannel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-ychannelvalue.html language=enus -->
## TOPIC 02060: YChannelValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-ychannelvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-ychannelvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value of Y in the formula: If (X compare Y), then W. Else, Z. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode YChannelValue { get; }ReturnsA BaseNode reference to the channel, or null if Y is a constant.

### YChannelValue

Gets the channel that specifies the value of *Y* in the formula: If (*X* compare *Y*), then *W*. Else, *Z*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) YChannelValue { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel, or null if *Y* is a constant.

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-yconstantvalue.html language=enus -->
## TOPIC 02061: YConstantValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-yconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-yconstantvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of Y in the formula: If (X compare Y), then W. Else, Z. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double YConstantValue { get; }ReturnsThe value of Y. This property gets a constant value regardless of whether the data source of Y is a constant o

### YConstantValue

Gets the constant value of *Y* in the formula: If (*X* compare *Y*), then *W*. Else, *Z*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double YConstantValue { get; }

#### Returns

The value of *Y*. This property gets a constant value regardless of whether the data source of *Y* is a constant or a channel.

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-zchannelvalue.html language=enus -->
## TOPIC 02062: ZChannelValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-zchannelvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-zchannelvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value of Z in the formula: If (X compare Y), then W. Else, Z. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode ZChannelValue { get; }ReturnsA BaseNode reference to the channel, or null if Z is a constant.

### ZChannelValue

Gets the channel that specifies the value of *Z* in the formula: If (*X* compare *Y*), then *W*. Else, *Z*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) ZChannelValue { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel, or null if *Z* is a constant.

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional-zconstantvalue.html language=enus -->
## TOPIC 02063: ZConstantValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional-zconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional-zconstantvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of Z in the formula: If (X compare Y), then W. Else, Z. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double ZConstantValue { get; }ReturnsThe value of Z. This property gets a constant value regardless of whether the data source of Z is a constant o

### ZConstantValue

Gets the constant value of *Z* in the formula: If (*X* compare *Y*), then *W*. Else, *Z*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double ZConstantValue { get; }

#### Returns

The value of *Z*. This property gets a constant value regardless of whether the data source of *Z* is a constant or a channel.

Parent topic:

Conditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditional.html language=enus -->
## TOPIC 02064: Conditional Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditional.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditional.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a CalculatedChannel with the conditional function. The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value. Derives fromCalculatedChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefiniti

### Conditional Class

Represents a [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) with the conditional function. The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value.

#### Derives from

- CalculatedChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Conditional : CalculatedChannel

#### Remarks

The conditional function can be expressed as: If (*X* compare *Y*), then *W*. Else, *Z*.

Use the members of this class to specify the channel to check for the condition and the type of comparison to use.

**Accessing this Class**

- Conditional Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Conditional(string, string, ushort, BaseNode, BaseNode, double, BaseNode) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and Z are both channel values, and W is a constant. |
| Conditional(string, string, ushort, BaseNode, BaseNode, double, double) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y is a channel value, and W and Z are both constants. |
| Conditional(string, string, ushort, BaseNode, BaseNode, BaseNode, BaseNode) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y, W, and Z are all channel values. |
| Conditional(string, string, ushort, BaseNode, BaseNode, BaseNode, double) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and W are channel values, and Z is a constant. |
| Conditional(string, string, ushort, BaseNode, double, double, BaseNode) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and W are constants, and Z is a channel value. |
| Conditional(string, string, ushort, BaseNode, double, double, double) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y, W, and Z are all constants. |
| Conditional(string, string, ushort, BaseNode, double, BaseNode, BaseNode) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y is a constant, and W and Z are both channel values. |
| Conditional(string, string, ushort, BaseNode, double, BaseNode, double) | Initializes a new instance of Conditional. In the conditional formula (If (X compare Y), then W. Else, Z.), Y and Z are both constants, and W is a channel value. |

#### Fields

| Name | Description |
| --- | --- |
| AND | NI VeriStand converts the values of the double data type to the I32 data type and then performs the AND operation on the values bitwise. |
| Equal | Equal to operation. |
| Greater | Greater than operation. |
| GreaterOrEqual | Greater than or equal to operation. |
| Less | Less than operation. |
| LessOrEqual | Less than or equal to operation. |
| NotEqual | Not equal operation. |
| OR | NI VeriStand converts the values of the double data type to the I32 data type and then performs the OR operation on the values bitwise. |

#### Properties

| Name | Description |
| --- | --- |
| ComparisonMode | Gets or sets the type of comparison to use for the condition. |
| WChannelValue | Gets the channel that specifies the value of W in the formula: If (X compare Y), then W. Else, Z. |
| WConstantValue | Gets the constant value of W in the formula: If (X compare Y), then W. Else, Z. |
| XChannel | Gets or sets the channel to check for the comparison condition. This channel is the value of X in the formula: If (X compare Y), then W. Else, Z. |
| YChannelValue | Gets the channel that specifies the value of Y in the formula: If (X compare Y), then W. Else, Z. |
| YConstantValue | Gets the constant value of Y in the formula: If (X compare Y), then W. Else, Z. |
| ZChannelValue | Gets the channel that specifies the value of Z in the formula: If (X compare Y), then W. Else, Z. |
| ZConstantValue | Gets the constant value of Z in the formula: If (X compare Y), then W. Else, Z. |

#### Methods

| Name | Description |
| --- | --- |
| SetWValue(double) | Sets W in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified constant value. |
| SetWValue(BaseNode) | Sets W in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified channel value. |
| SetYValue(double) | Sets Y in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified constant value. |
| SetYValue(BaseNode) | Sets Y in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified channel value. |
| SetZValue(BaseNode) | Sets Z in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified channel value. |
| SetZValue(double) | Sets Z in the conditional formula (If (X compare Y), then W. Else, Z.), to the specified constant value. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-conditionstepcomparison.html language=enus -->
## TOPIC 02065: ConditionStepComparison Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-conditionstepcomparison.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-conditionstepcomparison.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The condition to use when comparing Variable and Value in a Condition step. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ConditionStepComparisonMembersNameValueDescriptionGreater0Greater than operation. LessLess than operation. EqualEqual to operation. NotEqualNot eq

### ConditionStepComparison Enumeration

The condition to use when comparing *Variable* and *Value* in a [Condition](nationalinstruments-veristand-systemdefinitionapi-condition.html) step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ConditionStepComparison

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Greater | 0 | Greater than operation. |
| Less |  | Less than operation. |
| Equal |  | Equal to operation. |
| NotEqual |  | Not equal operation. |
| GreaterOrEqual |  | Greater than or equal to operation. |
| LessOrEqual |  | Less than or equal to operation. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter-afpdata.html language=enus -->
## TOPIC 02066: AFPData

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter-afpdata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter-afpdata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets an array of data used to configure the Counter feature of AutomaticFrameProcessing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint[] AFPData { get; set; }RemarksThe array consists of the following elements: AFPData[0] — The width, or number of bits to use

### AFPData

Gets or sets an array of data used to configure the [Counter](nationalinstruments-veristand-systemdefinitionapi-counter.html) feature of [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint[] AFPData { get; set; }

#### Remarks

- AFPData[0] — The width, or number of bits to use for the counter. The maximum is 8.
- AFPData[1] — A 32-bit unsigned integer whose most significant 16 bits specify the counter's bit offset, the number of bits by which to offset the bit(s) used for the counter. For example, given a bit offset of 2 and a width of 4, the counter exists on bits 2-5. The least significant 16 bits of this value specify the the storage offset, the number of bytes by which to offset the byte on which the counter data is stored.
- AFPData[2] — The initial value at which to start the counter. You can specify any number between 0 and 255. When the counter passes 255, it starts over at 0.
- AFPData[3] — A value that indicates whether to use the [AlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html) you specify to trigger writing data. A value of 1 specifies to update data whenever the value of the [AlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html) is non-zero. A value of 0 specifies to update data continuously.

#### Returns

An array whose elements are described in the Remarks section.

Parent topic:

Counter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter-alternatechannel.html language=enus -->
## TOPIC 02067: AlternateChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter-alternatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter-alternatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel used to trigger writing data when UseAlternateChannel is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode AlternateChannel { get; }ReturnsThe reference to the channel.

### AlternateChannel

Gets the channel used to trigger writing data when [UseAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-counter-usealternatechannel.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) AlternateChannel { get; }

#### Returns

The reference to the channel.

Parent topic:

Counter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter-indexcounter.html language=enus -->
## TOPIC 02068: IndexCounter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter-indexcounter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter-indexcounter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the index of the counter within the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int IndexCounter { get; set; }ReturnsThe index of the counter.

### IndexCounter

Gets or sets the index of the counter within the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int IndexCounter { get; set; }

#### Returns

The index of the counter.

Parent topic:

Counter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter-maxafplength.html language=enus -->
## TOPIC 02069: MaxAFPLength

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter-maxafplength.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter-maxafplength.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int MaxAFPLength { get; set; }ReturnsA representing the order of the polynomial.

### MaxAFPLength

Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int MaxAFPLength { get; set; }

#### Returns

A  representing the order of the polynomial.

Parent topic:

Counter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter-removealternatechannel.html language=enus -->
## TOPIC 02070: RemoveAlternateChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter-removealternatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter-removealternatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the AlternateChannel specified by SetAlternateChannel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveAlternateChannel()

### RemoveAlternateChannel()

Removes the *AlternateChannel* specified by [SetAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-counter-setalternatechannel__basenode.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveAlternateChannel()

Parent topic:

Counter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter-setalternatechannel__basenode.html language=enus -->
## TOPIC 02071: SetAlternateChannel(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter-setalternatechannel__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter-setalternatechannel__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a channel to use to trigger writing data when UseAlternateChannel is true. Data updates whenever the value of AlternateChannel is non-zero. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetAlternateChannel(BaseNode AlternateChannel)ParametersNameTypeDescriptionAl

### SetAlternateChannel(BaseNode)

Sets a channel to use to trigger writing data when [UseAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-counter-usealternatechannel.html) is true. Data updates whenever the value of *AlternateChannel*  is non-zero.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetAlternateChannel(BaseNode AlternateChannel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| AlternateChannel | BaseNode | The channel to use to trigger writing data. |

Parent topic:

Counter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter-usealternatechannel.html language=enus -->
## TOPIC 02072: UseAlternateChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter-usealternatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter-usealternatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the AlternateChannel specified by SetAlternateChannel is used to trigger writing data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UseAlternateChannel { get; }ReturnsA indicating whether to use the alternate channel. If true, data updates whenever the v

### UseAlternateChannel

Gets whether the *AlternateChannel* specified by [SetAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-counter-setalternatechannel__basenode.html) is used to trigger writing data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UseAlternateChannel { get; }

#### Returns

A  indicating whether to use the alternate channel. If true, data updates whenever the value of [AlternateChannel](nationalinstruments-veristand-systemdefinitionapi-counter-alternatechannel.html) is non-zero. If false, data updates continuously.

Parent topic:

Counter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-counter.html language=enus -->
## TOPIC 02073: Counter Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-counter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-counter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Counter section under the AutomaticFrameProcessing section of an outgoing frame of an NI-XNET CANPort. This feature increments specific bits every time the frame is transmitted across the bus. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### Counter Class

Represents the **Counter** section under the [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section of an outgoing frame of an NI-XNET [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html). This feature increments specific bits every time the frame is transmitted across the bus.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Counter : Section

#### Remarks

Use the members of this class to configure the counter. For example, you can specify a channel to use as a trigger to start counting.

**Accessing this Class**

- [GetCounter](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcounter.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| AFPData | Gets or sets an array of data used to configure the Counter feature of AutomaticFrameProcessing. |
| AlternateChannel | Gets the channel used to trigger writing data when UseAlternateChannel is true. |
| IndexCounter | Gets or sets the index of the counter within the frame. |
| MaxAFPLength | Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC. |
| UseAlternateChannel | Gets whether the AlternateChannel specified by SetAlternateChannel is used to trigger writing data. |

#### Methods

| Name | Description |
| --- | --- |
| RemoveAlternateChannel() | Removes the AlternateChannel specified by SetAlternateChannel. |
| SetAlternateChannel(BaseNode) | Sets a channel to use to trigger writing data when UseAlternateChannel is true. Data updates whenever the value of AlternateChannel is non-zero. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc-afpdata.html language=enus -->
## TOPIC 02074: AFPData

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc-afpdata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc-afpdata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets an array of data used to configure the CRC feature of AutomaticFrameProcessing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint[] AFPData { get; set; }RemarksThe array consists of the following elements: AFPData[0] — The first byte to include in the CRC.AFP

### AFPData

Gets or sets an array of data used to configure the [CRC](nationalinstruments-veristand-systemdefinitionapi-crc.html) feature of [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint[] AFPData { get; set; }

#### Remarks

- AFPData[0] — The first byte to include in the CRC.
- AFPData[1] — The last byte to include in the CRC.
- AFPData[2] — The storage offset, a number of bytes by which to offset the byte on which the CRC data is stored.
- AFPData[3] — A value that indicates whether to use the [AlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html) you specify to trigger writing data. A value of 1 specifies to update data whenever the value of the [AlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html) is non-zero. A value of 0 specifies to update data continuously.

#### Returns

An array whose elements are described in the Remarks section.

Parent topic:

CRC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html language=enus -->
## TOPIC 02075: AlternateChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel used to trigger writing data when UseAlternateChannel is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode AlternateChannel { get; }ReturnsThe reference to the channel.

### AlternateChannel

Gets the channel used to trigger writing data when [UseAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-usealternatechannel.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) AlternateChannel { get; }

#### Returns

The reference to the channel.

Parent topic:

CRC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc-indexcrc.html language=enus -->
## TOPIC 02076: IndexCRC

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc-indexcrc.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc-indexcrc.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the index of the CRC within the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int IndexCRC { get; set; }ReturnsThe index of the CRC.

### IndexCRC

Gets or sets the index of the CRC within the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int IndexCRC { get; set; }

#### Returns

The index of the CRC.

Parent topic:

CRC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc-maxafplength.html language=enus -->
## TOPIC 02077: MaxAFPLength

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc-maxafplength.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc-maxafplength.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int MaxAFPLength { get; set; }ReturnsA representing the order of the polynomial.

### MaxAFPLength

Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int MaxAFPLength { get; set; }

#### Returns

A  representing the order of the polynomial.

Parent topic:

CRC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc-removealternatechannel.html language=enus -->
## TOPIC 02078: RemoveAlternateChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc-removealternatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc-removealternatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the AlternateChannel specified by SetAlternateChannel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveAlternateChannel()

### RemoveAlternateChannel()

Removes the *AlternateChannel* specified by [SetAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-setalternatechannel__basenode.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveAlternateChannel()

Parent topic:

CRC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc-setalternatechannel__basenode.html language=enus -->
## TOPIC 02079: SetAlternateChannel(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc-setalternatechannel__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc-setalternatechannel__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a channel to use to trigger writing data when UseAlternateChannel is true. Data updates whenever the value of AlternateChannel is non-zero. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetAlternateChannel(BaseNode AlternateChannel)ParametersNameTypeDescriptionAl

### SetAlternateChannel(BaseNode)

Sets a channel to use to trigger writing data when [UseAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-usealternatechannel.html) is true. Data updates whenever the value of *AlternateChannel*  is non-zero.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetAlternateChannel(BaseNode AlternateChannel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| AlternateChannel | BaseNode | The channel to use to trigger writing data. |

Parent topic:

CRC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc-usealternatechannel.html language=enus -->
## TOPIC 02080: UseAlternateChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc-usealternatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc-usealternatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the AlternateChannel specified by SetAlternateChannel is used to trigger writing data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UseAlternateChannel { get; }ReturnsA indicating whether to use the alternate channel. If true, data updates whenever the v

### UseAlternateChannel

Gets whether the *AlternateChannel* specified by [SetAlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-setalternatechannel__basenode.html) is used to trigger writing data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UseAlternateChannel { get; }

#### Returns

A  indicating whether to use the alternate channel. If true, data updates whenever the value of [AlternateChannel](nationalinstruments-veristand-systemdefinitionapi-crc-alternatechannel.html) is non-zero. If false, data updates continuously.

Parent topic:

CRC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-crc.html language=enus -->
## TOPIC 02081: CRC Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-crc.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-crc.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the CRC section under the AutomaticFrameProcessing section of an outgoing frame of an NI-XNET CAN port. This feature performs a cyclic redundancy check. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CRC : SectionRemarksUse the members of

### CRC Class

Represents the **CRC** section under the [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section of an outgoing frame of an NI-XNET CAN port. This feature performs a cyclic redundancy check.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CRC : Section

#### Remarks

Use the members of this class to configure the CRC. For example, you can specify a channel to use as a trigger to start writing data to it.

**Accessing this Class**

- [GetCRC](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcrc.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| AFPData | Gets or sets an array of data used to configure the CRC feature of AutomaticFrameProcessing. |
| AlternateChannel | Gets the channel used to trigger writing data when UseAlternateChannel is true. |
| IndexCRC | Gets or sets the index of the CRC within the frame. |
| MaxAFPLength | Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC. |
| UseAlternateChannel | Gets whether the AlternateChannel specified by SetAlternateChannel is used to trigger writing data. |

#### Methods

| Name | Description |
| --- | --- |
| RemoveAlternateChannel() | Removes the AlternateChannel specified by SetAlternateChannel. |
| SetAlternateChannel(BaseNode) | Sets a channel to use to trigger writing data when UseAlternateChannel is true. Data updates whenever the value of AlternateChannel is non-zero. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-adddependencies__dependentfile_arr1.html language=enus -->
## TOPIC 02082: AddDependencies(DependentFile[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-adddependencies__dependentfile_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-adddependencies__dependentfile_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds dependencies to a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void AddDependencies(DependentFile[]

### AddDependencies(DependentFile[])

Adds dependencies to a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void AddDependencies(DependentFile[] dependencies)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dependencies | DependentFile[] | An array of type DependentFile that contains references to the dependencies. |

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-customdevice__string-string.html language=enus -->
## TOPIC 02083: CustomDevice(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-customdevice__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-customdevice__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CustomDevice class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDevice(string Name, string GUID)ParametersNameTypeDescriptionNamestringThe name associated with the custom device, as specified in the Custom Device XML file. GUIDstri

### CustomDevice(string, string)

Initializes a new instance of the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CustomDevice(string Name, string GUID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name associated with the custom device, as specified in the Custom Device XML file. |
| GUID | string | The GUID associated with the custom device, as specified in the Custom Device XML file. |

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-decimation.html language=enus -->
## TOPIC 02084: Decimation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-decimation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-decimation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int Decimation { get; set; }RemarksNI VeriStand handles

### Decimation

Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Decimation { get; set; }

#### Remarks

NI VeriStand handles decimation differently for inline and asynchronous custom devices.

**Inline Custom Devices**

The PCL does not call a custom device if this property specifies not to call the device on that iteration. For example, if you set this property to 4, the PCL calls the device on every fourth iteration.

Because inline custom devices execute within the PCL, the custom device must execute in a short enough amount of time for the entire PCL to complete a full iteration, including the execution of the custom device.

**Asynchronous Custom Devices**

This property only affects when the PCL reads and writes the FIFOs it uses to communicate with the custom device. For example, if you set this property to 4, the PCL reads and writes the FIFOs on every fourth iteration.

Because asynchronous custom devices run in a parallel loop to the PCL, the amount of time the custom device takes to execute does not affect the timing of the PCL execution.

#### Returns

The decimation factor. A value of 1 specifies no decimation.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-deviceenabledstate.html language=enus -->
## TOPIC 02085: DeviceEnabledState

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-deviceenabledstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-deviceenabledstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the state (enabled or disabled) of the custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool DeviceEnabledState { get; set; }RemarksThe effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate

### DeviceEnabledState

Gets or sets the state (enabled or disabled) of the custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool DeviceEnabledState { get; set; }

#### Remarks

The effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate TypeGUID and associated glyph to indicate whether the custom device is disabled.

#### Returns

A Boolean indicating the state of the custom device. If true, the custom device is enabled.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-driverviexecutionmode.html language=enus -->
## TOPIC 02086: DriverVIExecutionMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-driverviexecutionmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-driverviexecutionmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CDDriverExecMode DriverVIExecutionMode { get; set; }ReturnsAn enumeration value of CDDriverExecMod

### DriverVIExecutionMode

Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CDDriverExecMode](nationalinstruments-veristand-systemdefinitionapi-cddriverexecmode.html) DriverVIExecutionMode { get; set; }

#### Returns

An enumeration value of [CDDriverExecMode](nationalinstruments-veristand-systemdefinitionapi-cddriverexecmode.html).

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-exportcommonpropertiestojson__jobject.html language=enus -->
## TOPIC 02087: ExportCommonPropertiesToJson(JObject)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-exportcommonpropertiestojson__jobject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-exportcommonpropertiestojson__jobject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Export properties to the specified Json object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected override void ExportCommonPropertiesToJson(JObject propertiesContainer)ParametersNameTypeDescriptionpropertiesContainerJObjectThe Json object to which properties will be export

### ExportCommonPropertiesToJson(JObject)

Export properties to the specified Json object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected override void ExportCommonPropertiesToJson(JObject propertiesContainer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertiesContainer | JObject | The Json object to which properties will be exported. |

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttojson__out.html language=enus -->
## TOPIC 02088: ExportToJson(out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttojson__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttojson__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the current instance of CustomDevice to a JSON string. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Error ExportToJson(out string jsonString)ParametersNameTypeDescriptionjsonStringout stringThe JSON string representing the custom device configuration.ReturnsThe er

### ExportToJson(out string)

Exports the current instance of [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) to a JSON string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Error ExportToJson(out string jsonString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| jsonString | out string | The JSON string representing the custom device configuration. |

#### Returns

The error that prevented the export operation.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttojson__string.html language=enus -->
## TOPIC 02089: ExportToJson(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttojson__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttojson__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the current instance of CustomDevice to a JSON file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Error ExportToJson(string jsonFilePath)ParametersNameTypeDescriptionjsonFilePathstringThe file path where the JSON file will be created.ReturnsThe error that prevente

### ExportToJson(string)

Exports the current instance of [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) to a JSON file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Error ExportToJson(string jsonFilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| jsonFilePath | string | The file path where the JSON file will be created. |

#### Returns

The error that prevented the export operation.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttoxml__string.html language=enus -->
## TOPIC 02090: ExportToXml(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttoxml__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-exporttoxml__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the custom device configuration to the provided XML file path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Error ExportToXml(string filepath)ParametersNameTypeDescriptionfilepathstringPath of XML file to save the custom device configuration.ReturnsThe error that

### ExportToXml(string)

Exports the custom device configuration to the provided XML file path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Error ExportToXml(string filepath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | Path of XML file to save the custom device configuration. |

#### Returns

The error that prevented the export operation.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-fifosinkdepth.html language=enus -->
## TOPIC 02091: FIFOSinkDepth

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-fifosinkdepth.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-fifosinkdepth.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint FIFOSinkDepth { get; set; }ReturnsThe depth of the

### FIFOSinkDepth

Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint FIFOSinkDepth { get; set; }

#### Returns

The depth of the FIFO at the sink.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-fifosourcedepth.html language=enus -->
## TOPIC 02092: FIFOSourceDepth

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-fifosourcedepth.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-fifosourcedepth.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint FIFOSourceDepth { get; set; }ReturnsThe depth of

### FIFOSourceDepth

Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint FIFOSourceDepth { get; set; }

#### Returns

The depth of the FIFO at the source.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicechannellist.html language=enus -->
## TOPIC 02093: GetCustomDeviceChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicechannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicechannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CustomDeviceChannel elements from the current CustomDevice. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceChannel[] GetCustomDeviceChannelList()RemarksModifications you make to the contents of this list apply to the system defini

### GetCustomDeviceChannelList()

Gets an array that contains the [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html)[] GetCustomDeviceChannelList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html).

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicesectionlist.html language=enus -->
## TOPIC 02094: GetCustomDeviceSectionList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicesectionlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicesectionlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CustomDeviceSection elements from the current CustomDevice. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDevic

### GetCustomDeviceSectionList()

Gets an array that contains the [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html). Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html)[] GetCustomDeviceSectionList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html).

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicewaveformlist.html language=enus -->
## TOPIC 02095: GetCustomDeviceWaveformList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicewaveformlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicewaveformlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CustomDeviceWaveform elements from the current CustomDevice. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceWaveform[] GetCustomDeviceWaveformList()RemarksAny modification that you make to the contents of this array also apply to

### GetCustomDeviceWaveformList()

Gets an array that contains the [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html)[] GetCustomDeviceWaveformList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html).

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-getdependencies.html language=enus -->
## TOPIC 02096: GetDependencies()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-getdependencies.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-getdependencies.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DependentFile elements from the current CustomDevice. Dependent files are any files that the device requires and that deploy to the target along with the custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile[] GetDepende

### GetDependencies()

Gets an array that contains the [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html). Dependent files are any files that the device requires and that deploy to the target along with the custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html)[] GetDependencies()

#### Returns

An array that contains the [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) elements from the current [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html).

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-getdriverviforownertargettype.html language=enus -->
## TOPIC 02097: GetDriverVIForOwnerTargetType()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-getdriverviforownertargettype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-getdriverviforownertargettype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RT Driver VI for the target indicated by the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile

### GetDriverVIForOwnerTargetType()

Gets the RT Driver VI for the target indicated by the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) GetDriverVIForOwnerTargetType()

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the RT Driver VI.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-getdrivervis.html language=enus -->
## TOPIC 02098: GetDriverVIs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-getdrivervis.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-getdrivervis.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all the RT Driver VIs associated with the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile[] GetDr

### GetDriverVIs()

Gets all the RT Driver VIs associated with the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html)[] GetDriverVIs()

#### Returns

An array of [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) references to the RT Driver VIs.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-gettimingsourceinitvis.html language=enus -->
## TOPIC 02099: GetTimingSourceInitVIs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-gettimingsourceinitvis.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-gettimingsourceinitvis.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Timing Source Initialization VIs associated with the custom device. If you configure the custom device as the master timing source for the target, these VIs create a timing source for the Primary Control Loop. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Dependen

### GetTimingSourceInitVIs()

Gets the Timing Source Initialization VIs associated with the custom device. If you configure the custom device as the master timing source for the target, these VIs create a timing source for the Primary Control Loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html)[] GetTimingSourceInitVIs()

#### Returns

An array of [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) references to the Timing Source Initialization VIs.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromjson__string-out.html language=enus -->
## TOPIC 02100: ImportFromJson(string, out CustomDevice)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromjson__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromjson__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a CustomDevice from a JSON file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected Error ImportFromJson(string jsonFilePath, out CustomDevice deserializedCustomDevice)ParametersNameTypeDescriptionjsonFilePathstringThe file path of the JSON file to read.deserializedC

### ImportFromJson(string, out CustomDevice)

Imports a [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) from a JSON file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected Error ImportFromJson(string jsonFilePath, out CustomDevice deserializedCustomDevice)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| jsonFilePath | string | The file path of the JSON file to read. |
| deserializedCustomDevice | out CustomDevice | The imported custom device. |

#### Returns

The error that prevented the import operation, if one occurred.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromjson__string.html language=enus -->
## TOPIC 02101: ImportFromJson(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromjson__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromjson__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a CustomDevice configuration from a JSON file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Error ImportFromJson(string jsonFilePath)ParametersNameTypeDescriptionjsonFilePathstringThe file path of the JSON file to read.ReturnsThe error that prevented the import op

### ImportFromJson(string)

Imports a [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) configuration from a JSON file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Error ImportFromJson(string jsonFilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| jsonFilePath | string | The file path of the JSON file to read. |

#### Returns

The error that prevented the import operation.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromxml__string.html language=enus -->
## TOPIC 02102: ImportFromXml(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromxml__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-importfromxml__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports the custom device configuration from the provided XML file path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Error ImportFromXml(string filepath)ParametersNameTypeDescriptionfilepathstringPath of XML file from which the custom device configuration to be loaded.Re

### ImportFromXml(string)

Imports the custom device configuration from the provided XML file path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Error ImportFromXml(string filepath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | Path of XML file from which the custom device configuration to be loaded. |

#### Returns

The error that prevented the import operation.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-initializebasenodetypetocustomdevice__basenodetype.html language=enus -->
## TOPIC 02103: InitializeBaseNodeTypeToCustomDevice(BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-initializebasenodetypetocustomdevice__basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-initializebasenodetypetocustomdevice__basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes the BaseNodeType object to the specified custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static Error InitializeBaseNodeTypeToCustomDevice(BaseNodeType node)ParametersNameTypeDescriptionnodeBaseNodeTypeThe BaseNodeType object to initialize with the

### InitializeBaseNodeTypeToCustomDevice(BaseNodeType)

Initializes the BaseNodeType object to the specified custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static Error InitializeBaseNodeTypeToCustomDevice(BaseNodeType node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BaseNodeType | The BaseNodeType object to initialize with the custom device with. |

#### Returns

The error that prevented the initialization, if any.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-looptype.html language=enus -->
## TOPIC 02104: LoopType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-looptype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-looptype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of loop (TimedLoop or WhileLoop) in which the custom device runs. This property only applies to asynchronous custom devices. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CDLoopType LoopType { get; set; }ReturnsAn enumeration value of CDLoopType.

### LoopType

Gets or sets the type of loop (TimedLoop or WhileLoop) in which the custom device runs. This property only applies to asynchronous custom devices.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CDLoopType](nationalinstruments-veristand-systemdefinitionapi-cdlooptype.html) LoopType { get; set; }

#### Returns

An enumeration value of [CDLoopType](nationalinstruments-veristand-systemdefinitionapi-cdlooptype.html).

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-resetdependencies.html language=enus -->
## TOPIC 02105: ResetDependencies()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-resetdependencies.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-resetdependencies.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all the dependencies from the custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ResetDependencie

### ResetDependencies()

Removes all the dependencies from the custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ResetDependencies()

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-setdrivervis__dependentfile_arr1.html language=enus -->
## TOPIC 02106: SetDriverVIs(DependentFile[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-setdrivervis__dependentfile_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-setdrivervis__dependentfile_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RT Driver VIs to associate with the custom device. A custom device requires at least one RT Driver VI. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. SyntaxNamespace: NationalInstruments.VeriSta

### SetDriverVIs(DependentFile[])

Sets the RT Driver VIs to associate with the custom device. A custom device requires at least one RT Driver VI. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetDriverVIs(DependentFile[] driverVIs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| driverVIs | DependentFile[] | An array of references to the RT Driver VIs. |

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-settimingsourceinitvis__dependentfile_arr1.html language=enus -->
## TOPIC 02107: SetTimingSourceInitVIs(DependentFile[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-settimingsourceinitvis__dependentfile_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-settimingsourceinitvis__dependentfile_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Timing Source Initialization VIs to associate with the custom device. Timing Source Initialization VIs are required if you want to use a custom device that is not a timing and sync device as the master timing source for the Primary Control Loop. SyntaxNamespace: NationalInstruments.VeriStan

### SetTimingSourceInitVIs(DependentFile[])

Sets the Timing Source Initialization VIs to associate with the custom device. Timing Source Initialization VIs are required if you want to use a custom device that is not a timing and sync device as the master timing source for the Primary Control Loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetTimingSourceInitVIs(DependentFile[] timingSourceInitVIs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timingSourceInitVIs | DependentFile[] | An array of references to the Timing Source Initialization VIs. |

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-timedlooppriority.html language=enus -->
## TOPIC 02108: TimedLoopPriority

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-timedlooppriority.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-timedlooppriority.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the priority (High, Low, or Medium) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CDTimeLoopPriority TimedLoopPrio

### TimedLoopPriority

Gets or sets the priority (High, Low, or Medium) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CDTimeLoopPriority](nationalinstruments-veristand-systemdefinitionapi-cdtimelooppriority.html) TimedLoopPriority { get; set; }

#### Returns

An enumeration value of [CDTimeLoopPriority](nationalinstruments-veristand-systemdefinitionapi-cdtimelooppriority.html).

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-usedeviceclock.html language=enus -->
## TOPIC 02109: UseDeviceClock

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-usedeviceclock.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-usedeviceclock.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpubl

### UseDeviceClock

Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UseDeviceClock { get; set; }

#### Remarks

If true, the system passes the timing source from the PCL to the custom device RT Driver VI. The PCL runs the custom device Timed Loop after NI VeriStand sets the outputs of the custom device. This prevents the PCL from running late if the custom device finishes late.

#### Returns

true if the Timed Loop is synchronized with the PCL timing source. Otherwise false.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice-version.html language=enus -->
## TOPIC 02110: Version

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice-version.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice-version.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code. SyntaxNamespace: Nation

### Version

Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Version { get; set; }

#### Returns

A string stored with the custom device.

Parent topic:

CustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevice.html language=enus -->
## TOPIC 02111: CustomDevice Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a custom device in NI VeriStand. Derives fromCustomDeviceSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CustomDevice : CustomDeviceSectionRemarksUse the members of this class to get and set properties of the custom device, such as its execution mode

### CustomDevice Class

Represents a custom device in NI VeriStand.

#### Derives from

- CustomDeviceSection

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CustomDevice : CustomDeviceSection

#### Remarks

Use the members of this class to get and set properties of the custom device, such as its execution mode (asynchronous versus inline), timing information, and dependencies.

**Accessing this Class**

- [GetCustomDeviceList](nationalinstruments-veristand-systemdefinitionapi-customdevices-getcustomdevicelist.html)
- [CustomTimingDevice](nationalinstruments-veristand-systemdefinitionapi-target-customtimingdevice.html)
- [IDToCustomDevice](nationalinstruments-veristand-systemdefinitionapi-nodeidutil-idtocustomdevice__ulong.html)
- CustomDevice Constructor

Note

Refer to the *Creating Custom Devices* section of the *NI VeriStand Help* for more information about building custom devices. This content is also available from the *LabVIEW Help*.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CustomDevice(string, string) | Initializes a new instance of the CustomDevice class. |

#### Properties

| Name | Description |
| --- | --- |
| Decimation | Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device. |
| DeviceEnabledState | Gets or sets the state (enabled or disabled) of the custom device. |
| DriverVIExecutionMode | Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously. |
| FIFOSinkDepth | Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices. |
| FIFOSourceDepth | Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices. |
| LoopType | Gets or sets the type of loop (TimedLoop or WhileLoop) in which the custom device runs. This property only applies to asynchronous custom devices. |
| TimedLoopPriority | Gets or sets the priority (High, Low, or Medium) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops. |
| UseDeviceClock | Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops. |
| Version | Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code. |

#### Methods

| Name | Description |
| --- | --- |
| AddDependencies(DependentFile[]) | Adds dependencies to a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device. |
| ExportToJson(out string) | Exports the current instance of CustomDevice to a JSON string. |
| ExportToJson(string) | Exports the current instance of CustomDevice to a JSON file. |
| ExportToXml(string) | Exports the custom device configuration to the provided XML file path. |
| GetCustomDeviceChannelList() | Gets an array that contains the CustomDeviceChannel elements from the current CustomDevice. |
| GetCustomDeviceSectionList() | Gets an array that contains the CustomDeviceSection elements from the current CustomDevice. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy. |
| GetCustomDeviceWaveformList() | Gets an array that contains the CustomDeviceWaveform elements from the current CustomDevice. |
| GetDependencies() | Gets an array that contains the DependentFile elements from the current CustomDevice. Dependent files are any files that the device requires and that deploy to the target along with the custom device. |
| GetDriverVIForOwnerTargetType() | Gets the RT Driver VI for the target indicated by the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. |
| GetDriverVIs() | Gets all the RT Driver VIs associated with the custom device. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. |
| GetTimingSourceInitVIs() | Gets the Timing Source Initialization VIs associated with the custom device. If you configure the custom device as the master timing source for the target, these VIs create a timing source for the Primary Control Loop. |
| ImportFromJson(string) | Imports a CustomDevice configuration from a JSON file. |
| ImportFromXml(string) | Imports the custom device configuration from the provided XML file path. |
| ResetDependencies() | Removes all the dependencies from the custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device. |
| SetDriverVIs(DependentFile[]) | Sets the RT Driver VIs to associate with the custom device. A custom device requires at least one RT Driver VI. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes. |
| SetTimingSourceInitVIs(DependentFile[]) | Sets the Timing Source Initialization VIs to associate with the custom device. Timing Source Initialization VIs are required if you want to use a custom device that is not a timing and sync device as the master timing source for the Primary Control Loop. |
| ExportCommonPropertiesToJson(JObject) | Export properties to the specified Json object. |
| ImportFromJson(string, out CustomDevice) | Imports a CustomDevice from a JSON file. |
| InitializeBaseNodeTypeToCustomDevice(BaseNodeType) | Initializes the BaseNodeType object to the specified custom device. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-exportcommonpropertiestojson__jobject.html language=enus -->
## TOPIC 02112: ExportCommonPropertiesToJson(JObject)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-exportcommonpropertiestojson__jobject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-exportcommonpropertiestojson__jobject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Export properties to the specified Json object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected void ExportCommonPropertiesToJson(JObject propertiesContainer)ParametersNameTypeDescriptionpropertiesContainerJObjectThe Json object to which properties will be exported.

### ExportCommonPropertiesToJson(JObject)

Export properties to the specified Json object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected void ExportCommonPropertiesToJson(JObject propertiesContainer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertiesContainer | JObject | The Json object to which properties will be exported. |

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getbinarystringproperty__string-out.html language=enus -->
## TOPIC 02113: GetBinaryStringProperty(string, out byte[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getbinarystringproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getbinarystringproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the binary string value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetBinaryStringProperty(string name, out byte[] value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are

### GetBinaryStringProperty(string, out byte[])

Gets the binary string value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetBinaryStringProperty(string name, out byte[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out byte[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getbooleanproperty__string-out.html language=enus -->
## TOPIC 02114: GetBooleanProperty(string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getbooleanproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getbooleanproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Boolean value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetBooleanProperty(string name, out bool value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case-sensitiv

### GetBooleanProperty(string, out bool)

Gets the Boolean value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetBooleanProperty(string name, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out bool | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentfileproperty__string-out.html language=enus -->
## TOPIC 02115: GetDependentFileProperty(string, out DependentFile)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentfileproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentfileproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference to the dependent file that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDependentFileProperty(string name, out DependentFile value)ParametersNameTypeDescriptionnamestringThe nam

### GetDependentFileProperty(string, out DependentFile)

Gets the reference to the dependent file that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDependentFileProperty(string name, out DependentFile value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out DependentFile | The DependentFile that is the value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentnodeproperty__string-out.1.html language=enus -->
## TOPIC 02116: GetDependentNodeProperty(string, out BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentnodeproperty__string-out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentnodeproperty__string-out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference to the dependent node that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDependentNodeProperty(string name, out BaseNode value)ParametersNameTypeDescriptionnamestringThe name of

### GetDependentNodeProperty(string, out BaseNode)

Gets the reference to the dependent node that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDependentNodeProperty(string name, out BaseNode value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out BaseNode | The reference to the dependent node that is the value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentnodeproperty__string-out.html language=enus -->
## TOPIC 02117: GetDependentNodeProperty(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentnodeproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdependentnodeproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the dependent node, as specified in the system definition file, that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDependentNodeProperty(string name, out string nodePath)Parameters

### GetDependentNodeProperty(string, out string)

Gets the path to the dependent node, as specified in the system definition file, that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDependentNodeProperty(string name, out string nodePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| nodePath | out string | The path to the dependent node. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdictionaryarrayproperty__string-out.html language=enus -->
## TOPIC 02118: GetDictionaryArrayProperty(string, out Dictionary[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdictionaryarrayproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdictionaryarrayproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference to the Dictionary array that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDictionaryArrayProperty(string name, out Dictionary[] value)ParametersNameTypeDescriptionnamestringThe

### GetDictionaryArrayProperty(string, out Dictionary[])

Gets the reference to the [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html) array that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDictionaryArrayProperty(string name, out Dictionary[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out Dictionary[] | The array of Dictionary objects. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdictionaryproperty__string-out.html language=enus -->
## TOPIC 02119: GetDictionaryProperty(string, out Dictionary)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdictionaryproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdictionaryproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the reference to the Dictionary that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDictionaryProperty(string name, out Dictionary value)ParametersNameTypeDescriptionnamestringThe name of the p

### GetDictionaryProperty(string, out Dictionary)

Gets the reference to the [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html) that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDictionaryProperty(string name, out Dictionary value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out Dictionary | The Dictionary object. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdoublearrayproperty__string-out.html language=enus -->
## TOPIC 02120: GetDoubleArrayProperty(string, out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdoublearrayproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdoublearrayproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of double-precision floating point numbers that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDoubleArrayProperty(string name, out double[] value)ParametersNameTypeDescriptionnamestr

### GetDoubleArrayProperty(string, out double[])

Gets the array of double-precision floating point numbers that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDoubleArrayProperty(string name, out double[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out double[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdoubleproperty__string-out.html language=enus -->
## TOPIC 02121: GetDoubleProperty(string, out double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdoubleproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getdoubleproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the double-precision floating point value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetDoubleProperty(string name, out double value)ParametersNameTypeDescriptionnamestringThe name of the property. Propert

### GetDoubleProperty(string, out double)

Gets the double-precision floating point value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetDoubleProperty(string name, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out double | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-geti32arrayproperty__string-out.html language=enus -->
## TOPIC 02122: GetI32ArrayProperty(string, out int[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-geti32arrayproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-geti32arrayproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of 32-bit signed integers that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI32ArrayProperty(string name, out int[] value)ParametersNameTypeDescriptionnamestringThe name of the prop

### GetI32ArrayProperty(string, out int[])

Gets the array of 32-bit signed integers that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI32ArrayProperty(string name, out int[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out int[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-geti32property__string-out.html language=enus -->
## TOPIC 02123: GetI32Property(string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-geti32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-geti32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the 32-bit signed integer that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetI32Property(string name, out int value)ParametersNameTypeDescriptionnamestringThe name of the property. Property na

### GetI32Property(string, out int)

Gets the 32-bit signed integer that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetI32Property(string name, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out int | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getpropertynames.html language=enus -->
## TOPIC 02124: GetPropertyNames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getpropertynames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getpropertynames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the names of all the properties associated with a custom device item. Custom device item properties store and communicate state information. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string[] GetPropertyNames()ReturnsThe array of property name strings.

### GetPropertyNames()

Gets the names of all the properties associated with a custom device item. Custom device item properties store and communicate state information.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string[] GetPropertyNames()

#### Returns

The array of property name strings.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getpropertytype__string-out.html language=enus -->
## TOPIC 02125: GetPropertyType(string, out PropertyContent)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getpropertytype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getpropertytype__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the data type of the custom device item property specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetPropertyType(string propertyName, out PropertyContent type)ParametersNameTypeDescriptionpropertyNamestringThe name of the property. Prope

### GetPropertyType(string, out PropertyContent)

Gets the data type of the custom device item property specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetPropertyType(string propertyName, out PropertyContent type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. Property names are case sensitive. |
| type | out PropertyContent | The data type of the property. |

#### Returns

true if the *propertyName*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getstringarrayproperty__string-out.html language=enus -->
## TOPIC 02126: GetStringArrayProperty(string, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getstringarrayproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getstringarrayproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of strings that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetStringArrayProperty(string name, out string[] value)ParametersNameTypeDescriptionnamestringThe name of the property. Pro

### GetStringArrayProperty(string, out string[])

Gets the array of strings that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetStringArrayProperty(string name, out string[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out string[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getstringproperty__string-out.html language=enus -->
## TOPIC 02127: GetStringProperty(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getstringproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getstringproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetStringProperty(string name, out string value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case-sensitiv

### GetStringProperty(string, out string)

Gets the string value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetStringProperty(string name, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out string | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu16property__string-out.html language=enus -->
## TOPIC 02128: GetU16Property(string, out ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu16property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu16property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 16-bit integer value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU16Property(string name, out ushort value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are

### GetU16Property(string, out ushort)

Gets the unsigned 16-bit integer value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU16Property(string name, out ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out ushort | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu32arrayproperty__string-out.html language=enus -->
## TOPIC 02129: GetU32ArrayProperty(string, out uint[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu32arrayproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu32arrayproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the array of unsigned 32-bit integers that is the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU32ArrayProperty(string name, out uint[] value)ParametersNameTypeDescriptionnamestringThe name of the p

### GetU32ArrayProperty(string, out uint[])

Gets the array of unsigned 32-bit integers that is the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU32ArrayProperty(string name, out uint[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out uint[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu32property__string-out.html language=enus -->
## TOPIC 02130: GetU32Property(string, out uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 32-bit integer value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU32Property(string name, out uint value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are c

### GetU32Property(string, out uint)

Gets the unsigned 32-bit integer value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU32Property(string name, out uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out uint | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu64property__string-out.html language=enus -->
## TOPIC 02131: GetU64Property(string, out ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu64property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getu64property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unsigned 64-bit integer value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetU64Property(string name, out ulong value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are

### GetU64Property(string, out ulong)

Gets the unsigned 64-bit integer value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetU64Property(string name, out ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | out ulong | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getvariantproperty__string-out-out.html language=enus -->
## TOPIC 02132: GetVariantProperty(string, out byte[], out byte[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getvariantproperty__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-getvariantproperty__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the LabVIEW variant value of the custom device item property specified by name . The variant data type is a generic container for all other LabVIEW data types. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetVariantProperty(string name, out byte[] type, out byte

### GetVariantProperty(string, out byte[], out byte[])

Gets the LabVIEW variant value of the custom device item property specified by *name* . The variant data type is a generic container for all other LabVIEW data types.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetVariantProperty(string name, out byte[] type, out byte[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| type | out byte[] | The data type of value . |
| value | out byte[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-movenodeto__customdevicebase-out.html language=enus -->
## TOPIC 02133: MoveNodeTo(CustomDeviceBase, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-movenodeto__customdevicebase-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-movenodeto__customdevicebase-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves a custom device item to a new location within the custom device hierarchy. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool MoveNodeTo(CustomDeviceBase ParentType, out Error error)ParametersNameTypeDescriptionParentTypeCustomDeviceBaseThe reference to the parent no

### MoveNodeTo(CustomDeviceBase, out Error)

Moves a custom device item to a new location within the custom device hierarchy.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool MoveNodeTo(CustomDeviceBase ParentType, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ParentType | CustomDeviceBase | The reference to the parent node to move the item to. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the item moves successfully.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-movenodeto__customdevicebase.html language=enus -->
## TOPIC 02134: MoveNodeTo(CustomDeviceBase)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-movenodeto__customdevicebase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-movenodeto__customdevicebase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves a custom device item to a new location within the custom device hierarchy. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool MoveNodeTo(CustomDeviceBase ParentType)ParametersNameTypeDescriptionParentTypeCustomDeviceBaseThe reference to the parent node to move the it

### MoveNodeTo(CustomDeviceBase)

Moves a custom device item to a new location within the custom device hierarchy.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool MoveNodeTo(CustomDeviceBase ParentType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ParentType | CustomDeviceBase | The reference to the parent node to move the item to. |

#### Returns

true if the item moves successfully.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeerror__string.html language=enus -->
## TOPIC 02135: RemoveError(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeerror__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeerror__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes an error that matches the specified ErrorID . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveError(string ErrorID)RemarksUse the ReportError method to configure errors and set ErrorID strings. ParametersNameTypeDescriptionErrorIDstringThe ID string of the

### RemoveError(string)

Removes an error that matches the specified *ErrorID* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveError(string ErrorID)

#### Remarks

Use the [ReportError](nationalinstruments-veristand-systemdefinitionapi-customdevicebase-reporterror__string-bool-int-string.html) method to configure errors and set *ErrorID*  strings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ErrorID | string | The ID string of the error to remove. |

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeproperty__string-out.html language=enus -->
## TOPIC 02136: RemoveProperty(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool RemoveProperty(string name, out Error error)ParametersNameTypeDescriptionnamestringThe name of the property to remove. errorout ErrorReturns an NationalInstrument

### RemoveProperty(string, out Error)

Removes the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool RemoveProperty(string name, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property to remove. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the property is successfully removed.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeproperty__string.html language=enus -->
## TOPIC 02137: RemoveProperty(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeproperty__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-removeproperty__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool RemoveProperty(string name)ParametersNameTypeDescriptionnamestringThe name of the property to remove. Returnstrue if the property is successfully removed.

### RemoveProperty(string)

Removes the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool RemoveProperty(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property to remove. |

#### Returns

true if the property is successfully removed.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-renamenode__string-bool.html language=enus -->
## TOPIC 02138: RenameNode(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-renamenode__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-renamenode__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Renames this node to the name you specify, if the name that you specify is not already in use by a sibling of this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic new bool RenameNode(string NewName, bool ForceRename)ParametersNameTypeDescriptionNewNamestringThe new nam

### RenameNode(string, bool)

Renames this node to the name you specify, if the name that you specify is not already in use by a sibling of this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public new bool RenameNode(string NewName, bool ForceRename)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| NewName | string | The new name of the node. |
| ForceRename | bool | Renames the node even if it is protected. |

#### Returns

true if the node was renamed successfully; otherwise false.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-reporterror__string-bool-int-string.html language=enus -->
## TOPIC 02139: ReportError(string, bool, int, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-reporterror__string-bool-int-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-reporterror__string-bool-int-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to report an error that occurs during custom device execution. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ReportError(string ErrorID, bool isError, int errCode, string message)ParametersNameTypeDescriptionErrorIDstringA string that identifies the

### ReportError(string, bool, int, string)

Configures whether to report an error that occurs during custom device execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ReportError(string ErrorID, bool isError, int errCode, string message)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ErrorID | string | A string that identifies the error. |
| isError | bool | A Boolean that specifies whether to recognize errCode as an error. true if you want to report the error. |
| errCode | int | The error code that isError recognizes or ignores. In LabVIEW, this is the code element of the standard error cluster. |
| message | string | A message to publish when the error is reported. |

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setbinarystringproperty__string-byte_arr1.html language=enus -->
## TOPIC 02140: SetBinaryStringProperty(string, byte[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setbinarystringproperty__string-byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setbinarystringproperty__string-byte_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a binary string value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetBinaryStringProperty(string name, byte[] value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case-

### SetBinaryStringProperty(string, byte[])

Sets a binary string value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetBinaryStringProperty(string name, byte[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | byte[] | The value to set. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setbooleanproperty__string-bool.html language=enus -->
## TOPIC 02141: SetBooleanProperty(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setbooleanproperty__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setbooleanproperty__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Boolean value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetBooleanProperty(string name, bool value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case-sensitive.val

### SetBooleanProperty(string, bool)

Sets a Boolean value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetBooleanProperty(string name, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | bool | The value to set. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentfileproperty__string-dependentfile.html language=enus -->
## TOPIC 02142: SetDependentFileProperty(string, DependentFile)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentfileproperty__string-dependentfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentfileproperty__string-dependentfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a reference to a dependent file as the value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetDependentFileProperty(string name, DependentFile value)ParametersNameTypeDescriptionnamestringThe name of the pro

### SetDependentFileProperty(string, DependentFile)

Sets a reference to a dependent file as the value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetDependentFileProperty(string name, DependentFile value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | DependentFile | The DependentFile to set as the value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentnodeproperty__string-basenode.html language=enus -->
## TOPIC 02143: SetDependentNodeProperty(string, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentnodeproperty__string-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentnodeproperty__string-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a reference to a dependent node as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetDependentNodeProperty(string name, BaseNode value)ParametersNameTypeDescriptionnamestringThe name of the property.

### SetDependentNodeProperty(string, BaseNode)

Sets a reference to a dependent node as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetDependentNodeProperty(string name, BaseNode value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | BaseNode | The reference to the dependent node that is the value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentnodeproperty__string-string.html language=enus -->
## TOPIC 02144: SetDependentNodeProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentnodeproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdependentnodeproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a path to a dependent node, as specified in the system definition file, as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetDependentNodeProperty(string name, string depNodePath)ParametersNameTypeDe

### SetDependentNodeProperty(string, string)

Sets a path to a dependent node, as specified in the system definition file, as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetDependentNodeProperty(string name, string depNodePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| depNodePath | string | The path to the dependent node. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdictionaryarrayproperty__string-dictionary_arr1.html language=enus -->
## TOPIC 02145: SetDictionaryArrayProperty(string, Dictionary[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdictionaryarrayproperty__string-dictionary_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdictionaryarrayproperty__string-dictionary_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a reference to a Dictionary as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetDictionaryArrayProperty(string name, Dictionary[] value)ParametersNameTypeDescriptionnamestringThe name of the propert

### SetDictionaryArrayProperty(string, Dictionary[])

Sets a reference to a [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html) as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetDictionaryArrayProperty(string name, Dictionary[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | Dictionary[] | The reference to the Dictionary array. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdictionaryproperty__string-dictionary.html language=enus -->
## TOPIC 02146: SetDictionaryProperty(string, Dictionary)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdictionaryproperty__string-dictionary.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdictionaryproperty__string-dictionary.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a reference to a Dictionary element as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetDictionaryProperty(string name, Dictionary value)ParametersNameTypeDescriptionnamestringThe name of the proper

### SetDictionaryProperty(string, Dictionary)

Sets a reference to a [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html) element as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetDictionaryProperty(string name, Dictionary value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | Dictionary | The reference to the Dictionary element. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdoublearrayproperty__string-double_arr1.html language=enus -->
## TOPIC 02147: SetDoubleArrayProperty(string, double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdoublearrayproperty__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdoublearrayproperty__string-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an array of double-precision floating point numbers as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetDoubleArrayProperty(string name, double[] value)ParametersNameTypeDescriptionnamestringThe nam

### SetDoubleArrayProperty(string, double[])

Sets an array of double-precision floating point numbers as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetDoubleArrayProperty(string name, double[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | double[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdoubleproperty__string-double.html language=enus -->
## TOPIC 02148: SetDoubleProperty(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdoubleproperty__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setdoubleproperty__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a double-precision floating point value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetDoubleProperty(string name, double value)ParametersNameTypeDescriptionnamestringThe name of the property. Property nam

### SetDoubleProperty(string, double)

Sets a double-precision floating point value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetDoubleProperty(string name, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | double | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-seti32arrayproperty__string-int_arr1.html language=enus -->
## TOPIC 02149: SetI32ArrayProperty(string, int[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-seti32arrayproperty__string-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-seti32arrayproperty__string-int_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an array of 32-bit signed integers as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetI32ArrayProperty(string name, int[] value)ParametersNameTypeDescriptionnamestringThe name of the property. Prop

### SetI32ArrayProperty(string, int[])

Sets an array of 32-bit signed integers as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetI32ArrayProperty(string name, int[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | int[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-seti32property__string-int.html language=enus -->
## TOPIC 02150: SetI32Property(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-seti32property__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-seti32property__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a 32-bit signed integer value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetI32Property(string name, int value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case-sens

### SetI32Property(string, int)

Sets a 32-bit signed integer value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetI32Property(string name, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | int | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setlogfileproducerflag__bool.html language=enus -->
## TOPIC 02151: SetLogFileProducerFlag(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setlogfileproducerflag__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setlogfileproducerflag__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a flag indicating whether this node is a log file producer. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetLogFileProducerFlag(bool isLogFileProducer)ParametersNameTypeDescriptionisLogFileProducerboolSpecifies whether the node is a log file producer

### SetLogFileProducerFlag(bool)

Sets a flag indicating whether this node is a log file producer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetLogFileProducerFlag(bool isLogFileProducer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| isLogFileProducer | bool | Specifies whether the node is a log file producer |

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setstringarrayproperty__string-string_arr1.html language=enus -->
## TOPIC 02152: SetStringArrayProperty(string, string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setstringarrayproperty__string-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setstringarrayproperty__string-string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an array of strings as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetStringArrayProperty(string name, string[] value)ParametersNameTypeDescriptionnamestringThe name of the property. Property name

### SetStringArrayProperty(string, string[])

Sets an array of strings as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetStringArrayProperty(string name, string[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | string[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setstringproperty__string-string.html language=enus -->
## TOPIC 02153: SetStringProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setstringproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setstringproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a string value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetStringProperty(string name, string value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case-sensitive.val

### SetStringProperty(string, string)

Sets a string value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetStringProperty(string name, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | string | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu16property__string-ushort.html language=enus -->
## TOPIC 02154: SetU16Property(string, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu16property__string-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu16property__string-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an unsigned 16-bit integer value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetU16Property(string name, ushort value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are cas

### SetU16Property(string, ushort)

Sets an unsigned 16-bit integer value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetU16Property(string name, ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | ushort | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu32arrayproperty__string-uint_arr1.html language=enus -->
## TOPIC 02155: SetU32ArrayProperty(string, uint[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu32arrayproperty__string-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu32arrayproperty__string-uint_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an array of unsigned 32-bit integers as the value of the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetU32ArrayProperty(string name, uint[] value)ParametersNameTypeDescriptionnamestringThe name of the property. P

### SetU32ArrayProperty(string, uint[])

Sets an array of unsigned 32-bit integers as the value of the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetU32ArrayProperty(string name, uint[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | uint[] | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu32property__string-uint.html language=enus -->
## TOPIC 02156: SetU32Property(string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu32property__string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu32property__string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an unsigned 32-bit integer value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetU32Property(string name, uint value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case-

### SetU32Property(string, uint)

Sets an unsigned 32-bit integer value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetU32Property(string name, uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | uint | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu64property__string-ulong.html language=enus -->
## TOPIC 02157: SetU64Property(string, ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu64property__string-ulong.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setu64property__string-ulong.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets an unsigned 64-bit integer value for the custom device item property specified by name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetU64Property(string name, ulong value)ParametersNameTypeDescriptionnamestringThe name of the property. Property names are case

### SetU64Property(string, ulong)

Sets an unsigned 64-bit integer value for the custom device item property specified by *name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetU64Property(string name, ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| value | ulong | The value of the property. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setvariantproperty__string-byte_arr1-byte_arr1.html language=enus -->
## TOPIC 02158: SetVariantProperty(string, byte[], byte[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setvariantproperty__string-byte_arr1-byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-setvariantproperty__string-byte_arr1-byte_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a LabVIEW variant value for the custom device item property specified by name . The variant data type is a generic container for all other LabVIEW data types. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetVariantProperty(string name, byte[] type, byte[] value)

### SetVariantProperty(string, byte[], byte[])

Sets a LabVIEW variant value for the custom device item property specified by *name* . The variant data type is a generic container for all other LabVIEW data types.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetVariantProperty(string name, byte[] type, byte[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. Property names are case-sensitive. |
| type | byte[] | The data type of value . |
| value | byte[] | The value of the property as a byte array. |

#### Returns

true if the property *name*  is found.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase-typeguid.html language=enus -->
## TOPIC 02159: TypeGUID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase-typeguid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase-typeguid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the GUID associated with an item in a custom device. You can use this property to get or set the GUID for any component of a custom device that lists a GUID in the Custom Device XML file, such as the configuration page for the item, menu items that appear at run-time, Action VIs associa

### TypeGUID

Gets or sets the GUID associated with an item in a custom device. You can use this property to get or set the GUID for any component of a custom device that lists a GUID in the Custom Device XML file, such as the configuration page for the item, menu items that appear at run-time, Action VIs associated with the item, and so on.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override string TypeGUID { get; set; }

#### Returns

The GUID.

Parent topic:

CustomDeviceBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicebase.html language=enus -->
## TOPIC 02160: CustomDeviceBase Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicebase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicebase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a base class for NI VeriStand custom devices. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CustomDeviceBase : BaseNodeRemarksUse the members of this class to interact with items in a custom device. For example, you can get and set item pr

### CustomDeviceBase Class

Defines a base class for NI VeriStand custom devices.

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CustomDeviceBase : BaseNode

#### Remarks

Use the members of this class to interact with items in a custom device. For example, you can get and set item property values, move an item to a different location in the custom device hierarchy, associate GUIDs with items, and configure error reporting within the custom device.

**Accessing this Class**

- [IDToCustomDeviceBase](nationalinstruments-veristand-systemdefinitionapi-nodeidutil-idtocustomdevicebase__ulong.html)

Note

You also can access members of this class from any class that defines a custom device or custom device component.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| TypeGUID | Gets or sets the GUID associated with an item in a custom device. You can use this property to get or set the GUID for any component of a custom device that lists a GUID in the Custom Device XML file, such as the configuration page for the item, menu items that appear at run-time, Action VIs associated with the item, and so on. |

#### Methods

| Name | Description |
| --- | --- |
| GetBinaryStringProperty(string, out byte[]) | Gets the binary string value of the custom device item property specified by name . |
| GetBooleanProperty(string, out bool) | Gets the Boolean value of the custom device item property specified by name . |
| GetDependentFileProperty(string, out DependentFile) | Gets the reference to the dependent file that is the value of the custom device item property specified by name . |
| GetDependentNodeProperty(string, out BaseNode) | Gets the reference to the dependent node that is the value of the custom device item property specified by name . |
| GetDependentNodeProperty(string, out string) | Gets the path to the dependent node, as specified in the system definition file, that is the value of the custom device item property specified by name . |
| GetDictionaryArrayProperty(string, out Dictionary[]) | Gets the reference to the Dictionary array that is the value of the custom device item property specified by name . |
| GetDictionaryProperty(string, out Dictionary) | Gets the reference to the Dictionary that is the value of the custom device item property specified by name . |
| GetDoubleArrayProperty(string, out double[]) | Gets the array of double-precision floating point numbers that is the value of the custom device item property specified by name . |
| GetDoubleProperty(string, out double) | Gets the double-precision floating point value of the custom device item property specified by name . |
| GetI32ArrayProperty(string, out int[]) | Gets the array of 32-bit signed integers that is the value of the custom device item property specified by name . |
| GetI32Property(string, out int) | Gets the 32-bit signed integer that is the value of the custom device item property specified by name . |
| GetPropertyNames() | Gets the names of all the properties associated with a custom device item. Custom device item properties store and communicate state information. |
| GetPropertyType(string, out PropertyContent) | Gets the data type of the custom device item property specified by propertyName . |
| GetStringArrayProperty(string, out string[]) | Gets the array of strings that is the value of the custom device item property specified by name . |
| GetStringProperty(string, out string) | Gets the string value of the custom device item property specified by name . |
| GetU16Property(string, out ushort) | Gets the unsigned 16-bit integer value of the custom device item property specified by name . |
| GetU32ArrayProperty(string, out uint[]) | Gets the array of unsigned 32-bit integers that is the value of the custom device item property specified by name . |
| GetU32Property(string, out uint) | Gets the unsigned 32-bit integer value of the custom device item property specified by name . |
| GetU64Property(string, out ulong) | Gets the unsigned 64-bit integer value of the custom device item property specified by name . |
| GetVariantProperty(string, out byte[], out byte[]) | Gets the LabVIEW variant value of the custom device item property specified by name . The variant data type is a generic container for all other LabVIEW data types. |
| MoveNodeTo(CustomDeviceBase) | Moves a custom device item to a new location within the custom device hierarchy. |
| MoveNodeTo(CustomDeviceBase, out Error) | Moves a custom device item to a new location within the custom device hierarchy. |
| RemoveError(string) | Removes an error that matches the specified ErrorID . |
| RemoveProperty(string) | Removes the custom device item property specified by name . |
| RemoveProperty(string, out Error) | Removes the custom device item property specified by name . |
| RenameNode(string, bool) | Renames this node to the name you specify, if the name that you specify is not already in use by a sibling of this node. |
| ReportError(string, bool, int, string) | Configures whether to report an error that occurs during custom device execution. |
| SetBinaryStringProperty(string, byte[]) | Sets a binary string value for the custom device item property specified by name . |
| SetBooleanProperty(string, bool) | Sets a Boolean value for the custom device item property specified by name . |
| SetDependentFileProperty(string, DependentFile) | Sets a reference to a dependent file as the value for the custom device item property specified by name . |
| SetDependentNodeProperty(string, string) | Sets a path to a dependent node, as specified in the system definition file, as the value of the custom device item property specified by name . |
| SetDependentNodeProperty(string, BaseNode) | Sets a reference to a dependent node as the value of the custom device item property specified by name . |
| SetDictionaryArrayProperty(string, Dictionary[]) | Sets a reference to a Dictionary as the value of the custom device item property specified by name . |
| SetDictionaryProperty(string, Dictionary) | Sets a reference to a Dictionary element as the value of the custom device item property specified by name . |
| SetDoubleArrayProperty(string, double[]) | Sets an array of double-precision floating point numbers as the value of the custom device item property specified by name . |
| SetDoubleProperty(string, double) | Sets a double-precision floating point value for the custom device item property specified by name . |
| SetI32ArrayProperty(string, int[]) | Sets an array of 32-bit signed integers as the value of the custom device item property specified by name . |
| SetI32Property(string, int) | Sets a 32-bit signed integer value for the custom device item property specified by name . |
| SetLogFileProducerFlag(bool) | Sets a flag indicating whether this node is a log file producer. |
| SetStringArrayProperty(string, string[]) | Sets an array of strings as the value of the custom device item property specified by name . |
| SetStringProperty(string, string) | Sets a string value for the custom device item property specified by name . |
| SetU16Property(string, ushort) | Sets an unsigned 16-bit integer value for the custom device item property specified by name . |
| SetU32ArrayProperty(string, uint[]) | Sets an array of unsigned 32-bit integers as the value of the custom device item property specified by name . |
| SetU32Property(string, uint) | Sets an unsigned 32-bit integer value for the custom device item property specified by name . |
| SetU64Property(string, ulong) | Sets an unsigned 64-bit integer value for the custom device item property specified by name . |
| SetVariantProperty(string, byte[], byte[]) | Sets a LabVIEW variant value for the custom device item property specified by name . The variant data type is a generic container for all other LabVIEW data types. |
| ExportCommonPropertiesToJson(JObject) | Export properties to the specified Json object. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-bitfields.html language=enus -->
## TOPIC 02161: BitFields

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-bitfields.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-bitfields.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For internal use only. Stores various channel settings, such as its type, default value, whether it is faultable or scalable, and so on. Use the DefaultValue, Faultable, Scalable, and Type properties to get the information the bit field contains. SyntaxNamespace: NationalInstruments.VeriStand.System

### BitFields

For internal use only. Stores various channel settings, such as its type, default value, whether it is faultable or scalable, and so on. Use the [DefaultValue](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-defaultvalue.html), [Faultable](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-faultable.html), [Scalable](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scalable.html), and [Type](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-type.html) properties to get the information the bit field contains.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint BitFields { get; }

#### Returns

The unsigned 32-bit integer that represents the channel's bit field.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-columndimensions.html language=enus -->
## TOPIC 02162: ColumnDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-columndimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-columndimensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For internal use only. Gets the column dimensions of the custom device channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ColumnDimensions { get; }ReturnsCustom devices only support scalar channels. The value of this property is always 1.

### ColumnDimensions

For internal use only. Gets the column dimensions of the custom device channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ColumnDimensions { get; }

#### Returns

Custom devices only support scalar channels. The value of this property is always 1.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-customdevicechannel__string-string.html language=enus -->
## TOPIC 02163: CustomDeviceChannel(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-customdevicechannel__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-customdevicechannel__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CustomDeviceChannel class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceChannel(string Name, string GUID)ParametersNameTypeDescriptionNamestringThe name associated with the channel, as specified in the Custom Device XML file.

### CustomDeviceChannel(string, string)

Initializes a new instance of the [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CustomDeviceChannel(string Name, string GUID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name associated with the channel, as specified in the Custom Device XML file. |
| GUID | string | The GUID associated with the channel, as specified in the Custom Device XML file. |

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-datasource.html language=enus -->
## TOPIC 02164: DataSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-datasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-datasource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the source channel that maps to the current channel and provides it data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode DataSource { get; set; }ReturnsA BaseNode reference to the source channel.

### DataSource

Gets or sets the source channel that maps to the current channel and provides it data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) DataSource { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the source channel.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-defaultvalue.html language=enus -->
## TOPIC 02165: DefaultValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-defaultvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default value for a custom device channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double DefaultValue { get; set; }ReturnsThe 64-bit double precision floating point number that represents the default value of the channel.

### DefaultValue

Gets or sets the default value for a custom device channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double DefaultValue { get; set; }

#### Returns

The 64-bit double precision floating point number that represents the default value of the channel.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-exportcommonpropertiestojson__jobject.html language=enus -->
## TOPIC 02166: ExportCommonPropertiesToJson(JObject)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-exportcommonpropertiestojson__jobject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-exportcommonpropertiestojson__jobject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Export properties to the specified Json object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected override void ExportCommonPropertiesToJson(JObject propertiesContainer)ParametersNameTypeDescriptionpropertiesContainerJObjectThe Json object to which properties will be export

### ExportCommonPropertiesToJson(JObject)

Export properties to the specified Json object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected override void ExportCommonPropertiesToJson(JObject propertiesContainer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertiesContainer | JObject | The Json object to which properties will be exported. |

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-faultable.html language=enus -->
## TOPIC 02167: Faultable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-faultable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-faultable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Faultable { get; set; }Returnstrue if the channel is faultable.

### Faultable

Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Faultable { get; set; }

#### Returns

true if the channel is faultable.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-getvaluetable__out-out.html language=enus -->
## TOPIC 02168: GetValueTable(out string[], out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-getvaluetable__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-getvaluetable__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value table for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetValueTable(out string[] names, out double[] values)ParametersNameTypeDescriptionnamesout string[]The names for the channel value table.valuesout double[]The values for the channel v

### GetValueTable(out string[], out double[])

Gets the value table for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetValueTable(out string[] names, out double[] values)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | out string[] | The names for the channel value table. |
| values | out double[] | The values for the channel value table. |

#### Returns

Returns true if the channel value table is defined.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-groupname.html language=enus -->
## TOPIC 02169: GroupName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-groupname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-groupname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the group name for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected string GroupName { get; set; }RemarksA string that indicates the group name associated with the custom device channel.

### GroupName

Gets or sets the group name for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected string GroupName { get; set; }

#### Remarks

A string that indicates the group name associated with the custom device channel.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-importcommonpropertiesfromjson__jobject.html language=enus -->
## TOPIC 02170: ImportCommonPropertiesFromJson(JObject)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-importcommonpropertiesfromjson__jobject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-importcommonpropertiesfromjson__jobject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Import properties from the specified JSON object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected void ImportCommonPropertiesFromJson(JObject propertiesContainer)ParametersNameTypeDescriptionpropertiesContainerJObjectThe Json object from which properties will be imported.

### ImportCommonPropertiesFromJson(JObject)

Import properties from the specified JSON object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected void ImportCommonPropertiesFromJson(JObject propertiesContainer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertiesContainer | JObject | The Json object from which properties will be imported. |

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-isreadable.html language=enus -->
## TOPIC 02171: IsReadable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-isreadable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-isreadable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the channel is readable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsReadable { get; }

### IsReadable

Gets a value indicating whether the channel is readable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsReadable { get; }

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-iswritable.html language=enus -->
## TOPIC 02172: IsWritable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-iswritable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-iswritable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the channel is writable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsWritable { get; }

### IsWritable

Gets a value indicating whether the channel is writable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsWritable { get; }

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-removedatasource.html language=enus -->
## TOPIC 02173: RemoveDataSource()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-removedatasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-removedatasource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the source channel that maps to the current channel and provides it data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveDataSource()

### RemoveDataSource()

Removes the source channel that maps to the current channel and provides it data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveDataSource()

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-rowdimensions.html language=enus -->
## TOPIC 02174: RowDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-rowdimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-rowdimensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: For internal use only. Gets the row dimensions of the custom device channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int RowDimensions { get; }ReturnsCustom devices only support scalar channels. The value of this property is always 1.

### RowDimensions

For internal use only. Gets the row dimensions of the custom device channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int RowDimensions { get; }

#### Returns

Custom devices only support scalar channels. The value of this property is always 1.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scalable.html language=enus -->
## TOPIC 02175: Scalable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scalable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scalable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Scalable { get; set; }Returnstrue if the channel is scalable.

### Scalable

Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Scalable { get; set; }

#### Returns

true if the channel is scalable.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scale.html language=enus -->
## TOPIC 02176: Scale

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scale.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scale.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the value of the scale property on the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale Scale { get; set; }

### Scale

Gets or sets the value of the scale property on the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) Scale { get; set; }

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scaleunits.html language=enus -->
## TOPIC 02177: ScaleUnits

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scaleunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-scaleunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units of the scale associated with the custom device channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ScaleUnits { get; }RemarksThe units of the scale can be any arbitrary string. If there is no scale, this property returns the units of the custom dev

### ScaleUnits

Gets the units of the scale associated with the custom device channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ScaleUnits { get; }

#### Remarks

The units of the scale can be any arbitrary string. If there is no scale, this property returns the units of the custom device channel.

#### Returns

Returns a string that indicates the units associated with the custom device channel.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-setvaluetable__string_arr1-double_arr1.html language=enus -->
## TOPIC 02178: SetValueTable(string[], double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-setvaluetable__string_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-setvaluetable__string_arr1-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value table for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetValueTable(string[] names, double[] values)ParametersNameTypeDescriptionnamesstring[]The names for the channel value table.valuesdouble[]The values for the channel value table.

### SetValueTable(string[], double[])

Sets the value table for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetValueTable(string[] names, double[] values)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | string[] | The names for the channel value table. |
| values | double[] | The values for the channel value table. |

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-type.html language=enus -->
## TOPIC 02179: Type

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CDChannel_Type Type { get; set; }ReturnsAn enumeration value of CDChannel_Type.

### Type

Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CDChannel_Type](nationalinstruments-veristand-systemdefinitionapi-cdchannel_type.html) Type { get; set; }

#### Returns

An enumeration value of [CDChannel_Type](nationalinstruments-veristand-systemdefinitionapi-cdchannel_type.html).

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-units.html language=enus -->
## TOPIC 02180: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the units associated with a custom device channel. Units can be any string that makes sense for your custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Units { get; set; }ReturnsThe units associated with the channel.

### Units

Gets or sets the units associated with a custom device channel. Units can be any string that makes sense for your custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Units { get; set; }

#### Returns

The units associated with the channel.

Parent topic:

CustomDeviceChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html language=enus -->
## TOPIC 02181: CustomDeviceChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a channel in a custom device. Derives fromIChannelCustomDeviceBaseSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CustomDeviceChannel : IChannel, CustomDeviceBaseRemarksUse the members of this class to get and set properties of the channel, such as its defau

### CustomDeviceChannel Class

Represents a channel in a custom device.

#### Derives from

- IChannel
- CustomDeviceBase

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CustomDeviceChannel : IChannel, CustomDeviceBase

#### Remarks

Use the members of this class to get and set properties of the channel, such as its default value and whether it is faultable and scalable.

**Accessing this Class**

- [AddCustomDeviceChannelIfNotFound](nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicechannelifnotfound__string-string-out.html)
- [AddErrorChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicesection-adderrorchannel__string.html)
- [AddInputOverflowCountChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addinputoverflowcountchannel__string.html)
- [AddOutputUnderflowCountChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addoutputunderflowcountchannel__string.html)
- [IDToCustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-nodeidutil-idtocustomdevicechannel__ulong.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CustomDeviceChannel(string, string) | Initializes a new instance of the CustomDeviceChannel class. |

#### Properties

| Name | Description |
| --- | --- |
| BitFields | For internal use only. Stores various channel settings, such as its type, default value, whether it is faultable or scalable, and so on. Use the DefaultValue, Faultable, Scalable, and Type properties to get the information the bit field contains. |
| ColumnDimensions | For internal use only. Gets the column dimensions of the custom device channel. |
| DataSource | Gets or sets the source channel that maps to the current channel and provides it data. |
| DefaultValue | Gets or sets the default value for a custom device channel. |
| Faultable | Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion. |
| GroupName | Gets or sets the group name for the channel. |
| IsReadable | Gets a value indicating whether the channel is readable. |
| IsWritable | Gets a value indicating whether the channel is writable. |
| RowDimensions | For internal use only. Gets the row dimensions of the custom device channel. |
| Scalable | Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units. |
| Scale | Gets or sets the value of the scale property on the channel. |
| ScaleUnits | Gets the units of the scale associated with the custom device channel. |
| Type | Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable. |
| Units | Gets or sets the units associated with a custom device channel. Units can be any string that makes sense for your custom device. |

#### Methods

| Name | Description |
| --- | --- |
| GetValueTable(out string[], out double[]) | Gets the value table for the channel. |
| RemoveDataSource() | Removes the source channel that maps to the current channel and provides it data. |
| SetValueTable(string[], double[]) | Sets the value table for the channel. |
| ExportCommonPropertiesToJson(JObject) | Export properties to the specified Json object. |
| ImportCommonPropertiesFromJson(JObject) | Import properties from the specified JSON object. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevices-addcustomdevice__customdevice-out.html language=enus -->
## TOPIC 02182: AddCustomDevice(CustomDevice, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevices-addcustomdevice__customdevice-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevices-addcustomdevice__customdevice-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified CustomDevice to the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCustomDevice(CustomDevice customDevice, out Error error)RemarksThis method only adds the CustomDevice to a system definition. This method does not add sections o

### AddCustomDevice(CustomDevice, out Error)

Adds the specified [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) to the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCustomDevice(CustomDevice customDevice, out Error error)

#### Remarks

This method only adds the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) to a system definition. This method does not add sections or channels that belong to the custom device *or* set properties of the custom device. Even for pre-built custom devices included with NI VeriStand, such as the Embedded Data Logger, you must use members of the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) class to add a [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) or a [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) and to set properties of the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) separately from adding the custom device to the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| customDevice | CustomDevice | The custom device to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) was added successfully.

Parent topic:

CustomDevices Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevices-addcustomdevice__customdevice.html language=enus -->
## TOPIC 02183: AddCustomDevice(CustomDevice)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevices-addcustomdevice__customdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevices-addcustomdevice__customdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified CustomDevice to the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCustomDevice(CustomDevice customDevice)RemarksThis method only adds the CustomDevice to a system definition. This method does not add sections or channels that b

### AddCustomDevice(CustomDevice)

Adds the specified [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) to the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCustomDevice(CustomDevice customDevice)

#### Remarks

This method only adds the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) to a system definition. This method does not add sections or channels that belong to the custom device *or* set properties of the custom device. Even for pre-built custom devices included with NI VeriStand, such as the Embedded Data Logger, you must use members of the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) class to add a [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) or a [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) and to set properties of the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) separately from adding the custom device to the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| customDevice | CustomDevice | The custom device to add. |

#### Returns

true if the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) was added successfully.

Parent topic:

CustomDevices Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevices-getcustomdevicelist.html language=enus -->
## TOPIC 02184: GetCustomDeviceList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevices-getcustomdevicelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevices-getcustomdevicelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CustomDevice elements from the CustomDevices section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDevice[] GetCustomDeviceList()RemarksModifications you make to the contents of this list apply to the system definition. However, modif

### GetCustomDeviceList()

Gets an array that contains the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) elements from the [CustomDevices](nationalinstruments-veristand-systemdefinitionapi-customdevices.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html)[] GetCustomDeviceList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) elements from the [CustomDevices](nationalinstruments-veristand-systemdefinitionapi-customdevices.html) section.

Parent topic:

CustomDevices Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevices.html language=enus -->
## TOPIC 02185: CustomDevices Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevices.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevices.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the top-level Custom Devices section of a Target. This section contains all the custom devices (except timing and sync devices) that you add to the system definition. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CustomDevices : SectionR

### CustomDevices Class

Represents the top-level **Custom Devices** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html). This section contains all the custom devices (except timing and sync devices) that you add to the system definition.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CustomDevices : Section

#### Remarks

Use the members of this class to add a custom device or to get a list of all the custom devices that currently exist in the system definition.

**Accessing this Class**

- [GetCustomDevices](nationalinstruments-veristand-systemdefinitionapi-target-getcustomdevices.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddCustomDevice(CustomDevice, out Error) | Adds the specified CustomDevice to the system definition. |
| AddCustomDevice(CustomDevice) | Adds the specified CustomDevice to the system definition. |
| GetCustomDeviceList() | Gets an array that contains the CustomDevice elements from the CustomDevices section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicechannelifnotfound__string-string-out.html language=enus -->
## TOPIC 02186: AddCustomDeviceChannelIfNotFound(string, string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicechannelifnotfound__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicechannelifnotfound__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a custom device channel with the name and guid you specify to the current section, if the channel does not already exist under the section. If the channel you specify already exists, this method takes no action and returns a reference to the existing channel. SyntaxNamespace: NationalInstrument

### AddCustomDeviceChannelIfNotFound(string, string, out bool)

Adds a custom device channel with the *name*  and *guid*  you specify to the current section, if the channel does not already exist under the section. If the channel you specify already exists, this method takes no action and returns a reference to the existing channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) AddCustomDeviceChannelIfNotFound(string name, string guid, out bool newItem)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name associated with the channel, as specified in the Custom Device XML file. |
| guid | string | The GUID associated with the channel, as specified in the Custom Device XML file. |
| newItem | out bool | Returns true if the channel was added. |

#### Returns

The [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) reference for the channel specified by *name*  and *guid* .

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicesectionifnotfound__string-string-out.html language=enus -->
## TOPIC 02187: AddCustomDeviceSectionIfNotFound(string, string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicesectionifnotfound__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicesectionifnotfound__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a custom device subsection with the name and guid you specify to the current section, if the subsection does not already exist under the section. If the subsection does exist, this method does nothing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceSection

### AddCustomDeviceSectionIfNotFound(string, string, out bool)

Adds a custom device subsection with the *name*  and *guid*  you specify to the current section, if the subsection does not already exist under the section. If the subsection does exist, this method does nothing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) AddCustomDeviceSectionIfNotFound(string name, string guid, out bool newItem)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name associated with the section, as specified in the Custom Device XML file. |
| guid | string | The GUID associated with the section, as specified in the Custom Device XML file. |
| newItem | out bool | Returns true if the section was added. |

#### Returns

The [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) reference for the added section.

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicewaveformifnotfound__string-string-waveformtypedatatype-out.html language=enus -->
## TOPIC 02188: AddCustomDeviceWaveformIfNotFound(string, string, WaveformTypeDataType, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicewaveformifnotfound__string-string-waveformtypedatatype-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicewaveformifnotfound__string-string-waveformtypedatatype-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a CustomDeviceWaveform with the name , dataType and guid you specify to the current section, if the CustomDeviceWaveform does not already exist under the section. If the CustomDeviceWaveform you specify already exists, this method takes no action and returns a reference to the existing CustomDe

### AddCustomDeviceWaveformIfNotFound(string, string, WaveformTypeDataType, out bool)

Adds a CustomDeviceWaveform with the *name* , *dataType*  and *guid*  you specify to the current section, if the CustomDeviceWaveform does not already exist under the section. If the CustomDeviceWaveform you specify already exists, this method takes no action and returns a reference to the existing CustomDeviceWaveform.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) AddCustomDeviceWaveformIfNotFound(string name, string guid, WaveformTypeDataType dataType, out bool newItem)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name associated with the CustomDeviceWaveform, as specified in the Custom Device XML file. |
| guid | string | The GUID associated with the CustomDeviceWaveform, as specified in the Custom Device XML file. |
| dataType | WaveformTypeDataType | The data type associated with the CustomDeviceWaveform which is an enumeration value of NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType. |
| newItem | out bool | Returns true if the CustomDeviceWaveform was added. |

#### Returns

The [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) reference for the waveform specified by *name* , *dataType*  and *guid* .

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-adderrorchannel__string.html language=enus -->
## TOPIC 02189: AddErrorChannel(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-adderrorchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-adderrorchannel__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an error channel to the custom device. An asynchronous custom device can send a fatal error status to the Primary Control Loop of the VeriStand Engine by writing a non-zero error code value to this channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceCha

### AddErrorChannel(string)

Adds an error channel to the custom device. An asynchronous custom device can send a fatal error status to the Primary Control Loop of the VeriStand Engine by writing a non-zero error code value to this channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) AddErrorChannel(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the error channel. This can be any string. If the name you specify already exists, this method takes no action and returns a reference to the existing channel. |

#### Returns

The [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) reference for the error channel.

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addinputoverflowcountchannel__string.html language=enus -->
## TOPIC 02190: AddInputOverflowCountChannel(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addinputoverflowcountchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addinputoverflowcountchannel__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an input overflow count channel to a section in an asynchronous custom device. Input overflow count channels track the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A custom device can have only one input overflow count channel. Syntax

### AddInputOverflowCountChannel(string)

Adds an input overflow count channel to a section in an asynchronous custom device. Input overflow count channels track the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A custom device can have only one input overflow count channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) AddInputOverflowCountChannel(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the input overflow count channel. This can be any string. If the name you specify already exists, this method takes no action and returns a reference to the existing channel. |

#### Returns

The [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) reference for the input overflow count channel.

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addoutputunderflowcountchannel__string.html language=enus -->
## TOPIC 02191: AddOutputUnderflowCountChannel(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addoutputunderflowcountchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addoutputunderflowcountchannel__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an output underflow count channel to a section in an asynchronous custom device. Output underflow count channels track the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A custom device can have only one output underflow count

### AddOutputUnderflowCountChannel(string)

Adds an output underflow count channel to a section in an asynchronous custom device. Output underflow count channels track the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A custom device can have only one output underflow count channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) AddOutputUnderflowCountChannel(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the output underflow count channel. This can be any string. If the name you specify already exists, this method takes no action and returns a reference to the existing channel. |

#### Returns

The [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) reference for the input overflow count channel.

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-customdevicesection__string-string.html language=enus -->
## TOPIC 02192: CustomDeviceSection(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-customdevicesection__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-customdevicesection__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CustomDeviceSection and creates a section with the Name and GUID you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceSection(string Name, string GUID)ParametersNameTypeDescriptionNamestringThe name associated with the sectio

### CustomDeviceSection(string, string)

Initializes a new instance of [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) and creates a section with the *Name*  and *GUID*  you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CustomDeviceSection(string Name, string GUID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name associated with the section, as specified in the Custom Device XML file. |
| GUID | string | The GUID associated with the section, as specified in the Custom Device XML file. |

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicechannels.html language=enus -->
## TOPIC 02193: GetCustomDeviceChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicechannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicechannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CustomDeviceChannel elements from the current CustomDeviceSection. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected IEnumerable< CustomDeviceChannel > GetCustomDeviceChannels()RemarksModifications you make to the items of this list apply to the system definition.

### GetCustomDeviceChannels()

Gets the [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) elements from the current [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected IEnumerable< [CustomDeviceChannel](nationalinstruments-veristand-systemdefinitionapi-customdevicechannel.html) > GetCustomDeviceChannels()

#### Remarks

Note

Modifications you make to the items of this list apply to the system definition.

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicesections.html language=enus -->
## TOPIC 02194: GetCustomDeviceSections()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicesections.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicesections.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CustomDeviceSection elements from the current CustomDeviceSection. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected IEnumerable< CustomDevic

### GetCustomDeviceSections()

Gets the [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) elements from the current [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html). Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected IEnumerable< [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) > GetCustomDeviceSections()

#### Remarks

Note

Modifications you make to the items of this list apply to the system definition.

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicewaveforms.html language=enus -->
## TOPIC 02195: GetCustomDeviceWaveforms()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicewaveforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection-getcustomdevicewaveforms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CustomDeviceWaveform elements from the current CustomDeviceSection. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected IEnumerable< CustomDeviceWaveform > GetCustomDeviceWaveforms()RemarksModification you make to the items of this list apply to the system definition

### GetCustomDeviceWaveforms()

Gets the [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) elements from the current [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected IEnumerable< [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) > GetCustomDeviceWaveforms()

#### Remarks

Note

Modification you make to the items of this list apply to the system definition.

Parent topic:

CustomDeviceSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html language=enus -->
## TOPIC 02196: CustomDeviceSection Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a section under a custom device. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy. Derives fromCustomDeviceBaseSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CustomDeviceSection : Cus

### CustomDeviceSection Class

Represents a section under a custom device. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy.

#### Derives from

- CustomDeviceBase

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CustomDeviceSection : CustomDeviceBase

#### Remarks

Use the members of this class to add channels or subsections to a section of a custom device.

**Accessing this Class**

- [GetCustomDeviceSectionList](nationalinstruments-veristand-systemdefinitionapi-customdevice-getcustomdevicesectionlist.html)
- CustomDeviceSection Constructor

AddCustomDeviceSectionIfNotFound

IDToCustomDeviceSection

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CustomDeviceSection(string, string) | Initializes a new instance of CustomDeviceSection and creates a section with the Name and GUID you specify. |

#### Methods

| Name | Description |
| --- | --- |
| GetCustomDeviceChannels() | Gets the CustomDeviceChannel elements from the current CustomDeviceSection. |
| GetCustomDeviceSections() | Gets the CustomDeviceSection elements from the current CustomDeviceSection. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy. |
| GetCustomDeviceWaveforms() | Gets the CustomDeviceWaveform elements from the current CustomDeviceSection. |
| AddCustomDeviceChannelIfNotFound(string, string, out bool) | Adds a custom device channel with the name and guid you specify to the current section, if the channel does not already exist under the section. If the channel you specify already exists, this method takes no action and returns a reference to the existing channel. |
| AddCustomDeviceSectionIfNotFound(string, string, out bool) | Adds a custom device subsection with the name and guid you specify to the current section, if the subsection does not already exist under the section. If the subsection does exist, this method does nothing. |
| AddCustomDeviceWaveformIfNotFound(string, string, WaveformTypeDataType, out bool) | Adds a CustomDeviceWaveform with the name , dataType and guid you specify to the current section, if the CustomDeviceWaveform does not already exist under the section. If the CustomDeviceWaveform you specify already exists, this method takes no action and returns a reference to the existing CustomDeviceWaveform. |
| AddErrorChannel(string) | Adds an error channel to the custom device. An asynchronous custom device can send a fatal error status to the Primary Control Loop of the VeriStand Engine by writing a non-zero error code value to this channel. |
| AddInputOverflowCountChannel(string) | Adds an input overflow count channel to a section in an asynchronous custom device. Input overflow count channels track the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A custom device can have only one input overflow count channel. |
| AddOutputUnderflowCountChannel(string) | Adds an output underflow count channel to a section in an asynchronous custom device. Output underflow count channels track the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A custom device can have only one output underflow count channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-customdevicewaveform__string-string-waveformtypedatatype.html language=enus -->
## TOPIC 02197: CustomDeviceWaveform(string, string, WaveformTypeDataType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-customdevicewaveform__string-string-waveformtypedatatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-customdevicewaveform__string-string-waveformtypedatatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CustomDeviceWaveform class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceWaveform(string name, string guid, WaveformTypeDataType dataType)ParametersNameTypeDescriptionnamestringThe name of CustomDeviceWaveform, as specified in

### CustomDeviceWaveform(string, string, WaveformTypeDataType)

Initializes a new instance of the [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CustomDeviceWaveform(string name, string guid, WaveformTypeDataType dataType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of CustomDeviceWaveform, as specified in the Custom Device XML file. |
| guid | string | The GUID of CustomDeviceWaveform, as specified in the Custom Device XML file. |
| dataType | WaveformTypeDataType | The data type of CustomDeviceWaveform, which is an enumeration value of NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType |

Parent topic:

CustomDeviceWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-datatype.html language=enus -->
## TOPIC 02198: DataType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-datatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-datatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the data type associated with the CustomDeviceWaveform class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic WaveformTypeDataType DataType { get; set; }ReturnsThe data type of CustomDeviceWaveform, which is an enumeration value of NationalInstruments.VeriStand.

### DataType

Gets or sets the data type associated with the [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public WaveformTypeDataType DataType { get; set; }

#### Returns

The data type of [CustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html), which is an enumeration value of NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType.

Parent topic:

CustomDeviceWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-exportcommonpropertiestojson__jobject.html language=enus -->
## TOPIC 02199: ExportCommonPropertiesToJson(JObject)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-exportcommonpropertiestojson__jobject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-exportcommonpropertiestojson__jobject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Export properties to the specified Json object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected override void ExportCommonPropertiesToJson(JObject propertiesContainer)ParametersNameTypeDescriptionpropertiesContainerJObjectThe Json object to which properties will be export

### ExportCommonPropertiesToJson(JObject)

Export properties to the specified Json object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected override void ExportCommonPropertiesToJson(JObject propertiesContainer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertiesContainer | JObject | The Json object to which properties will be exported. |

Parent topic:

CustomDeviceWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-importcommonpropertiesfromjson__jobject.html language=enus -->
## TOPIC 02200: ImportCommonPropertiesFromJson(JObject)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-importcommonpropertiesfromjson__jobject.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-importcommonpropertiesfromjson__jobject.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Import properties from the specified JSON object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected void ImportCommonPropertiesFromJson(JObject propertiesContainer)ParametersNameTypeDescriptionpropertiesContainerJObjectThe Json object from which properties will be imported.

### ImportCommonPropertiesFromJson(JObject)

Import properties from the specified JSON object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected void ImportCommonPropertiesFromJson(JObject propertiesContainer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertiesContainer | JObject | The Json object from which properties will be imported. |

Parent topic:

CustomDeviceWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-units.html language=enus -->
## TOPIC 02201: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Units { get; set; }ReturnsThe units associated with the CustomDeviceWaveform.

### Units

Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Units { get; set; }

#### Returns

The units associated with the CustomDeviceWaveform.

Parent topic:

CustomDeviceWaveform Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html language=enus -->
## TOPIC 02202: CustomDeviceWaveform Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-customdevicewaveform.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a waveform in a custom device. Derives fromCustomDeviceBaseSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CustomDeviceWaveform : CustomDeviceBaseRemarksUse the members of this class to get and set the properties of CustomDeviceWaveform. You can use the foll

### CustomDeviceWaveform Class

Represents a waveform in a custom device.

#### Derives from

- CustomDeviceBase

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CustomDeviceWaveform : CustomDeviceBase

#### Remarks

Use the members of this class to get and set the properties of CustomDeviceWaveform.

You can use the following methods to access this class:

- [AddCustomDeviceWaveformIfNotFound](nationalinstruments-veristand-systemdefinitionapi-customdevicesection-addcustomdevicewaveformifnotfound__string-string-waveformtypedatatype-out.html)
- [IDToCustomDeviceWaveform](nationalinstruments-veristand-systemdefinitionapi-nodeidutil-idtocustomdevicewaveform__ulong.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CustomDeviceWaveform(string, string, WaveformTypeDataType) | Initializes a new instance of the CustomDeviceWaveform class. |

#### Properties

| Name | Description |
| --- | --- |
| DataType | Gets or sets the data type associated with the CustomDeviceWaveform class. |
| Units | Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device. |

#### Methods

| Name | Description |
| --- | --- |
| ExportCommonPropertiesToJson(JObject) | Export properties to the specified Json object. |
| ImportCommonPropertiesFromJson(JObject) | Import properties from the specified JSON object. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclic-addrawdatabasedframe__rawdatabasedframe-out.html language=enus -->
## TOPIC 02203: AddRawDataBasedFrame(RawDataBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclic-addrawdatabasedframe__rawdatabasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclic-addrawdatabasedframe__rawdatabasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified RawDataBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)ParametersNameTypeDescriptionrawDataBasedFrameRawDataB

### AddRawDataBasedFrame(RawDataBasedFrame, out Error)

Adds the specified [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) as an outgoing cyclic frame under a CAN or FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The RawDataBasedFrame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) was added successfully.

Parent topic:

Cyclic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclic-addrawdatabasedframe__rawdatabasedframe.html language=enus -->
## TOPIC 02204: AddRawDataBasedFrame(RawDataBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclic-addrawdatabasedframe__rawdatabasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclic-addrawdatabasedframe__rawdatabasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified RawDataBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe RawD

### AddRawDataBasedFrame(RawDataBasedFrame)

Adds the specified [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) as an outgoing cyclic frame under a CAN or FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The RawDataBasedFrame to add. |

#### Returns

true if the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) was added successfully.

Parent topic:

Cyclic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclic-addsignalbasedframe__signalbasedframe-out.html language=enus -->
## TOPIC 02205: AddSignalBasedFrame(SignalBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclic-addsignalbasedframe__signalbasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclic-addsignalbasedframe__signalbasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SignalBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)ParametersNameTypeDescriptionsignalBasedFrameSignalBasedFr

### AddSignalBasedFrame(SignalBasedFrame, out Error)

Adds the specified [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) as an outgoing cyclic frame under a CAN or FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The SignalBasedFrame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) was added successfully.

Parent topic:

Cyclic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclic-addsignalbasedframe__signalbasedframe.html language=enus -->
## TOPIC 02206: AddSignalBasedFrame(SignalBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclic-addsignalbasedframe__signalbasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclic-addsignalbasedframe__signalbasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SignalBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)ParametersNameTypeDescriptionsignalBasedFrameSignalBasedFrameThe SignalBase

### AddSignalBasedFrame(SignalBasedFrame)

Adds the specified [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) as an outgoing cyclic frame under a CAN or FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The SignalBasedFrame to add. |

#### Returns

true if the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) was added successfully.

Parent topic:

Cyclic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclic-getrawdatabasedframelist.html language=enus -->
## TOPIC 02207: GetRawDataBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclic-getrawdatabasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclic-getrawdatabasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the RawDataBasedFrame elements from the current Cyclic section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RawDataBasedFrame[] GetRawDataBasedFrameList()RemarksModifications you make to the contents of this list apply to the system definition

### GetRawDataBasedFrameList()

Gets an array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [Cyclic](nationalinstruments-veristand-systemdefinitionapi-cyclic.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html)[] GetRawDataBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [Cyclic](nationalinstruments-veristand-systemdefinitionapi-cyclic.html) section.

Parent topic:

Cyclic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclic-getsignalbasedframelist.html language=enus -->
## TOPIC 02208: GetSignalBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclic-getsignalbasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclic-getsignalbasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SignalBasedFrame elements from the current Cyclic section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedFrame[] GetSignalBasedFrameList()RemarksModifications you make to the contents of this list apply to the system definition. H

### GetSignalBasedFrameList()

Gets an array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [Cyclic](nationalinstruments-veristand-systemdefinitionapi-cyclic.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html)[] GetSignalBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [Cyclic](nationalinstruments-veristand-systemdefinitionapi-cyclic.html) section.

Parent topic:

Cyclic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclic.html language=enus -->
## TOPIC 02209: Cyclic Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclic.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclic.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Cyclic section that contains outgoing cyclic frames under an NI-XNET CAN or FlexRay port. Use cyclic frames when you want data changes to arrive at other ECUs within a well-defined deadline. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic cl

### Cyclic Class

Represents the **Cyclic** section that contains outgoing cyclic frames under an NI-XNET CAN or FlexRay port. Use cyclic frames when you want data changes to arrive at other ECUs within a well-defined deadline.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Cyclic : Section

#### Remarks

Use the members of this class to add or access cyclic frames under the port.

**Accessing this Class**

- [GetCyclic](nationalinstruments-veristand-systemdefinitionapi-outgoing-getcyclic.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddRawDataBasedFrame(RawDataBasedFrame) | Adds the specified RawDataBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. |
| AddRawDataBasedFrame(RawDataBasedFrame, out Error) | Adds the specified RawDataBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. |
| AddSignalBasedFrame(SignalBasedFrame, out Error) | Adds the specified SignalBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. |
| AddSignalBasedFrame(SignalBasedFrame) | Adds the specified SignalBasedFrame as an outgoing cyclic frame under a CAN or FlexRay port. |
| GetRawDataBasedFrameList() | Gets an array that contains the RawDataBasedFrame elements from the current Cyclic section. |
| GetSignalBasedFrameList() | Gets an array that contains the SignalBasedFrame elements from the current Cyclic section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addrawdatabasedframe__rawdatabasedframe-out.html language=enus -->
## TOPIC 02210: AddRawDataBasedFrame(RawDataBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addrawdatabasedframe__rawdatabasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addrawdatabasedframe__rawdatabasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified RawDataBasedFrame as an outgoing cyclic/event frame under a CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedF

### AddRawDataBasedFrame(RawDataBasedFrame, out Error)

Adds the specified [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) as an outgoing cyclic/event frame under a CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The RawDataBasedFrame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) was added successfully.

Parent topic:

CyclicEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addrawdatabasedframe__rawdatabasedframe.html language=enus -->
## TOPIC 02211: AddRawDataBasedFrame(RawDataBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addrawdatabasedframe__rawdatabasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addrawdatabasedframe__rawdatabasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified RawDataBasedFrame as an outgoing cyclic/event frame under a CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe RawDataBa

### AddRawDataBasedFrame(RawDataBasedFrame)

Adds the specified [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) as an outgoing cyclic/event frame under a CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The RawDataBasedFrame to add. |

#### Returns

true if the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) was added successfully.

Parent topic:

CyclicEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addsignalbasedframe__signalbasedframe-out.html language=enus -->
## TOPIC 02212: AddSignalBasedFrame(SignalBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addsignalbasedframe__signalbasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addsignalbasedframe__signalbasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SignalBasedFrame as an outgoing cyclic/event frame under a CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)ParametersNameTypeDescriptionsignalBasedFrameSignalBasedFrameTh

### AddSignalBasedFrame(SignalBasedFrame, out Error)

Adds the specified [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) as an outgoing cyclic/event frame under a CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The SignalBasedFrame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) was added successfully.

Parent topic:

CyclicEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addsignalbasedframe__signalbasedframe.html language=enus -->
## TOPIC 02213: AddSignalBasedFrame(SignalBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addsignalbasedframe__signalbasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclicevent-addsignalbasedframe__signalbasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SignalBasedFrame as an outgoing cyclic/event frame under a CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)ParametersNameTypeDescriptionsignalBasedFrameSignalBasedFrameThe SignalBasedFram

### AddSignalBasedFrame(SignalBasedFrame)

Adds the specified [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) as an outgoing cyclic/event frame under a CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The SignalBasedFrame to add. |

#### Returns

true if the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) was added successfully.

Parent topic:

CyclicEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclicevent-getrawdatabasedframelist.html language=enus -->
## TOPIC 02214: GetRawDataBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclicevent-getrawdatabasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclicevent-getrawdatabasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the RawDataBasedFrame elements from the current CyclicEvent section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RawDataBasedFrame[] GetRawDataBasedFrameList()RemarksModifications you make to the contents of this list apply to the system defin

### GetRawDataBasedFrameList()

Gets an array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [CyclicEvent](nationalinstruments-veristand-systemdefinitionapi-cyclicevent.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html)[] GetRawDataBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [CyclicEvent](nationalinstruments-veristand-systemdefinitionapi-cyclicevent.html) section.

Parent topic:

CyclicEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclicevent-getsignalbasedframelist.html language=enus -->
## TOPIC 02215: GetSignalBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclicevent-getsignalbasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclicevent-getsignalbasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SignalBasedFrame elements from the current CyclicEvent section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedFrame[] GetSignalBasedFrameList()RemarksModifications you make to the contents of this list apply to the system definiti

### GetSignalBasedFrameList()

Gets an array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [CyclicEvent](nationalinstruments-veristand-systemdefinitionapi-cyclicevent.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html)[] GetSignalBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [CyclicEvent](nationalinstruments-veristand-systemdefinitionapi-cyclicevent.html) section.

Parent topic:

CyclicEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cyclicevent.html language=enus -->
## TOPIC 02216: CyclicEvent Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cyclicevent.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cyclicevent.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the CyclicEvent section that contains outgoing cyclic/event frames under an NI-XNET CAN port. Use cyclic/event frames when you want data changes to arrive at other ECUs within a well-defined deadline with the additional ability to send frames on demand. Derives fromSectionSyntaxNamespace:

### CyclicEvent Class

Represents the **CyclicEvent** section that contains outgoing cyclic/event frames under an NI-XNET CAN port. Use cyclic/event frames when you want data changes to arrive at other ECUs within a well-defined deadline with the additional ability to send frames on demand.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CyclicEvent : Section

#### Remarks

Use the members of this class to add or access cyclic/event frames under the port.

**Accessing this Class**

- [GetCyclicEvent](nationalinstruments-veristand-systemdefinitionapi-outgoing-getcyclicevent.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddRawDataBasedFrame(RawDataBasedFrame) | Adds the specified RawDataBasedFrame as an outgoing cyclic/event frame under a CAN port. |
| AddRawDataBasedFrame(RawDataBasedFrame, out Error) | Adds the specified RawDataBasedFrame as an outgoing cyclic/event frame under a CAN port. |
| AddSignalBasedFrame(SignalBasedFrame, out Error) | Adds the specified SignalBasedFrame as an outgoing cyclic/event frame under a CAN port. |
| AddSignalBasedFrame(SignalBasedFrame) | Adds the specified SignalBasedFrame as an outgoing cyclic/event frame under a CAN port. |
| GetRawDataBasedFrameList() | Gets an array that contains the RawDataBasedFrame elements from the current CyclicEvent section. |
| GetSignalBasedFrameList() | Gets an array that contains the SignalBasedFrame elements from the current CyclicEvent section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daq-adddevice__daqdevice-out.html language=enus -->
## TOPIC 02217: AddDevice(DAQDevice, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daq-adddevice__daqdevice-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daq-adddevice__daqdevice-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDevice. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDevice(DAQDevice device, out Error error)ParametersNameTypeDescriptiondeviceDAQDeviceThe DAQDevice to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error oc

### AddDevice(DAQDevice, out Error)

Adds the specified [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDevice(DAQDevice device, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | DAQDevice | The DAQDevice to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) was added successfully.

Parent topic:

DAQ Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daq-adddevice__daqdevice.html language=enus -->
## TOPIC 02218: AddDevice(DAQDevice)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daq-adddevice__daqdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daq-adddevice__daqdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDevice. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDevice(DAQDevice device)ParametersNameTypeDescriptiondeviceDAQDeviceThe DAQDevice to add.Returnstrue if the DAQDevice was added successfully.

### AddDevice(DAQDevice)

Adds the specified [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDevice(DAQDevice device)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| device | DAQDevice | The DAQDevice to add. |

#### Returns

true if the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) was added successfully.

Parent topic:

DAQ Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daq-getdevicelist.html language=enus -->
## TOPIC 02219: GetDeviceList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daq-getdevicelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daq-getdevicelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQDevice elements from the current DAQ section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDevice[] GetDeviceList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications you m

### GetDeviceList()

Gets an array that contains the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) elements from the current [DAQ](nationalinstruments-veristand-systemdefinitionapi-daq.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html)[] GetDeviceList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) elements from the current [DAQ](nationalinstruments-veristand-systemdefinitionapi-daq.html) section.

Parent topic:

DAQ Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daq-gettasks.html language=enus -->
## TOPIC 02220: GetTasks()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daq-gettasks.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daq-gettasks.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQTasks section from the DAQ section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTasks GetTasks()ReturnsReturns the DAQTasks section.

### GetTasks()

Gets the DAQTasks section from the [DAQ](nationalinstruments-veristand-systemdefinitionapi-daq.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTasks](nationalinstruments-veristand-systemdefinitionapi-daqtasks.html) GetTasks()

#### Returns

Returns the DAQTasks section.

Parent topic:

DAQ Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daq.html language=enus -->
## TOPIC 02221: DAQ Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daq.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daq.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the DAQ section of a Chassis in the system definition. This section contains all the DAQ devices you add under the chassis. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQ : SectionRemarksUse the members of this class to add a DAQ devi

### DAQ Class

Represents the **DAQ** section of a [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) in the system definition. This section contains all the DAQ devices you add under the chassis.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQ : Section

#### Remarks

Use the members of this class to add a DAQ device or get a list of existing DAQ devices.

**Accessing this Class**

- [GetDAQ](nationalinstruments-veristand-systemdefinitionapi-chassis-getdaq.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddDevice(DAQDevice) | Adds the specified DAQDevice. |
| AddDevice(DAQDevice, out Error) | Adds the specified DAQDevice. |
| GetDeviceList() | Gets an array that contains the DAQDevice elements from the current DAQ section. |
| GetTasks() | Gets the DAQTasks section from the DAQ section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogchanneltype.html language=enus -->
## TOPIC 02222: DAQAnalogChannelType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogchanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogchanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement type of an analog DAQ channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQAnalogChannelTypeMembersNameValueDescriptionVoltage0The channel is a voltage channel, where voltage is expressed in volts. Current1The channel is a current channe

### DAQAnalogChannelType Enumeration

Specifies the measurement type of an analog DAQ channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQAnalogChannelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 0 | The channel is a voltage channel, where voltage is expressed in volts. |
| Current | 1 | The channel is a current channel, where current is expressed in amperes. |
| Other | -1 | The channel is of a measurement type other than current or voltage. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-channel.html language=enus -->
## TOPIC 02223: Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint Channel { get; set; }ReturnsThe channel number.

### Channel

Gets or sets the channel number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint Channel { get; set; }

#### Returns

The channel number.

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-channeltype.html language=enus -->
## TOPIC 02224: ChannelType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-channeltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-channeltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the measurement type of the channel (Current or Voltage). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogChannelType ChannelType { get; set; }ReturnsAn enumeration value of DAQAnalogChannelType.

### ChannelType

Gets or sets the measurement type of the channel (Current or Voltage).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogChannelType](nationalinstruments-veristand-systemdefinitionapi-daqanalogchanneltype.html) ChannelType { get; set; }

#### Returns

An enumeration value of [DAQAnalogChannelType](nationalinstruments-veristand-systemdefinitionapi-daqanalogchanneltype.html).

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-string-double-double-double-uint-daqanalogchanneltype.html language=enus -->
## TOPIC 02225: DAQAnalogInput(string, string, double, double, double, uint, DAQAnalogChannelType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-string-double-double-double-uint-daqanalogchanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-string-double-double-double-uint-daqanalogchanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogInput class with the name and configuration that you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInput(string Name, string Units, double InitialValue, double LowLevel, double HighLevel, uint Channel, DAQAnalogC

### DAQAnalogInput(string, string, double, double, double, uint, DAQAnalogChannelType)

Initializes a new instance of the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) class with the name and configuration that you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogInput(string Name, string Units, double InitialValue, double LowLevel, double HighLevel, uint Channel, DAQAnalogChannelType ChannelType)

#### Remarks

National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the analog input channel. |
| Units | string | The units to associate with the analog input channel. |
| InitialValue | double | The initial value of the analog input channel. |
| LowLevel | double | The minimum value of the analog input channel. |
| HighLevel | double | The maximum value of the analog input channel. |
| Channel | uint | The number for the analog input channel. |
| ChannelType | DAQAnalogChannelType | The DAQAnalogChannelType as Current or Voltage. |

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-daqmeasurementtype-double.html language=enus -->
## TOPIC 02226: DAQAnalogInput(string, uint, DAQMeasurementType, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-daqmeasurementtype-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-daqmeasurementtype-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInput(string name, uint channel, DAQMeasurementType measurementType, double initialValue)ParametersNameTypeDescriptionnamestringThe name of the analog input chann

### DAQAnalogInput(string, uint, DAQMeasurementType, double)

Initializes a new instance of the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogInput(string name, uint channel, DAQMeasurementType measurementType, double initialValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog input channel. |
| channel | uint | The channel number of the analog input channel. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |
| initialValue | double | The initial value of the analog input channel. |

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-daqmeasurementtype.html language=enus -->
## TOPIC 02227: DAQAnalogInput(string, uint, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInput(string name, uint channel, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringThe name of the analog input channel.channeluintThe cha

### DAQAnalogInput(string, uint, DAQMeasurementType)

Initializes a new instance of the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogInput(string name, uint channel, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog input channel. |
| channel | uint | The channel number of the analog input channel. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-string-double.html language=enus -->
## TOPIC 02228: DAQAnalogInput(string, uint, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInput(string name, uint channel, string pluginGUID, double initialValue)RemarksUse this constructor to create channels with a measurement type defined in a custom

### DAQAnalogInput(string, uint, string, double)

Initializes a new instance of the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogInput(string name, uint channel, string pluginGUID, double initialValue)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog input channel. |
| channel | uint | The channel number of the analog input channel. |
| pluginGUID | string | The GUID of the DAQ measurement type plug-in. |
| initialValue | double | The initial value of the analog input channel. |

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-string.html language=enus -->
## TOPIC 02229: DAQAnalogInput(string, uint, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-daqanaloginput__string-uint-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInput(string name, uint channel, string pluginGUID)RemarksUse this constructor to create channels with a measurement type defined in a custom DAQ measurement type

### DAQAnalogInput(string, uint, string)

Initializes a new instance of the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogInput(string name, uint channel, string pluginGUID)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog input channel. |
| channel | uint | The channel number of the analog input channel. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-highlevel.html language=enus -->
## TOPIC 02230: HighLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-highlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-highlevel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum value of the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double HighLevel { get; set; }ReturnsThe maximum value of the channel.

### HighLevel

Gets or sets the maximum value of the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double HighLevel { get; set; }

#### Returns

The maximum value of the channel.

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-initialvalue.html language=enus -->
## TOPIC 02231: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the analog input channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InitialValue { get; set; }ReturnsThe initial value of the channel.

### InitialValue

Gets or sets the initial value of the analog input channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InitialValue { get; set; }

#### Returns

The initial value of the channel.

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-isscxi.html language=enus -->
## TOPIC 02232: IsSCXI

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-isscxi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-isscxi.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the channel belongs to an SCXI module. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsSCXI { get; }Returnstrue if the channel belongs to an SCXI module. Otherwise false.

### IsSCXI

Gets whether the channel belongs to an SCXI module.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsSCXI { get; }

#### Returns

true if the channel belongs to an SCXI module. Otherwise false.

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-lowlevel.html language=enus -->
## TOPIC 02233: LowLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-lowlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-lowlevel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the minimum value of the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double LowLevel { get; set; }ReturnsThe minimum value of the channel.

### LowLevel

Gets or sets the minimum value of the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double LowLevel { get; set; }

#### Returns

The minimum value of the channel.

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-scximoduletype.html language=enus -->
## TOPIC 02234: SCXIModuleType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-scximoduletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput-scximoduletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the specific type of SCXI module to which the channel belongs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string SCXIModuleType { get; }ReturnsA string indicating the type of the SCXI module.

### SCXIModuleType

Gets the specific type of SCXI module to which the channel belongs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string SCXIModuleType { get; }

#### Returns

A string indicating the type of the SCXI module.

Parent topic:

DAQAnalogInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html language=enus -->
## TOPIC 02235: DAQAnalogInput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ analog input channel. Derives fromDAQChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQAnalogInput : DAQChannelRemarksUse the members of this class to get and set properties of the channel such as its high and low level and whether it belongs t

### DAQAnalogInput Class

Represents a DAQ analog input channel.

#### Derives from

- DAQChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQAnalogInput : DAQChannel

#### Remarks

Use the members of this class to get and set properties of the channel such as its high and low level and whether it belongs to an SCXI module.

**Accessing this Class**

- [GetAnalogInputList](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-getanaloginputlist.html)
- [GetAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-scximodule-getanaloginputs.html)
- DAQAnalogInput Constructor

National Instruments recommends that you use a version of the DAQAnalogInput constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQAnalogInput(string, uint, DAQMeasurementType, double) | Initializes a new instance of the DAQAnalogInput class. |
| DAQAnalogInput(string, string, double, double, double, uint, DAQAnalogChannelType) | Initializes a new instance of the DAQAnalogInput class with the name and configuration that you specify. |
| DAQAnalogInput(string, uint, DAQMeasurementType) | Initializes a new instance of the DAQAnalogInput class. |
| DAQAnalogInput(string, uint, string) | Initializes a new instance of the DAQAnalogInput class. |
| DAQAnalogInput(string, uint, string, double) | Initializes a new instance of the DAQAnalogInput class. |

#### Properties

| Name | Description |
| --- | --- |
| Channel | Gets or sets the channel number. |
| ChannelType | Gets or sets the measurement type of the channel (Current or Voltage). |
| HighLevel | Gets or sets the maximum value of the channel. |
| InitialValue | Gets or sets the initial value of the analog input channel. |
| IsSCXI | Gets whether the channel belongs to an SCXI module. |
| LowLevel | Gets or sets the minimum value of the channel. |
| SCXIModuleType | Gets the specific type of SCXI module to which the channel belongs. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addanaloginput__daqanaloginput-out.html language=enus -->
## TOPIC 02236: AddAnalogInput(DAQAnalogInput, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addanaloginput__daqanaloginput-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addanaloginput__daqanaloginput-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQAnalogInput channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAnalogInput(DAQAnalogInput analogInput, out Error error)ParametersNameTypeDescriptionanalogInputDAQAnalogInputThe DAQAnalogInput channel to add.errorout ErrorReturns an Nationa

### AddAnalogInput(DAQAnalogInput, out Error)

Adds the specified [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAnalogInput(DAQAnalogInput analogInput, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| analogInput | DAQAnalogInput | The DAQAnalogInput channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) channel was added successfully.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addanaloginput__daqanaloginput.html language=enus -->
## TOPIC 02237: AddAnalogInput(DAQAnalogInput)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addanaloginput__daqanaloginput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addanaloginput__daqanaloginput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQAnalogInput channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAnalogInput(DAQAnalogInput analogInput)ParametersNameTypeDescriptionanalogInputDAQAnalogInputThe DAQAnalogInput channel to add.Returnstrue if the DAQAnalogInput channel was add

### AddAnalogInput(DAQAnalogInput)

Adds the specified [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAnalogInput(DAQAnalogInput analogInput)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| analogInput | DAQAnalogInput | The DAQAnalogInput channel to add. |

#### Returns

true if the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) channel was added successfully.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addwaveformanaloginput__daqwaveformanaloginput-out.html language=enus -->
## TOPIC 02238: AddWaveformAnalogInput(DAQWaveformAnalogInput, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addwaveformanaloginput__daqwaveformanaloginput-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addwaveformanaloginput__daqwaveformanaloginput-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the DAQWaveformAnalogInput waveform that you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddWaveformAnalogInput(DAQWaveformAnalogInput waveformAnalogInput, out Error error)ParametersNameTypeDescriptionwaveformAnalogInputDAQWaveformAnalogInputThe DAQWav

### AddWaveformAnalogInput(DAQWaveformAnalogInput, out Error)

Adds the [DAQWaveformAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html) waveform that you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddWaveformAnalogInput(DAQWaveformAnalogInput waveformAnalogInput, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformAnalogInput | DAQWaveformAnalogInput | The DAQWaveformAnalogInput channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQWaveformAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html) channel was added successfully; otherwise false.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addwaveformanaloginput__daqwaveformanaloginput.html language=enus -->
## TOPIC 02239: AddWaveformAnalogInput(DAQWaveformAnalogInput)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addwaveformanaloginput__daqwaveformanaloginput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-addwaveformanaloginput__daqwaveformanaloginput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the DAQWaveformAnalogInput waveform that you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddWaveformAnalogInput(DAQWaveformAnalogInput waveformAnalogInput)ParametersNameTypeDescriptionwaveformAnalogInputDAQWaveformAnalogInputThe DAQWaveformAnalogInput

### AddWaveformAnalogInput(DAQWaveformAnalogInput)

Adds the [DAQWaveformAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html) waveform that you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddWaveformAnalogInput(DAQWaveformAnalogInput waveformAnalogInput)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformAnalogInput | DAQWaveformAnalogInput | The DAQWaveformAnalogInput channel to add. |

#### Returns

true if the [DAQWaveformAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html) channel was added successfully; otherwise false.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-getanaloginputlist.html language=enus -->
## TOPIC 02240: GetAnalogInputList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-getanaloginputlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-getanaloginputlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQAnalogInput elements from the current DAQAnalogInputs section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInput[] GetAnalogInputList()RemarksAny modification that you make to the contents of this array also apply to the system

### GetAnalogInputList()

Gets an array that contains the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) elements from the current [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html)[] GetAnalogInputList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) elements from the current [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) section.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-getwaveformanaloginputlist.html language=enus -->
## TOPIC 02241: GetWaveformAnalogInputList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-getwaveformanaloginputlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-getwaveformanaloginputlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQWaveformAnalogInput elements from the current DAQAnalogInputs section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQWaveformAnalogInput[] GetWaveformAnalogInputList()ReturnsReturns an array that contains the DAQWaveformAnalogInput ele

### GetWaveformAnalogInputList()

Gets an array that contains the [DAQWaveformAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html) elements from the current [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQWaveformAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html)[] GetWaveformAnalogInputList()

#### Returns

Returns an array that contains the [DAQWaveformAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqwaveformanaloginput.html) elements from the current [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) section.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-isslowbackgroundconvertenabled.html language=enus -->
## TOPIC 02242: IsSlowBackgroundConvertEnabled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-isslowbackgroundconvertenabled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-isslowbackgroundconvertenabled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the Slow Background Convert configuration is enabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsSlowBackgroundConvertEnabled { get; }ReturnsReturns whether the Hardware-Timed Single-Point Slow Background Convert configuration is enabled. true if the

### IsSlowBackgroundConvertEnabled

Gets whether the Slow Background Convert configuration is enabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsSlowBackgroundConvertEnabled { get; }

#### Returns

Returns whether the Hardware-Timed Single-Point Slow Background Convert configuration is enabled. true if the configuration is enabled; otherwise false

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-samplemode.html language=enus -->
## TOPIC 02243: SampleMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-samplemode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-samplemode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the acquisition is single-point or buffered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SampleMode SampleMode { get; set; }ReturnsSpecifies whether the acquisition is single-point or buffered.

### SampleMode

Gets or sets whether the acquisition is single-point or buffered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SampleMode](nationalinstruments-veristand-systemdefinitionapi-samplemode.html) SampleMode { get; set; }

#### Returns

Specifies whether the acquisition is single-point or buffered.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-slowbackgroundconvertmode__bool-double.html language=enus -->
## TOPIC 02244: SlowBackgroundConvertMode(bool, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-slowbackgroundconvertmode__bool-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-slowbackgroundconvertmode__bool-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Slow Background Convert configuration on supported devices. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SlowBackgroundConvertMode(bool enable, double rate)RemarksSpecifies to read from AI channels at the Sample rate that you specify. This option is use

### SlowBackgroundConvertMode(bool, double)

Specifies the Slow Background Convert configuration on supported devices.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SlowBackgroundConvertMode(bool enable, double rate)

#### Remarks

Note

This option is disabled if at least one of the following conditions is true:

- Hardware-timed single-pont sampling is disabled for the AI channels.
- This device is set to be the chassis master synchronization device.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| enable | bool | Enables support. true if you wish to enable support; otherwise false. |
| rate | double | The sample rate, in hertz (Hz). If you set this parameter to a value of -1, the method configures the device to use its maximum rate. |

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-slowbackgroundconvertrate.html language=enus -->
## TOPIC 02245: SlowBackgroundConvertRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-slowbackgroundconvertrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-slowbackgroundconvertrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Slow Background Convert sample rate. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double SlowBackgroundConvertRate { get; }ReturnsReturns the Slow Background Convert sample rate, in hertz (Hz).

### SlowBackgroundConvertRate

Gets the Slow Background Convert sample rate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double SlowBackgroundConvertRate { get; }

#### Returns

Returns the Slow Background Convert sample rate, in hertz (Hz).

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-waveformanaloginputtask.html language=enus -->
## TOPIC 02246: WaveformAnalogInputTask

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-waveformanaloginputtask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs-waveformanaloginputtask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the DAQTaskAI associated with the buffered acquisition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTaskAI WaveformAnalogInputTask { get; set; }ReturnsThe DAQTaskAI associated with the buffered acquisition.

### WaveformAnalogInputTask

Gets or sets the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) associated with the buffered acquisition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) WaveformAnalogInputTask { get; set; }

#### Returns

The [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) associated with the buffered acquisition.

Parent topic:

DAQAnalogInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html language=enus -->
## TOPIC 02247: DAQAnalogInputs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Analog Input section under a DAQDevice, which contains all DAQAnalogInput channels you add for the device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQAnalogInputs : SectionRemarksUse the members of this class to add analog input

### DAQAnalogInputs Class

Represents an **Analog Input** section under a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html), which contains all [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) channels you add for the device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQAnalogInputs : Section

#### Remarks

Note

You can improve performance by only adding the channels the system interacts with, as opposed to all the channels your hardware supports.

**Accessing this Class**

- [CreateAnalogInputs(out Error)](nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out.html)
- [GetAnalogInputSection](nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanaloginputsection.html)

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| IsSlowBackgroundConvertEnabled | Gets whether the Slow Background Convert configuration is enabled. |
| SampleMode | Gets or sets whether the acquisition is single-point or buffered. |
| SlowBackgroundConvertRate | Gets the Slow Background Convert sample rate. |
| WaveformAnalogInputTask | Gets or sets the DAQTaskAI associated with the buffered acquisition. |

#### Methods

| Name | Description |
| --- | --- |
| AddAnalogInput(DAQAnalogInput) | Adds the specified DAQAnalogInput channel. |
| AddAnalogInput(DAQAnalogInput, out Error) | Adds the specified DAQAnalogInput channel. |
| AddWaveformAnalogInput(DAQWaveformAnalogInput) | Adds the DAQWaveformAnalogInput waveform that you specify. |
| AddWaveformAnalogInput(DAQWaveformAnalogInput, out Error) | Adds the DAQWaveformAnalogInput waveform that you specify. |
| GetAnalogInputList() | Gets an array that contains the DAQAnalogInput elements from the current DAQAnalogInputs section. |
| GetWaveformAnalogInputList() | Gets an array that contains the DAQWaveformAnalogInput elements from the current DAQAnalogInputs section. |
| SlowBackgroundConvertMode(bool, double) | Specifies the Slow Background Convert configuration on supported devices. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-channel.html language=enus -->
## TOPIC 02248: Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint Channel { get; set; }ReturnsThe channel number.

### Channel

Gets or sets the channel number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint Channel { get; set; }

#### Returns

The channel number.

Parent topic:

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-channeltype.html language=enus -->
## TOPIC 02249: ChannelType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-channeltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-channeltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the measurement type of the channel (Current or Voltage). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogChannelType ChannelType { get; set; }ReturnsAn enumeration value of DAQAnalogChannelType.

### ChannelType

Gets or sets the measurement type of the channel (Current or Voltage).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogChannelType](nationalinstruments-veristand-systemdefinitionapi-daqanalogchanneltype.html) ChannelType { get; set; }

#### Returns

An enumeration value of [DAQAnalogChannelType](nationalinstruments-veristand-systemdefinitionapi-daqanalogchanneltype.html).

Parent topic:

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-string-double-double-double-uint-daqanalogchanneltype.html language=enus -->
## TOPIC 02250: DAQAnalogOutput(string, string, double, double, double, uint, DAQAnalogChannelType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-string-double-double-double-uint-daqanalogchanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-string-double-double-double-uint-daqanalogchanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQAnalogOutput with the name and configuration that you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutput(string Name, string Units, double InitialValue, double LowLevel, double HighLevel, uint Channel, DAQAnalogChannelTy

### DAQAnalogOutput(string, string, double, double, double, uint, DAQAnalogChannelType)

Initializes a new instance of [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) with the name and configuration that you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogOutput(string Name, string Units, double InitialValue, double LowLevel, double HighLevel, uint Channel, DAQAnalogChannelType ChannelType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the analog output channel. |
| Units | string | The units to associate with the analog output channel. |
| InitialValue | double | The initial value of the analog output channel. |
| LowLevel | double | The minimum value of the analog output channel. |
| HighLevel | double | The maximum value of the analog output channel. |
| Channel | uint | The number for the analog output channel. |
| ChannelType | DAQAnalogChannelType | The DAQAnalogChannelType as Current or Voltage. |

Parent topic:

DAQAnalogOutput Class
