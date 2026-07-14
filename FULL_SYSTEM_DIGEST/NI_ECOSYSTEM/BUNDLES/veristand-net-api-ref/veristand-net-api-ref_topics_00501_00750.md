# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=501 end=750 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addchannel__string-string.html language=enus -->
## TOPIC 00501: AddChannel(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addchannel__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addchannel__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new TdmsChannel with the specified name and channel path to the TdmsChannelGroup. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsChannel AddChannel(string name, string channelPath)ParametersNameTypeDescriptionnamestringThe name of the TdmsChannel.channelPathstringT

### AddChannel(string, string)

Adds a new TdmsChannel with the specified name and channel path to the TdmsChannelGroup.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsChannel](nationalinstruments-veristand-clientapi-logging-tdmschannel.html) AddChannel(string name, string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the TdmsChannel. |
| channelPath | string | The system definition path of the channel to log. |

#### Returns

The newly added TdmsChannel.

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addchannel__tdmschannel.html language=enus -->
## TOPIC 00502: AddChannel(TdmsChannel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addchannel__tdmschannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addchannel__tdmschannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified TdmsChannel to the TdmsChannelGroup. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void AddChannel(TdmsChannel channel)ParametersNameTypeDescriptionchannelTdmsChannelThe TdmsChannel to add.

### AddChannel(TdmsChannel)

Adds the specified TdmsChannel to the TdmsChannelGroup.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void AddChannel(TdmsChannel channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | TdmsChannel | The TdmsChannel to add. |

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addproperty__string-tdmspropertydatatype-object.html language=enus -->
## TOPIC 00503: AddProperty(string, TdmsPropertyDataType, object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addproperty__string-tdmspropertydatatype-object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addproperty__string-tdmspropertydatatype-object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new TdmsProperty with the specified name, data type, and value to the TdmsChannelGroup. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsProperty AddProperty(string name, TdmsPropertyDataType dataType, object value)ParametersNameTypeDescriptionnamestringThe name of t

### AddProperty(string, TdmsPropertyDataType, object)

Adds a new TdmsProperty with the specified name, data type, and value to the TdmsChannelGroup.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsProperty](nationalinstruments-veristand-clientapi-logging-tdmsproperty.html) AddProperty(string name, TdmsPropertyDataType dataType, object value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. |
| dataType | TdmsPropertyDataType | A TdmsPropertyDataType value that specifies the data type of the TDMS property. |
| value | object | The value of the property. |

#### Returns

The newly added TdmsProperty.

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addproperty__tdmsproperty.html language=enus -->
## TOPIC 00504: AddProperty(TdmsProperty)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addproperty__tdmsproperty.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-addproperty__tdmsproperty.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified TdmsProperty to the TdmsChannelGroup. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void AddProperty(TdmsProperty tdmsProperty)ParametersNameTypeDescriptiontdmsPropertyTdmsPropertyThe TdmsProperty to add.

### AddProperty(TdmsProperty)

Adds the specified TdmsProperty to the TdmsChannelGroup.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void AddProperty(TdmsProperty tdmsProperty)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tdmsProperty | TdmsProperty | The TdmsProperty to add. |

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-description.html language=enus -->
## TOPIC 00505: Description

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-description.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-description.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the description of the TDMS channel group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Description { get; set; }

### Description

Gets or sets a value indicating the description of the TDMS channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Description { get; set; }

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannel__string.html language=enus -->
## TOPIC 00506: GetChannel(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannel__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the specified TDMS channel associated with this TdmsChannelGroup. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsChannel GetChannel(string name)ParametersNameTypeDescriptionnamestringThe name of the channelReturnsIf the channel exists in the TDMS channel group, re

### GetChannel(string)

Returns the specified TDMS channel associated with this TdmsChannelGroup.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsChannel](nationalinstruments-veristand-clientapi-logging-tdmschannel.html) GetChannel(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel |

#### Returns

If the channel exists in the TDMS channel group, returns a TdmsChannel that represents the channel specified by name (parameter); otherwise, returns null.

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannelnames.html language=enus -->
## TOPIC 00507: GetChannelNames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannelnames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannelnames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of channel names for the channels in the TDMS channel group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] GetChannelNames()ReturnsAn array of channel names for the channels in the TDMS channel group.

### GetChannelNames()

Returns an array of channel names for the channels in the TDMS channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] GetChannelNames()

#### Returns

An array of channel names for the channels in the TDMS channel group.

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannelpaths.html language=enus -->
## TOPIC 00508: GetChannelPaths()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannelpaths.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getchannelpaths.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of channel paths for the channels in the TDMS channel group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] GetChannelPaths()ReturnsAn array of channel paths for the channels in the TDMS channel group.

### GetChannelPaths()

Returns an array of channel paths for the channels in the TDMS channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] GetChannelPaths()

#### Returns

An array of channel paths for the channels in the TDMS channel group.

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getproperty__string.html language=enus -->
## TOPIC 00509: GetProperty(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getproperty__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getproperty__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the specified TDMS property associated with this TdmsChannelGroup. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsProperty GetProperty(string name)ParametersNameTypeDescriptionnamestringThe name of the propertyReturnsIf the property exists on the TDMS channel grou

### GetProperty(string)

Returns the specified TDMS property associated with this TdmsChannelGroup.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsProperty](nationalinstruments-veristand-clientapi-logging-tdmsproperty.html) GetProperty(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property |

#### Returns

If the property exists on the TDMS channel group, returns a TdmsProperty that represents the property specified by name (parameter); otherwise, returns null.

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getpropertynames.html language=enus -->
## TOPIC 00510: GetPropertyNames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getpropertynames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-getpropertynames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of property names for the TDMS channel group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] GetPropertyNames()ReturnsAn array of property names for the TDMS channel group.

### GetPropertyNames()

Returns an array of property names for the TDMS channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] GetPropertyNames()

#### Returns

An array of property names for the TDMS channel group.

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-name.html language=enus -->
## TOPIC 00511: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the name of the TDMS channel group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Name { get; set; }

### Name

Gets or sets a value indicating the name of the TDMS channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Name { get; set; }

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-tdmschannelgroup__string.html language=enus -->
## TOPIC 00512: TdmsChannelGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-tdmschannelgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-tdmschannelgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TdmsChannelGroup class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsChannelGroup(string name)ParametersNameTypeDescriptionnamestringThe name of the TDMS channel group.

### TdmsChannelGroup(string)

Initializes a new instance of the TdmsChannelGroup class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public TdmsChannelGroup(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the TDMS channel group. |

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-timechannelname.html language=enus -->
## TOPIC 00513: TimeChannelName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-timechannelname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-timechannelname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the name of the time channel in the channel group. This property is ignored if TimeChannelOptions is set to NoTimeChannel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string TimeChannelName { get; set; }

### TimeChannelName

Gets or sets a value indicating the name of the time channel in the channel group. This property is ignored if TimeChannelOptions is set to NoTimeChannel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string TimeChannelName { get; set; }

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-timechanneloptions.html language=enus -->
## TOPIC 00514: TimeChannelOptions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-timechanneloptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup-timechanneloptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to include a time channel as the first channel in the channel group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TimeChannelOptions TimeChannelOptions { get; set; }

### TimeChannelOptions

Gets or sets a value indicating whether to include a time channel as the first channel in the channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TimeChannelOptions](nationalinstruments-veristand-clientapi-logging-timechanneloptions.html) TimeChannelOptions { get; set; }

Parent topic:

TdmsChannelGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmschannelgroup.html language=enus -->
## TOPIC 00515: TdmsChannelGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmschannelgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmschannelgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a TDMS channel group to log. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TdmsChannelGroupConstructorsNameDescriptionTdmsChannelGroup(string)Initializes a new instance of the TdmsChannelGroup class. PropertiesNameDescriptionDescriptionGets or

### TdmsChannelGroup Class

Specifies a TDMS channel group to log.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TdmsChannelGroup

#### Constructors

| Name | Description |
| --- | --- |
| TdmsChannelGroup(string) | Initializes a new instance of the TdmsChannelGroup class. |

#### Properties

| Name | Description |
| --- | --- |
| Description | Gets or sets a value indicating the description of the TDMS channel group. |
| Name | Gets or sets a value indicating the name of the TDMS channel group. |
| TimeChannelName | Gets or sets a value indicating the name of the time channel in the channel group. This property is ignored if TimeChannelOptions is set to NoTimeChannel. |
| TimeChannelOptions | Gets or sets a value indicating whether to include a time channel as the first channel in the channel group. |

#### Methods

| Name | Description |
| --- | --- |
| AddChannel(TdmsChannel) | Adds the specified TdmsChannel to the TdmsChannelGroup. |
| AddChannel(string, string) | Adds a new TdmsChannel with the specified name and channel path to the TdmsChannelGroup. |
| AddProperty(string, TdmsPropertyDataType, object) | Adds a new TdmsProperty with the specified name, data type, and value to the TdmsChannelGroup. |
| AddProperty(TdmsProperty) | Adds the specified TdmsProperty to the TdmsChannelGroup. |
| GetChannel(string) | Returns the specified TDMS channel associated with this TdmsChannelGroup. |
| GetChannelNames() | Returns an array of channel names for the channels in the TDMS channel group. |
| GetChannelPaths() | Returns an array of channel paths for the channels in the TDMS channel group. |
| GetProperty(string) | Returns the specified TDMS property associated with this TdmsChannelGroup. |
| GetPropertyNames() | Returns an array of property names for the TDMS channel group. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-addchannelgroup__string.html language=enus -->
## TOPIC 00516: AddChannelGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-addchannelgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-addchannelgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new TdmsChannelGroup with the specified name to the TdmsLogFile. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsChannelGroup AddChannelGroup(string name)ParametersNameTypeDescriptionnamestringThe name of the TdmsChannelGroup.ReturnsThe newly added TdmsChannelGroup.

### AddChannelGroup(string)

Adds a new TdmsChannelGroup with the specified name to the TdmsLogFile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsChannelGroup](nationalinstruments-veristand-clientapi-logging-tdmschannelgroup.html) AddChannelGroup(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the TdmsChannelGroup. |

#### Returns

The newly added TdmsChannelGroup.

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-addchannelgroup__tdmschannelgroup.html language=enus -->
## TOPIC 00517: AddChannelGroup(TdmsChannelGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-addchannelgroup__tdmschannelgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-addchannelgroup__tdmschannelgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified TdmsChannelGroup to the TdmsLogFile. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void AddChannelGroup(TdmsChannelGroup group)ParametersNameTypeDescriptiongroupTdmsChannelGroupThe TdmsChannelGroup to add.

### AddChannelGroup(TdmsChannelGroup)

Adds the specified TdmsChannelGroup to the TdmsLogFile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void AddChannelGroup(TdmsChannelGroup group)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| group | TdmsChannelGroup | The TdmsChannelGroup to add. |

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-addproperty__string-tdmspropertydatatype-object.html language=enus -->
## TOPIC 00518: AddProperty(string, TdmsPropertyDataType, object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-addproperty__string-tdmspropertydatatype-object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-addproperty__string-tdmspropertydatatype-object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new TdmsProperty with the specified name, data type, and value to the TdmsLogFile. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsProperty AddProperty(string name, TdmsPropertyDataType dataType, object value)ParametersNameTypeDescriptionnamestringThe name of the pr

### AddProperty(string, TdmsPropertyDataType, object)

Adds a new TdmsProperty with the specified name, data type, and value to the TdmsLogFile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsProperty](nationalinstruments-veristand-clientapi-logging-tdmsproperty.html) AddProperty(string name, TdmsPropertyDataType dataType, object value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property. |
| dataType | TdmsPropertyDataType | A TdmsPropertyDataType value that specifies the data type of the TDMS property. |
| value | object | The value of the property. |

#### Returns

The newly added TdmsProperty.

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-addproperty__tdmsproperty.html language=enus -->
## TOPIC 00519: AddProperty(TdmsProperty)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-addproperty__tdmsproperty.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-addproperty__tdmsproperty.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified TdmsProperty to the TdmsLogFile. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void AddProperty(TdmsProperty tdmsProperty)ParametersNameTypeDescriptiontdmsPropertyTdmsPropertyThe TdmsProperty to add.

### AddProperty(TdmsProperty)

Adds the specified TdmsProperty to the TdmsLogFile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void AddProperty(TdmsProperty tdmsProperty)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tdmsProperty | TdmsProperty | The TdmsProperty to add. |

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-applyrootpropertiestogroups.html language=enus -->
## TOPIC 00520: ApplyRootPropertiesToGroups

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-applyrootpropertiestogroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-applyrootpropertiestogroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to apply all root file properties to each channel group in the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool ApplyRootPropertiesToGroups { get; set; }

### ApplyRootPropertiesToGroups

Gets or sets a value indicating whether to apply all root file properties to each channel group in the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool ApplyRootPropertiesToGroups { get; set; }

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-description.html language=enus -->
## TOPIC 00521: Description

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-description.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-description.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the description of the TDMS Log File. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Description { get; set; }

### Description

Gets or sets a value indicating the description of the TDMS Log File.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Description { get; set; }

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-getchannelgroup__string.html language=enus -->
## TOPIC 00522: GetChannelGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-getchannelgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-getchannelgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the specified TDMS channel group associated with this TdmsLogFile. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsChannelGroup GetChannelGroup(string name)ParametersNameTypeDescriptionnamestringThe name of the channel groupReturnsIf the channel group exists in the

### GetChannelGroup(string)

Returns the specified TDMS channel group associated with this TdmsLogFile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsChannelGroup](nationalinstruments-veristand-clientapi-logging-tdmschannelgroup.html) GetChannelGroup(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel group |

#### Returns

If the channel group exists in the TDMS log file, returns a TdmsChannelGroup that represents the channel group specified by name (parameter); otherwise, returns null.

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-getchannelgroupnames.html language=enus -->
## TOPIC 00523: GetChannelGroupNames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-getchannelgroupnames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-getchannelgroupnames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of channel group names for the channel groups in the TDMS log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] GetChannelGroupNames()ReturnsAn array of channel group names for the channel groups in the TDMS log file.

### GetChannelGroupNames()

Returns an array of channel group names for the channel groups in the TDMS log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] GetChannelGroupNames()

#### Returns

An array of channel group names for the channel groups in the TDMS log file.

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-getproperty__string.html language=enus -->
## TOPIC 00524: GetProperty(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-getproperty__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-getproperty__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the specified TDMS property associated with this TdmsLogFile. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsProperty GetProperty(string name)ParametersNameTypeDescriptionnamestringThe name of the propertyReturnsIf the property exists on the TDMS log file, returns

### GetProperty(string)

Returns the specified TDMS property associated with this TdmsLogFile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsProperty](nationalinstruments-veristand-clientapi-logging-tdmsproperty.html) GetProperty(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the property |

#### Returns

If the property exists on the TDMS log file, returns a TdmsProperty that represents the property specified by name (parameter); otherwise, returns null.

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-getpropertynames.html language=enus -->
## TOPIC 00525: GetPropertyNames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-getpropertynames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-getpropertynames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of property names for the TDMS log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string[] GetPropertyNames()ReturnsAn array of property names for the TDMS log file.

### GetPropertyNames()

Returns an array of property names for the TDMS log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string[] GetPropertyNames()

#### Returns

An array of property names for the TDMS log file.

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-loggingchannels.html language=enus -->
## TOPIC 00526: LoggingChannels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-loggingchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-loggingchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic override HashSet< string > LoggingChannels { get; }

### LoggingChannels

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public override HashSet< string > LoggingChannels { get; }

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile-tdmslogfile__string-fileconflictoperation.html language=enus -->
## TOPIC 00527: TdmsLogFile(string, FileConflictOperation)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile-tdmslogfile__string-fileconflictoperation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile-tdmslogfile__string-fileconflictoperation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TdmsLogFile class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsLogFile(string baseFilePath, FileConflictOperation fileConflictOperation)ParametersNameTypeDescriptionbaseFilePathstringThe base file path used to specify the log file path

### TdmsLogFile(string, FileConflictOperation)

Initializes a new instance of the TdmsLogFile class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public TdmsLogFile(string baseFilePath, FileConflictOperation fileConflictOperation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseFilePath | string | The base file path used to specify the log file path. |
| fileConflictOperation | FileConflictOperation | The operation to take if a file already exists at the specified path. |

Parent topic:

TdmsLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmslogfile.html language=enus -->
## TOPIC 00528: TdmsLogFile Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmslogfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmslogfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a TDMS log file. Derives fromLogFileSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TdmsLogFile : LogFileConstructorsNameDescriptionTdmsLogFile(string, FileConflictOperation)Initializes a new instance of the TdmsLogFile class. PropertiesNameDescriptionApplyRoot

### TdmsLogFile Class

Specifies a TDMS log file.

#### Derives from

- LogFile

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TdmsLogFile : LogFile

#### Constructors

| Name | Description |
| --- | --- |
| TdmsLogFile(string, FileConflictOperation) | Initializes a new instance of the TdmsLogFile class. |

#### Properties

| Name | Description |
| --- | --- |
| ApplyRootPropertiesToGroups | Gets or sets a value indicating whether to apply all root file properties to each channel group in the log file. |
| Description | Gets or sets a value indicating the description of the TDMS Log File. |
| LoggingChannels |  |

#### Methods

| Name | Description |
| --- | --- |
| AddChannelGroup(string) | Adds a new TdmsChannelGroup with the specified name to the TdmsLogFile. |
| AddChannelGroup(TdmsChannelGroup) | Adds the specified TdmsChannelGroup to the TdmsLogFile. |
| AddProperty(TdmsProperty) | Adds the specified TdmsProperty to the TdmsLogFile. |
| AddProperty(string, TdmsPropertyDataType, object) | Adds a new TdmsProperty with the specified name, data type, and value to the TdmsLogFile. |
| GetChannelGroup(string) | Returns the specified TDMS channel group associated with this TdmsLogFile. |
| GetChannelGroupNames() | Returns an array of channel group names for the channel groups in the TDMS log file. |
| GetProperty(string) | Returns the specified TDMS property associated with this TdmsLogFile. |
| GetPropertyNames() | Returns an array of property names for the TDMS log file. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmsproperty-datatype.html language=enus -->
## TOPIC 00529: DataType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmsproperty-datatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmsproperty-datatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the data type of the TdmsProperty. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsPropertyDataType DataType { get; }

### DataType

Gets a value indicating the data type of the TdmsProperty.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TdmsPropertyDataType](nationalinstruments-veristand-clientapi-logging-tdmspropertydatatype.html) DataType { get; }

Parent topic:

TdmsProperty Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmsproperty-name.html language=enus -->
## TOPIC 00530: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmsproperty-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmsproperty-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the name of the TdmsProperty. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Name { get; }

### Name

Gets a value indicating the name of the TdmsProperty.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Name { get; }

Parent topic:

TdmsProperty Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmsproperty-tdmsproperty__string-tdmspropertydatatype-object.html language=enus -->
## TOPIC 00531: TdmsProperty(string, TdmsPropertyDataType, object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmsproperty-tdmsproperty__string-tdmspropertydatatype-object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmsproperty-tdmsproperty__string-tdmspropertydatatype-object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TdmsProperty class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TdmsProperty(string name, TdmsPropertyDataType dataType, object value)ParametersNameTypeDescriptionnamestringThe name of the TdmsPropertydataTypeTdmsPropertyDataTypeThe data t

### TdmsProperty(string, TdmsPropertyDataType, object)

Initializes a new instance of the TdmsProperty class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public TdmsProperty(string name, TdmsPropertyDataType dataType, object value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the TdmsProperty |
| dataType | TdmsPropertyDataType | The data type of the TdmsProperty |
| value | object | The value of the TdmsProperty. This value must be the same data type as specified in dataType. |

Parent topic:

TdmsProperty Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmsproperty-value.html language=enus -->
## TOPIC 00532: Value

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmsproperty-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmsproperty-value.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the value of the TdmsProperty. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic object Value { get; set; }

### Value

Gets or sets a value indicating the value of the TdmsProperty.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public object Value { get; set; }

Parent topic:

TdmsProperty Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmsproperty.html language=enus -->
## TOPIC 00533: TdmsProperty Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmsproperty.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmsproperty.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a way to create a TDMS property which can be added to a TDMS file, channel group, or channel. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TdmsPropertyConstructorsNameDescriptionTdmsProperty(string, TdmsPropertyDataType, object)Initializes a n

### TdmsProperty Class

Provides a way to create a TDMS property which can be added to a TDMS file, channel group, or channel.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TdmsProperty

#### Constructors

| Name | Description |
| --- | --- |
| TdmsProperty(string, TdmsPropertyDataType, object) | Initializes a new instance of the TdmsProperty class. |

#### Properties

| Name | Description |
| --- | --- |
| DataType | Gets a value indicating the data type of the TdmsProperty. |
| Name | Gets a value indicating the name of the TdmsProperty. |
| Value | Gets or sets a value indicating the value of the TdmsProperty. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmspropertydatatype.html language=enus -->
## TOPIC 00534: TdmsPropertyDataType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmspropertydatatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmspropertydatatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a TDMS property's data type. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic enum TdmsPropertyDataTypeMembersNameValueDescriptionNone0Boolean33The TDMS property's data type is Boolean. DateTime68The TDMS property's data type is DateTime. Double10The TDMS property's d

### TdmsPropertyDataType Enumeration

Specifies a TDMS property's data type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public enum TdmsPropertyDataType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 |  |
| Boolean | 33 | The TDMS property's data type is Boolean. |
| DateTime | 68 | The TDMS property's data type is DateTime. |
| Double | 10 | The TDMS property's data type is Double. |
| Float | 9 | The TDMS property's data type is Float. |
| Int16 | 2 | The TDMS property's data type is Int16. |
| Int32 | 3 | The TDMS property's data type is Int32. |
| Int64 | 4 | The TDMS property's data type is Int64. |
| Int8 | 1 | The TDMS property's data type is Int8. |
| String | 32 | The TDMS property's data type is String. |
| UInt16 | 6 | The TDMS property's data type is UInt16. |
| UInt32 | 7 | The TDMS property's data type is UInt32. |
| UInt64 | 8 | The TDMS property's data type is UInt64. |
| UInt8 | 5 | The TDMS property's data type is UInt8. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-canconvert__type.html language=enus -->
## TOPIC 00535: CanConvert(Type)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-canconvert__type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-canconvert__type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic override bool CanConvert(Type objectType)

### CanConvert(Type)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public override bool CanConvert(Type objectType)

Parent topic:

TdmsPropertyJsonConverter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-readjson__jsonreader-type-object-jsonserializer.html language=enus -->
## TOPIC 00536: ReadJson(JsonReader, Type, object, JsonSerializer)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-readjson__jsonreader-type-object-jsonserializer.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-readjson__jsonreader-type-object-jsonserializer.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)

### ReadJson(JsonReader, Type, object, JsonSerializer)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)

Parent topic:

TdmsPropertyJsonConverter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-writejson__jsonwriter-object-jsonserializer.html language=enus -->
## TOPIC 00537: WriteJson(JsonWriter, object, JsonSerializer)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-writejson__jsonwriter-object-jsonserializer.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter-writejson__jsonwriter-object-jsonserializer.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)

### WriteJson(JsonWriter, object, JsonSerializer)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)

Parent topic:

TdmsPropertyJsonConverter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter.html language=enus -->
## TOPIC 00538: TdmsPropertyJsonConverter Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-tdmspropertyjsonconverter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides custom serialization and deserialization for TdmsProperty objects. Derives fromJsonConverterSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TdmsPropertyJsonConverter : JsonConverterMethodsNameDescriptionCanConvert(Type)ReadJson(JsonReader, Type, object, JsonSeri

### TdmsPropertyJsonConverter Class

Provides custom serialization and deserialization for TdmsProperty objects.

#### Derives from

- JsonConverter

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TdmsPropertyJsonConverter : JsonConverter

#### Methods

| Name | Description |
| --- | --- |
| CanConvert(Type) |  |
| ReadJson(JsonReader, Type, object, JsonSerializer) |  |
| WriteJson(JsonWriter, object, JsonSerializer) |  |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogchannel-channelpath.html language=enus -->
## TOPIC 00539: ChannelPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogchannel-channelpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogchannel-channelpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the system definition path of the channel to log. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string ChannelPath { get; set; }

### ChannelPath

Gets or sets a value indicating the system definition path of the channel to log.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string ChannelPath { get; set; }

Parent topic:

TextLogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogchannel-includechannelunitsinname.html language=enus -->
## TOPIC 00540: IncludeChannelUnitsInName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogchannel-includechannelunitsinname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogchannel-includechannelunitsinname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to include the units of the channel to log in the column header. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic bool IncludeChannelUnitsInName { get; set; }

### IncludeChannelUnitsInName

Gets or sets a value indicating whether to include the units of the channel to log in the column header.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public bool IncludeChannelUnitsInName { get; set; }

Parent topic:

TextLogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogchannel-name.html language=enus -->
## TOPIC 00541: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogchannel-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogchannel-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the name of the channel in the text file column header. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string Name { get; set; }

### Name

Gets or sets a value indicating the name of the channel in the text file column header.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string Name { get; set; }

Parent topic:

TextLogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogchannel-textlogchannel__string-string-bool.html language=enus -->
## TOPIC 00542: TextLogChannel(string, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogchannel-textlogchannel__string-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogchannel-textlogchannel__string-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TextLogChannel class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TextLogChannel(string name, string channelPath, bool includeChannelUnitsInName)ParametersNameTypeDescriptionnamestringSpecifies the name of the channel in the text file colu

### TextLogChannel(string, string, bool)

Initializes a new instance of the TextLogChannel class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public TextLogChannel(string name, string channelPath, bool includeChannelUnitsInName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Specifies the name of the channel in the text file column header. |
| channelPath | string | Specifies the system definition path of the channel to log. |
| includeChannelUnitsInName | bool | Specifies whether to include the units of the channel to log in the column header. |

Parent topic:

TextLogChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogchannel.html language=enus -->
## TOPIC 00543: TextLogChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies information about a channel to log in a text file. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TextLogChannelConstructorsNameDescriptionTextLogChannel(string, string, bool)Initializes a new instance of the TextLogChannel class. PropertiesNam

### TextLogChannel Class

Specifies information about a channel to log in a text file.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TextLogChannel

#### Constructors

| Name | Description |
| --- | --- |
| TextLogChannel(string, string, bool) | Initializes a new instance of the TextLogChannel class. |

#### Properties

| Name | Description |
| --- | --- |
| ChannelPath | Gets or sets a value indicating the system definition path of the channel to log. |
| IncludeChannelUnitsInName | Gets or sets a value indicating whether to include the units of the channel to log in the column header. |
| Name | Gets or sets a value indicating the name of the channel in the text file column header. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-addchannel__string-string-bool.html language=enus -->
## TOPIC 00544: AddChannel(string, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-addchannel__string-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-addchannel__string-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new channel to the list of channels to log. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TextLogChannel AddChannel(string name, string channelPath, bool includeChannelUnitsInName)ParametersNameTypeDescriptionnamestringSpecifies the name of the channel in the text fil

### AddChannel(string, string, bool)

Adds a new channel to the list of channels to log.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TextLogChannel](nationalinstruments-veristand-clientapi-logging-textlogchannel.html) AddChannel(string name, string channelPath, bool includeChannelUnitsInName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Specifies the name of the channel in the text file column header. |
| channelPath | string | Specifies the system definition path of the channel to log. |
| includeChannelUnitsInName | bool | Specifies whether to include the units of the channel to log in the column header. |

#### Returns

The newly added TextLogChannel

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-addchannel__textlogchannel.html language=enus -->
## TOPIC 00545: AddChannel(TextLogChannel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-addchannel__textlogchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-addchannel__textlogchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified channel to the list of channels to log. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic void AddChannel(TextLogChannel channel)ParametersNameTypeDescriptionchannelTextLogChannelSpecifies information about the channel to log.

### AddChannel(TextLogChannel)

Adds the specified channel to the list of channels to log.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public void AddChannel(TextLogChannel channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | TextLogChannel | Specifies information about the channel to log. |

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-channels.html language=enus -->
## TOPIC 00546: Channels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-channels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the channels to log. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TextLogChannel[] Channels { get; }

### Channels

Gets a value indicating the channels to log.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [TextLogChannel](nationalinstruments-veristand-clientapi-logging-textlogchannel.html)[] Channels { get; }

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-decimalplaces.html language=enus -->
## TOPIC 00547: DecimalPlaces

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-decimalplaces.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-decimalplaces.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the number of decimal places used when converting the numeric log data to string. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic uint DecimalPlaces { get; set; }

### DecimalPlaces

Gets or sets a value indicating the number of decimal places used when converting the numeric log data to string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public uint DecimalPlaces { get; set; }

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-delimiter.html language=enus -->
## TOPIC 00548: Delimiter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-delimiter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-delimiter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the delimiter between columns in the text file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic Delimiter Delimiter { get; set; }

### Delimiter

Gets or sets a value indicating the delimiter between columns in the text file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public [Delimiter](nationalinstruments-veristand-clientapi-logging-delimiter.html) Delimiter { get; set; }

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-headertext.html language=enus -->
## TOPIC 00549: HeaderText

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-headertext.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-headertext.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the header text to insert at the beginning of the text log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic string HeaderText { get; set; }

### HeaderText

Gets or sets a value indicating the header text to insert at the beginning of the text log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public string HeaderText { get; set; }

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-loggingchannels.html language=enus -->
## TOPIC 00550: LoggingChannels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-loggingchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-loggingchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic override HashSet< string > LoggingChannels { get; }

### LoggingChannels

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public override HashSet< string > LoggingChannels { get; }

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile-textlogfile__string-fileconflictoperation-delimiter-uint.html language=enus -->
## TOPIC 00551: TextLogFile(string, FileConflictOperation, Delimiter, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile-textlogfile__string-fileconflictoperation-delimiter-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile-textlogfile__string-fileconflictoperation-delimiter-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TextLogFile class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TextLogFile(string baseFilePath, FileConflictOperation fileConflictOperation, Delimiter delimiter, uint decimalPlaces)ParametersNameTypeDescriptionbaseFilePathstringThe base fi

### TextLogFile(string, FileConflictOperation, Delimiter, uint)

Initializes a new instance of the TextLogFile class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public TextLogFile(string baseFilePath, FileConflictOperation fileConflictOperation, Delimiter delimiter, uint decimalPlaces)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseFilePath | string | The base file path used to specify the log file path |
| fileConflictOperation | FileConflictOperation | The operation to take if a file already exists at the specified path |
| delimiter | Delimiter | The delimiter between columns in the text file |
| decimalPlaces | uint | The number of decimal places used when converting the numeric log data to string |

Parent topic:

TextLogFile Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-textlogfile.html language=enus -->
## TOPIC 00552: TextLogFile Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-textlogfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-textlogfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies information about a text log file. Derives fromLogFileSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TextLogFile : LogFileConstructorsNameDescriptionTextLogFile(string, FileConflictOperation, Delimiter, uint)Initializes a new instance of the TextLogFile class.

### TextLogFile Class

Specifies information about a text log file.

#### Derives from

- LogFile

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TextLogFile : LogFile

#### Constructors

| Name | Description |
| --- | --- |
| TextLogFile(string, FileConflictOperation, Delimiter, uint) | Initializes a new instance of the TextLogFile class. |

#### Properties

| Name | Description |
| --- | --- |
| Channels | Gets a value indicating the channels to log. |
| DecimalPlaces | Gets or sets a value indicating the number of decimal places used when converting the numeric log data to string. |
| Delimiter | Gets or sets a value indicating the delimiter between columns in the text file. |
| HeaderText | Gets or sets a value indicating the header text to insert at the beginning of the text log file. |
| LoggingChannels |  |

#### Methods

| Name | Description |
| --- | --- |
| AddChannel(string, string, bool) | Adds a new channel to the list of channels to log. |
| AddChannel(TextLogChannel) | Adds the specified channel to the list of channels to log. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-timechanneloptions.html language=enus -->
## TOPIC 00553: TimeChannelOptions Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-timechanneloptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-timechanneloptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies options for automatically including a time channel at the beginning of the channel group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic enum TimeChannelOptionsMembersNameValueDescriptionNoTimeChannel0Specifies not to add a time channel automatically. AbsoluteTime1S

### TimeChannelOptions Enumeration

Specifies options for automatically including a time channel at the beginning of the channel group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public enum TimeChannelOptions

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NoTimeChannel | 0 | Specifies not to add a time channel automatically. |
| AbsoluteTime | 1 | Specifies to add the Absolute Time channel. |
| SystemTime | 2 | Specifies to add the System Time channel. |
| SystemTimeMicroseconds | 3 | Specifies to add the System Time Microseconds channel. |
| AbsoluteTimeAsDouble | 4 | Specifies to add the Absolute Time channel and to log it as a double. |
| RelativeTimeToFirstStartTrigger | 5 | Specifies to add a time channel that has relative values to the timestamp of the first start trigger. |
| RelativeTimeToSessionStart | 6 | Specifies to add a time channel that has relative values to the start of the logging session. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-timesegmentingspecification-timelimit.html language=enus -->
## TOPIC 00554: TimeLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-timesegmentingspecification-timelimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-timesegmentingspecification-timelimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the time in seconds after which a log file will be segmented. This value cannot be negative. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic double TimeLimit { get; set; }

### TimeLimit

Gets or sets a value indicating the time in seconds after which a log file will be segmented. This value cannot be negative.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double TimeLimit { get; set; }

Parent topic:

TimeSegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-timesegmentingspecification-timesegmentingspecification__int-double.html language=enus -->
## TOPIC 00555: TimeSegmentingSpecification(int, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-timesegmentingspecification-timesegmentingspecification__int-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-timesegmentingspecification-timesegmentingspecification__int-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TimeSegmentingSpecification class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic TimeSegmentingSpecification(int maxInstances, double timeLimit)ParametersNameTypeDescriptionmaxInstancesintThe maximum number of file instances that can be crea

### TimeSegmentingSpecification(int, double)

Initializes a new instance of the TimeSegmentingSpecification class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public TimeSegmentingSpecification(int maxInstances, double timeLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maxInstances | int | The maximum number of file instances that can be created. A value of -1 indicates that an unlimited number of file instances can be created. |
| timeLimit | double | The time in seconds after which a log file will be segmented. |

Parent topic:

TimeSegmentingSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-timesegmentingspecification.html language=enus -->
## TOPIC 00556: TimeSegmentingSpecification Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-timesegmentingspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-timesegmentingspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to segment log files after a certain amount of time in seconds has elapsed. Derives fromSegmentingSpecificationSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class TimeSegmentingSpecification : SegmentingSpecificationConstructorsNameDescriptionTimeSegmentingSpecific

### TimeSegmentingSpecification Class

Specifies to segment log files after a certain amount of time in seconds has elapsed.

#### Derives from

- SegmentingSpecification

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class TimeSegmentingSpecification : SegmentingSpecification

#### Constructors

| Name | Description |
| --- | --- |
| TimeSegmentingSpecification(int, double) | Initializes a new instance of the TimeSegmentingSpecification class. |

#### Properties

| Name | Description |
| --- | --- |
| TimeLimit | Gets or sets a value indicating the time in seconds after which a log file will be segmented. This value cannot be negative. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-trigger.html language=enus -->
## TOPIC 00557: Trigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-trigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-trigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a condition that determines when logging starts or stops. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class Trigger

### Trigger Class

Specifies a condition that determines when logging starts or stops.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class Trigger

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-valuechangetrigger-deadband.html language=enus -->
## TOPIC 00558: Deadband

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-valuechangetrigger-deadband.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-valuechangetrigger-deadband.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the deadband. The absolute difference of the change in the channel value must be greater than this amount for the trigger condition to occur. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic double Deadband { get; set; }

### Deadband

Gets or sets a value indicating the deadband. The absolute difference of the change in the channel value must be greater than this amount for the trigger condition to occur.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public double Deadband { get; set; }

Parent topic:

ValueChangeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-valuechangetrigger-valuechangetrigger__string-double.html language=enus -->
## TOPIC 00559: ValueChangeTrigger(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-valuechangetrigger-valuechangetrigger__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-valuechangetrigger-valuechangetrigger__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ValueChangeTrigger class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic ValueChangeTrigger(string channelPath, double deadband)ParametersNameTypeDescriptionchannelPathstringThe system definition path of the channel to monitor.deadbanddoubleT

### ValueChangeTrigger(string, double)

Initializes a new instance of the ValueChangeTrigger class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public ValueChangeTrigger(string channelPath, double deadband)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | The system definition path of the channel to monitor. |
| deadband | double | The absolute difference of the change in the channel value must be greater than this amount for the trigger condition to occur. |

Parent topic:

ValueChangeTrigger Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging-valuechangetrigger.html language=enus -->
## TOPIC 00560: ValueChangeTrigger Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging-valuechangetrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging-valuechangetrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a trigger condition that occurs when a channel value changes by more than a certain absolute amount. Derives fromSingleChannelTriggerSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.Loggingpublic class ValueChangeTrigger : SingleChannelTriggerConstructorsNameDescriptionValueChangeT

### ValueChangeTrigger Class

Specifies a trigger condition that occurs when a channel value changes by more than a certain absolute amount.

#### Derives from

- SingleChannelTrigger

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.Logging](nationalinstruments-veristand-clientapi-logging.html)

public class ValueChangeTrigger : SingleChannelTrigger

#### Constructors

| Name | Description |
| --- | --- |
| ValueChangeTrigger(string, double) | Initializes a new instance of the ValueChangeTrigger class. |

#### Properties

| Name | Description |
| --- | --- |
| Deadband | Gets or sets a value indicating the deadband. The absolute difference of the change in the channel value must be greater than this amount for the trigger condition to occur. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.Logging

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-logging.html language=enus -->
## TOPIC 00561: NationalInstruments.VeriStand.ClientAPI.Logging

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-logging.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-logging.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionAnalogEdgeTriggerSpecifies a trigger condition that occur on an analog edge. DataLoggingSerializationBinderProvides a custom serialization binder for handling DataLogging known types during deserialization. DataLoggingSessionErrorEventArgsProvides data about errors that occur d

### NationalInstruments.VeriStand.ClientAPI.Logging

#### Classes

| Name | Description |
| --- | --- |
| AnalogEdgeTrigger | Specifies a trigger condition that occur on an analog edge. |
| DataLoggingSerializationBinder | Provides a custom serialization binder for handling DataLogging known types during deserialization. |
| DataLoggingSessionErrorEventArgs | Provides data about errors that occur during data logging sessions for the DataLoggingSessionError event. |
| DataLoggingSessionStartEventArgs | Provides data about a new data logging session for the DataLoggingSessionStart event. |
| DataLoggingSessionStateChangeEventArgs | Provides data about the state of a data logging session for the DataLoggingSessionStateChange event. |
| DataLoggingSessionStopEventArgs | Provides data about a data logging session that stopped for the DataLoggingSessionStop event. |
| DataLoggingSpecification | Specifies properties for a data logging session. |
| DefaultTrigger | Specifies a trigger that always evaluates to a certain result. |
| DigitalEdgeTrigger | Specifies a trigger condition that occur on an digital edge. |
| FootprintSegmentingSpecification | Specifies to segment log files after they reach a certain size in bytes. |
| FormulaTrigger | Specifies a trigger condition based on a Boolean expression that operates on a set of channel values. |
| InRangeTrigger | Specifies a trigger condition that occurs when a value falls within a specified range. |
| LogFile | Specifies information about a log file. |
| LogFileClosedEventArgs | Provides data about a closed log file for the LogFileClosed event. |
| LogFileOpenedEventArgs | Provides data about an opened log file for the LogFileOpened event. |
| NewLogFilesCompleteEventArgs | Provides data about newly produced log files on a target for the NewLogFilesComplete event. |
| SegmentingSpecification | Specifies a condition that determines when to segment log files during data logging. This base class specifies never to segment the log file. |
| SingleChannelTrigger | Specifies a trigger whose condition is based on a single channel value. |
| TdmsChannel | Specifies a TDMS channel to log. |
| TdmsChannelGroup | Specifies a TDMS channel group to log. |
| TdmsLogFile | Specifies a TDMS log file. |
| TdmsProperty | Provides a way to create a TDMS property which can be added to a TDMS file, channel group, or channel. |
| TdmsPropertyJsonConverter | Provides custom serialization and deserialization for TdmsProperty objects. |
| TextLogChannel | Specifies information about a channel to log in a text file. |
| TextLogFile | Specifies information about a text log file. |
| TimeSegmentingSpecification | Specifies to segment log files after a certain amount of time in seconds has elapsed. |
| Trigger | Specifies a condition that determines when logging starts or stops. |
| ValueChangeTrigger | Specifies a trigger condition that occurs when a channel value changes by more than a certain absolute amount. |

#### Interfaces

| Name | Description |
| --- | --- |
| IDataLogging | Specifies an interface to automate data logging in the VeriStand Gateway. |

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| DataLoggingSessionState | Specifies the state of a data logging session. |
| Delimiter | Specifies the delimiter for columns in the text log file. |
| FileConflictOperation | Specifies options for what to do if a file already exists at the specified location. |
| Slope | Specifies a rising or falling slope. |
| TdmsPropertyDataType | Specifies a TDMS property's data type. |
| TimeChannelOptions | Specifies options for automatically including a time channel at the beginning of the channel group. |

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-channels.html language=enus -->
## TOPIC 00562: channels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-channels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The list of channels to log in the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic LogChannel[] channels

### channels

The list of channels to log in the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [LogChannel](nationalinstruments-veristand-clientapi-logchannel.html)[] channels

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-description.html language=enus -->
## TOPIC 00563: description

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-description.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-description.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The description for the data log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string description

### description

The description for the data log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string description

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-file_path.html language=enus -->
## TOPIC 00564: file_path

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-file_path.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-file_path.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The file path for the data log file. The file must be a TDMS file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string file_path

### file_path

The file path for the data log file. The file must be a TDMS file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string file_path

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-high_limit.html language=enus -->
## TOPIC 00565: high_limit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-high_limit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-high_limit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The high limit for trigger limit analysis. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic double high_limit

### high_limit

The high limit for trigger limit analysis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double high_limit

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-loginfo.html language=enus -->
## TOPIC 00566: LogInfo()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-loginfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-loginfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LogInfo class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic LogInfo()

### LogInfo()

Initializes a new instance of the [LogInfo](nationalinstruments-veristand-clientapi-loginfo.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public LogInfo()

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-low_limit.html language=enus -->
## TOPIC 00567: low_limit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-low_limit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-low_limit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The low limit for trigger limit analysis. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic double low_limit

### low_limit

The low limit for trigger limit analysis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double low_limit

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-rate.html language=enus -->
## TOPIC 00568: rate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-rate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-rate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The requested rate in Hz at which data is logged to the log file. Data is logged at the closest possible rate to this value that does not exceed the rate at which a target produces data. The default value is Inf, which specifies that all samples are logged. SyntaxNamespace: NationalInstruments.VeriS

### rate

The requested rate in Hz at which data is logged to the log file. Data is logged at the closest possible rate to this value that does not exceed the rate at which a target produces data. The default value is Inf, which specifies that all samples are logged.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double rate

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-replace_file.html language=enus -->
## TOPIC 00569: replace_file

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-replace_file.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-replace_file.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A flag specifying whether to replace an existing log file or append data to the file. TRUE specifies to replace the log file. FALSE specifies to append data to the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool replace_file

### replace_file

A flag specifying whether to replace an existing log file or append data to the file. TRUE specifies to replace the log file. FALSE specifies to append data to the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool replace_file

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-root_properties.html language=enus -->
## TOPIC 00570: root_properties

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-root_properties.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-root_properties.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A dictionary containing property name and property value strings. These properties are written as metadata to the root item in the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Dictionary< string, string > root_properties

### root_properties

A dictionary containing property name and property value strings. These properties are written as metadata to the root item in the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public Dictionary< string, string > root_properties

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-trigger_channel.html language=enus -->
## TOPIC 00571: trigger_channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-trigger_channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-trigger_channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string trigger_channel

### trigger_channel

The path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the **System Explorer** window configuration tree.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string trigger_channel

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo-trigger_type.html language=enus -->
## TOPIC 00572: trigger_type

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo-trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo-trigger_type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The type of trigger to use for the log file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic trigger trigger_type

### trigger_type

The type of [trigger](nationalinstruments-veristand-clientapi-loginfo-trigger.html) to use for the log file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [trigger](nationalinstruments-veristand-clientapi-loginfo-trigger.html) trigger_type

Parent topic:

LogInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-loginfo.html language=enus -->
## TOPIC 00573: LogInfo Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-loginfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-loginfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines data log file configuration settings. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class LogInfoConstructorsNameDescriptionLogInfo()Initializes a new instance of the LogInfo class. FieldsNameDescriptionchannelsThe list of channels to log in the log file. des

### LogInfo Class

Defines data log file configuration settings.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class LogInfo

#### Constructors

| Name | Description |
| --- | --- |
| LogInfo() | Initializes a new instance of the LogInfo class. |

#### Fields

| Name | Description |
| --- | --- |
| channels | The list of channels to log in the log file. |
| description | The description for the data log file. |
| file_path | The file path for the data log file. The file must be a TDMS file. |
| high_limit | The high limit for trigger limit analysis. |
| low_limit | The low limit for trigger limit analysis. |
| rate | The requested rate in Hz at which data is logged to the log file. Data is logged at the closest possible rate to this value that does not exceed the rate at which a target produces data. The default value is Inf, which specifies that all samples are logged. |
| replace_file | A flag specifying whether to replace an existing log file or append data to the file. TRUE specifies to replace the log file. FALSE specifies to append data to the log file. |
| root_properties | A dictionary containing property name and property value strings. These properties are written as metadata to the root item in the log file. |
| trigger_channel | The path to the channel, as specified in the system definition file, on which to perform trigger limit analysis. The path matches the node hierarchy that appears in the System Explorer window configuration tree. |
| trigger_type | The type of trigger to use for the log file. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-modelcommand.html language=enus -->
## TOPIC 00574: ModelCommand Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-modelcommand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-modelcommand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Command to change the execution state of a model running on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum ModelCommandMembersNameValueDescriptionStart0Starts running the model. Pause1Pauses the model. Reset2Resets the model to its initial state.

### ModelCommand Enumeration

Command to change the execution state of a model running on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum ModelCommand

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Start | 0 | Starts running the model. |
| Pause | 1 | Pauses the model. |
| Reset | 2 | Resets the model to its initial state. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-modelstate.html language=enus -->
## TOPIC 00575: ModelState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-modelstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-modelstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The execution state of a model running on the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum ModelStateMembersNameValueDescriptionRunning0The model is running. Paused1The model is paused. Resetting2The model is resetting. Idle3The model is idle. Stopped4The model is stop

### ModelState Enumeration

The execution state of a model running on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum ModelState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Running | 0 | The model is running. |
| Paused | 1 | The model is paused. |
| Resetting | 2 | The model is resetting. |
| Idle | 3 | The model is idle. |
| Stopped | 4 | The model is stopped. |
| Restoring | 5 | Restoring the model execution state from a file. |
| Saving | 6 | Saving information about the current execution state of the model to a file. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-channelcolumndimension.html language=enus -->
## TOPIC 00576: ChannelColumnDimension

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-channelcolumndimension.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-channelcolumndimension.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The number of columns in a channel node value. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic uint ChannelColumnDimension

### ChannelColumnDimension

The number of columns in a channel node value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public uint ChannelColumnDimension

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-channelrowdimension.html language=enus -->
## TOPIC 00577: ChannelRowDimension

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-channelrowdimension.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-channelrowdimension.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The number of rows in a channel node value. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic uint ChannelRowDimension

### ChannelRowDimension

The number of rows in a channel node value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public uint ChannelRowDimension

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-channelunit.html language=enus -->
## TOPIC 00578: ChannelUnit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-channelunit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-channelunit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The unit associated with a channel node value. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string ChannelUnit

### ChannelUnit

The unit associated with a channel node value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string ChannelUnit

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-channelvaluetablenames.html language=enus -->
## TOPIC 00579: ChannelValueTableNames

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-channelvaluetablenames.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-channelvaluetablenames.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The names for the channel value table. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string[] ChannelValueTableNames

### ChannelValueTableNames

The names for the channel value table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string[] ChannelValueTableNames

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-channelvaluetablevalues.html language=enus -->
## TOPIC 00580: ChannelValueTableValues

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-channelvaluetablevalues.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-channelvaluetablevalues.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The values for the channel value table. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic double[] ChannelValueTableValues

### ChannelValueTableValues

The values for the channel value table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double[] ChannelValueTableValues

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-fullpath.html language=enus -->
## TOPIC 00581: FullPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-fullpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-fullpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The full path to a node, as specified in the system definition file. The path matches the node hierarchy that appears in the System Explorer window configuration tree. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string FullPath

### FullPath

The full path to a node, as specified in the system definition file. The path matches the node hierarchy that appears in the **System Explorer** window configuration tree.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string FullPath

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-ischannel.html language=enus -->
## TOPIC 00582: IsChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-ischannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-ischannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: TRUE if a node is a channel. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool IsChannel

### IsChannel

TRUE if a node is a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool IsChannel

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-isfaultable.html language=enus -->
## TOPIC 00583: IsFaultable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-isfaultable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-isfaultable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: TRUE if a node can be faulted. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool IsFaultable

### IsFaultable

TRUE if a node can be faulted.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool IsFaultable

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-isreadable.html language=enus -->
## TOPIC 00584: IsReadable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-isreadable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-isreadable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: TRUE if you can read from a node. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool IsReadable

### IsReadable

TRUE if you can read from a node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool IsReadable

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-isscalable.html language=enus -->
## TOPIC 00585: IsScalable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-isscalable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-isscalable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: TRUE if you can scale a node. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool IsScalable

### IsScalable

TRUE if you can scale a node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool IsScalable

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-iswaveform.html language=enus -->
## TOPIC 00586: IsWaveform

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-iswaveform.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-iswaveform.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: TRUE if a node is a waveform. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool IsWaveform

### IsWaveform

TRUE if a node is a waveform.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool IsWaveform

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-iswritable.html language=enus -->
## TOPIC 00587: IsWritable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-iswritable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-iswritable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: TRUE if you can write to a node. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool IsWritable

### IsWritable

TRUE if you can write to a node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool IsWritable

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-name.html language=enus -->
## TOPIC 00588: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The name of a node in the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Name

### Name

The name of a node in the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Name

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-nodeinfo.html language=enus -->
## TOPIC 00589: NodeInfo()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-nodeinfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-nodeinfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NodeInfo class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic NodeInfo()

### NodeInfo()

Initializes a new instance of the [NodeInfo](nationalinstruments-veristand-clientapi-nodeinfo.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public NodeInfo()

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-type.html language=enus -->
## TOPIC 00590: Type

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The GUID of a node in the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Type

### Type

The GUID of a node in the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Type

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo-waveformdatatype.html language=enus -->
## TOPIC 00591: WaveformDataType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo-waveformdatatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo-waveformdatatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The data type of a waveform node. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic WaveformTypeDataType WaveformDataType

### WaveformDataType

The data type of a waveform node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public WaveformTypeDataType WaveformDataType

Parent topic:

NodeInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-nodeinfo.html language=enus -->
## TOPIC 00592: NodeInfo Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-nodeinfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-nodeinfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides information about and configures a node in the system definition file. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class NodeInfoConstructorsNameDescriptionNodeInfo()Initializes a new instance of the NodeInfo class. FieldsNameDescriptionChannelColumnDimens

### NodeInfo Class

Provides information about and configures a node in the system definition file.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class NodeInfo

#### Constructors

| Name | Description |
| --- | --- |
| NodeInfo() | Initializes a new instance of the NodeInfo class. |

#### Fields

| Name | Description |
| --- | --- |
| ChannelColumnDimension | The number of columns in a channel node value. |
| ChannelRowDimension | The number of rows in a channel node value. |
| ChannelUnit | The unit associated with a channel node value. |
| ChannelValueTableNames | The names for the channel value table. |
| ChannelValueTableValues | The values for the channel value table. |
| FullPath | The full path to a node, as specified in the system definition file. The path matches the node hierarchy that appears in the System Explorer window configuration tree. |
| IsChannel | TRUE if a node is a channel. |
| IsFaultable | TRUE if a node can be faulted. |
| IsReadable | TRUE if you can read from a node. |
| IsScalable | TRUE if you can scale a node. |
| IsWaveform | TRUE if a node is a waveform. |
| IsWritable | TRUE if you can write to a node. |
| Name | The name of a node in the system definition file. |
| Type | The GUID of a node in the system definition file. |
| WaveformDataType | The data type of a waveform node. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-newvalue.html language=enus -->
## TOPIC 00593: NewValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-newvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-newvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the new value of the model parameter. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DataArray NewValue { get; }ReturnsAn array containing the new value of the model parameter.

### NewValue

Gets a value indicating the new value of the model parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public DataArray NewValue { get; }

#### Returns

An array containing the new value of the model parameter.

Parent topic:

ParameterValueChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-parametername.html language=enus -->
## TOPIC 00594: ParameterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-parametername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-parametername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the name of the model parameter whose value changed. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string ParameterName { get; }ReturnsThe name of the model parameter.

### ParameterName

Gets a value indicating the name of the model parameter whose value changed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string ParameterName { get; }

#### Returns

The name of the model parameter.

Parent topic:

ParameterValueChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-parametervaluechangeeventargs__string-string-dataarray.html language=enus -->
## TOPIC 00595: ParameterValueChangeEventArgs(string, string, DataArray)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-parametervaluechangeeventargs__string-string-dataarray.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-parametervaluechangeeventargs__string-string-dataarray.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ParameterValueChangeEventArgs class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic ParameterValueChangeEventArgs(string target, string paramName, DataArray value)ParametersNameTypeDescriptiontargetstringThe name of the target on which the model para

### ParameterValueChangeEventArgs(string, string, DataArray)

Initializes a new instance of the [ParameterValueChangeEventArgs](nationalinstruments-veristand-clientapi-parametervaluechangeeventargs.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public ParameterValueChangeEventArgs(string target, string paramName, DataArray value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | string | The name of the target on which the model parameter exists. |
| paramName | string | The name of the model parameter whose value changed. |
| value | DataArray | An array containing the new value of the model parameter. |

Parent topic:

ParameterValueChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-target.html language=enus -->
## TOPIC 00596: Target

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluechangeeventargs-target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the name of the target to which the new model parameter value was applied. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Target { get; }ReturnsThe name of the target.

### Target

Gets a value indicating the name of the target to which the new model parameter value was applied.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Target { get; }

#### Returns

The name of the target.

Parent topic:

ParameterValueChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluechangeeventargs.html language=enus -->
## TOPIC 00597: ParameterValueChangeEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluechangeeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluechangeeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about model parameter value changes for the ParameterValueChanged and ParameterValueChangeEventHandler events. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class ParameterValueChangeEventArgs : EventArgsThread SafetyAny members of this type are no

### ParameterValueChangeEventArgs Class

Provides data about model parameter value changes for the [ParameterValueChanged](nationalinstruments-veristand-clientapi-imodelmanager2-parametervaluechanged.html) and [ParameterValueChangeEventHandler](nationalinstruments-veristand-clientapi-parametervaluewatcher-parametervaluechangeeventhandler.html) events.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class ParameterValueChangeEventArgs : EventArgs

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ParameterValueChangeEventArgs(string, string, DataArray) | Initializes a new instance of the ParameterValueChangeEventArgs class. |

#### Properties

| Name | Description |
| --- | --- |
| NewValue | Gets a value indicating the new value of the model parameter. |
| ParameterName | Gets a value indicating the name of the model parameter whose value changed. |
| Target | Gets a value indicating the name of the target to which the new model parameter value was applied. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluewatcher-dispose.html language=enus -->
## TOPIC 00598: Dispose()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluewatcher-dispose.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluewatcher-dispose.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Explicit disposal method. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic void Dispose()

### Dispose()

Explicit disposal method.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public void Dispose()

Parent topic:

ParameterValueWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluewatcher-dispose__bool.html language=enus -->
## TOPIC 00599: Dispose(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluewatcher-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluewatcher-dispose__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Dispose method according to the IDisposable design pattern. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIprotected void Dispose(bool disposing)ParametersNameTypeDescriptiondisposingboolboolean indicating if the disposal is safe or not (explicit or due to the finalizer)

### Dispose(bool)

Dispose method according to the IDisposable design pattern.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

protected void Dispose(bool disposing)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| disposing | bool | boolean indicating if the disposal is safe or not (explicit or due to the finalizer) |

Parent topic:

ParameterValueWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluewatcher-onparametervaluechange__object-parametervaluechangeeventargs.html language=enus -->
## TOPIC 00600: OnParameterValueChange(object, ParameterValueChangeEventArgs)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluewatcher-onparametervaluechange__object-parametervaluechangeeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluewatcher-onparametervaluechange__object-parametervaluechangeeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Method used to interface between the event in the IModelManager2 and the event in the ParameterValueWatcher class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIprotected void OnParameterValueChange(object sender, ParameterValueChangeEventArgs e)ParametersNameTypeDescriptionsenderobjectObj

### OnParameterValueChange(object, ParameterValueChangeEventArgs)

Method used to interface between the event in the IModelManager2 and the event in the ParameterValueWatcher class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

protected void OnParameterValueChange(object sender, ParameterValueChangeEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | Object producing the event |
| e | ParameterValueChangeEventArgs | Instance containing the data relevant to this value change |

Parent topic:

ParameterValueWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluewatcher-parametervaluechangeeventhandler.html language=enus -->
## TOPIC 00601: ParameterValueChangeEventHandler

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluewatcher-parametervaluechangeeventhandler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluewatcher-parametervaluechangeeventhandler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event to register a callback to receive notifications when model parameter values are changed. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic EventHandler< ParameterValueChangeEventArgs > ParameterValueChangeEventHandler

### ParameterValueChangeEventHandler

Event to register a callback to receive notifications when model parameter values are changed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public EventHandler< [ParameterValueChangeEventArgs](nationalinstruments-veristand-clientapi-parametervaluechangeeventargs.html) > ParameterValueChangeEventHandler

Parent topic:

ParameterValueWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluewatcher-parametervaluewatcher__imodelmanager2-string-string.html language=enus -->
## TOPIC 00602: ParameterValueWatcher(IModelManager2, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluewatcher-parametervaluewatcher__imodelmanager2-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluewatcher-parametervaluewatcher__imodelmanager2-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ParameterValueWatcher class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic ParameterValueWatcher(IModelManager2 mgr, string target, string parameter)ParametersNameTypeDescriptionmgrIModelManager2Instance of the interface with which to register the p

### ParameterValueWatcher(IModelManager2, string, string)

Initializes a new instance of the ParameterValueWatcher class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public ParameterValueWatcher(IModelManager2 mgr, string target, string parameter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| mgr | IModelManager2 | Instance of the interface with which to register the parameter value changed event |
| target | string | Target the parameter exists on |
| parameter | string | Name of the parameter to register the event for |

Parent topic:

ParameterValueWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-parametervaluewatcher.html language=enus -->
## TOPIC 00603: ParameterValueWatcher Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-parametervaluewatcher.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-parametervaluewatcher.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class essentially serves as a wrapper around the parameter value change event (specific to one parameter) for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. Then,

### ParameterValueWatcher Class

This class essentially serves as a wrapper around the parameter value change event (specific to one parameter) for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. Then, LabVIEW users can register to the event within this class for use in the event structure in LabVIEW.

#### Derives from

- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class ParameterValueWatcher : IDisposable

#### Constructors

| Name | Description |
| --- | --- |
| ParameterValueWatcher(IModelManager2, string, string) | Initializes a new instance of the ParameterValueWatcher class. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Explicit disposal method. |
| Dispose(bool) | Dispose method according to the IDisposable design pattern. |
| OnParameterValueChange(object, ParameterValueChangeEventArgs) | Method used to interface between the event in the IModelManager2 and the event in the ParameterValueWatcher class. |

#### Events

| Name | Description |
| --- | --- |
| ParameterValueChangeEventHandler | Event to register a callback to receive notifications when model parameter values are changed. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-playmodeenum.html language=enus -->
## TOPIC 00604: PlayModeEnum Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-playmodeenum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-playmodeenum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The play mode of the Macro Player tool, which specifies the speed at which the tool plays back macro files. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum PlayModeEnumMembersNameValueDescriptionIgnoreTiming0Ignores timing information in macro files and plays back files as fast a

### PlayModeEnum Enumeration

The play mode of the Macro Player tool, which specifies the speed at which the tool plays back macro files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum PlayModeEnum

#### Members

| Name | Value | Description |
| --- | --- | --- |
| IgnoreTiming | 0 | Ignores timing information in macro files and plays back files as fast as possible. |
| UseTiming | 1 | Uses timing information in macro files to play back files at the speed at which they were recorded. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-playstateenum.html language=enus -->
## TOPIC 00605: PlayStateEnum Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-playstateenum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-playstateenum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The current state of the Macro Player tool. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum PlayStateEnumMembersNameValueDescriptionNotPlaying0The Macro Player is idle. Playing1The Macro Player is playing back a macro file. Paused2The Macro Player is paused in the middle of playb

### PlayStateEnum Enumeration

The current state of the Macro Player tool.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum PlayStateEnum

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NotPlaying | 0 | The Macro Player is idle. |
| Playing | 1 | The Macro Player is playing back a macro file. |
| Paused | 2 | The Macro Player is paused in the middle of playback. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-remotesequencecallinfo-remotesequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-string-int.html language=enus -->
## TOPIC 00606: RemoteSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-remotesequencecallinfo-remotesequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-remotesequencecallinfo-remotesequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RemoteSequenceCallInfo. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic RemoteSequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout, string ZipPath, int GroupNumber)Paramete

### RemoteSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, string, int)

Initializes a new instance of [RemoteSequenceCallInfo](nationalinstruments-veristand-clientapi-remotesequencecallinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public RemoteSequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout, string ZipPath, int GroupNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| SequencePath | string | The file path of the sequence file to execute. |
| Target | string | The name of the target on which to execute the sequence. |
| ParameterAssignments | SequenceParameterAssignmentInfo[] | The parameter assignments for the sequence. |
| Debug | bool | Whether the sequence executes in debug mode. |
| Timeout | double | The timeout in milliseconds within which the sequence must complete each time step. |
| ZipPath | string | The file path of the zip file containing the top level sequence file and dependencies to execute. |
| GroupNumber | int | Specifies the group number of the sequence |

Parent topic:

RemoteSequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-remotesequencecallinfo-remotesequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-string.html language=enus -->
## TOPIC 00607: RemoteSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-remotesequencecallinfo-remotesequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-remotesequencecallinfo-remotesequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RemoteSequenceCallInfo. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic RemoteSequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout, string ZipPath)ParametersNameTypeDescrip

### RemoteSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, string)

Initializes a new instance of [RemoteSequenceCallInfo](nationalinstruments-veristand-clientapi-remotesequencecallinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public RemoteSequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout, string ZipPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| SequencePath | string | The file path of the sequence file to execute. |
| Target | string | The name of the target on which to execute the sequence. |
| ParameterAssignments | SequenceParameterAssignmentInfo[] | The parameter assignments for the sequence. |
| Debug | bool | Whether the sequence executes in debug mode. |
| Timeout | double | The timeout in milliseconds within which the sequence must complete each time step. |
| ZipPath | string | The file path of the zip file containing the top level sequence file and dependencies to execute. |

Parent topic:

RemoteSequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-remotesequencecallinfo-zippath.html language=enus -->
## TOPIC 00608: ZipPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-remotesequencecallinfo-zippath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-remotesequencecallinfo-zippath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the file path of the zip file containing the top-level sequence and dependencies. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string ZipPath { get; }

### ZipPath

Gets the file path of the zip file containing the top-level sequence and dependencies.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string ZipPath { get; }

Parent topic:

RemoteSequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-remotesequencecallinfo.html language=enus -->
## TOPIC 00609: RemoteSequenceCallInfo Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-remotesequencecallinfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-remotesequencecallinfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides information about a remote stimulus profile sequence. Derives fromSequenceCallInfoSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class RemoteSequenceCallInfo : SequenceCallInfoConstructorsNameDescriptionRemoteSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[]

### RemoteSequenceCallInfo Class

Provides information about a remote stimulus profile sequence.

#### Derives from

- SequenceCallInfo

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class RemoteSequenceCallInfo : SequenceCallInfo

#### Constructors

| Name | Description |
| --- | --- |
| RemoteSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, string, int) | Initializes a new instance of RemoteSequenceCallInfo. |
| RemoteSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, string) | Initializes a new instance of RemoteSequenceCallInfo. |

#### Properties

| Name | Description |
| --- | --- |
| ZipPath | Gets the file path of the zip file containing the top-level sequence and dependencies. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-configurationfilepath.html language=enus -->
## TOPIC 00610: ConfigurationFilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-configurationfilepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-configurationfilepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Path to the file containing the runtime configuration applied on RuntimeConfigurableSectionPath. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string ConfigurationFilePath { get; }

### ConfigurationFilePath

Path to the file containing the runtime configuration applied on [RuntimeConfigurableSectionPath](nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurablesectionpath.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string ConfigurationFilePath { get; }

Parent topic:

RuntimeConfigurationChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurablesectionpath.html language=enus -->
## TOPIC 00611: RuntimeConfigurableSectionPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurablesectionpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurablesectionpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Path to the Custom Device's runtime configurable section. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string RuntimeConfigurableSectionPath { get; }

### RuntimeConfigurableSectionPath

Path to the Custom Device's runtime configurable section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string RuntimeConfigurableSectionPath { get; }

Parent topic:

RuntimeConfigurationChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurationchangeaction.html language=enus -->
## TOPIC 00612: RuntimeConfigurationChangeAction

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurationchangeaction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurationchangeaction.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Runtime configuration action on Custom Device's runtime configurable section. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic RuntimeConfigurationChangeAction RuntimeConfigurationChangeAction { get; }

### RuntimeConfigurationChangeAction

Runtime configuration action on Custom Device's runtime configurable section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public RuntimeConfigurationChangeAction RuntimeConfigurationChangeAction { get; }

Parent topic:

RuntimeConfigurationChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurationchangeeventargs__string-string-runtimeconfigurationchangeaction.html language=enus -->
## TOPIC 00613: RuntimeConfigurationChangeEventArgs(string, string, RuntimeConfigurationChangeAction)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurationchangeeventargs__string-string-runtimeconfigurationchangeaction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs-runtimeconfigurationchangeeventargs__string-string-runtimeconfigurationchangeaction.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the RuntimeConfigurationChangeEventArgs class Initializes a new instance of the RuntimeConfigurationChangeEventArgs class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic RuntimeConfigurationChangeEventArgs(string runtimeConfigurableSectionPath, string co

### RuntimeConfigurationChangeEventArgs(string, string, RuntimeConfigurationChangeAction)

Initializes a new instance of the RuntimeConfigurationChangeEventArgs class Initializes a new instance of the RuntimeConfigurationChangeEventArgs class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public RuntimeConfigurationChangeEventArgs(string runtimeConfigurableSectionPath, string configurationFilePath, RuntimeConfigurationChangeAction runtimeConfigurationChangeAction)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableSectionPath | string | Path to the Custom Device's runtime configurable section. |
| configurationFilePath | string | Path to the file containing the runtime configuration applied on runtimeConfigurableSectionPath . |
| runtimeConfigurationChangeAction | RuntimeConfigurationChangeAction | runtime configuration action on Custom Device's runtime configurable section |

Parent topic:

RuntimeConfigurationChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs.html language=enus -->
## TOPIC 00614: RuntimeConfigurationChangeEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-runtimeconfigurationchangeeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about runtime configuration change event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class RuntimeConfigurationChangeEventArgs : EventArgsConstructorsNameDescriptionRuntimeConfigurationChangeEventArgs(string, string, RuntimeConfigurationChangeAc

### RuntimeConfigurationChangeEventArgs Class

Provides data about runtime configuration change event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class RuntimeConfigurationChangeEventArgs : EventArgs

#### Constructors

| Name | Description |
| --- | --- |
| RuntimeConfigurationChangeEventArgs(string, string, RuntimeConfigurationChangeAction) | Initializes a new instance of the RuntimeConfigurationChangeEventArgs class Initializes a new instance of the RuntimeConfigurationChangeEventArgs class. |

#### Properties

| Name | Description |
| --- | --- |
| ConfigurationFilePath | Path to the file containing the runtime configuration applied on RuntimeConfigurableSectionPath. |
| RuntimeConfigurableSectionPath | Path to the Custom Device's runtime configurable section. |
| RuntimeConfigurationChangeAction | Runtime configuration action on Custom Device's runtime configurable section. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-runtimeconfigurationstate.html language=enus -->
## TOPIC 00615: RuntimeConfigurationState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-runtimeconfigurationstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-runtimeconfigurationstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The current state of the runtime configuration on the runtime configurable node. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum RuntimeConfigurationStateMembersNameValueDescriptionUnconfigured0The runtime configuration is not configured. Configuring1The runtime configuration is

### RuntimeConfigurationState Enumeration

The current state of the runtime configuration on the runtime configurable node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum RuntimeConfigurationState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Unconfigured | 0 | The runtime configuration is not configured. |
| Configuring | 1 | The runtime configuration is being configured. |
| Configured | 2 | The runtime configuration is configured. |
| Applying | 3 | The runtime configuration is being applied. |
| Applied | 4 | The runtime configuration is applied. |
| Removing | 5 | The rumtime configuration is being removed. |
| Error | 6 | An error occurred while applying or removing the runtime configuration. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-scaletype.html language=enus -->
## TOPIC 00616: ScaleType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-scaletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-scaletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The type of calibration scale. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum ScaleTypeMembersNameValueDescriptionPolynomial0A polynomial scale. This type provides up to a fourth order scale. Thermocouple1A thermocouple scale, which converts volts to temperature. None2No scale i

### ScaleType Enumeration

The type of calibration scale.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum ScaleType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Polynomial | 0 | A polynomial scale. This type provides up to a fourth order scale. |
| Thermocouple | 1 | A thermocouple scale, which converts volts to temperature. |
| None | 2 | No scale is applied. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-debug.html language=enus -->
## TOPIC 00617: Debug

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-debug.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-debug.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the sequence executes in debug mode. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool Debug { get; set; }

### Debug

Gets or sets whether the sequence executes in debug mode.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool Debug { get; set; }

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-groupnumber.html language=enus -->
## TOPIC 00618: GroupNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-groupnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-groupnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the groupNumber. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic int GroupNumber { get; set; }

### GroupNumber

Gets or sets the groupNumber.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public int GroupNumber { get; set; }

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-parameterassignments.html language=enus -->
## TOPIC 00619: ParameterAssignments

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-parameterassignments.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-parameterassignments.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the parameter assignments for the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceParameterAssignmentInfo[] ParameterAssignments { get; set; }

### ParameterAssignments

Gets or sets the parameter assignments for the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [SequenceParameterAssignmentInfo](nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo.html)[] ParameterAssignments { get; set; }

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-sequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-int.html language=enus -->
## TOPIC 00620: SequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-sequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-sequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SequenceCallInfo with a group. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout, int GroupNumber)ParametersNameTypeDescr

### SequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, int)

Initializes a new instance of [SequenceCallInfo](nationalinstruments-veristand-clientapi-sequencecallinfo.html) with a group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public SequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout, int GroupNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| SequencePath | string | The file path of the sequence file to execute. |
| Target | string | The name of the target on which to execute the sequence. |
| ParameterAssignments | SequenceParameterAssignmentInfo[] | The parameter assignments for the sequence. |
| Debug | bool | Whether the sequence executes in debug mode. |
| Timeout | double | The timeout in milliseconds within which the sequence must complete each time step. |
| GroupNumber | int | Specifies the group number of the sequence |

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-sequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double.html language=enus -->
## TOPIC 00621: SequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-sequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-sequencecallinfo__string-string-sequenceparameterassignmentinfo_arr1-bool-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SequenceCallInfo. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout)ParametersNameTypeDescriptionSequencePathstringThe fi

### SequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double)

Initializes a new instance of [SequenceCallInfo](nationalinstruments-veristand-clientapi-sequencecallinfo.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public SequenceCallInfo(string SequencePath, string Target, SequenceParameterAssignmentInfo[] ParameterAssignments, bool Debug, double Timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| SequencePath | string | The file path of the sequence file to execute. |
| Target | string | The name of the target on which to execute the sequence. |
| ParameterAssignments | SequenceParameterAssignmentInfo[] | The parameter assignments for the sequence. |
| Debug | bool | Whether the sequence executes in debug mode. |
| Timeout | double | The timeout in milliseconds within which the sequence must complete each time step. |

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-sequencepath.html language=enus -->
## TOPIC 00622: SequencePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-sequencepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-sequencepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the file path of the sequence file to execute. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string SequencePath { get; set; }

### SequencePath

Gets or sets the file path of the sequence file to execute.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string SequencePath { get; set; }

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-target.html language=enus -->
## TOPIC 00623: Target

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the target on which to execute the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Target { get; set; }

### Target

Gets or sets the name of the target on which to execute the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Target { get; set; }

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo-timeout.html language=enus -->
## TOPIC 00624: Timeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo-timeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo-timeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the timeout in milliseconds within which the sequence must complete a time step. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic double Timeout { get; set; }

### Timeout

Gets or sets the timeout in milliseconds within which the sequence must complete a time step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public double Timeout { get; set; }

Parent topic:

SequenceCallInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecallinfo.html language=enus -->
## TOPIC 00625: SequenceCallInfo Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecallinfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecallinfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides information about a stimulus profile sequence. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class SequenceCallInfoConstructorsNameDescriptionSequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, int)Initializes a new instance of

### SequenceCallInfo Class

Provides information about a stimulus profile sequence.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class SequenceCallInfo

#### Constructors

| Name | Description |
| --- | --- |
| SequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double, int) | Initializes a new instance of SequenceCallInfo with a group. |
| SequenceCallInfo(string, string, SequenceParameterAssignmentInfo[], bool, double) | Initializes a new instance of SequenceCallInfo. |

#### Properties

| Name | Description |
| --- | --- |
| Debug | Gets or sets whether the sequence executes in debug mode. |
| GroupNumber | Gets or sets the groupNumber. |
| ParameterAssignments | Gets or sets the parameter assignments for the sequence. |
| SequencePath | Gets or sets the file path of the sequence file to execute. |
| Target | Gets or sets the name of the target on which to execute the sequence. |
| Timeout | Gets or sets the timeout in milliseconds within which the sequence must complete a time step. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecompleteeventargs-aborted.html language=enus -->
## TOPIC 00626: Aborted

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecompleteeventargs-aborted.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecompleteeventargs-aborted.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the sequence execution was aborted. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool Aborted { get; }

### Aborted

Gets whether the sequence execution was aborted.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool Aborted { get; }

Parent topic:

SequenceCompleteEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecompleteeventargs-error.html language=enus -->
## TOPIC 00627: Error

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecompleteeventargs-error.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecompleteeventargs-error.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the final error state of the sequence execution. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic Error Error { get; }

### Error

Gets the final error state of the sequence execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public Error Error { get; }

Parent topic:

SequenceCompleteEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecompleteeventargs-returnvalue.html language=enus -->
## TOPIC 00628: ReturnValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecompleteeventargs-returnvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecompleteeventargs-returnvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the return value for the completed sequence. Return values generally indicate some type of pass/fail information, and can be any data type. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DataValue ReturnValue { get; }

### ReturnValue

Gets the return value for the completed sequence. Return values generally indicate some type of pass/fail information, and can be any data type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DataValue](nationalinstruments-veristand-data-datavalue.html) ReturnValue { get; }

Parent topic:

SequenceCompleteEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecompleteeventargs-sequencecompleteeventargs__datavalue-bool-error.html language=enus -->
## TOPIC 00629: SequenceCompleteEventArgs(DataValue, bool, Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecompleteeventargs-sequencecompleteeventargs__datavalue-bool-error.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecompleteeventargs-sequencecompleteeventargs__datavalue-bool-error.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SequenceCompleteEventArgs with the specified ReturnValue . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceCompleteEventArgs(DataValue ReturnValue, bool Aborted, Error Error)ParametersNameTypeDescriptionReturnValueDataValueThe final return value f

### SequenceCompleteEventArgs(DataValue, bool, Error)

Initializes a new instance of [SequenceCompleteEventArgs](nationalinstruments-veristand-clientapi-sequencecompleteeventargs.html) with the specified *ReturnValue* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public SequenceCompleteEventArgs(DataValue ReturnValue, bool Aborted, Error Error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ReturnValue | DataValue | The final return value for the sequence. |
| Aborted | bool | Whether the sequence was aborted prematurely. |
| Error | Error | The final error state of the sequence execution. |

Parent topic:

SequenceCompleteEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencecompleteeventargs.html language=enus -->
## TOPIC 00630: SequenceCompleteEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencecompleteeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencecompleteeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event data returned when a sequence completes execution. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class SequenceCompleteEventArgs : EventArgsConstructorsNameDescriptionSequenceCompleteEventArgs(DataValue, bool, Error)Initializes a new instance of SequenceCo

### SequenceCompleteEventArgs Class

Event data returned when a sequence completes execution.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class SequenceCompleteEventArgs : EventArgs

#### Constructors

| Name | Description |
| --- | --- |
| SequenceCompleteEventArgs(DataValue, bool, Error) | Initializes a new instance of SequenceCompleteEventArgs with the specified ReturnValue . |

#### Properties

| Name | Description |
| --- | --- |
| Aborted | Gets whether the sequence execution was aborted. |
| Error | Gets the final error state of the sequence execution. |
| ReturnValue | Gets the return value for the completed sequence. Return values generally indicate some type of pass/fail information, and can be any data type. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-parametername.html language=enus -->
## TOPIC 00631: ParameterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-parametername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-parametername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the parameter. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string ParameterName { get; }

### ParameterName

Gets the name of the parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string ParameterName { get; }

Parent topic:

SequenceParameterAssignmentInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-sequenceparameterassignmentinfo__string-dataresource.html language=enus -->
## TOPIC 00632: SequenceParameterAssignmentInfo(string, DataResource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-sequenceparameterassignmentinfo__string-dataresource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-sequenceparameterassignmentinfo__string-dataresource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SequenceParameterAssignmentInfo with the specified ParameterName and Value . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceParameterAssignmentInfo(string ParameterName, DataResource Value)ParametersNameTypeDescriptionParameterNamestringThe name

### SequenceParameterAssignmentInfo(string, DataResource)

Initializes a new instance of [SequenceParameterAssignmentInfo](nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo.html) with the specified *ParameterName*  and *Value* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public SequenceParameterAssignmentInfo(string ParameterName, DataResource Value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | string | The name of the parameter. |
| Value | DataResource | The value of the parameter. |

Parent topic:

SequenceParameterAssignmentInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-value.html language=enus -->
## TOPIC 00633: Value

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo-value.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the parameter. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic DataResource Value { get; }

### Value

Gets the value of the parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [DataResource](nationalinstruments-veristand-data-dataresource.html) Value { get; }

Parent topic:

SequenceParameterAssignmentInfo Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo.html language=enus -->
## TOPIC 00634: SequenceParameterAssignmentInfo Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequenceparameterassignmentinfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides information about an input parameter of a real-time sequence. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class SequenceParameterAssignmentInfoConstructorsNameDescriptionSequenceParameterAssignmentInfo(string, DataResource)Initializes a new instance of Seq

### SequenceParameterAssignmentInfo Class

Provides information about an input parameter of a real-time sequence.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class SequenceParameterAssignmentInfo

#### Constructors

| Name | Description |
| --- | --- |
| SequenceParameterAssignmentInfo(string, DataResource) | Initializes a new instance of SequenceParameterAssignmentInfo with the specified ParameterName and Value . |

#### Properties

| Name | Description |
| --- | --- |
| ParameterName | Gets the name of the parameter. |
| Value | Gets the value of the parameter. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencestate.html language=enus -->
## TOPIC 00635: SequenceState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencestate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencestate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The execution state of a sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum SequenceStateMembersNameValueDescriptionIdle0The sequence is idle, and has not run. Running1The sequence is running. SingleStepping2The sequence is single-stepping. Paused3The sequence is paused. S

### SequenceState Enumeration

The execution state of a sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum SequenceState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Idle | 0 | The sequence is idle, and has not run. |
| Running | 1 | The sequence is running. |
| SingleStepping | 2 | The sequence is single-stepping. |
| Paused | 3 | The sequence is paused. |
| Stopped | 4 | The sequence has stopped executing. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-aborted.html language=enus -->
## TOPIC 00636: aborted

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-aborted.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-aborted.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether sequence execution is aborted. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool aborted { get; }

### aborted

Gets whether sequence execution is aborted.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool aborted { get; }

Parent topic:

SequenceStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-sequencestatechangeeventargs__sequencestate-bool.html language=enus -->
## TOPIC 00637: SequenceStateChangeEventArgs(SequenceState, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-sequencestatechangeeventargs__sequencestate-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-sequencestatechangeeventargs__sequencestate-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SequenceStateChangeEventArgs. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceStateChangeEventArgs(SequenceState state, bool aborted)ParametersNameTypeDescriptionstateSequenceStateGets the execution SequenceState of the sequence.abortedboolGets wh

### SequenceStateChangeEventArgs(SequenceState, bool)

Initializes a new instance of [SequenceStateChangeEventArgs](nationalinstruments-veristand-clientapi-sequencestatechangeeventargs.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public SequenceStateChangeEventArgs(SequenceState state, bool aborted)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| state | SequenceState | Gets the execution SequenceState of the sequence. |
| aborted | bool | Gets whether sequence execution is aborted. |

Parent topic:

SequenceStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-state.html language=enus -->
## TOPIC 00638: state

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-state.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencestatechangeeventargs-state.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the execution SequenceState of the sequence. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic SequenceState state { get; }

### state

Gets the execution [SequenceState](nationalinstruments-veristand-clientapi-sequencestate.html) of the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [SequenceState](nationalinstruments-veristand-clientapi-sequencestate.html) state { get; }

Parent topic:

SequenceStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-sequencestatechangeeventargs.html language=enus -->
## TOPIC 00639: SequenceStateChangeEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-sequencestatechangeeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-sequencestatechangeeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event data returned when the execution state of a real-time sequence changes. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class SequenceStateChangeEventArgs : EventArgsConstructorsNameDescriptionSequenceStateChangeEventArgs(SequenceState, bool)Initializes a ne

### SequenceStateChangeEventArgs Class

Event data returned when the execution state of a real-time sequence changes.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class SequenceStateChangeEventArgs : EventArgs

#### Constructors

| Name | Description |
| --- | --- |
| SequenceStateChangeEventArgs(SequenceState, bool) | Initializes a new instance of SequenceStateChangeEventArgs. |

#### Properties

| Name | Description |
| --- | --- |
| aborted | Gets whether sequence execution is aborted. |
| state | Gets the execution SequenceState of the sequence. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-servercreateoptions-hidegettingstartedwindow.html language=enus -->
## TOPIC 00640: HideGettingStartedWindow

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-servercreateoptions-hidegettingstartedwindow.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-servercreateoptions-hidegettingstartedwindow.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether the server should show the getting started window when a project is not active. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool HideGettingStartedWindow { get; set; }

### HideGettingStartedWindow

Whether the server should show the getting started window when a project is not active.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool HideGettingStartedWindow { get; set; }

Parent topic:

ServerCreateOptions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-servercreateoptions-shutdownserveronprocessexit.html language=enus -->
## TOPIC 00641: ShutDownServerOnProcessExit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-servercreateoptions-shutdownserveronprocessexit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-servercreateoptions-shutdownserveronprocessexit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether the server process should shutdown when the process that starts it exits. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic bool ShutDownServerOnProcessExit { get; set; }

### ShutDownServerOnProcessExit

Whether the server process should shutdown when the process that starts it exits.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public bool ShutDownServerOnProcessExit { get; set; }

Parent topic:

ServerCreateOptions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-servercreateoptions.html language=enus -->
## TOPIC 00642: ServerCreateOptions Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-servercreateoptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-servercreateoptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Options for starting the VeriStand server. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class ServerCreateOptionsPropertiesNameDescriptionHideGettingStartedWindowWhether the server should show the getting started window when a project is not active. ShutDownServerOn

### ServerCreateOptions Class

Options for starting the VeriStand server.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class ServerCreateOptions

#### Properties

| Name | Description |
| --- | --- |
| HideGettingStartedWindow | Whether the server should show the getting started window when a project is not active. |
| ShutDownServerOnProcessExit | Whether the server process should shutdown when the process that starts it exits. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-stimulusresult.html language=enus -->
## TOPIC 00643: StimulusResult Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-stimulusresult.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-stimulusresult.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The result of stimulus generation. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum StimulusResultMembersNameValueDescriptionNone0No result available. Passed1Stimulus generation passed. Failed2Stimulus generation failed. Error3Stimulus generation returned an error.

### StimulusResult Enumeration

The result of stimulus generation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum StimulusResult

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No result available. |
| Passed | 1 | Stimulus generation passed. |
| Failed | 2 | Stimulus generation failed. |
| Error | 3 | Stimulus generation returned an error. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-stimulusstate.html language=enus -->
## TOPIC 00644: StimulusState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-stimulusstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-stimulusstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The state of the stimulus profile manager. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum StimulusStateMembersNameValueDescriptionStopped0The stimulus profile manager is stopped. Starting1The stimulus profile manager is starting. Running2The stimulus profile manager is running.

### StimulusState Enumeration

The state of the stimulus profile manager.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum StimulusState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Stopped | 0 | The stimulus profile manager is stopped. |
| Starting | 1 | The stimulus profile manager is starting. |
| Running | 2 | The stimulus profile manager is running. |
| Stopping | 3 | The stimulus profile manager is stopping. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-systemstate.html language=enus -->
## TOPIC 00645: SystemState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-systemstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-systemstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The current state of the system to which the VeriStand Gateway is connected. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum SystemStateMembersNameValueDescriptionIdle0A configuration file is loaded but not running. Active1A configuration is running.

### SystemState Enumeration

The current state of the system to which the VeriStand Gateway is connected.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum SystemState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Idle | 0 | A configuration file is loaded but not running. |
| Active | 1 | A configuration is running. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-targetstate.html language=enus -->
## TOPIC 00646: TargetState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-targetstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-targetstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The current state of the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum TargetStateMembersNameValueDescriptionDisconnected0The target is not connected. Running1The target is connected and running a system definition. Idle2The target is connected but not running a system

### TargetState Enumeration

The current state of the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum TargetState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disconnected | 0 | The target is not connected. |
| Running | 1 | The target is connected and running a system definition. |
| Idle | 2 | The target is connected but not running a system definition. |
| Disabled | 3 | The target is disabled in the system definition. |
| Connecting | 4 | The gateway is establishing a connection to the target. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-targetstatechangeeventargs-target.html language=enus -->
## TOPIC 00647: Target

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-targetstatechangeeventargs-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-targetstatechangeeventargs-target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the name of the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic string Target { get; }

### Target

Gets a value indicating the name of the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public string Target { get; }

Parent topic:

TargetStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-targetstatechangeeventargs-targetstate.html language=enus -->
## TOPIC 00648: TargetState

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-targetstatechangeeventargs-targetstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-targetstatechangeeventargs-targetstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the current state of the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic TargetState TargetState { get; }

### TargetState

Gets a value indicating the current state of the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public [TargetState](nationalinstruments-veristand-clientapi-targetstate.html) TargetState { get; }

Parent topic:

TargetStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-targetstatechangeeventargs-targetstatechangeeventargs__string-targetstate.html language=enus -->
## TOPIC 00649: TargetStateChangeEventArgs(string, TargetState)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-targetstatechangeeventargs-targetstatechangeeventargs__string-targetstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-targetstatechangeeventargs-targetstatechangeeventargs__string-targetstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TargetStateChangeEventArgs class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic TargetStateChangeEventArgs(string target, TargetState state)ParametersNameTypeDescriptiontargetstringName of the targetstateTargetStateState of the target

### TargetStateChangeEventArgs(string, TargetState)

Initializes a new instance of the TargetStateChangeEventArgs class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public TargetStateChangeEventArgs(string target, TargetState state)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | string | Name of the target |
| state | TargetState | State of the target |

Parent topic:

TargetStateChangeEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-targetstatechangeeventargs.html language=enus -->
## TOPIC 00650: TargetStateChangeEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-targetstatechangeeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-targetstatechangeeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data about target state change event. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic class TargetStateChangeEventArgs : EventArgsConstructorsNameDescriptionTargetStateChangeEventArgs(string, TargetState)Initializes a new instance of the TargetStateChange

### TargetStateChangeEventArgs Class

Provides data about target state change event.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public class TargetStateChangeEventArgs : EventArgs

#### Constructors

| Name | Description |
| --- | --- |
| TargetStateChangeEventArgs(string, TargetState) | Initializes a new instance of the TargetStateChangeEventArgs class. |

#### Properties

| Name | Description |
| --- | --- |
| Target | Gets a value indicating the name of the target. |
| TargetState | Gets a value indicating the current state of the target. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-temperatureunits.html language=enus -->
## TOPIC 00651: TemperatureUnits Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-temperatureunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-temperatureunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The temperature units to use for thermocouple calibration. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum TemperatureUnitsMembersNameValueDescriptionC0Celsius. F1Fahrenheit. K2Kelvin. R3Rankine.

### TemperatureUnits Enumeration

The temperature units to use for thermocouple calibration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum TemperatureUnits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| C | 0 | Celsius. |
| F | 1 | Fahrenheit. |
| K | 2 | Kelvin. |
| R | 3 | Rankine. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-thermocoupletype.html language=enus -->
## TOPIC 00652: ThermocoupleType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-thermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-thermocoupletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The type of thermocouple to use for thermocouple calibration. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPIpublic enum ThermocoupleTypeMembersNameValueDescriptionB0Type B. E1Type E. J2Type J. K3Type K. R4Type R. S5Type S. T6Type T. N7Type N.

### ThermocoupleType Enumeration

The type of thermocouple to use for thermocouple calibration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI](nationalinstruments-veristand-clientapi.html)

public enum ThermocoupleType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| B | 0 | Type B. |
| E | 1 | Type E. |
| J | 2 | Type J. |
| K | 3 | Type K. |
| R | 4 | Type R. |
| S | 5 | Type S. |
| T | 6 | Type T. |
| N | 7 | Type N. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-getwaveformdtvalues__string_arr1-out.html language=enus -->
## TOPIC 00653: GetWaveformDtValues(string[], out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-getwaveformdtvalues__string_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-getwaveformdtvalues__string_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the dt values for multiple waveforms from the target. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Error GetWaveformDtValues(string[] waveformPaths, out double[] dtValues)ParametersNameTypeDescriptionwaveformPathsstring[]Paths of waveforms to query the dt fro

### GetWaveformDtValues(string[], out double[])

Gets the dt values for multiple waveforms from the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) GetWaveformDtValues(string[] waveformPaths, out double[] dtValues)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformPaths | string[] | Paths of waveforms to query the dt from |
| dtValues | out double[] | Time delta between samples for each of the specified waveform paths. If the waveform has not been published in the engine, the value will be NaN. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWaveformStreaming Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-registerforcdbwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatacdbeventargs..html language=enus -->
## TOPIC 00654: RegisterForCDBWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataCDBEventArgs >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-registerforcdbwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatacdbeventargs..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-registerforcdbwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatacdbeventargs..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers a delegate to receive data defined by waveform stream specifications. Waveforms must be of complex double data type. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Error RegisterForCDBWaveformData(WaveformStreamSpecification[] waveformStreamSpecifications,

### RegisterForCDBWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataCDBEventArgs >)

Registers a delegate to receive data defined by waveform stream specifications. Waveforms must be of complex double data type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RegisterForCDBWaveformData(WaveformStreamSpecification[] waveformStreamSpecifications, EventHandler< WaveformDataCDBEventArgs > eventHandler)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Waveform stream specifications associated with delegate. Must specify waveforms of double data type. |
| eventHandler | EventHandler< WaveformDataCDBEventArgs > | Delegate function to be called when the event is raised. |

#### Returns

Error indicating whether registration was successful.

Parent topic:

IWaveformStreaming Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-registerfordblwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatadbleventargs..html language=enus -->
## TOPIC 00655: RegisterForDBLWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataDBLEventArgs >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-registerfordblwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatadbleventargs..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-registerfordblwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatadbleventargs..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers a delegate to receive data defined by waveform stream specifications. Waveforms must be of double data type. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Error RegisterForDBLWaveformData(WaveformStreamSpecification[] waveformStreamSpecifications, EventHa

### RegisterForDBLWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataDBLEventArgs >)

Registers a delegate to receive data defined by waveform stream specifications. Waveforms must be of double data type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) RegisterForDBLWaveformData(WaveformStreamSpecification[] waveformStreamSpecifications, EventHandler< WaveformDataDBLEventArgs > eventHandler)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Waveform stream specifications associated with delegate. Must specify waveforms of double data type. |
| eventHandler | EventHandler< WaveformDataDBLEventArgs > | Delegate function to be called when the event is raised. |

#### Returns

Error indicating whether registration was successful.

Parent topic:

IWaveformStreaming Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-startstreamingwaveforms__waveformstreamspecification_arr1.html language=enus -->
## TOPIC 00656: StartStreamingWaveforms(WaveformStreamSpecification[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-startstreamingwaveforms__waveformstreamspecification_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-startstreamingwaveforms__waveformstreamspecification_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts waveform streaming for the given waveform stream specifications. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Error StartStreamingWaveforms(WaveformStreamSpecification[] waveformStreamSpecifications)ParametersNameTypeDescriptionwaveformStreamSpecificationsW

### StartStreamingWaveforms(WaveformStreamSpecification[])

Starts waveform streaming for the given waveform stream specifications.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) StartStreamingWaveforms(WaveformStreamSpecification[] waveformStreamSpecifications)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Specifies the settings of the waveform streams. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWaveformStreaming Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-stopstreamingwaveforms__waveformstreamspecification_arr1.html language=enus -->
## TOPIC 00657: StopStreamingWaveforms(WaveformStreamSpecification[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-stopstreamingwaveforms__waveformstreamspecification_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-stopstreamingwaveforms__waveformstreamspecification_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops waveform streaming for the given waveform stream specifications. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Error StopStreamingWaveforms(WaveformStreamSpecification[] waveformStreamSpecifications)ParametersNameTypeDescriptionwaveformStreamSpecificationsWav

### StopStreamingWaveforms(WaveformStreamSpecification[])

Stops waveform streaming for the given waveform stream specifications.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) StopStreamingWaveforms(WaveformStreamSpecification[] waveformStreamSpecifications)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Specifies the settings of the waveform streams. |

#### Returns

Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0.

Parent topic:

IWaveformStreaming Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-unregisterforcdbwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatacdbeventargs..html language=enus -->
## TOPIC 00658: UnregisterForCDBWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataCDBEventArgs >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-unregisterforcdbwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatacdbeventargs..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-unregisterforcdbwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatacdbeventargs..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters a delegate to receive data defined by waveform stream specifications. Waveforms must be of complex double data type. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Error UnregisterForCDBWaveformData(WaveformStreamSpecification[] waveformStreamSpecificati

### UnregisterForCDBWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataCDBEventArgs >)

Unregisters a delegate to receive data defined by waveform stream specifications. Waveforms must be of complex double data type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) UnregisterForCDBWaveformData(WaveformStreamSpecification[] waveformStreamSpecifications, EventHandler< WaveformDataCDBEventArgs > eventHandler)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Waveform stream specifications to no longer associate with delegate. Must specify waveforms of double data type. |
| eventHandler | EventHandler< WaveformDataCDBEventArgs > | Delegate function that was registered to the event. |

#### Returns

Error indicating whether unregistration was successful.

Parent topic:

IWaveformStreaming Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-unregisterfordblwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatadbleventargs..html language=enus -->
## TOPIC 00659: UnregisterForDBLWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataDBLEventArgs >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-unregisterfordblwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatadbleventargs..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming-unregisterfordblwaveformdata__waveformstreamspecification_arr1-eventhandler_waveformdatadbleventargs..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters a delegate to receive data defined by waveform stream specifications. Waveforms must be of double data type. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Error UnregisterForDBLWaveformData(WaveformStreamSpecification[] waveformStreamSpecifications, Eve

### UnregisterForDBLWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataDBLEventArgs >)

Unregisters a delegate to receive data defined by waveform stream specifications. Waveforms must be of double data type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [Error](nationalinstruments-veristand-clientapi-stimulusresult.html) UnregisterForDBLWaveformData(WaveformStreamSpecification[] waveformStreamSpecifications, EventHandler< WaveformDataDBLEventArgs > eventHandler)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Waveform stream specifications to no longer associate with delegate. Must specify waveforms of double data type. |
| eventHandler | EventHandler< WaveformDataDBLEventArgs > | Delegate function that was registered to the event. |

#### Returns

Error indicating whether unregistration was successful.

Parent topic:

IWaveformStreaming Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming.html language=enus -->
## TOPIC 00660: IWaveformStreaming Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an interface to stream waveform data from the VeriStand gateway. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic interface IWaveformStreamingMethodsNameDescriptionGetWaveformDtValues(string[], out double[])Gets the dt values for multiple wav

### IWaveformStreaming Interface

Specifies an interface to stream waveform data from the VeriStand gateway.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public interface IWaveformStreaming

#### Methods

| Name | Description |
| --- | --- |
| GetWaveformDtValues(string[], out double[]) | Gets the dt values for multiple waveforms from the target. |
| RegisterForCDBWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataCDBEventArgs >) | Registers a delegate to receive data defined by waveform stream specifications. Waveforms must be of complex double data type. |
| RegisterForDBLWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataDBLEventArgs >) | Registers a delegate to receive data defined by waveform stream specifications. Waveforms must be of double data type. |
| StartStreamingWaveforms(WaveformStreamSpecification[]) | Starts waveform streaming for the given waveform stream specifications. |
| StopStreamingWaveforms(WaveformStreamSpecification[]) | Stops waveform streaming for the given waveform stream specifications. |
| UnregisterForCDBWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataCDBEventArgs >) | Unregisters a delegate to receive data defined by waveform stream specifications. Waveforms must be of complex double data type. |
| UnregisterForDBLWaveformData(WaveformStreamSpecification[], EventHandler< WaveformDataDBLEventArgs >) | Unregisters a delegate to receive data defined by waveform stream specifications. Waveforms must be of double data type. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-equals__streamalldata.html language=enus -->
## TOPIC 00661: Equals(StreamAllData)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-equals__streamalldata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-equals__streamalldata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamAllData. Equivalency is determined using the properties of the StreamAllData. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool Equals(StreamAllData other)ParametersNameTypeDes

### Equals(StreamAllData)

Determines whether the specified *other*  object is equal to the current instance of [StreamAllData](nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html). Equivalency is determined using the properties of the [StreamAllData](nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool Equals(StreamAllData other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | StreamAllData | The StreamAllData object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

StreamAllData Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-equals__waveformstreamcondition.html language=enus -->
## TOPIC 00662: Equals(WaveformStreamCondition)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-equals__waveformstreamcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-equals__waveformstreamcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamAllData. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override bool Equals(WaveformStreamCondition other)RemarksThe StreamAllData type inherits from WaveformStreamCondition. Pa

### Equals(WaveformStreamCondition)

Determines whether the specified *other*  object is equal to the current instance of [StreamAllData](nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override bool Equals(WaveformStreamCondition other)

#### Remarks

The [StreamAllData](nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html) type inherits from [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | WaveformStreamCondition | The WaveformStreamCondition object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [StreamAllData](nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html). Otherwise, false.

Parent topic:

StreamAllData Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-gethashcode.html language=enus -->
## TOPIC 00663: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a StreamAllData object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override int GetHashCode()RemarksOverrides object.

### GetHashCode()

Serves as a hash function for a [StreamAllData](nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [StreamAllData](nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html) object.

Parent topic:

StreamAllData Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-streamalldata.html language=enus -->
## TOPIC 00664: StreamAllData()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-streamalldata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata-streamalldata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the StreamAllData class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic StreamAllData()

### StreamAllData()

Initializes a new instance of the StreamAllData class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public StreamAllData()

Parent topic:

StreamAllData Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html language=enus -->
## TOPIC 00665: StreamAllData Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamalldata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a stream condition that is always true. Derives fromWaveformStreamConditionIEquatable< StreamAllData >SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class StreamAllData : WaveformStreamCondition, IEquatable< StreamAllData >ConstructorsNameDescriptionStream

### StreamAllData Class

Specifies a stream condition that is always true.

#### Derives from

- WaveformStreamCondition
- IEquatable< StreamAllData >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class StreamAllData : WaveformStreamCondition, IEquatable< StreamAllData >

#### Constructors

| Name | Description |
| --- | --- |
| StreamAllData() | Initializes a new instance of the StreamAllData class. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(WaveformStreamCondition) | Determines whether the specified other object is equal to the current instance of StreamAllData. |
| Equals(StreamAllData) | Determines whether the specified other object is equal to the current instance of StreamAllData. Equivalency is determined using the properties of the StreamAllData. |
| GetHashCode() | Serves as a hash function for a StreamAllData object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-equals__streamfirstnseconds.html language=enus -->
## TOPIC 00666: Equals(StreamFirstNSeconds)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-equals__streamfirstnseconds.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-equals__streamfirstnseconds.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamFirstNSeconds. Equivalency is determined using the properties of the StreamFirstNSeconds. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool Equals(StreamFirstNSeconds other)Par

### Equals(StreamFirstNSeconds)

Determines whether the specified *other*  object is equal to the current instance of [StreamFirstNSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html). Equivalency is determined using the properties of the [StreamFirstNSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool Equals(StreamFirstNSeconds other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | StreamFirstNSeconds | The StreamFirstNSeconds object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

StreamFirstNSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-equals__waveformstreamcondition.html language=enus -->
## TOPIC 00667: Equals(WaveformStreamCondition)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-equals__waveformstreamcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-equals__waveformstreamcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamFirstNSeconds. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override bool Equals(WaveformStreamCondition other)RemarksThe StreamFirstNSeconds type inherits from WaveformStreamC

### Equals(WaveformStreamCondition)

Determines whether the specified *other*  object is equal to the current instance of [StreamFirstNSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override bool Equals(WaveformStreamCondition other)

#### Remarks

The [StreamFirstNSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html) type inherits from [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | WaveformStreamCondition | The WaveformStreamCondition object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [StreamFirstNSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html). Otherwise, false.

Parent topic:

StreamFirstNSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-gethashcode.html language=enus -->
## TOPIC 00668: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a StreamFirstNSeconds object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override int GetHashCode()RemarksOverrides o

### GetHashCode()

Serves as a hash function for a [StreamFirstNSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [StreamFirstNSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html) object.

Parent topic:

StreamFirstNSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-nseconds.html language=enus -->
## TOPIC 00669: NSeconds

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-nseconds.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-nseconds.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the N seconds after waveform start the condition is true. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double NSeconds { get; set; }

### NSeconds

Gets or sets a value indicating the N seconds after waveform start the condition is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double NSeconds { get; set; }

Parent topic:

StreamFirstNSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-streamfirstnseconds__double.html language=enus -->
## TOPIC 00670: StreamFirstNSeconds(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-streamfirstnseconds__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds-streamfirstnseconds__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the StreamFirstNSeconds class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic StreamFirstNSeconds(double nSeconds)ParametersNameTypeDescriptionnSecondsdoubleLength in seconds after the waveform starts that this stream condition is true

### StreamFirstNSeconds(double)

Initializes a new instance of the StreamFirstNSeconds class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public StreamFirstNSeconds(double nSeconds)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nSeconds | double | Length in seconds after the waveform starts that this stream condition is true |

Parent topic:

StreamFirstNSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html language=enus -->
## TOPIC 00671: StreamFirstNSeconds Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamfirstnseconds.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a waveform streaming condition that is true during the first N seconds of waveform data after the waveform starts. Derives fromWaveformStreamConditionIEquatable< StreamFirstNSeconds >SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class StreamFirstNSeconds

### StreamFirstNSeconds Class

Specifies a waveform streaming condition that is true during the first N seconds of waveform data after the waveform starts.

#### Derives from

- WaveformStreamCondition
- IEquatable< StreamFirstNSeconds >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class StreamFirstNSeconds : WaveformStreamCondition, IEquatable< StreamFirstNSeconds >

#### Constructors

| Name | Description |
| --- | --- |
| StreamFirstNSeconds(double) | Initializes a new instance of the StreamFirstNSeconds class. |

#### Properties

| Name | Description |
| --- | --- |
| NSeconds | Gets or sets a value indicating the N seconds after waveform start the condition is true. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(WaveformStreamCondition) | Determines whether the specified other object is equal to the current instance of StreamFirstNSeconds. |
| Equals(StreamFirstNSeconds) | Determines whether the specified other object is equal to the current instance of StreamFirstNSeconds. Equivalency is determined using the properties of the StreamFirstNSeconds. |
| GetHashCode() | Serves as a hash function for a StreamFirstNSeconds object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-equals__streaminrangedbl.html language=enus -->
## TOPIC 00672: Equals(StreamInRangeDBL)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-equals__streaminrangedbl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-equals__streaminrangedbl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamInRangeDBL. Equivalency is determined using the properties of the StreamInRangeDBL. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool Equals(StreamInRangeDBL other)ParametersNa

### Equals(StreamInRangeDBL)

Determines whether the specified *other*  object is equal to the current instance of [StreamInRangeDBL](nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html). Equivalency is determined using the properties of the [StreamInRangeDBL](nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool Equals(StreamInRangeDBL other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | StreamInRangeDBL | The StreamInRangeDBL object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

StreamInRangeDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-equals__waveformstreamcondition.html language=enus -->
## TOPIC 00673: Equals(WaveformStreamCondition)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-equals__waveformstreamcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-equals__waveformstreamcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamInRangeDBL. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override bool Equals(WaveformStreamCondition other)RemarksThe StreamInRangeDBL type inherits from WaveformStreamConditi

### Equals(WaveformStreamCondition)

Determines whether the specified *other*  object is equal to the current instance of [StreamInRangeDBL](nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override bool Equals(WaveformStreamCondition other)

#### Remarks

The [StreamInRangeDBL](nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html) type inherits from [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | WaveformStreamCondition | The WaveformStreamCondition object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [StreamInRangeDBL](nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html). Otherwise, false.

Parent topic:

StreamInRangeDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-gethashcode.html language=enus -->
## TOPIC 00674: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a StreamInRangeDBL object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override int GetHashCode()RemarksOverrides obje

### GetHashCode()

Serves as a hash function for a [StreamInRangeDBL](nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [StreamInRangeDBL](nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html) object.

Parent topic:

StreamInRangeDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-highlimit.html language=enus -->
## TOPIC 00675: HighLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-highlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-highlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the high limit value of the waveform stream condition. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double HighLimit { get; set; }

### HighLimit

Gets or sets a value indicating the high limit value of the waveform stream condition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double HighLimit { get; set; }

Parent topic:

StreamInRangeDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-invert.html language=enus -->
## TOPIC 00676: Invert

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-invert.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-invert.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to invert the range check. If the range check is inverted, then the stream condition occurs when the value falls outside the specified range. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool Invert { get; set; }

### Invert

Gets or sets a value indicating whether to invert the range check. If the range check is inverted, then the stream condition occurs when the value falls outside the specified range.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool Invert { get; set; }

Parent topic:

StreamInRangeDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-lowlimit.html language=enus -->
## TOPIC 00677: LowLimit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-lowlimit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-lowlimit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the low limit value of the waveform stream condition. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double LowLimit { get; set; }

### LowLimit

Gets or sets a value indicating the low limit value of the waveform stream condition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double LowLimit { get; set; }

Parent topic:

StreamInRangeDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-streaminrangedbl__double-double-bool.html language=enus -->
## TOPIC 00678: StreamInRangeDBL(double, double, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-streaminrangedbl__double-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl-streaminrangedbl__double-double-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the StreamInRangeDBL class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic StreamInRangeDBL(double highLimit, double lowLimit, bool invert)ParametersNameTypeDescriptionhighLimitdoubleSpecifies the highest value that the waveform data ca

### StreamInRangeDBL(double, double, bool)

Initializes a new instance of the StreamInRangeDBL class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public StreamInRangeDBL(double highLimit, double lowLimit, bool invert)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| highLimit | double | Specifies the highest value that the waveform data can be for the stream condition to be true. |
| lowLimit | double | Specifies the lowest value that the waveform data can be for the stream condition to be true. |
| invert | bool | Specifies if the range check should be inverted. This effectively makes it an out of range condition. |

Parent topic:

StreamInRangeDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html language=enus -->
## TOPIC 00679: StreamInRangeDBL Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streaminrangedbl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a waveform streaming condition for waveforms of Double data type that is true when the data is inside a defined range. Derives fromWaveformStreamConditionIEquatable< StreamInRangeDBL >SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class StreamInRangeDBL :

### StreamInRangeDBL Class

Specifies a waveform streaming condition for waveforms of Double data type that is true when the data is inside a defined range.

#### Derives from

- WaveformStreamCondition
- IEquatable< StreamInRangeDBL >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class StreamInRangeDBL : WaveformStreamCondition, IEquatable< StreamInRangeDBL >

#### Constructors

| Name | Description |
| --- | --- |
| StreamInRangeDBL(double, double, bool) | Initializes a new instance of the StreamInRangeDBL class. |

#### Properties

| Name | Description |
| --- | --- |
| HighLimit | Gets or sets a value indicating the high limit value of the waveform stream condition. |
| Invert | Gets or sets a value indicating whether to invert the range check. If the range check is inverted, then the stream condition occurs when the value falls outside the specified range. |
| LowLimit | Gets or sets a value indicating the low limit value of the waveform stream condition. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(WaveformStreamCondition) | Determines whether the specified other object is equal to the current instance of StreamInRangeDBL. |
| Equals(StreamInRangeDBL) | Determines whether the specified other object is equal to the current instance of StreamInRangeDBL. Equivalency is determined using the properties of the StreamInRangeDBL. |
| GetHashCode() | Serves as a hash function for a StreamInRangeDBL object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-equals__streamnofmseconds.html language=enus -->
## TOPIC 00680: Equals(StreamNOfMSeconds)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-equals__streamnofmseconds.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-equals__streamnofmseconds.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamNOfMSeconds. Equivalency is determined using the properties of the StreamNOfMSeconds. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool Equals(StreamNOfMSeconds other)Parameter

### Equals(StreamNOfMSeconds)

Determines whether the specified *other*  object is equal to the current instance of [StreamNOfMSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html). Equivalency is determined using the properties of the [StreamNOfMSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool Equals(StreamNOfMSeconds other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | StreamNOfMSeconds | The StreamNOfMSeconds object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

StreamNOfMSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-equals__waveformstreamcondition.html language=enus -->
## TOPIC 00681: Equals(WaveformStreamCondition)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-equals__waveformstreamcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-equals__waveformstreamcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StreamNOfMSeconds. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override bool Equals(WaveformStreamCondition other)RemarksThe StreamNOfMSeconds type inherits from WaveformStreamCondi

### Equals(WaveformStreamCondition)

Determines whether the specified *other*  object is equal to the current instance of [StreamNOfMSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override bool Equals(WaveformStreamCondition other)

#### Remarks

The [StreamNOfMSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html) type inherits from [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | WaveformStreamCondition | The WaveformStreamCondition object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [StreamNOfMSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html). Otherwise, false.

Parent topic:

StreamNOfMSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-gethashcode.html language=enus -->
## TOPIC 00682: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a StreamNOfMSeconds object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override int GetHashCode()RemarksOverrides obj

### GetHashCode()

Serves as a hash function for a [StreamNOfMSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [StreamNOfMSeconds](nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html) object.

Parent topic:

StreamNOfMSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-mseconds.html language=enus -->
## TOPIC 00683: MSeconds

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-mseconds.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-mseconds.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the M seconds after waveform start that the N seconds true duration repeats. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double MSeconds { get; set; }

### MSeconds

Gets or sets a value indicating the M seconds after waveform start that the N seconds true duration repeats.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double MSeconds { get; set; }

Parent topic:

StreamNOfMSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-nseconds.html language=enus -->
## TOPIC 00684: NSeconds

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-nseconds.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-nseconds.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the N seconds after waveform start the condition is true. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double NSeconds { get; set; }

### NSeconds

Gets or sets a value indicating the N seconds after waveform start the condition is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double NSeconds { get; set; }

Parent topic:

StreamNOfMSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-streamnofmseconds__double-double.html language=enus -->
## TOPIC 00685: StreamNOfMSeconds(double, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-streamnofmseconds__double-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds-streamnofmseconds__double-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the StreamNOfMSeconds class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic StreamNOfMSeconds(double nSeconds, double mSeconds)ParametersNameTypeDescriptionnSecondsdoubleLength in seconds after the waveform starts that this stream condi

### StreamNOfMSeconds(double, double)

Initializes a new instance of the StreamNOfMSeconds class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public StreamNOfMSeconds(double nSeconds, double mSeconds)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nSeconds | double | Length in seconds after the waveform starts that this stream condition is true |
| mSeconds | double | Length in seconds after the waveform starts to begin repeating the N seconds true duration |

Parent topic:

StreamNOfMSeconds Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html language=enus -->
## TOPIC 00686: StreamNOfMSeconds Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-streamnofmseconds.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a waveform streaming condition that is true during the first N seconds of waveform data after the waveform starts and true again for N seconds after M total seconds have elapsed. Derives fromWaveformStreamConditionIEquatable< StreamNOfMSeconds >SyntaxNamespace: NationalInstruments.VeriStan

### StreamNOfMSeconds Class

Specifies a waveform streaming condition that is true during the first N seconds of waveform data after the waveform starts and true again for N seconds after M total seconds have elapsed.

#### Derives from

- WaveformStreamCondition
- IEquatable< StreamNOfMSeconds >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class StreamNOfMSeconds : WaveformStreamCondition, IEquatable< StreamNOfMSeconds >

#### Constructors

| Name | Description |
| --- | --- |
| StreamNOfMSeconds(double, double) | Initializes a new instance of the StreamNOfMSeconds class. |

#### Properties

| Name | Description |
| --- | --- |
| MSeconds | Gets or sets a value indicating the M seconds after waveform start that the N seconds true duration repeats. |
| NSeconds | Gets or sets a value indicating the N seconds after waveform start the condition is true. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(WaveformStreamCondition) | Determines whether the specified other object is equal to the current instance of StreamNOfMSeconds. |
| Equals(StreamNOfMSeconds) | Determines whether the specified other object is equal to the current instance of StreamNOfMSeconds. Equivalency is determined using the properties of the StreamNOfMSeconds. |
| GetHashCode() | Serves as a hash function for a StreamNOfMSeconds object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs-imaginarydata.html language=enus -->
## TOPIC 00687: ImaginaryData

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs-imaginarydata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs-imaginarydata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the imaginary part of the complex data of the waveform stream. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double[] ImaginaryData { get; }ReturnsAn array containing the imaginary part of the complex data.

### ImaginaryData

Gets a value indicating the imaginary part of the complex data of the waveform stream.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double[] ImaginaryData { get; }

#### Returns

An array containing the imaginary part of the complex data.

Parent topic:

WaveformDataCDBEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs-realdata.html language=enus -->
## TOPIC 00688: RealData

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs-realdata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs-realdata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the real part of the complex data of the waveform stream. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double[] RealData { get; }ReturnsAn array containing the real part of the complex data.

### RealData

Gets a value indicating the real part of the complex data of the waveform stream.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double[] RealData { get; }

#### Returns

An array containing the real part of the complex data.

Parent topic:

WaveformDataCDBEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs.html language=enus -->
## TOPIC 00689: WaveformDataCDBEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides new waveform-stream data for the WaveformDataEventHandler event. Derives fromWaveformDataEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class WaveformDataCDBEventArgs : WaveformDataEventArgsPropertiesNameDescriptionImaginaryDataGets a value indicat

### WaveformDataCDBEventArgs Class

Provides new waveform-stream data for the [WaveformDataEventHandler](nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdataeventhandler.html) event.

#### Derives from

- WaveformDataEventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformDataCDBEventArgs : WaveformDataEventArgs

#### Properties

| Name | Description |
| --- | --- |
| ImaginaryData | Gets a value indicating the imaginary part of the complex data of the waveform stream. |
| RealData | Gets a value indicating the real part of the complex data of the waveform stream. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatadbleventargs-data.html language=enus -->
## TOPIC 00690: Data

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatadbleventargs-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatadbleventargs-data.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the data of the waveform stream. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double[] Data { get; }ReturnsAn array containing the data of the waveform stream.

### Data

Gets a value indicating the data of the waveform stream.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double[] Data { get; }

#### Returns

An array containing the data of the waveform stream.

Parent topic:

WaveformDataDBLEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatadbleventargs.html language=enus -->
## TOPIC 00691: WaveformDataDBLEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatadbleventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatadbleventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides new waveform-stream data for the WaveformDataEventHandler event. Derives fromWaveformDataEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class WaveformDataDBLEventArgs : WaveformDataEventArgsPropertiesNameDescriptionDataGets a value indicating the d

### WaveformDataDBLEventArgs Class

Provides new waveform-stream data for the [WaveformDataEventHandler](nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdataeventhandler.html) event.

#### Derives from

- WaveformDataEventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformDataDBLEventArgs : WaveformDataEventArgs

#### Properties

| Name | Description |
| --- | --- |
| Data | Gets a value indicating the data of the waveform stream. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-dt.html language=enus -->
## TOPIC 00692: Dt

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-dt.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-dt.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the time interval in seconds between data points in the waveform. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic double Dt { get; }ReturnsThe time interval in seconds between data points in the waveform.

### Dt

Gets a value indicating the time interval in seconds between data points in the waveform.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double Dt { get; }

#### Returns

The time interval in seconds between data points in the waveform.

Parent topic:

WaveformDataEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-fractionsofasecond.html language=enus -->
## TOPIC 00693: FractionsOfASecond

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-fractionsofasecond.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-fractionsofasecond.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the positive fractions of a second, representing the number of 2^-64 seconds, at waveform start of the waveform stream. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic ulong FractionsOfASecond { get; }ReturnsThe positive fraction of seconds, r

### FractionsOfASecond

Gets a value indicating the positive fractions of a second, representing the number of 2^-64 seconds, at waveform start of the waveform stream.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public ulong FractionsOfASecond { get; }

#### Returns

The positive fraction of seconds, representing the number of 2^-64 seconds.

Parent topic:

WaveformDataEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-offsetfromstartinsamples.html language=enus -->
## TOPIC 00694: OffsetFromStartInSamples

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-offsetfromstartinsamples.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-offsetfromstartinsamples.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the number of samples by which the first sample in the current data array is offset from the first sample in the waveform. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic ulong OffsetFromStartInSamples { get; }ReturnsThe number of samples by w

### OffsetFromStartInSamples

Gets a value indicating the number of samples by which the first sample in the current data array is offset from the first sample in the waveform.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public ulong OffsetFromStartInSamples { get; }

#### Returns

The number of samples by which the first sample in the data array is offset from the first sample in the waveform.

Parent topic:

WaveformDataEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-secondssinceepoch.html language=enus -->
## TOPIC 00695: SecondsSinceEpoch

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-secondssinceepoch.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-secondssinceepoch.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the number of seconds since the epoch 01/01/1904 00:00:00.00 UTC (using the Gregorian calendar and ignoring leap seconds), interpreted as a 64-bit signed twos compliment integer, at waveform start of the waveform stream. SyntaxNamespace: NationalInstruments.VeriStand.ClientAP

### SecondsSinceEpoch

Gets a value indicating the number of seconds since the epoch 01/01/1904 00:00:00.00 UTC (using the Gregorian calendar and ignoring leap seconds), interpreted as a 64-bit signed twos compliment integer, at waveform start of the waveform stream.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public long SecondsSinceEpoch { get; }

#### Returns

The number of seconds since 01/01/1904.

Parent topic:

WaveformDataEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-waveformstreamspecification.html language=enus -->
## TOPIC 00696: WaveformStreamSpecification

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-waveformstreamspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs-waveformstreamspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating the waveform stream specification that defines the waveform stream. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformStreamSpecification WaveformStreamSpecification { get; }ReturnsThe WaveformStreamSpecification.

### WaveformStreamSpecification

Gets a value indicating the waveform stream specification that defines the waveform stream.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [WaveformStreamSpecification](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification.html) WaveformStreamSpecification { get; }

#### Returns

The [WaveformStreamSpecification](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification.html).

Parent topic:

WaveformDataEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs.html language=enus -->
## TOPIC 00697: WaveformDataEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdataeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for waveform stream data events. Derives fromEventArgsSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class WaveformDataEventArgs : EventArgsRemarksThis is a base class from which more specific waveform data event types inherit. PropertiesNameDescriptio

### WaveformDataEventArgs Class

Provides data for waveform stream data events.

#### Derives from

- EventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformDataEventArgs : EventArgs

#### Remarks

This is a base class from which more specific waveform data event types inherit.

#### Properties

| Name | Description |
| --- | --- |
| Dt | Gets a value indicating the time interval in seconds between data points in the waveform. |
| FractionsOfASecond | Gets a value indicating the positive fractions of a second, representing the number of 2^-64 seconds, at waveform start of the waveform stream. |
| OffsetFromStartInSamples | Gets a value indicating the number of samples by which the first sample in the current data array is offset from the first sample in the waveform. |
| SecondsSinceEpoch | Gets a value indicating the number of seconds since the epoch 01/01/1904 00:00:00.00 UTC (using the Gregorian calendar and ignoring leap seconds), interpreted as a 64-bit signed twos compliment integer, at waveform start of the waveform stream. |
| WaveformStreamSpecification | Gets a value indicating the waveform stream specification that defines the waveform stream. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-dispose.html language=enus -->
## TOPIC 00698: Dispose()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-dispose.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-dispose.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Explicit disposal method. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic void Dispose()

### Dispose()

Explicit disposal method.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public void Dispose()

Parent topic:

WaveformDataWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-streaminterface.html language=enus -->
## TOPIC 00699: StreamInterface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-streaminterface.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-streaminterface.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the interface this watcher object uses. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingprotected IWaveformStreaming StreamInterface { get; set; }

### StreamInterface

Gets or sets the interface this watcher object uses.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

protected [IWaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming-iwaveformstreaming.html) StreamInterface { get; set; }

Parent topic:

WaveformDataWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-watcherspecslist.html language=enus -->
## TOPIC 00700: WatcherSpecsList

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-watcherspecslist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-watcherspecslist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the list of specifications this watcher object watches. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingprotected List< WaveformStreamSpecification > WatcherSpecsList { get; set; }

### WatcherSpecsList

Gets or sets the list of specifications this watcher object watches.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

protected List< [WaveformStreamSpecification](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification.html) > WatcherSpecsList { get; set; }

Parent topic:

WaveformDataWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-waveformstreamspecifications.html language=enus -->
## TOPIC 00701: WaveformStreamSpecifications

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-waveformstreamspecifications.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher-waveformstreamspecifications.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the waveform stream specifications associated with this WaveformDataWatcher. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformStreamSpecification[] WaveformStreamSpecifications { get; set; }ReturnsThe waveform stream specifications associated with

### WaveformStreamSpecifications

Gets or sets the waveform stream specifications associated with this WaveformDataWatcher.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [WaveformStreamSpecification](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification.html)[] WaveformStreamSpecifications { get; set; }

#### Returns

The waveform stream specifications associated with the WaveformDataWatcher.

Parent topic:

WaveformDataWatcher Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher.html language=enus -->
## TOPIC 00702: WaveformDataWatcher Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcher.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform s

### WaveformDataWatcher Class

This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform stream specifications to watch also update the event registration. LabVIEW users can register to the event within this class for use in the event structure in LabVIEW.

#### Derives from

- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformDataWatcher : IDisposable

#### Properties

| Name | Description |
| --- | --- |
| StreamInterface | Gets or sets the interface this watcher object uses. |
| WatcherSpecsList | Gets or sets the list of specifications this watcher object watches. |
| WaveformStreamSpecifications | Gets or sets the waveform stream specifications associated with this WaveformDataWatcher. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Explicit disposal method. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdataeventhandler.html language=enus -->
## TOPIC 00703: WaveformDataEventHandler

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdataeventhandler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdataeventhandler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event to register a callback to receive notifications when waveform data arrives. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic EventHandler< WaveformDataCDBEventArgs > WaveformDataEventHandler

### WaveformDataEventHandler

Event to register a callback to receive notifications when waveform data arrives.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public EventHandler< [WaveformDataCDBEventArgs](nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatacdbeventargs.html) > WaveformDataEventHandler

Parent topic:

WaveformDataWatcherCDB Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdatawatchercdb__iwaveformstreaming-waveformstreamspecification_arr1.html language=enus -->
## TOPIC 00704: WaveformDataWatcherCDB(IWaveformStreaming, WaveformStreamSpecification[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdatawatchercdb__iwaveformstreaming-waveformstreamspecification_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdatawatchercdb__iwaveformstreaming-waveformstreamspecification_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the WaveformDataWatcherCDB class with the specified waveform stream specifications. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformDataWatcherCDB(IWaveformStreaming streamInterface, WaveformStreamSpecification[] waveformStreamSp

### WaveformDataWatcherCDB(IWaveformStreaming, WaveformStreamSpecification[])

Initializes a new instance of the WaveformDataWatcherCDB class with the specified waveform stream specifications.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public WaveformDataWatcherCDB(IWaveformStreaming streamInterface, WaveformStreamSpecification[] waveformStreamSpecifications)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| streamInterface | IWaveformStreaming | Instance of the interface with which to register the waveform data event |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Waveform Stream Specifications this watcher returns data for. |

Parent topic:

WaveformDataWatcherCDB Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdatawatchercdb__iwaveformstreaming.html language=enus -->
## TOPIC 00705: WaveformDataWatcherCDB(IWaveformStreaming)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdatawatchercdb__iwaveformstreaming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb-waveformdatawatchercdb__iwaveformstreaming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the WaveformDataWatcherCDB class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformDataWatcherCDB(IWaveformStreaming streamInterface)ParametersNameTypeDescriptionstreamInterfaceIWaveformStreamingInstance of the interface with whic

### WaveformDataWatcherCDB(IWaveformStreaming)

Initializes a new instance of the WaveformDataWatcherCDB class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public WaveformDataWatcherCDB(IWaveformStreaming streamInterface)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| streamInterface | IWaveformStreaming | Instance of the interface with which to register the waveform data event |

Parent topic:

WaveformDataWatcherCDB Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb.html language=enus -->
## TOPIC 00706: WaveformDataWatcherCDB Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatchercdb.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform s

### WaveformDataWatcherCDB Class

This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform stream specifications to watch also update the event registration. LabVIEW users can register to the event within this class for use in the event structure in LabVIEW.

#### Derives from

- WaveformDataWatcher

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformDataWatcherCDB : WaveformDataWatcher

#### Constructors

| Name | Description |
| --- | --- |
| WaveformDataWatcherCDB(IWaveformStreaming, WaveformStreamSpecification[]) | Initializes a new instance of the WaveformDataWatcherCDB class with the specified waveform stream specifications. |
| WaveformDataWatcherCDB(IWaveformStreaming) | Initializes a new instance of the WaveformDataWatcherCDB class. |

#### Events

| Name | Description |
| --- | --- |
| WaveformDataEventHandler | Event to register a callback to receive notifications when waveform data arrives. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdataeventhandler.html language=enus -->
## TOPIC 00707: WaveformDataEventHandler

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdataeventhandler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdataeventhandler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Event to register a callback to receive notifications when waveform data arrives. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic EventHandler< WaveformDataDBLEventArgs > WaveformDataEventHandler

### WaveformDataEventHandler

Event to register a callback to receive notifications when waveform data arrives.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public EventHandler< [WaveformDataDBLEventArgs](nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatadbleventargs.html) > WaveformDataEventHandler

Parent topic:

WaveformDataWatcherDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdatawatcherdbl__iwaveformstreaming-waveformstreamspecification_arr1.html language=enus -->
## TOPIC 00708: WaveformDataWatcherDBL(IWaveformStreaming, WaveformStreamSpecification[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdatawatcherdbl__iwaveformstreaming-waveformstreamspecification_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdatawatcherdbl__iwaveformstreaming-waveformstreamspecification_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the WaveformDataWatcherDBL class with the specified waveform stream specifications. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformDataWatcherDBL(IWaveformStreaming streamInterface, WaveformStreamSpecification[] waveformStreamSp

### WaveformDataWatcherDBL(IWaveformStreaming, WaveformStreamSpecification[])

Initializes a new instance of the WaveformDataWatcherDBL class with the specified waveform stream specifications.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public WaveformDataWatcherDBL(IWaveformStreaming streamInterface, WaveformStreamSpecification[] waveformStreamSpecifications)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| streamInterface | IWaveformStreaming | Instance of the interface with which to register the waveform data event |
| waveformStreamSpecifications | WaveformStreamSpecification[] | Waveform Stream Specifications this watcher returns data for. |

Parent topic:

WaveformDataWatcherDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdatawatcherdbl__iwaveformstreaming.html language=enus -->
## TOPIC 00709: WaveformDataWatcherDBL(IWaveformStreaming)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdatawatcherdbl__iwaveformstreaming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl-waveformdatawatcherdbl__iwaveformstreaming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the WaveformDataWatcherDBL class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformDataWatcherDBL(IWaveformStreaming streamInterface)ParametersNameTypeDescriptionstreamInterfaceIWaveformStreamingInstance of the interface with whic

### WaveformDataWatcherDBL(IWaveformStreaming)

Initializes a new instance of the WaveformDataWatcherDBL class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public WaveformDataWatcherDBL(IWaveformStreaming streamInterface)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| streamInterface | IWaveformStreaming | Instance of the interface with which to register the waveform data event |

Parent topic:

WaveformDataWatcherDBL Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl.html language=enus -->
## TOPIC 00710: WaveformDataWatcherDBL Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformdatawatcherdbl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform s

### WaveformDataWatcherDBL Class

This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform stream specifications to watch also update the event registration. LabVIEW users can register to the event within this class for use in the event structure in LabVIEW.

#### Derives from

- WaveformDataWatcher

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformDataWatcherDBL : WaveformDataWatcher

#### Constructors

| Name | Description |
| --- | --- |
| WaveformDataWatcherDBL(IWaveformStreaming, WaveformStreamSpecification[]) | Initializes a new instance of the WaveformDataWatcherDBL class with the specified waveform stream specifications. |
| WaveformDataWatcherDBL(IWaveformStreaming) | Initializes a new instance of the WaveformDataWatcherDBL class. |

#### Events

| Name | Description |
| --- | --- |
| WaveformDataEventHandler | Event to register a callback to receive notifications when waveform data arrives. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition-equals__waveformstreamcondition.html language=enus -->
## TOPIC 00711: Equals(WaveformStreamCondition)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition-equals__waveformstreamcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition-equals__waveformstreamcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of WaveformStreamCondition. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool Equals(WaveformStreamCondition other)RemarksThe WaveformStreamCondition type inherits from WaveformStreamCo

### Equals(WaveformStreamCondition)

Determines whether the specified *other*  object is equal to the current instance of [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool Equals(WaveformStreamCondition other)

#### Remarks

The [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html) type inherits from [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | WaveformStreamCondition | The WaveformStreamCondition object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html). Otherwise, false.

Parent topic:

WaveformStreamCondition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition-gethashcode.html language=enus -->
## TOPIC 00712: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a WaveformStreamCondition object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override int GetHashCode()RemarksOverrid

### GetHashCode()

Serves as a hash function for a [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html) object.

Parent topic:

WaveformStreamCondition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html language=enus -->
## TOPIC 00713: WaveformStreamCondition Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a condition that determines when waveform streaming is active. Derives fromIEquatable< WaveformStreamCondition >SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class WaveformStreamCondition : IEquatable< WaveformStreamCondition >MethodsNameDescriptionEquals

### WaveformStreamCondition Class

Specifies a condition that determines when waveform streaming is active.

#### Derives from

- IEquatable< WaveformStreamCondition >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformStreamCondition : IEquatable< WaveformStreamCondition >

#### Methods

| Name | Description |
| --- | --- |
| Equals(WaveformStreamCondition) | Determines whether the specified other object is equal to the current instance of WaveformStreamCondition. |
| GetHashCode() | Serves as a hash function for a WaveformStreamCondition object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-bindtoname__type-out-out.html language=enus -->
## TOPIC 00714: BindToName(Type, out string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-bindtoname__type-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-bindtoname__type-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the assembly name and type name for the specified serializedType . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic void BindToName(Type serializedType, out string assemblyName, out string typeName)ParametersNameTypeDescriptionserializedTypeTypeThe Type of

### BindToName(Type, out string, out string)

Determines the assembly name and type name for the specified *serializedType* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public void BindToName(Type serializedType, out string assemblyName, out string typeName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| serializedType | Type | The Type of the object to serialize. |
| assemblyName | out string | The assembly name of the specified serializedType . |
| typeName | out string | The type name of the specified serializedType . |

Parent topic:

WaveformStreamConditionSerializationBinder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-bindtotype__string-string.html language=enus -->
## TOPIC 00715: BindToType(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-bindtotype__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-bindtotype__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the Type of the object with the specified typeName . SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic Type BindToType(string assemblyName, string typeName)ParametersNameTypeDescriptionassemblyNamestringThe name of the assembly to bind the type to.typeNamest

### BindToType(string, string)

Determines the Type of the object with the specified *typeName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public Type BindToType(string assemblyName, string typeName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| assemblyName | string | The name of the assembly to bind the type to. |
| typeName | string | The name of the type to bind. |

#### Returns

The Type of the object with the specified *typeName* .

Parent topic:

WaveformStreamConditionSerializationBinder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-waveformstreamconditionserializationbinder.html language=enus -->
## TOPIC 00716: WaveformStreamConditionSerializationBinder()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-waveformstreamconditionserializationbinder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder-waveformstreamconditionserializationbinder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the WaveformStreamConditionSerializationBinder class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformStreamConditionSerializationBinder()

### WaveformStreamConditionSerializationBinder()

Initializes a new instance of the [WaveformStreamConditionSerializationBinder](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public WaveformStreamConditionSerializationBinder()

Parent topic:

WaveformStreamConditionSerializationBinder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder.html language=enus -->
## TOPIC 00717: WaveformStreamConditionSerializationBinder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamconditionserializationbinder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a custom serialization binder for handling WaveformStreamCondition known types during deserialization. Derives fromISerializationBinderSyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class WaveformStreamConditionSerializationBinder : ISerializationBinderCons

### WaveformStreamConditionSerializationBinder Class

Provides a custom serialization binder for handling WaveformStreamCondition known types during deserialization.

#### Derives from

- ISerializationBinder

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformStreamConditionSerializationBinder : ISerializationBinder

#### Constructors

| Name | Description |
| --- | --- |
| WaveformStreamConditionSerializationBinder() | Initializes a new instance of the WaveformStreamConditionSerializationBinder class. |

#### Methods

| Name | Description |
| --- | --- |
| BindToName(Type, out string, out string) | Determines the assembly name and type name for the specified serializedType . |
| BindToType(string, string) | Determines the Type of the object with the specified typeName . |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-customrate.html language=enus -->
## TOPIC 00718: CustomRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-customrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-customrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the requested rate in Hertz at which data will be streamed. The actual rates at which data is streamed may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless StreamDataAtAcquisionRate

### CustomRate

Gets or sets a value indicating the requested rate in Hertz at which data will be streamed. The actual rates at which data is streamed may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless [StreamDataAtAcquisionRate](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-streamdataatacquisionrate.html) is false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public double CustomRate { get; set; }

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-equals__object.html language=enus -->
## TOPIC 00719: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the current object is equivalent to another object of the same type. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectAn object to compare with this object.Returnstrue if the curre

### Equals(object)

Indicates whether the current object is equivalent to another object of the same type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | An object to compare with this object. |

#### Returns

true if the current object is equivalent to the other parameter; otherwise, false.

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-equals__waveformstreamspecification.html language=enus -->
## TOPIC 00720: Equals(WaveformStreamSpecification)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-equals__waveformstreamspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-equals__waveformstreamspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the current WaveformStreamSpecification is equivalent to another WaveformStreamSpecification. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool Equals(WaveformStreamSpecification other)ParametersNameTypeDescriptionotherWaveformStreamSpecification

### Equals(WaveformStreamSpecification)

Indicates whether the current WaveformStreamSpecification is equivalent to another WaveformStreamSpecification.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool Equals(WaveformStreamSpecification other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | WaveformStreamSpecification | An WaveformStreamSpecification to compare with this WaveformStreamSpecification. |

#### Returns

true if the current WaveformStreamSpecification is equivalent to the other parameter; otherwise, false.

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-gethashcode.html language=enus -->
## TOPIC 00721: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for this WaveformStreamSpecification. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic override int GetHashCode()ReturnsThe hash code for this WaveformStreamSpecification.

### GetHashCode()

Returns the hash code for this WaveformStreamSpecification.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public override int GetHashCode()

#### Returns

The hash code for this WaveformStreamSpecification.

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-streamcondition.html language=enus -->
## TOPIC 00722: StreamCondition

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-streamcondition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-streamcondition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the condition used to determine when to stream data. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformStreamCondition StreamCondition { get; set; }

### StreamCondition

Gets or sets a value indicating the condition used to determine when to stream data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public [WaveformStreamCondition](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamcondition.html) StreamCondition { get; set; }

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-streamdataatacquisionrate.html language=enus -->
## TOPIC 00723: StreamDataAtAcquisionRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-streamdataatacquisionrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-streamdataatacquisionrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the waveform stream data is transferred at the rate at which the target is acquiring the data. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic bool StreamDataAtAcquisionRate { get; set; }Returnstrue to stream all data produced

### StreamDataAtAcquisionRate

Gets or sets a value indicating whether the waveform stream data is transferred at the rate at which the target is acquiring the data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public bool StreamDataAtAcquisionRate { get; set; }

#### Returns

true to stream all data produced by a target. false to stream data using the rate specified by [CustomRate](nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-customrate.html), which may mean the target decimates the data before streaming it.

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-waveformpath.html language=enus -->
## TOPIC 00724: WaveformPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-waveformpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-waveformpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the system definition path of the waveform to stream. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic string WaveformPath { get; set; }

### WaveformPath

Gets or sets a value indicating the system definition path of the waveform to stream.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public string WaveformPath { get; set; }

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-waveformstreamspecification__string.html language=enus -->
## TOPIC 00725: WaveformStreamSpecification(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-waveformstreamspecification__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification-waveformstreamspecification__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the WaveformStreamSpecification class. SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic WaveformStreamSpecification(string waveformPath)ParametersNameTypeDescriptionwaveformPathstringThe system definition path of the waveform to stream.

### WaveformStreamSpecification(string)

Initializes a new instance of the WaveformStreamSpecification class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public WaveformStreamSpecification(string waveformPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| waveformPath | string | The system definition path of the waveform to stream. |

Parent topic:

WaveformStreamSpecification Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification.html language=enus -->
## TOPIC 00726: WaveformStreamSpecification Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming-waveformstreamspecification.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies properties for a waveform stream. Derives fromIEquatable< WaveformStreamSpecification >SyntaxNamespace: NationalInstruments.VeriStand.ClientAPI.WaveformStreamingpublic class WaveformStreamSpecification : IEquatable< WaveformStreamSpecification >ConstructorsNameDescriptionWaveformStreamSpec

### WaveformStreamSpecification Class

Specifies properties for a waveform stream.

#### Derives from

- IEquatable< WaveformStreamSpecification >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.ClientAPI.WaveformStreaming](nationalinstruments-veristand-clientapi-waveformstreaming.html)

public class WaveformStreamSpecification : IEquatable< WaveformStreamSpecification >

#### Constructors

| Name | Description |
| --- | --- |
| WaveformStreamSpecification(string) | Initializes a new instance of the WaveformStreamSpecification class. |

#### Properties

| Name | Description |
| --- | --- |
| CustomRate | Gets or sets a value indicating the requested rate in Hertz at which data will be streamed. The actual rates at which data is streamed may be coerced to an even divisor of the rates at which the targets in the system definition produce data. This property is ignored unless StreamDataAtAcquisionRate is false. |
| StreamCondition | Gets or sets a value indicating the condition used to determine when to stream data. |
| StreamDataAtAcquisionRate | Gets or sets a value indicating whether the waveform stream data is transferred at the rate at which the target is acquiring the data. |
| WaveformPath | Gets or sets a value indicating the system definition path of the waveform to stream. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Indicates whether the current object is equivalent to another object of the same type. |
| Equals(WaveformStreamSpecification) | Indicates whether the current WaveformStreamSpecification is equivalent to another WaveformStreamSpecification. |
| GetHashCode() | Returns the hash code for this WaveformStreamSpecification. |

Parent topic:

NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi-waveformstreaming.html language=enus -->
## TOPIC 00727: NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi-waveformstreaming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi-waveformstreaming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionStreamAllDataSpecifies a stream condition that is always true. StreamFirstNSecondsSpecifies a waveform streaming condition that is true during the first N seconds of waveform data after the waveform starts. StreamInRangeDBLSpecifies a waveform streaming condition for waveforms

### NationalInstruments.VeriStand.ClientAPI.WaveformStreaming

#### Classes

| Name | Description |
| --- | --- |
| StreamAllData | Specifies a stream condition that is always true. |
| StreamFirstNSeconds | Specifies a waveform streaming condition that is true during the first N seconds of waveform data after the waveform starts. |
| StreamInRangeDBL | Specifies a waveform streaming condition for waveforms of Double data type that is true when the data is inside a defined range. |
| StreamNOfMSeconds | Specifies a waveform streaming condition that is true during the first N seconds of waveform data after the waveform starts and true again for N seconds after M total seconds have elapsed. |
| WaveformDataCDBEventArgs | Provides new waveform-stream data for the WaveformDataEventHandler event. |
| WaveformDataDBLEventArgs | Provides new waveform-stream data for the WaveformDataEventHandler event. |
| WaveformDataEventArgs | Provides data for waveform stream data events. |
| WaveformDataWatcher | This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform stream specifications to watch also update the event registration. LabVIEW users can register to the event within this class for use in the event structure in LabVIEW. |
| WaveformDataWatcherCDB | This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform stream specifications to watch also update the event registration. LabVIEW users can register to the event within this class for use in the event structure in LabVIEW. |
| WaveformDataWatcherDBL | This class serves as a wrapper around the waveform stream data event for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. The set and get properties for which waveform stream specifications to watch also update the event registration. LabVIEW users can register to the event within this class for use in the event structure in LabVIEW. |
| WaveformStreamCondition | Specifies a condition that determines when waveform streaming is active. |
| WaveformStreamConditionSerializationBinder | Provides a custom serialization binder for handling WaveformStreamCondition known types during deserialization. |
| WaveformStreamSpecification | Specifies properties for a waveform stream. |

#### Interfaces

| Name | Description |
| --- | --- |
| IWaveformStreaming | Specifies an interface to stream waveform data from the VeriStand gateway. |

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-clientapi.html language=enus -->
## TOPIC 00728: NationalInstruments.VeriStand.ClientAPI

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-clientapi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-clientapi.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionAlarmChangeEventArgsProvides data about an alarm event. AlarmFlagDataProvides data about the alarm flag. AlarmInfoProvides information about and configures an individual alarm. AlarmStateWatcherThis class essentially serves as a wrapper around the alarm state change event (spec

### NationalInstruments.VeriStand.ClientAPI

#### Classes

| Name | Description |
| --- | --- |
| AlarmChangeEventArgs | Provides data about an alarm event. |
| AlarmFlagData | Provides data about the alarm flag. |
| AlarmInfo | Provides information about and configures an individual alarm. |
| AlarmStateWatcher | This class essentially serves as a wrapper around the alarm state change event (specific to one alarm) for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. Then, LabVIEW users can register to the event within this class for use in the event structure in LabVIEW. |
| AlarmTriggerEventArgs | Provides data about a triggered alarm for the OnAlarmTrigger2 event. |
| CalibrationUpdateEventArgs | Provides data about channel calibration for the OnCalibrationUpdate event. |
| ChannelValueChangeEventArgs | Provides data about channel value changes for the ChannelValueChangeEventHandler event. |
| ChannelValueWatcher | This class essentially serves as a wrapper around the channel value change event (specific to one parameter) for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. Then, LabVIEW users can register to the event within this class for use in the event structure in LabVIEW. |
| DeployOptions | Defines the options for deploying the system definition file. |
| Factory | Provides access to the NI VeriStand system and the various interfaces available in the Execution API. Any code you write using this API must include a Factory constructor to access NI VeriStand. |
| LogChannel | Represents the logging properties for individual channels. |
| LogInfo | Defines data log file configuration settings. |
| NodeInfo | Provides information about and configures a node in the system definition file. |
| ParameterValueChangeEventArgs | Provides data about model parameter value changes for the ParameterValueChanged and ParameterValueChangeEventHandler events. |
| ParameterValueWatcher | This class essentially serves as a wrapper around the parameter value change event (specific to one parameter) for the purpose of allowing access to this event easier to obtain from within LabVIEW. Constructing and destructing the object registers and unregisters, respectively, from the event. Then, LabVIEW users can register to the event within this class for use in the event structure in LabVIEW. |
| RemoteSequenceCallInfo | Provides information about a remote stimulus profile sequence. |
| RuntimeConfigurationChangeEventArgs | Provides data about runtime configuration change event. |
| SequenceCallInfo | Provides information about a stimulus profile sequence. |
| SequenceCompleteEventArgs | Event data returned when a sequence completes execution. |
| SequenceParameterAssignmentInfo | Provides information about an input parameter of a real-time sequence. |
| SequenceStateChangeEventArgs | Event data returned when the execution state of a real-time sequence changes. |
| ServerCreateOptions | Options for starting the VeriStand server. |
| TargetStateChangeEventArgs | Provides data about target state change event. |

#### Interfaces

| Name | Description |
| --- | --- |
| IAlarm | Interface to control and observe a specific alarm running on the target. Use the GetIAlarm(string) method of the Factory class to access this interface. |
| IAlarmManager | Interface to control and observe alarms running on a target. |
| IAlarmManager2 | Interface to control and observe alarms running on a target. Use the GetIAlarmManager2 method of the Factory class to access this interface. |
| ICalibration | This interface is obsolete in NI VeriStand 2012 and later. Use the ICalibration2 interface instead. Interface to get and set calibration settings for channels on the test system. Use the GetICalibration method of the Factory class to access this interface. This interface is associated with the legacy calibration feature. |
| ICalibration2 | Interface to get and set calibration settings for channels on the test system. Use the GetICalibration2 method of the Factory class to access this interface. |
| IChannelFault | Interface to view, set, and clear channel software faults. Use the GetIChannelFault() method of the Factory class to access this interface. |
| IChannelMonitor | Client Interface for Monitoring a Channel. |
| ICustomDevice | Interface to interact with custom devices in NI VeriStand. Use the GetICustomDevice method of the Factory class to access this interface. |
| IDiagnostics | Interface for Veristand Engine Diagnostics. |
| IErrorProviding | Interface for the error providing tool. Use this interface to translate electrical errors into channel value pairs. |
| IMacroPlayer | Interface to the Macro Player tool. Use this interface to load and play back a macro (.nivsmacro) file you created using the IMacroRecorder interface. Use the GetIMacroPlayer method of the Factory class to access this interface. |
| IMacroRecorder | Interface to the Macro Recorder tool. You can use the members of this interface to record commands the VeriStand Gateway sends to a target. You can save the recorded commands to a macro (.nivsmacro) file to later play back using the IMacroPlayer interface. Use the GetIMacroRecorder method of the Factory class to access this interface. |
| IModel | Interface to control and observe a specific model running on the execution host. Use the GetIModel(string) method of the Factory class to access this interface. |
| IModelManager | Interface to control and observe models running on the first target. You must use the members of the IModelManager2 interface if you want to specify one of multiple targets. |
| IModelManager2 | Interface to control and observe models running on an execution host. Use the GetIModelManager2 method of the Factory class to access this interface. |
| IProject | Interface to automate an NI VeriStand project. Use the GetIProject(string, string, string, string) method of the Factory class to access this interface and specify the project you want to automate. |
| IRuntimeConfigurationManager | Interface to manage configurations that can be modified at runtime without the need to undeploy. |
| ISequenceControl | Automates and monitors the execution of a sequence in a stimulus profile session. |
| IStimulus | Some members of this interface are deprecated in NI VeriStand 2010 and later. Use the IStimulusProfileSession interface instead. |
| IStimulus2 | This interface is deprecated in VeriStand 2011 and later. Use the IStimulusProfileSession interface instead. Interface to control stimulus generation. Use the GetIStimulus2 method of the Factory class to access this interface. |
| IStimulusProfileSession | Interface to control and monitor Stimulus Profile Session execution. |
| IUDPChannelStreamSession | Interface for deploying and undeploying UDP Channel Stream sessions. |
| IWorkspace | Interface to perform basic workspace operations, such as getting and setting channel data. Note The IWorkspace2 interface inherits the members of this interface and provides extended functionality. |
| IWorkspace2 | Interface to perform basic workspace operations, such as getting, setting, and logging channel data. |

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| AcknowledgementStatus | Specifies the acknowledgement status of an alarm. |
| AlarmMode | The operating mode of an alarm running on the target. The operating mode of an alarm specifies the action that occurs when the alarm is triggered. |
| AlarmPriority | The priority of an alarm running on the target. |
| AlarmState | The state of an alarm running on the target. |
| ByteOrder | Specifies the byte order of data. |
| CJCType | The type of CJC sensor to use for thermocouple calibration. |
| ModelCommand | Command to change the execution state of a model running on the target. |
| ModelState | The execution state of a model running on the target. |
| PlayModeEnum | The play mode of the Macro Player tool, which specifies the speed at which the tool plays back macro files. |
| PlayStateEnum | The current state of the Macro Player tool. |
| RuntimeConfigurationState | The current state of the runtime configuration on the runtime configurable node. |
| ScaleType | The type of calibration scale. |
| SequenceState | The execution state of a sequence. |
| StimulusResult | The result of stimulus generation. |
| StimulusState | The state of the stimulus profile manager. |
| SystemState | The current state of the system to which the VeriStand Gateway is connected. |
| TargetState | The current state of the target. |
| TemperatureUnits | The temperature units to use for thermocouple calibration. |
| ThermocoupleType | The type of thermocouple to use for thermocouple calibration. |

#### Delegates

| Name | Description |
| --- | --- |
| DOnAlarmTrigger | Represents the method that handles the OnAlarmTrigger event. |
| DOnAlarmTrigger2 | Delegate to define the OnAlarmTrigger2 event handler. |
| DOnGatewayErrorNotification | Delegate to define the OnGatewayErrorNotification event handler. |
| DOnGatewayStatusNotification | Delegate to define the OnGatewayStatusNotification event handler. |
| DOnMacroCommandLine | Delegate to define the OnMacroCommandLine event handler. |
| DOnMacroComplete | Delegate to define the OnMacroComplete event handler. |
| DOnMacroErrorMessage | Delegate to define the OnMacroErrorMessage event handler. |
| DOnMacroPercentComplete | Delegate to define the OnMacroPercentComplete event handler. |
| DOnSequenceComplete | Delegate to define the SequenceComplete event handler. |
| DOnSequenceStateChange | Delegate to define the StateChange event handler. |
| DOnSessionComplete | Delegate to define the SessionComplete event handler. |
| DOnSessionUndeploy | Delegate to define the SessionUndeploy event handler. |
| DOnSystemStateChange | Delegate to define the OnSystemStateChange event handler. |

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-booleanvalue.html language=enus -->
## TOPIC 00729: BooleanValue()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-booleanvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-booleanvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanValue. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic BooleanValue()

### BooleanValue()

Initializes a new instance of [BooleanValue](nationalinstruments-veristand-data-booleanvalue.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public BooleanValue()

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-booleanvalue__bool.html language=enus -->
## TOPIC 00730: BooleanValue(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-booleanvalue__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-booleanvalue__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanValue with the specified value. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic BooleanValue(bool value)ParametersNameTypeDescriptionvalueboolThe value of the Boolean.

### BooleanValue(bool)

Initializes a new instance of [BooleanValue](nationalinstruments-veristand-data-booleanvalue.html) with the specified value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public BooleanValue(bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | bool | The value of the Boolean. |

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-booleanvalue__booleanvalue.html language=enus -->
## TOPIC 00731: BooleanValue(BooleanValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-booleanvalue__booleanvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-booleanvalue__booleanvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanValue by copying an existing BooleanValue instance. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic BooleanValue(BooleanValue node)ParametersNameTypeDescriptionnodeBooleanValueThe instance of BooleanValue to copy.

### BooleanValue(BooleanValue)

Initializes a new instance of [BooleanValue](nationalinstruments-veristand-data-booleanvalue.html) by copying an existing [BooleanValue](nationalinstruments-veristand-data-booleanvalue.html) instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public BooleanValue(BooleanValue node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BooleanValue | The instance of BooleanValue to copy. |

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-clone.html language=enus -->
## TOPIC 00732: Clone()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-clone.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-clone.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new object that is a copy of the current boolean value. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override object Clone()ReturnsA new object that is a copy of this instance.

### Clone()

Creates a new object that is a copy of the current boolean value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override object Clone()

#### Returns

A new object that is a copy of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-compareto__scalardatavalue.html language=enus -->
## TOPIC 00733: CompareTo(ScalarDataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-compareto__scalardatavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-compareto__scalardatavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares this instance to a specified object and returns an integer that indicates their relationship to each other. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override int CompareTo(ScalarDataValue other)ParametersNameTypeDescriptionotherScalarDataValueThe object to compare to this i

### CompareTo(ScalarDataValue)

Compares this instance to a specified object and returns an integer that indicates their relationship to each other.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override int CompareTo(ScalarDataValue other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ScalarDataValue | The object to compare to this instance. |

#### Returns

other

| Condition | Return Value |
| --- | --- |
| Less than zero | This instance is false and other is true.) |
| Zero | This instance and other are equal (either both are true or false.) |
| Greater than zero | This instance is true and other is false, or other is null. |

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-equals__dataresource.html language=enus -->
## TOPIC 00734: Equals(DataResource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-equals__dataresource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-equals__dataresource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating whether this instance is equal to the specified DataResource object. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override bool Equals(DataResource other)ParametersNameTypeDescriptionotherDataResourceThe data resource to compare to this instance.Returnstrue if

### Equals(DataResource)

Returns a value indicating whether this instance is equal to the specified [DataResource](nationalinstruments-veristand-data-dataresource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override bool Equals(DataResource other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | DataResource | The data resource to compare to this instance. |

#### Returns

true if *other*  is a [BooleanValue](nationalinstruments-veristand-data-booleanvalue.html) and has the same value as this instance; otherwise false.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-fromstring__string.html language=enus -->
## TOPIC 00735: FromString(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-fromstring__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to its bool equivalent. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override bool FromString(string ValueString)ParametersNameTypeDescriptionValueStringstringThe string to convert to a Boolean.Returnstrue if the conversion succeeded; otherwise false.

### FromString(string)

Converts the specified string to its bool equivalent.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override bool FromString(string ValueString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| ValueString | string | The string to convert to a Boolean. |

#### Returns

true if the conversion succeeded; otherwise false.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-getbytes.html language=enus -->
## TOPIC 00736: GetBytes()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-getbytes.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-getbytes.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Boolean value as an array of bytes. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override byte[] GetBytes()ReturnsAn array of bytes with length 2.

### GetBytes()

Returns the Boolean value as an array of bytes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override byte[] GetBytes()

#### Returns

An array of bytes with length 2.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-setbytes__byte_arr1.html language=enus -->
## TOPIC 00737: SetBytes(byte[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-setbytes__byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-setbytes__byte_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the BooleanValue to true or false based on Bytes . SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override void SetBytes(byte[] Bytes)RemarksIf the byte at Bytes[0] is a nonzero value, sets the Boolean value to true; otherwise, false. ParametersNameTypeDescriptionBytesbyte[]An array

### SetBytes(byte[])

Sets the [BooleanValue](nationalinstruments-veristand-data-booleanvalue.html) to true or false based on *Bytes* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override void SetBytes(byte[] Bytes)

#### Remarks

If the byte at Bytes[0] is a nonzero value, sets the Boolean value to true; otherwise, false.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Bytes | byte[] | An array of bytes. |

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-size.html language=enus -->
## TOPIC 00738: Size

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-size.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-size.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the size of the Boolean value. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override long Size { get; }ReturnsThe size of the Boolean in bytes.

### Size

Gets the size of the Boolean value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override long Size { get; }

#### Returns

The size of the Boolean in bytes.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-toboolean.html language=enus -->
## TOPIC 00739: ToBoolean()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-toboolean.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-toboolean.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of this instance as a bool. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override bool ToBoolean()ReturnsA bool instance equivalent to the value of this instance.

### ToBoolean()

Returns the value of this instance as a bool.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override bool ToBoolean()

#### Returns

A bool instance equivalent to the value of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-todouble.html language=enus -->
## TOPIC 00740: ToDouble()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-todouble.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-todouble.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of this instance as an equivalent double-precision floating point number. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override double ToDouble()ReturnsA double instance equivalent to the value of this instance.

### ToDouble()

Returns the value of this instance as an equivalent double-precision floating point number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override double ToDouble()

#### Returns

A double instance equivalent to the value of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-toint32.html language=enus -->
## TOPIC 00741: ToInt32()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-toint32.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-toint32.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of this instance as an equivalent 32-bit signed integer. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override int ToInt32()ReturnsAn int instance equivalent to the value of this instance.

### ToInt32()

Returns the value of this instance as an equivalent 32-bit signed integer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override int ToInt32()

#### Returns

An int instance equivalent to the value of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-toint64.html language=enus -->
## TOPIC 00742: ToInt64()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-toint64.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-toint64.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of this instance as an equivalent 64-bit signed integer. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override long ToInt64()ReturnsAn long instance equivalent to the value of this instance.

### ToInt64()

Returns the value of this instance as an equivalent 64-bit signed integer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override long ToInt64()

#### Returns

An long instance equivalent to the value of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-tostring.html language=enus -->
## TOPIC 00743: ToString()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-tostring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-tostring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of this instance as an equivalent string. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override string ToString()ReturnsA string instance equivalent to the value of this instance.

### ToString()

Returns the value of this instance as an equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override string ToString()

#### Returns

A string instance equivalent to the value of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-touint32.html language=enus -->
## TOPIC 00744: ToUInt32()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-touint32.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-touint32.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of this instance as an equivalent 32-bit unsigned integer. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override uint ToUInt32()ReturnsA uint instance equivalent to the value of this instance.

### ToUInt32()

Returns the value of this instance as an equivalent 32-bit unsigned integer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override uint ToUInt32()

#### Returns

A uint instance equivalent to the value of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-touint64.html language=enus -->
## TOPIC 00745: ToUInt64()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-touint64.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-touint64.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of this instance as an equivalent 64-bit unsigned integer. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override ulong ToUInt64()ReturnsA ulong instance equivalent to the value of this instance.

### ToUInt64()

Returns the value of this instance as an equivalent 64-bit unsigned integer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override ulong ToUInt64()

#### Returns

A ulong instance equivalent to the value of this instance.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-type.html language=enus -->
## TOPIC 00746: Type

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the data type of the Boolean value. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic override DataType Type { get; }ReturnsThe data type of the Boolean value, as an enumeration value of DataType.

### Type

Gets the data type of the Boolean value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public override [DataType](nationalinstruments-veristand-data-datatype.html) Type { get; }

#### Returns

The data type of the Boolean value, as an enumeration value of [DataType](nationalinstruments-veristand-data-datatype.html).

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue-value.html language=enus -->
## TOPIC 00747: Value

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue-value.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the value of the Boolean. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic bool Value { get; set; }ReturnsThe value of the Boolean.

### Value

Gets or sets the value of the Boolean.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public bool Value { get; set; }

#### Returns

The value of the Boolean.

Parent topic:

BooleanValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvalue.html language=enus -->
## TOPIC 00748: BooleanValue Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Boolean value. Derives fromScalarDataValueSyntaxNamespace: NationalInstruments.VeriStand.Datapublic class BooleanValue : ScalarDataValueThread SafetyAny members of this type are not guaranteed to be thread safe.ConstructorsNameDescriptionBooleanValue(bool)Initializes a new instance of B

### BooleanValue Class

Represents a Boolean value.

#### Derives from

- ScalarDataValue

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public class BooleanValue : ScalarDataValue

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| BooleanValue(bool) | Initializes a new instance of BooleanValue with the specified value. |
| BooleanValue(BooleanValue) | Initializes a new instance of BooleanValue by copying an existing BooleanValue instance. |
| BooleanValue() | Initializes a new instance of BooleanValue. |

#### Properties

| Name | Description |
| --- | --- |
| Size | Gets the size of the Boolean value. |
| Type | Gets the data type of the Boolean value. |
| Value | Gets or sets the value of the Boolean. |

#### Methods

| Name | Description |
| --- | --- |
| Clone() | Creates a new object that is a copy of the current boolean value. |
| CompareTo(ScalarDataValue) | Compares this instance to a specified object and returns an integer that indicates their relationship to each other. |
| Equals(DataResource) | Returns a value indicating whether this instance is equal to the specified DataResource object. |
| FromString(string) | Converts the specified string to its bool equivalent. |
| GetBytes() | Returns the Boolean value as an array of bytes. |
| SetBytes(byte[]) | Sets the BooleanValue to true or false based on Bytes . |
| ToBoolean() | Returns the value of this instance as a bool. |
| ToDouble() | Returns the value of this instance as an equivalent double-precision floating point number. |
| ToInt32() | Returns the value of this instance as an equivalent 32-bit signed integer. |
| ToInt64() | Returns the value of this instance as an equivalent 64-bit signed integer. |
| ToString() | Returns the value of this instance as an equivalent string. |
| ToUInt32() | Returns the value of this instance as an equivalent 32-bit unsigned integer. |
| ToUInt64() | Returns the value of this instance as an equivalent 64-bit unsigned integer. |

Parent topic:

NationalInstruments.VeriStand.Data

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvaluearray-booleanvaluearray.html language=enus -->
## TOPIC 00749: BooleanValueArray()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvaluearray-booleanvaluearray.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvaluearray-booleanvaluearray.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanValueArray with an empty array of BooleanValue objects. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic BooleanValueArray()

### BooleanValueArray()

Initializes a new instance of [BooleanValueArray](nationalinstruments-veristand-data-booleanvaluearray.html) with an empty array of [BooleanValue](nationalinstruments-veristand-data-booleanvalue.html) objects.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public BooleanValueArray()

Parent topic:

BooleanValueArray Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-data-booleanvaluearray-booleanvaluearray__bool_arr1.html language=enus -->
## TOPIC 00750: BooleanValueArray(bool[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-data-booleanvaluearray-booleanvaluearray__bool_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-data-booleanvaluearray-booleanvaluearray__bool_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanValueArray with the specified array of bool values. SyntaxNamespace: NationalInstruments.VeriStand.Datapublic BooleanValueArray(bool[] Value)ParametersNameTypeDescriptionValuebool[]An array of Boolean values.

### BooleanValueArray(bool[])

Initializes a new instance of [BooleanValueArray](nationalinstruments-veristand-data-booleanvaluearray.html) with the specified array of bool values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.Data](nationalinstruments-veristand-data.html)

public BooleanValueArray(bool[] Value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Value | bool[] | An array of Boolean values. |

Parent topic:

BooleanValueArray Class
