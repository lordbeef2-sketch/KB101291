# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=3501 end=3750 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels-getfolders.html language=enus -->
## TOPIC 03501: GetFolders()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels-getfolders.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels-getfolders.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ReflectiveMemoryFolder elements from the current ReflectiveMemoryDataChannels section. This method gets the defined organizational folders into which data channels of a reflective memory device are categorized. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefi

### GetFolders()

Gets an array that contains the [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) elements from the current [ReflectiveMemoryDataChannels](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels.html) section. This method gets the defined organizational folders into which data channels of a reflective memory device are categorized.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html)[] GetFolders()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) elements from the current [ReflectiveMemoryDataChannels](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels.html) section.

Parent topic:

ReflectiveMemoryDataChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels.html language=enus -->
## TOPIC 03502: ReflectiveMemoryDataChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the top-level Data Channels section of a ReflectiveMemory device. This section contains all the data channels for the device, as well as sub-folders that you can use to organize the channels. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class

### ReflectiveMemoryDataChannels Class

Represents the top-level **Data Channels** section of a [ReflectiveMemory](nationalinstruments-veristand-systemdefinitionapi-reflectivememory.html) device. This section contains all the data channels for the device, as well as sub-folders that you can use to organize the channels.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ReflectiveMemoryDataChannels : Section

#### Remarks

Use the members of this class to add or access data channels or sub-folders.

**Accessing this Class**

- [GetDataChannels](nationalinstruments-veristand-systemdefinitionapi-reflectivememory-getdatachannels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddDataChannel(ReflectiveMemoryDataChannel, out Error) | Adds the specified ReflectiveMemoryDataChannel to the Data Channels section. |
| AddDataChannel(ReflectiveMemoryDataChannel) | Adds the specified ReflectiveMemoryDataChannel to the Data Channels section. |
| AddFolder(ReflectiveMemoryFolder) | Adds the specified ReflectiveMemoryFolder under the Data Channels section. |
| AddFolder(ReflectiveMemoryFolder, out Error) | Adds the specified ReflectiveMemoryFolder under the Data Channels section. |
| GetDataChannels() | Gets an array that contains the ReflectiveMemoryDataChannel elements from the current ReflectiveMemoryDataChannels section. This method gets the individual defined data channels for the reflective memory device. |
| GetFolders() | Gets an array that contains the ReflectiveMemoryFolder elements from the current ReflectiveMemoryDataChannels section. This method gets the defined organizational folders into which data channels of a reflective memory device are categorized. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-adddatachannel__reflectivememorydatachannel-out.html language=enus -->
## TOPIC 03503: AddDataChannel(ReflectiveMemoryDataChannel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-adddatachannel__reflectivememorydatachannel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-adddatachannel__reflectivememorydatachannel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ReflectiveMemoryFolder under the folder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDataChannel(ReflectiveMemoryDataChannel reflectiveMemoryDataChannel, out Error error)ParametersNameTypeDescriptionreflectiveMemoryDataChannelReflectiveMemoryDa

### AddDataChannel(ReflectiveMemoryDataChannel, out Error)

Adds the specified [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) under the folder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDataChannel(ReflectiveMemoryDataChannel reflectiveMemoryDataChannel, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| reflectiveMemoryDataChannel | ReflectiveMemoryDataChannel | The data channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the data channel was added successfully.

Parent topic:

ReflectiveMemoryFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-adddatachannel__reflectivememorydatachannel.html language=enus -->
## TOPIC 03504: AddDataChannel(ReflectiveMemoryDataChannel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-adddatachannel__reflectivememorydatachannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-adddatachannel__reflectivememorydatachannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ReflectiveMemoryDataChannel under the folder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDataChannel(ReflectiveMemoryDataChannel reflectiveMemoryDataChannel)ParametersNameTypeDescriptionreflectiveMemoryDataChannelReflectiveMemoryDataChannelThe

### AddDataChannel(ReflectiveMemoryDataChannel)

Adds the specified [ReflectiveMemoryDataChannel](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannel.html) under the folder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDataChannel(ReflectiveMemoryDataChannel reflectiveMemoryDataChannel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| reflectiveMemoryDataChannel | ReflectiveMemoryDataChannel | The data channel to add. |

#### Returns

true if the data channel was added successfully.

Parent topic:

ReflectiveMemoryFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-addfolder__reflectivememoryfolder-out.html language=enus -->
## TOPIC 03505: AddFolder(ReflectiveMemoryFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-addfolder__reflectivememoryfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-addfolder__reflectivememoryfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ReflectiveMemoryFolder under the Data Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFolder(ReflectiveMemoryFolder reflectiveMemoryFolder, out Error error)ParametersNameTypeDescriptionreflectiveMemoryFolderReflectiveMemoryFolderT

### AddFolder(ReflectiveMemoryFolder, out Error)

Adds the specified [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) under the **Data Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFolder(ReflectiveMemoryFolder reflectiveMemoryFolder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| reflectiveMemoryFolder | ReflectiveMemoryFolder | The folder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the folder was added successfully.

Parent topic:

ReflectiveMemoryFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-addfolder__reflectivememoryfolder.html language=enus -->
## TOPIC 03506: AddFolder(ReflectiveMemoryFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-addfolder__reflectivememoryfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-addfolder__reflectivememoryfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ReflectiveMemoryFolder under the Data Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFolder(ReflectiveMemoryFolder reflectiveMemoryFolder)ParametersNameTypeDescriptionreflectiveMemoryFolderReflectiveMemoryFolderThe folder to add.

### AddFolder(ReflectiveMemoryFolder)

Adds the specified [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) under the **Data Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFolder(ReflectiveMemoryFolder reflectiveMemoryFolder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| reflectiveMemoryFolder | ReflectiveMemoryFolder | The folder to add. |

#### Returns

true if the folder was added successfully.

Parent topic:

ReflectiveMemoryFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-getdatachannels.html language=enus -->
## TOPIC 03507: GetDataChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-getdatachannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-getdatachannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ReflectiveMemoryDataChannel elements from the current ReflectiveMemoryFolder. This method gets the individual data channels that are categorized under the current folder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReflectiveMemoryDataChan

### GetDataChannels()

Gets an array that contains the [ReflectiveMemoryDataChannel](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannel.html) elements from the current [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html). This method gets the individual data channels that are categorized under the current folder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReflectiveMemoryDataChannel](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannel.html)[] GetDataChannels()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ReflectiveMemoryDataChannel](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannel.html) elements from the current [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html).

Parent topic:

ReflectiveMemoryFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-getfolders.html language=enus -->
## TOPIC 03508: GetFolders()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-getfolders.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-getfolders.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ReflectiveMemoryFolder elements from the current ReflectiveMemoryFolder. This method gets the subfolders of the current folder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReflectiveMemoryFolder[] GetFolders()RemarksModifications you make

### GetFolders()

Gets an array that contains the [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) elements from the current [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html). This method gets the subfolders of the current folder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html)[] GetFolders()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) elements from the current [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html).

Parent topic:

ReflectiveMemoryFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-reflectivememoryfolder__string-string.html language=enus -->
## TOPIC 03509: ReflectiveMemoryFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-reflectivememoryfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder-reflectivememoryfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ReflectiveMemoryFolder with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReflectiveMemoryFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the folder. Descriptionstri

### ReflectiveMemoryFolder(string, string)

Initializes a new instance of [ReflectiveMemoryFolder](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html) with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ReflectiveMemoryFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the folder. |
| Description | string | The description of the folder. |

Parent topic:

ReflectiveMemoryFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html language=enus -->
## TOPIC 03510: ReflectiveMemoryFolder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a folder under a reflective memory device. Folders can contain data channels or additional sub-folders. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ReflectiveMemoryFolder : SectionRemarksUse the members of this class to add or access d

### ReflectiveMemoryFolder Class

Represents a folder under a reflective memory device. Folders can contain data channels or additional sub-folders.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ReflectiveMemoryFolder : Section

#### Remarks

Use the members of this class to add or access data channels or sub-folders under a reflective memory folder.

**Accessing this Class**

- [AddFolder(ReflectiveMemoryFolder, out Error)](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels-addfolder__reflectivememoryfolder-out.html)
- [GetFolders](nationalinstruments-veristand-systemdefinitionapi-reflectivememorydatachannels-getfolders.html)
- ReflectiveMemoryFolder Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ReflectiveMemoryFolder(string, string) | Initializes a new instance of ReflectiveMemoryFolder with the specified name and description. |

#### Methods

| Name | Description |
| --- | --- |
| AddDataChannel(ReflectiveMemoryDataChannel, out Error) | Adds the specified ReflectiveMemoryFolder under the folder. |
| AddDataChannel(ReflectiveMemoryDataChannel) | Adds the specified ReflectiveMemoryDataChannel under the folder. |
| AddFolder(ReflectiveMemoryFolder) | Adds the specified ReflectiveMemoryFolder under the Data Channels section. |
| AddFolder(ReflectiveMemoryFolder, out Error) | Adds the specified ReflectiveMemoryFolder under the Data Channels section. |
| GetDataChannels() | Gets an array that contains the ReflectiveMemoryDataChannel elements from the current ReflectiveMemoryFolder. This method gets the individual data channels that are categorized under the current folder. |
| GetFolders() | Gets an array that contains the ReflectiveMemoryFolder elements from the current ReflectiveMemoryFolder. This method gets the subfolders of the current folder. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getringreadlatecount.html language=enus -->
## TOPIC 03511: GetRingReadLateCount()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getringreadlatecount.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getringreadlatecount.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Ring Read Late Count channel for a ReflectiveMemory device, which tracks how often the device is late reading data from the reflective memory network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReflectiveMemoryRingReadLateCount GetRingReadLateCount()ReturnsA Re

### GetRingReadLateCount()

Gets the Ring Read Late Count channel for a [ReflectiveMemory](nationalinstruments-veristand-systemdefinitionapi-reflectivememory.html) device, which tracks how often the device is late reading data from the reflective memory network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReflectiveMemoryRingReadLateCount](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryringreadlatecount.html) GetRingReadLateCount()

#### Returns

A [ReflectiveMemoryRingReadLateCount](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryringreadlatecount.html) reference.

Parent topic:

ReflectiveMemoryInformationChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getwritelatecount.html language=enus -->
## TOPIC 03512: GetWriteLateCount()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getwritelatecount.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getwritelatecount.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Write Late Count channel for a ReflectiveMemory device, which tracks how often the device is late writing data to the reflective memory network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReflectiveMemoryWriteLateCount GetWriteLateCount()ReturnsA ReflectiveMemo

### GetWriteLateCount()

Gets the Write Late Count channel for a [ReflectiveMemory](nationalinstruments-veristand-systemdefinitionapi-reflectivememory.html) device, which tracks how often the device is late writing data to the reflective memory network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReflectiveMemoryWriteLateCount](nationalinstruments-veristand-systemdefinitionapi-reflectivememorywritelatecount.html) GetWriteLateCount()

#### Returns

A [ReflectiveMemoryWriteLateCount](nationalinstruments-veristand-systemdefinitionapi-reflectivememorywritelatecount.html) reference.

Parent topic:

ReflectiveMemoryInformationChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels.html language=enus -->
## TOPIC 03513: ReflectiveMemoryInformationChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Information Channels section under a reflective memory device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ReflectiveMemoryInformationChannels : SectionRemarksUse the members of this class to access the Late Count channels for the

### ReflectiveMemoryInformationChannels Class

Represents the **Information Channels** section under a reflective memory device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ReflectiveMemoryInformationChannels : Section

#### Remarks

Use the members of this class to access the Late Count channels for the device.

**Accessing this Class**

- [GetInformationChannels](nationalinstruments-veristand-systemdefinitionapi-reflectivememory-getinformationchannels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetRingReadLateCount() | Gets the Ring Read Late Count channel for a ReflectiveMemory device, which tracks how often the device is late reading data from the reflective memory network. |
| GetWriteLateCount() | Gets the Write Late Count channel for a ReflectiveMemory device, which tracks how often the device is late writing data to the reflective memory network. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinterrupttype.html language=enus -->
## TOPIC 03514: ReflectiveMemoryInterruptType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinterrupttype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinterrupttype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of interrupt a ReflectiveMemory device sends or receives. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ReflectiveMemoryInterruptTypeRemarksAll of the reflective memory interrupts in NI VeriStand are second tier interrupts. If enabled on the receivi

### ReflectiveMemoryInterruptType Enumeration

Specifies the type of interrupt a [ReflectiveMemory](nationalinstruments-veristand-systemdefinitionapi-reflectivememory.html) device sends or receives.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ReflectiveMemoryInterruptType

#### Remarks

Note

Refer to the hardware documentation for your reflective memory device for detailed information about how specific nodes handle interrupts.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| LinkResetInterrupt | 0 | A reset node request. This interrupt does not cause an immediate reset, and the ID of the sending node is not stored in the receiving node's Sender ID FIFO. This interrupt simply sets a bit in the Local Input Status Register of the receiving node. Because this interrupt does not force-reset the node, you can use it for any purpose. |
| NetworkInterrupt1 |  | Network interrupt 1. This is a general purpose interrupt. The ID of the sending node is stored in the receiving node's Sender ID FIFO, and the interrupt data is stored in a companion data FIFO. |
| NetworkInterrupt2 |  | Network interrupt 2. This is a general purpose interrupt. The ID of the sending node is stored in the receiving node's Sender ID FIFO, and the interrupt data is stored in a companion data FIFO. |
| NetworkInterrupt3 |  | Network interrupt 3. This is a general purpose interrupt. The ID of the sending node is stored in the receiving node's Sender ID FIFO, and the interrupt data is stored in a companion data FIFO. |
| NetworkInitInterrupt |  | A network initialization interrupt, which is sent when you initialize or start up the reflective memory network. The ID of the sending node is stored in the receiving node's Sender ID FIFO, and the interrupt data is stored in a companion data FIFO. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-exportmemorytable.html language=enus -->
## TOPIC 03515: ExportMemoryTable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-exportmemorytable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-exportmemorytable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ExportMemoryTable { get; set; }Returnstrue if the memory table is exported to a text file at compile time.

### ExportMemoryTable

Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ExportMemoryTable { get; set; }

#### Returns

true if the memory table is exported to a text file at compile time.

Parent topic:

ReflectiveMemoryNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-exportmemorytablefile.html language=enus -->
## TOPIC 03516: ExportMemoryTableFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-exportmemorytablefile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-exportmemorytablefile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the file path for the text file to export the memory table to at compile time if ExportMemoryTable is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic byte[] ExportMemoryTableFile { get; set; }ReturnsThe memory table.

### ExportMemoryTableFile

Gets or sets the file path for the text file to export the memory table to at compile time if [ExportMemoryTable](nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-exportmemorytable.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public byte[] ExportMemoryTableFile { get; set; }

#### Returns

The memory table.

Parent topic:

ReflectiveMemoryNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-maximumendmemoryaddress.html language=enus -->
## TOPIC 03517: MaximumEndMemoryAddress

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-maximumendmemoryaddress.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-maximumendmemoryaddress.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with StartMemoryAddress to specify the maximum amount of reflected memory allocated to NI VeriStand. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int MaximumEnd

### MaximumEndMemoryAddress

Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with [StartMemoryAddress](nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-startmemoryaddress.html) to specify the maximum amount of reflected memory allocated to NI VeriStand.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int MaximumEndMemoryAddress { get; set; }

#### Remarks

Specify sufficient space to pass NI VeriStand channel data around the reflective memory network without consuming the entire network. If you specify insufficient memory, NI VeriStand returns an error when you run the system definition. Allocating too much memory to NI VeriStand channel data can prevent other data from writing to the network.

**Related Topics**

- [StartMemoryAddress](nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-startmemoryaddress.html)

#### Returns

The maximum end address, as an integer.

Parent topic:

ReflectiveMemoryNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-startmemoryaddress.html language=enus -->
## TOPIC 03518: StartMemoryAddress

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-startmemoryaddress.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-startmemoryaddress.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with MaximumEndMemoryAddress to specify the maximum amount of reflected memory allocated to NI VeriStand. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int StartMemory

### StartMemoryAddress

Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with [MaximumEndMemoryAddress](nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-maximumendmemoryaddress.html) to specify the maximum amount of reflected memory allocated to NI VeriStand.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int StartMemoryAddress { get; set; }

#### Remarks

Specify sufficient space to pass NI VeriStand channel data around the reflective memory network without consuming the entire network. If you specify insufficient memory, NI VeriStand returns an error when you run the system definition. Allocating too much memory to NI VeriStand channel data can prevent other data from writing to the network.

**Related Topics**

- [MaximumEndMemoryAddress](nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork-maximumendmemoryaddress.html)

#### Returns

The start address, as an integer.

Parent topic:

ReflectiveMemoryNetwork Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork.html language=enus -->
## TOPIC 03519: ReflectiveMemoryNetwork Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorynetwork.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the reflective memory network that ReflectiveMemory devices use to share data. A single system definition can have only one reflective memory network. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ReflectiveMemoryNetwork : SectionRemarks

### ReflectiveMemoryNetwork Class

Represents the reflective memory network that [ReflectiveMemory](nationalinstruments-veristand-systemdefinitionapi-reflectivememory.html) devices use to share data. A single system definition can have only one reflective memory network.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ReflectiveMemoryNetwork : Section

#### Remarks

Use the members of this class to set the amount of space in reflective memory to reserve for NI VeriStand and to export the memory table NI VeriStand creates at compile time.

**Accessing this Class**

- [GetReflectiveMemoryNetwork](nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork-getreflectivememorynetwork.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ExportMemoryTable | Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file. |
| ExportMemoryTableFile | Gets or sets the file path for the text file to export the memory table to at compile time if ExportMemoryTable is true. |
| MaximumEndMemoryAddress | Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with StartMemoryAddress to specify the maximum amount of reflected memory allocated to NI VeriStand. |
| StartMemoryAddress | Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with MaximumEndMemoryAddress to specify the maximum amount of reflected memory allocated to NI VeriStand. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememoryringreadlatecount.html language=enus -->
## TOPIC 03520: ReflectiveMemoryRingReadLateCount Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememoryringreadlatecount.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememoryringreadlatecount.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Ring Read Late Count channel of a reflective memory device. This channel increments any time the device is not able to read a section of data from reflective memory because the section was still getting written to by another device. If this channel increments, the section of invalid dat

### ReflectiveMemoryRingReadLateCount Class

Represents a **Ring Read Late Count** channel of a reflective memory device. This channel increments any time the device is not able to read a section of data from reflective memory because the section was still getting written to by another device. If this channel increments, the section of invalid data was not copied to the local channels.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ReflectiveMemoryRingReadLateCount : Channel

#### Remarks

Use the members of this class to get information about the channel.

**Accessing this Class**

- [GetRingReadLateCount](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getringreadlatecount.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-reflectivememorywritelatecount.html language=enus -->
## TOPIC 03521: ReflectiveMemoryWriteLateCount Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-reflectivememorywritelatecount.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-reflectivememorywritelatecount.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Node Write Late Count channel of a reflective memory device. This channel increments any time the device is not able to write data to the reflective memory network because a new iteration of the Primary Control Loop started before the write operation was complete. In this situation, the

### ReflectiveMemoryWriteLateCount Class

Represents a **Node Write Late Count** channel of a reflective memory device. This channel increments any time the device is not able to write data to the reflective memory network because a new iteration of the Primary Control Loop started before the write operation was complete. In this situation, the PCL does not write or read any data for the iteration where the write operation failed to complete.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ReflectiveMemoryWriteLateCount : Channel

#### Remarks

Use the members of this class to get information about the channel.

**Accessing this Class**

- [GetWriteLateCount](nationalinstruments-veristand-systemdefinitionapi-reflectivememoryinformationchannels-getwritelatecount.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-replaybehavior.html language=enus -->
## TOPIC 03522: ReplayBehavior Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-replaybehavior.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-replaybehavior.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether and how frames in a data replay file on an NI-XNET CAN port are filtered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ReplayBehaviorMembersNameValueDescriptionReplayEntireFile0Replays all the frames in the data replay file. ExcludeFrameIDs1Replays

### ReplayBehavior Enumeration

Specifies whether and how frames in a data replay file on an NI-XNET CAN port are filtered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ReplayBehavior

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ReplayEntireFile | 0 | Replays all the frames in the data replay file. |
| ExcludeFrameIDs | 1 | Replays all frames except those specified by FrameIDs. |
| IncludeFrameIDs | 2 | Replays only the frames specified by FrameIDs. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-addchannelmappings__string_arr1-string_arr1-out.html language=enus -->
## TOPIC 03523: AddChannelMappings(string[], string[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-addchannelmappings__string_arr1-string_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-addchannelmappings__string_arr1-string_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds new channel mappings to the system. The source channels map to the destination channels, but the destination channels store the mapping information. This method overwrites any pre-existing mapping information on a destination channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinit

### AddChannelMappings(string[], string[], out Error)

Adds new channel mappings to the system. The source channels map to the destination channels, but the destination channels store the mapping information. This method overwrites any pre-existing mapping information on a destination channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddChannelMappings(string[] channelPathSources, string[] channelPathDestinations, out Error error)

#### Remarks

The *channelPathSources*  and *channelPathDestinations*  arrays are associated by index, such that the source channel at index *n* in *channelPathSources*  maps to the destination channel at the same index *n* in *channelPathDestinations* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPathSources | string[] | A list of source channel paths. |
| channelPathDestinations | string[] | A list of destination channel paths. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the channel mappings were added successfully.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-addchannelmappings__string_arr1-string_arr1.html language=enus -->
## TOPIC 03524: AddChannelMappings(string[], string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-addchannelmappings__string_arr1-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-addchannelmappings__string_arr1-string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds new channel mappings to the system. The source channels map to the destination channels, but the destination channels store the mapping information. This method overwrites any pre-existing mapping information on a destination channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinit

### AddChannelMappings(string[], string[])

Adds new channel mappings to the system. The source channels map to the destination channels, but the destination channels store the mapping information. This method overwrites any pre-existing mapping information on a destination channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddChannelMappings(string[] channelPathSources, string[] channelPathDestinations)

#### Remarks

The *channelPathSources*  and *channelPathDestinations*  arrays are associated by index, such that the source channel at index *n* in *channelPathSources*  maps to the destination channel at the same index *n* in *channelPathDestinations* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPathSources | string[] | A list of source channel paths. |
| channelPathDestinations | string[] | A list of destination channel paths. |

#### Returns

true if the channel mappings were added successfully.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-clearchannelmappings.html language=enus -->
## TOPIC 03525: ClearChannelMappings()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-clearchannelmappings.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-clearchannelmappings.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all channel mappings in the system. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ClearChannelMappings()

### ClearChannelMappings()

Clears all channel mappings in the system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ClearChannelMappings()

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-creationdate.html language=enus -->
## TOPIC 03526: CreationDate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-creationdate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-creationdate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the creation date of the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double CreationDate { get; set; }ReturnsThe date and time the file was created.

### CreationDate

Gets or sets the creation date of the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double CreationDate { get; set; }

#### Returns

The date and time the file was created.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-creator.html language=enus -->
## TOPIC 03527: Creator

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-creator.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-creator.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the user account name of the system definition file creator. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Creator { get; set; }ReturnsThe user account name of the file creator.

### Creator

Gets or sets the user account name of the system definition file creator.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Creator { get; set; }

#### Returns

The user account name of the file creator.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-deletechannelmappings__string_arr1.html language=enus -->
## TOPIC 03528: DeleteChannelMappings(string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-deletechannelmappings__string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-deletechannelmappings__string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes channel mappings on the specified channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void DeleteChannelMappings(string[] channelPathDestinations)ParametersNameTypeDescriptionchannelPathDestinationsstring[]A list of channel paths.

### DeleteChannelMappings(string[])

Removes channel mappings on the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void DeleteChannelMappings(string[] channelPathDestinations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPathDestinations | string[] | A list of channel paths. |

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-getaliases.html language=enus -->
## TOPIC 03529: GetAliases()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-getaliases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-getaliases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Aliases section of the system definition, which contains any channel aliases you define. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Aliases GetAliases()ReturnsAn Aliases object.

### GetAliases()

Gets the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section of the system definition, which contains any channel aliases you define.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) GetAliases()

#### Returns

An [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) object.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-getchannelmappings__out-out.html language=enus -->
## TOPIC 03530: GetChannelMappings(out string[], out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-getchannelmappings__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-getchannelmappings__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all mapped channels in the system. The arrays this method returns are data copies. Neither the array containers nor their contents can be modified directly. Use the AddChannelMappings(string[], string[], out Error), ClearChannelMappings, or DeleteChannelMappings methods to modify channel mappin

### GetChannelMappings(out string[], out string[])

Gets all mapped channels in the system. The arrays this method returns are data copies. Neither the array containers nor their contents can be modified directly. Use the [AddChannelMappings(string[], string[], out Error)](nationalinstruments-veristand-systemdefinitionapi-root-addchannelmappings__string_arr1-string_arr1-out.html), [ClearChannelMappings](nationalinstruments-veristand-systemdefinitionapi-root-clearchannelmappings.html), or [DeleteChannelMappings](nationalinstruments-veristand-systemdefinitionapi-root-deletechannelmappings__string_arr1.html) methods to modify channel mapping data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetChannelMappings(out string[] channelPathSources, out string[] channelPathDestinations)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPathSources | out string[] | Upon return, contains an array of source channel paths. |
| channelPathDestinations | out string[] | Upon return, contains an array of destination channel paths. |

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-getdatasharingnetwork.html language=enus -->
## TOPIC 03531: GetDataSharingNetwork()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-getdatasharingnetwork.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-getdatasharingnetwork.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DataSharingNetwork section of the system definition, which contains the reflective memory network that reflective memory devices use to share data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DataSharingNetwork GetDataSharingNetwork()ReturnsA DataSharingNetwork

### GetDataSharingNetwork()

Gets the [DataSharingNetwork](nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork.html) section of the system definition, which contains the reflective memory network that reflective memory devices use to share data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DataSharingNetwork](nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork.html) GetDataSharingNetwork()

#### Returns

A [DataSharingNetwork](nationalinstruments-veristand-systemdefinitionapi-datasharingnetwork.html) object.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-getscales.html language=enus -->
## TOPIC 03532: GetScales()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-getscales.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-getscales.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the scales section of the system definition, which contains any scales you define. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scales GetScales()ReturnsA Scales object.

### GetScales()

Gets the scales section of the system definition, which contains any scales you define.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) GetScales()

#### Returns

A Scales object.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-getsysteminitialization.html language=enus -->
## TOPIC 03533: GetSystemInitialization()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-getsysteminitialization.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-getsysteminitialization.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SystemInitialization section of the system definition, which specifies the deployment order and reboot action of targets. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SystemInitialization GetSystemInitialization()ReturnsA SystemInitialization object.

### GetSystemInitialization()

Gets the [SystemInitialization](nationalinstruments-veristand-systemdefinitionapi-systeminitialization.html) section of the system definition, which specifies the deployment order and reboot action of targets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SystemInitialization](nationalinstruments-veristand-systemdefinitionapi-systeminitialization.html) GetSystemInitialization()

#### Returns

A [SystemInitialization](nationalinstruments-veristand-systemdefinitionapi-systeminitialization.html) object.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-getsystemmappings.html language=enus -->
## TOPIC 03534: GetSystemMappings()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-getsystemmappings.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-getsystemmappings.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SystemMappings section of the system definition, which contains channel mapping information. You can map two channels so that one channel, the source, sends data to the second channel, the destination. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SystemMappings G

### GetSystemMappings()

Gets the [SystemMappings](nationalinstruments-veristand-systemdefinitionapi-systemmappings.html) section of the system definition, which contains channel mapping information. You can map two channels so that one channel, the source, sends data to the second channel, the destination.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SystemMappings](nationalinstruments-veristand-systemdefinitionapi-systemmappings.html) GetSystemMappings()

#### Returns

A [SystemMappings](nationalinstruments-veristand-systemdefinitionapi-systemmappings.html) object.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-gettargets.html language=enus -->
## TOPIC 03535: GetTargets()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-gettargets.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-gettargets.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Targets section, which contains all the targets you add to the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Targets GetTargets()RemarksFor example code and more information about this method, refer to one of the following help topics: LabVIEW W

### GetTargets()

Gets the [Targets](nationalinstruments-veristand-systemdefinitionapi-targets.html) section, which contains all the targets you add to the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Targets](nationalinstruments-veristand-systemdefinitionapi-targets.html) GetTargets()

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

A [Targets](nationalinstruments-veristand-systemdefinitionapi-targets.html) object.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-refreshnodedependencies.html language=enus -->
## TOPIC 03536: RefreshNodeDependencies()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-refreshnodedependencies.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-refreshnodedependencies.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Evaluates broken dependencies on other nodes to determine if the dependencies can be automatically repaired. Consider the situation where the current node was dependent on another node, and the other node is deleted. If the other node is later added back to the system definition, this method repairs

### RefreshNodeDependencies()

Evaluates broken dependencies on other nodes to determine if the dependencies can be automatically repaired. Consider the situation where the current node was dependent on another node, and the other node is deleted. If the other node is later added back to the system definition, this method repairs the broken dependency.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Error RefreshNodeDependencies()

#### Returns

Returns an error object.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root-version.html language=enus -->
## TOPIC 03537: Version

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root-version.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root-version.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the system definition file version number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Version { get; set; }ReturnsThe version information.

### Version

Gets or sets the system definition file version number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Version { get; set; }

#### Returns

The version information.

Parent topic:

Root Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-root.html language=enus -->
## TOPIC 03538: Root Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-root.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-root.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the root node of the system definition. Derives fromBaseNodeBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Root : BaseNode, BaseNodeRemarksUse the members of this class to get and set information about the version and creation of the system definiti

### Root Class

Represents the root node of the system definition.

#### Derives from

- BaseNode
- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Root : BaseNode, BaseNode

#### Remarks

Use the members of this class to get and set information about the version and creation of the system definition, and to add or access targets, channel mappings, data sharing networks, aliases, and so on.

**Accessing this Class**

- [GetDocumentRoot](nationalinstruments-veristand-systemdefinitionapi-basenode-getdocumentroot.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| CreationDate | Gets or sets the creation date of the system definition file. |
| Creator | Gets or sets the user account name of the system definition file creator. |
| Version | Gets or sets the system definition file version number. |

#### Methods

| Name | Description |
| --- | --- |
| AddChannelMappings(string[], string[], out Error) | Adds new channel mappings to the system. The source channels map to the destination channels, but the destination channels store the mapping information. This method overwrites any pre-existing mapping information on a destination channel. |
| AddChannelMappings(string[], string[]) | Adds new channel mappings to the system. The source channels map to the destination channels, but the destination channels store the mapping information. This method overwrites any pre-existing mapping information on a destination channel. |
| ClearChannelMappings() | Clears all channel mappings in the system. |
| DeleteChannelMappings(string[]) | Removes channel mappings on the specified channels. |
| GetAliases() | Gets the Aliases section of the system definition, which contains any channel aliases you define. |
| GetChannelMappings(out string[], out string[]) | Gets all mapped channels in the system. The arrays this method returns are data copies. Neither the array containers nor their contents can be modified directly. Use the AddChannelMappings(string[], string[], out Error), ClearChannelMappings, or DeleteChannelMappings methods to modify channel mapping data. |
| GetDataSharingNetwork() | Gets the DataSharingNetwork section of the system definition, which contains the reflective memory network that reflective memory devices use to share data. |
| GetScales() | Gets the scales section of the system definition, which contains any scales you define. |
| GetSystemInitialization() | Gets the SystemInitialization section of the system definition, which specifies the deployment order and reboot action of targets. |
| GetSystemMappings() | Gets the SystemMappings section of the system definition, which contains channel mapping information. You can map two channels so that one channel, the source, sends data to the second channel, the destination. |
| GetTargets() | Gets the Targets section, which contains all the targets you add to the system definition. |
| RefreshNodeDependencies() | Evaluates broken dependencies on other nodes to determine if the dependencies can be automatically repaired. Consider the situation where the current node was dependent on another node, and the other node is deleted. If the other node is later added back to the system definition, this method repairs the broken dependency. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-isfaultable.html language=enus -->
## TOPIC 03539: IsFaultable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-isfaultable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-isfaultable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether channels under this section are faultable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsFaultable { get; }

### IsFaultable

Indicates whether channels under this section are faultable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsFaultable { get; }

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-isscalable.html language=enus -->
## TOPIC 03540: IsScalable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-isscalable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-isscalable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether channels under this section are scalable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsScalable { get; }

### IsScalable

Indicates whether channels under this section are scalable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsScalable { get; }

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-loadconfigurationfile__basenodetype-string-out.html language=enus -->
## TOPIC 03541: LoadConfigurationFile(BaseNodeType, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-loadconfigurationfile__basenodetype-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-loadconfigurationfile__basenodetype-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Load the RuntimeConfiguration under the specified parent RuntimeConfigurableSection. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool LoadConfigurationFile(BaseNodeType runtimeConfigurableNode, string configurationFilePath, out Error error)ParametersNameTypeDescri

### LoadConfigurationFile(BaseNodeType, string, out Error)

Load the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) under the specified parent [RuntimeConfigurableSection](nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool LoadConfigurationFile(BaseNodeType runtimeConfigurableNode, string configurationFilePath, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableNode | BaseNodeType | Specifies the parent node |
| configurationFilePath | string | Specifies the RuntimeConfigurableSection file path |
| error | out Error | Upon return, contains the error that caused failure to load the RuntimeConfiguration under this section. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) was successfully loaded under this section.

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-loadconfigurationfile__string-out.html language=enus -->
## TOPIC 03542: LoadConfigurationFile(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-loadconfigurationfile__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-loadconfigurationfile__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the RuntimeConfiguration under this section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool LoadConfigurationFile(string configurationFilePath, out Error error)ParametersNameTypeDescriptionconfigurationFilePathstringSpecifies the RuntimeConfiguration file path.er

### LoadConfigurationFile(string, out Error)

Loads the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) under this section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool LoadConfigurationFile(string configurationFilePath, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| configurationFilePath | string | Specifies the RuntimeConfiguration file path. |
| error | out Error | Upon return, contains the error that cause the failure of loading RuntimeConfiguration under this section. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) was successfully loaded under this section.

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-reservedchannelcapacity.html language=enus -->
## TOPIC 03543: ReservedChannelCapacity

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-reservedchannelcapacity.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-reservedchannelcapacity.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the number of channels that can be added under this section while the system is deployed. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint ReservedChannelCapacity { get; }RemarksFor multidimensional channels, each element counts as one channel against this lim

### ReservedChannelCapacity

Represents the number of channels that can be added under this section while the system is deployed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint ReservedChannelCapacity { get; }

#### Remarks

For multidimensional channels, each element counts as one channel against this limit.

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-runtimeconfigurablesection__string-uint-bool-bool.html language=enus -->
## TOPIC 03544: RuntimeConfigurableSection(string, uint, bool, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-runtimeconfigurablesection__string-uint-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-runtimeconfigurablesection__string-uint-bool-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the RuntimeConfigurableSection. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RuntimeConfigurableSection(string name, uint reservedChannelCapacity, bool isFaultable, bool isScalable)ParametersNameTypeDescriptionnamestringThe name of the runtim

### RuntimeConfigurableSection(string, uint, bool, bool)

Initializes a new instance of the [RuntimeConfigurableSection](nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public RuntimeConfigurableSection(string name, uint reservedChannelCapacity, bool isFaultable, bool isScalable)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the runtime configuration. |
| reservedChannelCapacity | uint | Specifies the number of channels that can be added under this section while the system is deployed. |
| isFaultable | bool | Specifies whether channels under this section are faultable. |
| isScalable | bool | Specifies whether channels under this section are scalable. |

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-runtimeconfigurablesection__string.html language=enus -->
## TOPIC 03545: RuntimeConfigurableSection(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-runtimeconfigurablesection__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-runtimeconfigurablesection__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the RuntimeConfigurableSection. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RuntimeConfigurableSection(string name)ParametersNameTypeDescriptionnamestringThe name of the runtime configuration.

### RuntimeConfigurableSection(string)

Initializes a new instance of the [RuntimeConfigurableSection](nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public RuntimeConfigurableSection(string name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the runtime configuration. |

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-unloadconfigurationfile__basenodetype-out.html language=enus -->
## TOPIC 03546: UnloadConfigurationFile(BaseNodeType, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-unloadconfigurationfile__basenodetype-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-unloadconfigurationfile__basenodetype-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unloads the runtime configuration under the specified parent RuntimeConfigurableSection. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool UnloadConfigurationFile(BaseNodeType runtimeConfigurableNode, out Error error)ParametersNameTypeDescriptionruntimeConfigurable

### UnloadConfigurationFile(BaseNodeType, out Error)

Unloads the runtime configuration under the specified parent [RuntimeConfigurableSection](nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool UnloadConfigurationFile(BaseNodeType runtimeConfigurableNode, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeConfigurableNode | BaseNodeType | Specifies the parent node. |
| error | out Error | Upon return, contains the error that caused the failure to unload the RuntimeConfiguration under this section. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) was successfully unloaded from this section.

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-unloadconfigurationfile__out.html language=enus -->
## TOPIC 03547: UnloadConfigurationFile(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-unloadconfigurationfile__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection-unloadconfigurationfile__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unloads the RuntimeConfiguration under this section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UnloadConfigurationFile(out Error error)ParametersNameTypeDescriptionerrorout ErrorUpon return, contains the error that caused the failure to unload the RuntimeConfigura

### UnloadConfigurationFile(out Error)

Unloads the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) under this section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UnloadConfigurationFile(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Upon return, contains the error that caused the failure to unload the RuntimeConfiguration under this section. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) was successfully unloaded from this section.

Parent topic:

RuntimeConfigurableSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection.html language=enus -->
## TOPIC 03548: RuntimeConfigurableSection Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfigurablesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a section where child nodes (sections and channels) can be dynamically added while the system is deployed using IRuntimeConfigurationManager. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class RuntimeConfigurableSection : SectionRemarksThis c

### RuntimeConfigurableSection Class

Represents a section where child nodes (sections and channels) can be dynamically added while the system is deployed using [IRuntimeConfigurationManager](nationalinstruments-veristand-clientapi-iruntimeconfigurationmanager.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class RuntimeConfigurableSection : Section

#### Remarks

This class contains properties that specifies capabilities and reserves capacity for the child nodes.

#### Constructors

| Name | Description |
| --- | --- |
| RuntimeConfigurableSection(string, uint, bool, bool) | Initializes a new instance of the RuntimeConfigurableSection. |
| RuntimeConfigurableSection(string) | Initializes a new instance of the RuntimeConfigurableSection. |

#### Properties

| Name | Description |
| --- | --- |
| IsFaultable | Indicates whether channels under this section are faultable. |
| IsScalable | Indicates whether channels under this section are scalable. |
| ReservedChannelCapacity | Represents the number of channels that can be added under this section while the system is deployed. |

#### Methods

| Name | Description |
| --- | --- |
| LoadConfigurationFile(string, out Error) | Loads the RuntimeConfiguration under this section. |
| UnloadConfigurationFile(out Error) | Unloads the RuntimeConfiguration under this section. |
| LoadConfigurationFile(BaseNodeType, string, out Error) | Load the RuntimeConfiguration under the specified parent RuntimeConfigurableSection. |
| UnloadConfigurationFile(BaseNodeType, out Error) | Unloads the runtime configuration under the specified parent RuntimeConfigurableSection. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-addchildnodes__basenode_arr1-out.html language=enus -->
## TOPIC 03549: AddChildNodes(BaseNode[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-addchildnodes__basenode_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-addchildnodes__basenode_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds sections and channels to the RuntimeConfiguration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddChildNodes(BaseNode[] childNodes, out Error error)ParametersNameTypeDescriptionchildNodesBaseNode[]Specifies the child nodes to be added.errorout ErrorUpon return,

### AddChildNodes(BaseNode[], out Error)

Adds sections and channels to the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddChildNodes(BaseNode[] childNodes, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| childNodes | BaseNode[] | Specifies the child nodes to be added. |
| error | out Error | Upon return, contains the error. |

#### Returns

true if the child nodes are added successfully.

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-basesection.html language=enus -->
## TOPIC 03550: BaseSection

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-basesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-basesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the base section where you can add sections and channels as child nodes for runtime configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDeviceSection BaseSection { get; }

### BaseSection

Gets the base section where you can add sections and channels as child nodes for runtime configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDeviceSection](nationalinstruments-veristand-systemdefinitionapi-customdevicesection.html) BaseSection { get; }

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-getaliases__out-out-out-out.html language=enus -->
## TOPIC 03551: GetAliases(out string, out string[], out string[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-getaliases__out-out-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-getaliases__out-out-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves all aliases from a specified runtime alias folder in the RuntimeConfiguration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetAliases(out string runtimeAliasFolderName, out string[] referencedChannels, out string[] aliasNames, out Error error)ParametersNam

### GetAliases(out string, out string[], out string[], out Error)

Retrieves all aliases from a specified runtime alias folder in the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetAliases(out string runtimeAliasFolderName, out string[] referencedChannels, out string[] aliasNames, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeAliasFolderName | out string | Upon return, Contains the name of the runtime alias folder from which aliases will be retrieved. |
| referencedChannels | out string[] | Upon return, contains the list of channels linked to the aliases in the runtime alias folder. |
| aliasNames | out string[] | Upon return, contains the list of alias names present under the runtime alias folder. |
| error | out Error | Upon return, contains any error that occurred while retrieving the aliases. If no error occurs, this parameter will indicate no error. |

#### Returns

true if the aliases were successfully retrieved from the runtime alias folder, otherwise false

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-getchildnodes.html language=enus -->
## TOPIC 03552: GetChildNodes()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-getchildnodes.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-getchildnodes.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array containing the child nodes under RuntimeConfiguration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode[] GetChildNodes()ReturnsAn array of child nodes under RuntimeConfiguration.

### GetChildNodes()

Gets an array containing the child nodes under [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html)[] GetChildNodes()

#### Returns

An array of child nodes under [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html).

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-runtimeconfiguration__string-string-string-string-string.html language=enus -->
## TOPIC 03553: RuntimeConfiguration(string, string, string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-runtimeconfiguration__string-string-string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-runtimeconfiguration__string-string-string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RuntimeConfiguration with the specified configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RuntimeConfiguration(string name, string description, string creator, string version, string filePath)ParametersNameTypeDescriptionnamestringT

### RuntimeConfiguration(string, string, string, string, string)

Initializes a new instance of [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) with the specified configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public RuntimeConfiguration(string name, string description, string creator, string version, string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the RuntimeConfiguration. |
| description | string | The description of the RuntimeConfiguration. |
| creator | string | The user account name of the RuntimeConfiguration file creator. |
| version | string | The file format version of the rRuntimeConfiguration file. |
| filePath | string | The path to the RuntimeConfiguration file on disk. |

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-runtimeconfiguration__string.html language=enus -->
## TOPIC 03554: RuntimeConfiguration(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-runtimeconfiguration__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-runtimeconfiguration__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RuntimeConfiguration with the specified file path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RuntimeConfiguration(string nivsruntimeconfigFile)ParametersNameTypeDescriptionnivsruntimeconfigFilestringSpecifies the path to the RuntimeConfigu

### RuntimeConfiguration(string)

Initializes a new instance of [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) with the specified file path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public RuntimeConfiguration(string nivsruntimeconfigFile)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nivsruntimeconfigFile | string | Specifies the path to the RuntimeConfiguration file. |

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-saveconfigurationfile__out.html language=enus -->
## TOPIC 03555: SaveConfigurationFile(out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-saveconfigurationfile__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-saveconfigurationfile__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the RuntimeConfiguration to disk. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SaveConfigurationFile(out string error)ParametersNameTypeDescriptionerrorout stringUpon return, contains the error that caused the RuntimeConfiguration file to fail saving. If no err

### SaveConfigurationFile(out string)

Saves the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) to disk.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SaveConfigurationFile(out string error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out string | Upon return, contains the error that caused the RuntimeConfiguration file to fail saving. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) file was saved successfully.

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-saveconfigurationfile__string-out.html language=enus -->
## TOPIC 03556: SaveConfigurationFile(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-saveconfigurationfile__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-saveconfigurationfile__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the RuntimeConfiguration to the specified file path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SaveConfigurationFile(string filePath, out string error)ParametersNameTypeDescriptionfilePathstringThe path to save the RuntimeConfiguration file on disk.errorout

### SaveConfigurationFile(string, out string)

Saves the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) to the specified file path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SaveConfigurationFile(string filePath, out string error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path to save the RuntimeConfiguration file on disk. |
| error | out string | Upon return, contains the error that caused the RuntimeConfiguration file to fail saving. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html) file was saved successfully.

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-setaliases__string-string_arr1-string_arr1-out.html language=enus -->
## TOPIC 03557: SetAliases(string, string[], string[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-setaliases__string-string_arr1-string_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration-setaliases__string-string_arr1-string_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set Aliases for the channels in RuntimeConfiguration. The referencedChannels are relative RuntimeConfiguration. Note: The runtimeAliasFolderName must be unique across all runtime configurations. If it's not unique, then only the first applied configuration with that name will be added; subsequent on

### SetAliases(string, string[], string[], out Error)

Set Aliases for the channels in [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html). The *referencedChannels*  are relative [RuntimeConfiguration](nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html). Note: The *runtimeAliasFolderName*  must be unique across all runtime configurations. If it's not unique, then only the first applied configuration with that name will be added; subsequent ones will be ignored.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetAliases(string runtimeAliasFolderName, string[] referencedChannels, string[] aliasNames, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| runtimeAliasFolderName | string | The name of the alias folder under which aliases will be added. |
| referencedChannels | string[] | The referenced channels. |
| aliasNames | string[] | The alias names. When the configuration is applied, each alias name will be prefixed with runtimeAliasFolderName . |
| error | out Error | Upon return, contains the error that caused the RuntimeConfiguration file to fail saving. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the aliases were successfully applied to the runtime alias folder.

Parent topic:

RuntimeConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html language=enus -->
## TOPIC 03558: RuntimeConfiguration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-runtimeconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a runtime configuration file, which contains section property and channels that can be applied under RuntimeConfigurableSection without having to undeploy the system using APIs from NationalInstruments.VeriStand.ClientAPI.IRuntimeConfiguration. Derives fromNoneSyntaxNamespace: NationalIns

### RuntimeConfiguration Class

Represents a runtime configuration file, which contains section property and channels that can be applied under RuntimeConfigurableSection without having to undeploy the system using APIs from NationalInstruments.VeriStand.ClientAPI.IRuntimeConfiguration.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class RuntimeConfiguration

#### Constructors

| Name | Description |
| --- | --- |
| RuntimeConfiguration(string, string, string, string, string) | Initializes a new instance of RuntimeConfiguration with the specified configuration. |
| RuntimeConfiguration(string) | Initializes a new instance of RuntimeConfiguration with the specified file path. |

#### Properties

| Name | Description |
| --- | --- |
| BaseSection | Gets the base section where you can add sections and channels as child nodes for runtime configuration. |

#### Methods

| Name | Description |
| --- | --- |
| AddChildNodes(BaseNode[], out Error) | Adds sections and channels to the RuntimeConfiguration. |
| GetAliases(out string, out string[], out string[], out Error) | Retrieves all aliases from a specified runtime alias folder in the RuntimeConfiguration. |
| GetChildNodes() | Gets an array containing the child nodes under RuntimeConfiguration. |
| SaveConfigurationFile(out string) | Saves the RuntimeConfiguration to disk. |
| SaveConfigurationFile(string, out string) | Saves the RuntimeConfiguration to the specified file path. |
| SetAliases(string, string[], string[], out Error) | Set Aliases for the channels in RuntimeConfiguration. The referencedChannels are relative RuntimeConfiguration. Note: The runtimeAliasFolderName must be unique across all runtime configurations. If it's not unique, then only the first applied configuration with that name will be added; subsequent ones will be ignored. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-samplemode.html language=enus -->
## TOPIC 03559: SampleMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-samplemode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-samplemode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Whether the AI acquisition is single-point or buffered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum SampleModeMembersNameValueDescriptionSinglePoint0A single point acquisition that runs at the main NI VeriStand loop rate. Waveform1A high-speed acquisition which retu

### SampleMode Enumeration

Whether the AI acquisition is single-point or buffered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum SampleMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SinglePoint | 0 | A single point acquisition that runs at the main NI VeriStand loop rate. |
| Waveform | 1 | A high-speed acquisition which returns waveform data and with timing defined by an associated. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scale-scaletype.html language=enus -->
## TOPIC 03560: ScaleType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scale-scaletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scale-scaletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the scale type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ScaleType ScaleType { get; }ReturnsAn enumeration of ScaleType.

### ScaleType

Gets the scale type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ScaleType](nationalinstruments-veristand-systemdefinitionapi-scaletype.html) ScaleType { get; }

#### Returns

An enumeration of [ScaleType](nationalinstruments-veristand-systemdefinitionapi-scaletype.html).

Parent topic:

Scale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scale-scaleunit.html language=enus -->
## TOPIC 03561: ScaleUnit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scale-scaleunit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scale-scaleunit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the scale unit. This can be any arbitrary string. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ScaleUnit { get; set; }

### ScaleUnit

Gets or sets the scale unit. This can be any arbitrary string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ScaleUnit { get; set; }

Parent topic:

Scale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scale.html language=enus -->
## TOPIC 03562: Scale Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scale.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scale.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a base class for different types of scales allowed in system definition files. You can create scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriS

### Scale Class

Defines a base class for different types of scales allowed in system definition files. You can create scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Scale : Section

#### Remarks

Use the members of this class to get information about a scale. Use members of the [LookupTable](nationalinstruments-veristand-systemdefinitionapi-lookuptable.html), [PolynomialScale](nationalinstruments-veristand-systemdefinitionapi-polynomialscale.html), and [ThermocoupleScale](nationalinstruments-veristand-systemdefinitionapi-thermocouplescale.html) classes to create those types of scales.

**Accessing this Class**

- [GetScaleList(bool)](nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalelist__bool.html)
- [GetScaleList(bool)](nationalinstruments-veristand-systemdefinitionapi-scales-getscalelist__bool.html)

#### Properties

| Name | Description |
| --- | --- |
| ScaleType | Gets the scale type. |
| ScaleUnit | Gets or sets the scale unit. This can be any arbitrary string. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-addnewscalefolder__string-string-out.html language=enus -->
## TOPIC 03563: AddNewScaleFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-addnewscalefolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-addnewscalefolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new ScaleFolder with the specified name and description to another ScaleFolder as a subfolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewScaleFolder(string name, string description, out Error error)ParametersNameTypeDescriptionnamestringThe name of th

### AddNewScaleFolder(string, string, out Error)

Adds a new [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) with the specified name and description to another ScaleFolder as a subfolder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewScaleFolder(string name, string description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the new ScaleFolder. |
| description | string | The description of the new ScaleFolder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-addnewscalefolder__string-string.html language=enus -->
## TOPIC 03564: AddNewScaleFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-addnewscalefolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-addnewscalefolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new ScaleFolder with the specified name and description to another ScaleFolder as a subfolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewScaleFolder(string name, string description)ParametersNameTypeDescriptionnamestringThe name of the new ScaleFolder

### AddNewScaleFolder(string, string)

Adds a new [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) with the specified name and description to another ScaleFolder as a subfolder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewScaleFolder(string name, string description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the new ScaleFolder. |
| description | string | The description of the new ScaleFolder. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscale__scale-out.html language=enus -->
## TOPIC 03565: AddScale(Scale, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscale__scale-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscale__scale-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Scale to the ScaleFolder section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScale(Scale scale, out Error error)ParametersNameTypeDescriptionscaleScaleThe scale to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no

### AddScale(Scale, out Error)

Adds the specified [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) to the ScaleFolder section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScale(Scale scale, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the scale was added successfully.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscale__scale.html language=enus -->
## TOPIC 03566: AddScale(Scale)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscale__scale.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscale__scale.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Scale to the ScaleFolder section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScale(Scale scale)ParametersNameTypeDescriptionscaleScaleThe scale to add.Returnstrue if the scale was added successfully.

### AddScale(Scale)

Adds the specified [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) to the ScaleFolder section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScale(Scale scale)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale to add. |

#### Returns

true if the scale was added successfully.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscalefolder__scalefolder-out.html language=enus -->
## TOPIC 03567: AddScaleFolder(ScaleFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscalefolder__scalefolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscalefolder__scalefolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ScaleFolder to another ScaleFolder as a subfolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScaleFolder(ScaleFolder folder, out Error error)ParametersNameTypeDescriptionfolderScaleFolderThe new ScaleFolder to add.errorout ErrorReturns an Nat

### AddScaleFolder(ScaleFolder, out Error)

Adds the specified [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) to another ScaleFolder as a subfolder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScaleFolder(ScaleFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | ScaleFolder | The new ScaleFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscalefolder__scalefolder.html language=enus -->
## TOPIC 03568: AddScaleFolder(ScaleFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscalefolder__scalefolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-addscalefolder__scalefolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ScaleFolder to another ScaleFolder as a subfolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScaleFolder(ScaleFolder folder)ParametersNameTypeDescriptionfolderScaleFolderThe new ScaleFolder to add.Returnstrue if the ScaleFolder was added succ

### AddScaleFolder(ScaleFolder)

Adds the specified [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) to another ScaleFolder as a subfolder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScaleFolder(ScaleFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | ScaleFolder | The new ScaleFolder to add. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-createscale__string-scaletype-out.html language=enus -->
## TOPIC 03569: CreateScale(string, ScaleType, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-createscale__string-scaletype-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-createscale__string-scaletype-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a scale of the specified type and adds it to the ScaleFolder section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale CreateScale(string name, ScaleType type, out Error error)ParametersNameTypeDescriptionnamestringThe name of the scale.typeScaleTypeThe type of

### CreateScale(string, ScaleType, out Error)

Creates a scale of the specified type and adds it to the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) CreateScale(string name, ScaleType type, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the scale. |
| type | ScaleType | The type of the scale. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Reference to the newly created scale

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-createscale__string-scaletype.html language=enus -->
## TOPIC 03570: CreateScale(string, ScaleType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-createscale__string-scaletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-createscale__string-scaletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a scale of the specified type and adds it to the ScaleFolder section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateScale(string name, ScaleType type)ParametersNameTypeDescriptionnamestringThe name of the scale.typeScaleTypeThe type of the scale. Returns

### CreateScale(string, ScaleType)

Creates a scale of the specified type and adds it to the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateScale(string name, ScaleType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the scale. |
| type | ScaleType | The type of the scale. |

#### Returns

true if the scale was added successfully.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalefolderlist.html language=enus -->
## TOPIC 03571: GetScaleFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalefolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalefolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ScaleFolder elements from the current ScaleFolder section. This method returns only folders that are direct descendants of the ScaleFolder section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ScaleFolder[] GetScaleFolderList()RemarksModifi

### GetScaleFolderList()

Gets an array that contains the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) elements from the current ScaleFolder section. This method returns only folders that are direct descendants of the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html)[] GetScaleFolderList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) elements from the current [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) section.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalefolderlist__bool.html language=enus -->
## TOPIC 03572: GetScaleFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalefolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalefolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains ScaleFolder elements from the current ScaleFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ScaleFolder[] GetScaleFolderList(bool deep)ParametersNameTypeDescriptiondeepboolSpecifies whether the method traverses each child ScaleFolder elemen

### GetScaleFolderList(bool)

Gets an array that contains [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) elements from the current ScaleFolder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html)[] GetScaleFolderList(bool deep)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ScaleFolder element of the ScaleFolder instance. true if the method traverses each child ScaleFolder instance to search for other ScaleFolder instances to traverse or other ScaleFolder elements to add to the result list; otherwise false. |

#### Returns

An array of ScaleFolder elements.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalelist.html language=enus -->
## TOPIC 03573: GetScaleList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Scale elements from the ScaleFolder section. This method returns only scale elements that are direct descendants of the ScaleFolder section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale[] GetScaleList()RemarksModifications you make to

### GetScaleList()

Gets an array that contains the [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) elements from the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) section. This method returns only scale elements that are direct descendants of the ScaleFolder section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html)[] GetScaleList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) elements from the current [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) section.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalelist__bool.html language=enus -->
## TOPIC 03574: GetScaleList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalelist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalelist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains Scale elements from the current ScaleFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale[] GetScaleList(bool deep)ParametersNameTypeDescriptiondeepboolSpecifies whether the method traverses each child ScaleFolder element of the ScaleFold

### GetScaleList(bool)

Gets an array that contains [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) elements from the current [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html)[] GetScaleList(bool deep)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ScaleFolder element of the ScaleFolder instance. true if the method traverses each child ScaleFolder instance to search for other ScaleFolder instances to traverse or other Scale elements to add to the result list; otherwise false. |

#### Returns

An array of Scale elements.

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder-scalefolder__string-string.html language=enus -->
## TOPIC 03575: ScaleFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder-scalefolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder-scalefolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ScaleFolder class with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ScaleFolder(string name, string description)ParametersNameTypeDescriptionnamestringThe name of the ScaleFolder.descriptionstringThe de

### ScaleFolder(string, string)

Initializes a new instance of the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) class with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ScaleFolder(string name, string description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the ScaleFolder. |
| description | string | The description of the ScaleFolder. |

Parent topic:

ScaleFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scalefolder.html language=enus -->
## TOPIC 03576: ScaleFolder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scalefolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scalefolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a folder under the Scales section of the system definition. Folders simply organize scales into logical groups. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ScaleFolder : SectionRemarksUse the members of this class to add a new or acces

### ScaleFolder Class

Represents a folder under the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section of the system definition. Folders simply organize scales into logical groups.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ScaleFolder : Section

#### Remarks

Use the members of this class to add a new or access an existing scale or subfolder within the current scale folder.

**Accessing this Class**

- [GetScaleFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-scales-getscalefolderlist__bool.html)
- [GetScaleFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-scalefolder-getscalefolderlist__bool.html)
- ScaleFolder Constructor

#### Constructors

| Name | Description |
| --- | --- |
| ScaleFolder(string, string) | Initializes a new instance of the ScaleFolder class with the specified name and description. |

#### Methods

| Name | Description |
| --- | --- |
| AddNewScaleFolder(string, string) | Adds a new ScaleFolder with the specified name and description to another ScaleFolder as a subfolder. |
| AddNewScaleFolder(string, string, out Error) | Adds a new ScaleFolder with the specified name and description to another ScaleFolder as a subfolder. |
| AddScale(Scale, out Error) | Adds the specified Scale to the ScaleFolder section. |
| AddScale(Scale) | Adds the specified Scale to the ScaleFolder section. |
| AddScaleFolder(ScaleFolder, out Error) | Adds the specified ScaleFolder to another ScaleFolder as a subfolder. |
| AddScaleFolder(ScaleFolder) | Adds the specified ScaleFolder to another ScaleFolder as a subfolder. |
| CreateScale(string, ScaleType, out Error) | Creates a scale of the specified type and adds it to the ScaleFolder section. |
| CreateScale(string, ScaleType) | Creates a scale of the specified type and adds it to the ScaleFolder section. |
| GetScaleFolderList() | Gets an array that contains the ScaleFolder elements from the current ScaleFolder section. This method returns only folders that are direct descendants of the ScaleFolder section. |
| GetScaleFolderList(bool) | Gets an array that contains ScaleFolder elements from the current ScaleFolder. |
| GetScaleList() | Gets an array that contains the Scale elements from the ScaleFolder section. This method returns only scale elements that are direct descendants of the ScaleFolder section. |
| GetScaleList(bool) | Gets an array that contains Scale elements from the current ScaleFolder. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-addnewscalefolder__string-string-out.html language=enus -->
## TOPIC 03577: AddNewScaleFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-addnewscalefolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-addnewscalefolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ScaleFolder to the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewScaleFolder(string name, string description, out Error error)ParametersNameTypeDescriptionnamestringThe name of the new ScaleFolder.descriptionstringThe descripti

### AddNewScaleFolder(string, string, out Error)

Adds the specified [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) to the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewScaleFolder(string name, string description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the new ScaleFolder. |
| description | string | The description of the new ScaleFolder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-addnewscalefolder__string-string.html language=enus -->
## TOPIC 03578: AddNewScaleFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-addnewscalefolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-addnewscalefolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ScaleFolder to the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewScaleFolder(string name, string description)ParametersNameTypeDescriptionnamestringThe name of the new ScaleFolder.descriptionstringThe description of the new Sca

### AddNewScaleFolder(string, string)

Adds the specified [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) to the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewScaleFolder(string name, string description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the new ScaleFolder. |
| description | string | The description of the new ScaleFolder. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-addscale__scale-out.html language=enus -->
## TOPIC 03579: AddScale(Scale, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-addscale__scale-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-addscale__scale-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Scale to the ScaleFolder section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScale(Scale scale, out Error error)ParametersNameTypeDescriptionscaleScaleThe scale to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no

### AddScale(Scale, out Error)

Adds the specified [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) to the ScaleFolder section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScale(Scale scale, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the scale was added successfully.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-addscale__scale.html language=enus -->
## TOPIC 03580: AddScale(Scale)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-addscale__scale.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-addscale__scale.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Scale to the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScale(Scale scale)ParametersNameTypeDescriptionscaleScaleThe scale to add.Returnstrue if the scale was added successfully.

### AddScale(Scale)

Adds the specified [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) to the Scales section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScale(Scale scale)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scale | Scale | The scale to add. |

#### Returns

true if the scale was added successfully.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-addscalefolder__scalefolder-out.html language=enus -->
## TOPIC 03581: AddScaleFolder(ScaleFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-addscalefolder__scalefolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-addscalefolder__scalefolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ScaleFolder to the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScaleFolder(ScaleFolder folder, out Error error)ParametersNameTypeDescriptionfolderScaleFolderThe new ScaleFolder to add.errorout ErrorReturns an NationalInstruments

### AddScaleFolder(ScaleFolder, out Error)

Adds the specified [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) to the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScaleFolder(ScaleFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | ScaleFolder | The new ScaleFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-addscalefolder__scalefolder.html language=enus -->
## TOPIC 03582: AddScaleFolder(ScaleFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-addscalefolder__scalefolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-addscalefolder__scalefolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ScaleFolder to the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddScaleFolder(ScaleFolder folder)ParametersNameTypeDescriptionfolderScaleFolderThe new ScaleFolder to add.Returnstrue if the ScaleFolder was added successfully.

### AddScaleFolder(ScaleFolder)

Adds the specified [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) to the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddScaleFolder(ScaleFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | ScaleFolder | The new ScaleFolder to add. |

#### Returns

true if the ScaleFolder was added successfully.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-createscale__string-scaletype-out.html language=enus -->
## TOPIC 03583: CreateScale(string, ScaleType, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-createscale__string-scaletype-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-createscale__string-scaletype-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a scale of the specified type and adds it to the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale CreateScale(string name, ScaleType type, out Error error)ParametersNameTypeDescriptionnamestringThe name of the scale.typeScaleTypeThe type of the s

### CreateScale(string, ScaleType, out Error)

Creates a scale of the specified type and adds it to the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) CreateScale(string name, ScaleType type, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the scale. |
| type | ScaleType | The type of the scale. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

reference to the newly created scale

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-createscale__string-scaletype.html language=enus -->
## TOPIC 03584: CreateScale(string, ScaleType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-createscale__string-scaletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-createscale__string-scaletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a scale of the specified type and adds it to the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateScale(string name, ScaleType type)ParametersNameTypeDescriptionnamestringThe name of the scale.typeScaleTypeThe type of the scale. Returnstrue

### CreateScale(string, ScaleType)

Creates a scale of the specified type and adds it to the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateScale(string name, ScaleType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the scale. |
| type | ScaleType | The type of the scale. |

#### Returns

true if the scale was added successfully.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-getscalefolderlist.html language=enus -->
## TOPIC 03585: GetScaleFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-getscalefolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-getscalefolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ScaleFolder elements from the Scales section. This method returns only folders that are direct descendants of the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ScaleFolder[] GetScaleFolderList()RemarksModifications you make t

### GetScaleFolderList()

Gets an array that contains the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) elements from the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section. This method returns only folders that are direct descendants of the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html)[] GetScaleFolderList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) elements from the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-getscalefolderlist__bool.html language=enus -->
## TOPIC 03586: GetScaleFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-getscalefolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-getscalefolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ScaleFolder elements from the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ScaleFolder[] GetScaleFolderList(bool deep)ParametersNameTypeDescriptiondeepboolSpecifies whether the method traverses each child ScaleFolder element

### GetScaleFolderList(bool)

Gets an array that contains the [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html) elements from the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html)[] GetScaleFolderList(bool deep)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ScaleFolder element of the Scales section. true if the method traverses each child ScaleFolder instance to search for other ScaleFolder instances to traverse or other ScaleFolder elements to add to the result list; otherwise false. |

#### Returns

An array of ScaleFolder elements.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-getscalelist.html language=enus -->
## TOPIC 03587: GetScaleList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-getscalelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-getscalelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Scale elements from the Scales section. This method returns only scale elements that are direct descendants of the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale[] GetScaleList()RemarksModifications you make to the conte

### GetScaleList()

Gets an array that contains the [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) elements from the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section. This method returns only scale elements that are direct descendants of the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html)[] GetScaleList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) elements from the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales-getscalelist__bool.html language=enus -->
## TOPIC 03588: GetScaleList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales-getscalelist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales-getscalelist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Scale elements from the Scales section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Scale[] GetScaleList(bool deep)ParametersNameTypeDescriptiondeepboolSpecifies whether the method traverses each child ScaleFolder element of the Scales sec

### GetScaleList(bool)

Gets an array that contains the [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) elements from the [Scales](nationalinstruments-veristand-systemdefinitionapi-scales.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html)[] GetScaleList(bool deep)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ScaleFolder element of the Scales section. true if the method traverses each child ScaleFolder instance to search for other ScaleFolder instances to traverse or other Scale elements to add to the result list; otherwise false. |

#### Returns

An array of Scale elements.

Parent topic:

Scales Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scales.html language=enus -->
## TOPIC 03589: Scales Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scales.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scales.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Scales section of the system definition, which contains Scale objects. Use scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemD

### Scales Class

Represents the **Scales** section of the system definition, which contains [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html) objects. Use scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Scales : Section

#### Remarks

Use the members of this class to add or access a scale or [ScaleFolder](nationalinstruments-veristand-systemdefinitionapi-scalefolder.html).

**Accessing this Class**

- [GetScales](nationalinstruments-veristand-systemdefinitionapi-root-getscales.html)

#### Methods

| Name | Description |
| --- | --- |
| AddNewScaleFolder(string, string) | Adds the specified ScaleFolder to the Scales section. |
| AddNewScaleFolder(string, string, out Error) | Adds the specified ScaleFolder to the Scales section. |
| AddScale(Scale, out Error) | Adds the specified Scale to the ScaleFolder section. |
| AddScale(Scale) | Adds the specified Scale to the Scales section. |
| AddScaleFolder(ScaleFolder, out Error) | Adds the specified ScaleFolder to the Scales section. |
| AddScaleFolder(ScaleFolder) | Adds the specified ScaleFolder to the Scales section. |
| CreateScale(string, ScaleType) | Creates a scale of the specified type and adds it to the Scales section. |
| CreateScale(string, ScaleType, out Error) | Creates a scale of the specified type and adds it to the Scales section. |
| GetScaleFolderList() | Gets an array that contains the ScaleFolder elements from the Scales section. This method returns only folders that are direct descendants of the Scales section. |
| GetScaleFolderList(bool) | Gets an array that contains the ScaleFolder elements from the Scales section. |
| GetScaleList() | Gets an array that contains the Scale elements from the Scales section. This method returns only scale elements that are direct descendants of the Scales section. |
| GetScaleList(bool) | Gets an array that contains the Scale elements from the Scales section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scaletype.html language=enus -->
## TOPIC 03590: ScaleType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scaletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scaletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This enumeration is used to select the Scale Type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ScaleTypeMembersNameValueDescriptionPolynomial0The scale is a Polynomial Scale. ThermocoupleThe scale is a Thermocouple Scale. LookupTableThe scale is a Lookup Table.

### ScaleType Enumeration

This enumeration is used to select the Scale Type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ScaleType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Polynomial | 0 | The scale is a Polynomial Scale. |
| Thermocouple |  | The scale is a Thermocouple Scale. |
| LookupTable |  | The scale is a Lookup Table. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1100-scxi1100__string.html language=enus -->
## TOPIC 03591: SCXI1100(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1100-scxi1100__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1100-scxi1100__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1100 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1100(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1100(string)

Initializes a new instance of [SCXI1100](nationalinstruments-veristand-systemdefinitionapi-scxi1100.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1100(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1100 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1100.html language=enus -->
## TOPIC 03592: SCXI1100 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1100.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1100.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1100 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1100 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1100 Constructor Thread Safe

### SCXI1100 Class

Represents an SCXI-1100 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1100 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1100 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1100(string) | Initializes a new instance of SCXI1100 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1102-scxi1102__string.html language=enus -->
## TOPIC 03593: SCXI1102(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1102-scxi1102__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1102-scxi1102__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1102 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1102(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1102(string)

Initializes a new instance of [SCXI1102](nationalinstruments-veristand-systemdefinitionapi-scxi1102.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1102(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1102 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1102.html language=enus -->
## TOPIC 03594: SCXI1102 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1102.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1102.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1102 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1102 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1102 Constructor Thread Safe

### SCXI1102 Class

Represents an SCXI-1102 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1102 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1102 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1102(string) | Initializes a new instance of SCXI1102 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1102b-scxi1102b__string.html language=enus -->
## TOPIC 03595: SCXI1102B(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1102b-scxi1102b__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1102b-scxi1102b__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1102B with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1102B(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1102B(string)

Initializes a new instance of [SCXI1102B](nationalinstruments-veristand-systemdefinitionapi-scxi1102b.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1102B(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1102B Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1102b.html language=enus -->
## TOPIC 03596: SCXI1102B Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1102b.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1102b.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1102B module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1102B : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1102B Constructor Thread S

### SCXI1102B Class

Represents an SCXI-1102B module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1102B : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1102B Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1102B(string) | Initializes a new instance of SCXI1102B with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1102c-scxi1102c__string.html language=enus -->
## TOPIC 03597: SCXI1102C(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1102c-scxi1102c__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1102c-scxi1102c__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1102C with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1102C(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1102C(string)

Initializes a new instance of [SCXI1102C](nationalinstruments-veristand-systemdefinitionapi-scxi1102c.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1102C(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1102C Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1102c.html language=enus -->
## TOPIC 03598: SCXI1102C Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1102c.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1102c.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1102C module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1102C : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1102C Constructor Thread S

### SCXI1102C Class

Represents an SCXI-1102C module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1102C : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1102C Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1102C(string) | Initializes a new instance of SCXI1102C with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1104-scxi1104__string.html language=enus -->
## TOPIC 03599: SCXI1104(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1104-scxi1104__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1104-scxi1104__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1104 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1104(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1104(string)

Initializes a new instance of [SCXI1104](nationalinstruments-veristand-systemdefinitionapi-scxi1104.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1104(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1104 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1104.html language=enus -->
## TOPIC 03600: SCXI1104 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1104.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1104.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1104 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1104 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1104 Constructor Thread Safe

### SCXI1104 Class

Represents an SCXI-1104 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1104 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1104 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1104(string) | Initializes a new instance of SCXI1104 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1104c-scxi1104c__string.html language=enus -->
## TOPIC 03601: SCXI1104C(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1104c-scxi1104c__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1104c-scxi1104c__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1104C with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1104C(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1104C(string)

Initializes a new instance of [SCXI1104C](nationalinstruments-veristand-systemdefinitionapi-scxi1104c.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1104C(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1104C Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1104c.html language=enus -->
## TOPIC 03602: SCXI1104C Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1104c.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1104c.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1104C module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1104C : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1104C Constructor Thread S

### SCXI1104C Class

Represents an SCXI-1104C module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1104C : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1104C Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1104C(string) | Initializes a new instance of SCXI1104C with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1112-scxi1112__string.html language=enus -->
## TOPIC 03603: SCXI1112(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1112-scxi1112__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1112-scxi1112__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1112 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1112(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1112(string)

Initializes a new instance of [SCXI1112](nationalinstruments-veristand-systemdefinitionapi-scxi1112.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1112(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1112 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1112.html language=enus -->
## TOPIC 03604: SCXI1112 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1112.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1112.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1112 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1112 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1112 Constructor Thread Safe

### SCXI1112 Class

Represents an SCXI-1112 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1112 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1112 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1112(string) | Initializes a new instance of SCXI1112 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1120-scxi1120__string.html language=enus -->
## TOPIC 03605: SCXI1120(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1120-scxi1120__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1120-scxi1120__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1120 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1120(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1120(string)

Initializes a new instance of [SCXI1120](nationalinstruments-veristand-systemdefinitionapi-scxi1120.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1120(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1120 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1120.html language=enus -->
## TOPIC 03606: SCXI1120 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1120.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1120.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1120 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1120 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1120 Constructor Thread Safe

### SCXI1120 Class

Represents an SCXI-1120 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1120 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1120 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1120(string) | Initializes a new instance of SCXI1120 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1120d-scxi1120d__string.html language=enus -->
## TOPIC 03607: SCXI1120D(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1120d-scxi1120d__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1120d-scxi1120d__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1120D with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1120D(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1120D(string)

Initializes a new instance of [SCXI1120D](nationalinstruments-veristand-systemdefinitionapi-scxi1120d.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1120D(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1120D Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1120d.html language=enus -->
## TOPIC 03608: SCXI1120D Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1120d.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1120d.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1120D module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1120D : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1120D Constructor Thread S

### SCXI1120D Class

Represents an SCXI-1120D module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1120D : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1120D Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1120D(string) | Initializes a new instance of SCXI1120D with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1121-scxi1121__string.html language=enus -->
## TOPIC 03609: SCXI1121(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1121-scxi1121__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1121-scxi1121__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1121 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1121(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1121(string)

Initializes a new instance of [SCXI1121](nationalinstruments-veristand-systemdefinitionapi-scxi1121.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1121(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1121 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1121.html language=enus -->
## TOPIC 03610: SCXI1121 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1121.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1121.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1121 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1121 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1121 Constructor Thread Safe

### SCXI1121 Class

Represents an SCXI-1121 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1121 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1121 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1121(string) | Initializes a new instance of SCXI1121 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1122-scxi1122__string.html language=enus -->
## TOPIC 03611: SCXI1122(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1122-scxi1122__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1122-scxi1122__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1122 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1122(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1122(string)

Initializes a new instance of [SCXI1122](nationalinstruments-veristand-systemdefinitionapi-scxi1122.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1122(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1122 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1122.html language=enus -->
## TOPIC 03612: SCXI1122 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1122.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1122.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1122 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1122 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1122 Constructor Thread Safe

### SCXI1122 Class

Represents an SCXI-1122 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1122 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1122 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1122(string) | Initializes a new instance of SCXI1122 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1124-scxi1124__string.html language=enus -->
## TOPIC 03613: SCXI1124(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1124-scxi1124__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1124-scxi1124__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1124 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1124(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1124(string)

Initializes a new instance of [SCXI1124](nationalinstruments-veristand-systemdefinitionapi-scxi1124.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1124(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1124 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1124.html language=enus -->
## TOPIC 03614: SCXI1124 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1124.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1124.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1124 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1124 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1124 Constructor Thread Safe

### SCXI1124 Class

Represents an SCXI-1124 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1124 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1124 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1124(string) | Initializes a new instance of SCXI1124 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1125-scxi1125__string.html language=enus -->
## TOPIC 03615: SCXI1125(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1125-scxi1125__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1125-scxi1125__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1125 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1125(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1125(string)

Initializes a new instance of [SCXI1125](nationalinstruments-veristand-systemdefinitionapi-scxi1125.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1125(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1125 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1125.html language=enus -->
## TOPIC 03616: SCXI1125 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1125.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1125.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1125 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1125 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1125 Constructor Thread Safe

### SCXI1125 Class

Represents an SCXI-1125 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1125 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1125 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1125(string) | Initializes a new instance of SCXI1125 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1126-scxi1126__string.html language=enus -->
## TOPIC 03617: SCXI1126(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1126-scxi1126__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1126-scxi1126__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1126 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1126(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1126(string)

Initializes a new instance of [SCXI1126](nationalinstruments-veristand-systemdefinitionapi-scxi1126.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1126(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1126 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1126.html language=enus -->
## TOPIC 03618: SCXI1126 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1126.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1126.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1126 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1126 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1126 Constructor Thread Safe

### SCXI1126 Class

Represents an SCXI-1126 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1126 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1126 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1126(string) | Initializes a new instance of SCXI1126 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1127-scxi1127__string.html language=enus -->
## TOPIC 03619: SCXI1127(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1127-scxi1127__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1127-scxi1127__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1127 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1127(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1127(string)

Initializes a new instance of [SCXI1127](nationalinstruments-veristand-systemdefinitionapi-scxi1127.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1127(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1127 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1127.html language=enus -->
## TOPIC 03620: SCXI1127 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1127.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1127.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1127 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1127 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1127 Constructor Thread Safe

### SCXI1127 Class

Represents an SCXI-1127 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1127 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1127 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1127(string) | Initializes a new instance of SCXI1127 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1128-scxi1128__string.html language=enus -->
## TOPIC 03621: SCXI1128(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1128-scxi1128__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1128-scxi1128__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1128 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1128(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1128(string)

Initializes a new instance of [SCXI1128](nationalinstruments-veristand-systemdefinitionapi-scxi1128.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1128(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1128 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1128.html language=enus -->
## TOPIC 03622: SCXI1128 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1128.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1128.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1128 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1128 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1128 Constructor Thread Safe

### SCXI1128 Class

Represents an SCXI-1128 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1128 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1128 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1128(string) | Initializes a new instance of SCXI1128 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1140-scxi1140__string.html language=enus -->
## TOPIC 03623: SCXI1140(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1140-scxi1140__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1140-scxi1140__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1140 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1140(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1140(string)

Initializes a new instance of [SCXI1140](nationalinstruments-veristand-systemdefinitionapi-scxi1140.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1140(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1140 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1140.html language=enus -->
## TOPIC 03624: SCXI1140 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1140.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1140.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1140 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1140 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1140 Constructor Thread Safe

### SCXI1140 Class

Represents an SCXI-1140 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1140 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1140 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1140(string) | Initializes a new instance of SCXI1140 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1141-scxi1141__string.html language=enus -->
## TOPIC 03625: SCXI1141(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1141-scxi1141__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1141-scxi1141__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1141 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1141(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1141(string)

Initializes a new instance of [SCXI1141](nationalinstruments-veristand-systemdefinitionapi-scxi1141.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1141(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1141 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1141.html language=enus -->
## TOPIC 03626: SCXI1141 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1141.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1141.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1141 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1141 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1141 Constructor Thread Safe

### SCXI1141 Class

Represents an SCXI-1141 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1141 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1141 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1141(string) | Initializes a new instance of SCXI1141 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1142-scxi1142__string.html language=enus -->
## TOPIC 03627: SCXI1142(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1142-scxi1142__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1142-scxi1142__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1142 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1142(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1142(string)

Initializes a new instance of [SCXI1142](nationalinstruments-veristand-systemdefinitionapi-scxi1142.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1142(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1142 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1142.html language=enus -->
## TOPIC 03628: SCXI1142 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1142.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1142.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1142 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1142 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1142 Constructor Thread Safe

### SCXI1142 Class

Represents an SCXI-1142 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1142 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1142 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1142(string) | Initializes a new instance of SCXI1142 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1143-scxi1143__string.html language=enus -->
## TOPIC 03629: SCXI1143(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1143-scxi1143__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1143-scxi1143__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1143 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1143(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1143(string)

Initializes a new instance of [SCXI1143](nationalinstruments-veristand-systemdefinitionapi-scxi1143.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1143(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1143 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1143.html language=enus -->
## TOPIC 03630: SCXI1143 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1143.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1143.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1143 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1143 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1143 Constructor Thread Safe

### SCXI1143 Class

Represents an SCXI-1143 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1143 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1143 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1143(string) | Initializes a new instance of SCXI1143 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1160-scxi1160__string.html language=enus -->
## TOPIC 03631: SCXI1160(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1160-scxi1160__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1160-scxi1160__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1160 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1160(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1160(string)

Initializes a new instance of [SCXI1160](nationalinstruments-veristand-systemdefinitionapi-scxi1160.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1160(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1160 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1160.html language=enus -->
## TOPIC 03632: SCXI1160 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1160.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1160.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1160 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1160 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1160 Constructor Thread Safe

### SCXI1160 Class

Represents an SCXI-1160 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1160 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1160 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1160(string) | Initializes a new instance of SCXI1160 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1161-scxi1161__string.html language=enus -->
## TOPIC 03633: SCXI1161(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1161-scxi1161__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1161-scxi1161__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1161 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1161(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1161(string)

Initializes a new instance of [SCXI1161](nationalinstruments-veristand-systemdefinitionapi-scxi1161.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1161(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1161 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1161.html language=enus -->
## TOPIC 03634: SCXI1161 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1161.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1161.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1161 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1161 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1161 Constructor Thread Safe

### SCXI1161 Class

Represents an SCXI-1161 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1161 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1161 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1161(string) | Initializes a new instance of SCXI1161 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1162-scxi1162__string.html language=enus -->
## TOPIC 03635: SCXI1162(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1162-scxi1162__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1162-scxi1162__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1162 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1162(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1162(string)

Initializes a new instance of [SCXI1162](nationalinstruments-veristand-systemdefinitionapi-scxi1162.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1162(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1162 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1162.html language=enus -->
## TOPIC 03636: SCXI1162 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1162.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1162.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1162 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1162 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1162 Constructor Thread Safe

### SCXI1162 Class

Represents an SCXI-1162 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1162 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1162 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1162(string) | Initializes a new instance of SCXI1162 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1162hv-scxi1162hv__string.html language=enus -->
## TOPIC 03637: SCXI1162HV(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1162hv-scxi1162hv__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1162hv-scxi1162hv__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1162HV with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1162HV(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1162HV(string)

Initializes a new instance of [SCXI1162HV](nationalinstruments-veristand-systemdefinitionapi-scxi1162hv.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1162HV(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1162HV Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1162hv.html language=enus -->
## TOPIC 03638: SCXI1162HV Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1162hv.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1162hv.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1162HV module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1162HV : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1162HV Constructor Threa

### SCXI1162HV Class

Represents an SCXI-1162HV module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1162HV : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1162HV Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1162HV(string) | Initializes a new instance of SCXI1162HV with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1163-scxi1163__string.html language=enus -->
## TOPIC 03639: SCXI1163(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1163-scxi1163__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1163-scxi1163__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1163 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1163(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1163(string)

Initializes a new instance of [SCXI1163](nationalinstruments-veristand-systemdefinitionapi-scxi1163.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1163(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1163 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1163.html language=enus -->
## TOPIC 03640: SCXI1163 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1163.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1163.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1163 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1163 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1163 Constructor Thread Safe

### SCXI1163 Class

Represents an SCXI-1163 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1163 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1163 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1163(string) | Initializes a new instance of SCXI1163 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1163r-scxi1163r__string.html language=enus -->
## TOPIC 03641: SCXI1163R(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1163r-scxi1163r__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1163r-scxi1163r__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1163R with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1163R(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1163R(string)

Initializes a new instance of [SCXI1163R](nationalinstruments-veristand-systemdefinitionapi-scxi1163r.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1163R(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1163R Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1163r.html language=enus -->
## TOPIC 03642: SCXI1163R Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1163r.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1163r.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1163R module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1163R : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1163R Constructor Thread S

### SCXI1163R Class

Represents an SCXI-1163R module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1163R : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1163R Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1163R(string) | Initializes a new instance of SCXI1163R with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1190-scxi1190__string.html language=enus -->
## TOPIC 03643: SCXI1190(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1190-scxi1190__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1190-scxi1190__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1190 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1190(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1190(string)

Initializes a new instance of [SCXI1190](nationalinstruments-veristand-systemdefinitionapi-scxi1190.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1190(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1190 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1190.html language=enus -->
## TOPIC 03644: SCXI1190 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1190.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1190.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1190 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1190 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1190 Constructor Thread Safe

### SCXI1190 Class

Represents an SCXI-1190 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1190 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1190 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1190(string) | Initializes a new instance of SCXI1190 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1191-scxi1191__string.html language=enus -->
## TOPIC 03645: SCXI1191(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1191-scxi1191__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1191-scxi1191__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1191 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1191(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1191(string)

Initializes a new instance of [SCXI1191](nationalinstruments-veristand-systemdefinitionapi-scxi1191.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1191(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1191 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1191.html language=enus -->
## TOPIC 03646: SCXI1191 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1191.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1191.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1191 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1191 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1191 Constructor Thread Safe

### SCXI1191 Class

Represents an SCXI-1191 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1191 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1191 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1191(string) | Initializes a new instance of SCXI1191 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1192-scxi1192__string.html language=enus -->
## TOPIC 03647: SCXI1192(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1192-scxi1192__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1192-scxi1192__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1192 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1192(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1192(string)

Initializes a new instance of [SCXI1192](nationalinstruments-veristand-systemdefinitionapi-scxi1192.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1192(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1192 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1192.html language=enus -->
## TOPIC 03648: SCXI1192 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1192.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1192.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1192 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1192 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1192 Constructor Thread Safe

### SCXI1192 Class

Represents an SCXI-1192 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1192 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1192 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1192(string) | Initializes a new instance of SCXI1192 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1520-scxi1520__string.html language=enus -->
## TOPIC 03649: SCXI1520(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1520-scxi1520__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1520-scxi1520__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1520 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1520(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1520(string)

Initializes a new instance of [SCXI1520](nationalinstruments-veristand-systemdefinitionapi-scxi1520.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1520(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1520 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1520.html language=enus -->
## TOPIC 03650: SCXI1520 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1520.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1520.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1520 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1520 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1520 Constructor Thread Safe

### SCXI1520 Class

Represents an SCXI-1520 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1520 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1520 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1520(string) | Initializes a new instance of SCXI1520 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1530-scxi1530__string.html language=enus -->
## TOPIC 03651: SCXI1530(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1530-scxi1530__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1530-scxi1530__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1530 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1530(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1530(string)

Initializes a new instance of [SCXI1530](nationalinstruments-veristand-systemdefinitionapi-scxi1530.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1530(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1530 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1530.html language=enus -->
## TOPIC 03652: SCXI1530 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1530.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1530.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1530 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1530 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1530 Constructor Thread Safe

### SCXI1530 Class

Represents an SCXI-1530 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1530 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1530 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1530(string) | Initializes a new instance of SCXI1530 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1531-scxi1531__string.html language=enus -->
## TOPIC 03653: SCXI1531(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1531-scxi1531__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1531-scxi1531__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1531 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1531(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1531(string)

Initializes a new instance of [SCXI1531](nationalinstruments-veristand-systemdefinitionapi-scxi1531.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1531(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1531 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1531.html language=enus -->
## TOPIC 03654: SCXI1531 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1531.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1531.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1531 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1531 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1531 Constructor Thread Safe

### SCXI1531 Class

Represents an SCXI-1531 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1531 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1531 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1531(string) | Initializes a new instance of SCXI1531 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1540-scxi1540__string.html language=enus -->
## TOPIC 03655: SCXI1540(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1540-scxi1540__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1540-scxi1540__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1540 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1540(string Name)ParametersNameTypeDescriptionNamestringThe name of the module.

### SCXI1540(string)

Initializes a new instance of [SCXI1540](nationalinstruments-veristand-systemdefinitionapi-scxi1540.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1540(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the module. |

Parent topic:

SCXI1540 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1540.html language=enus -->
## TOPIC 03656: SCXI1540 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1540.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1540.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1540 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1540 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1540 Constructor Thread Safe

### SCXI1540 Class

Represents an SCXI-1540 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1540 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1540 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1540(string) | Initializes a new instance of SCXI1540 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1581-scxi1581__string.html language=enus -->
## TOPIC 03657: SCXI1581(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1581-scxi1581__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1581-scxi1581__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXI1581 with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXI1581(string Name)ParametersNameTypeDescriptionNamestringThe name of the SCXI1581.

### SCXI1581(string)

Initializes a new instance of [SCXI1581](nationalinstruments-veristand-systemdefinitionapi-scxi1581.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXI1581(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the SCXI1581. |

Parent topic:

SCXI1581 Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxi1581.html language=enus -->
## TOPIC 03658: SCXI1581 Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxi1581.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxi1581.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI-1581 module that you can add to an SCXIChassis. Derives fromSCXIModuleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXI1581 : SCXIModuleRemarksUse the members of this class to access the module. Accessing this ClassSCXI1581 Constructor Thread Safe

### SCXI1581 Class

Represents an SCXI-1581 module that you can add to an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- SCXIModule

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXI1581 : SCXIModule

#### Remarks

Use the members of this class to access the module.

**Accessing this Class**

- SCXI1581 Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXI1581(string) | Initializes a new instance of SCXI1581 with the specified name. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxichassis-addscximodule__scximodule-out.html language=enus -->
## TOPIC 03659: AddSCXIModule(SCXIModule, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxichassis-addscximodule__scximodule-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxichassis-addscximodule__scximodule-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SCXIModule to the SCXI chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSCXIModule(SCXIModule scxiModule, out Error error)ParametersNameTypeDescriptionscxiModuleSCXIModuleThe SCXI module to add.errorout ErrorReturns an NationalInstruments.V

### AddSCXIModule(SCXIModule, out Error)

Adds the specified [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html) to the SCXI chassis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSCXIModule(SCXIModule scxiModule, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scxiModule | SCXIModule | The SCXI module to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the module was added successfully.

Parent topic:

SCXIChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxichassis-addscximodule__scximodule.html language=enus -->
## TOPIC 03660: AddSCXIModule(SCXIModule)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxichassis-addscximodule__scximodule.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxichassis-addscximodule__scximodule.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SCXIModule to the SCXI chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSCXIModule(SCXIModule scxiModule)ParametersNameTypeDescriptionscxiModuleSCXIModuleThe SCXI module to add.Returnstrue if the module was added successfully.

### AddSCXIModule(SCXIModule)

Adds the specified [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html) to the SCXI chassis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSCXIModule(SCXIModule scxiModule)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scxiModule | SCXIModule | The SCXI module to add. |

#### Returns

true if the module was added successfully.

Parent topic:

SCXIChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxichassis-getscximodules.html language=enus -->
## TOPIC 03661: GetSCXIModules()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxichassis-getscximodules.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxichassis-getscximodules.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SCXIModule elements from the current SCXIChassis. This method gets the modules in the chassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXIModule[] GetSCXIModules()RemarksModifications you make to the contents of this list apply to the

### GetSCXIModules()

Gets an array that contains the [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html) elements from the current [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html). This method gets the modules in the chassis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html)[] GetSCXIModules()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html) elements from the current [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

Parent topic:

SCXIChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scxichassis.html language=enus -->
## TOPIC 03662: SCXIChassis Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scxichassis.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scxichassis.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI chassis under a DAQDevice. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXIChassis : SectionRemarksUse the members of this class to add an SCXIModule to the chassis or to get a list of existing modules. Accessing this ClassCrea

### SCXIChassis Class

Represents an SCXI chassis under a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXIChassis : Section

#### Remarks

Use the members of this class to add an [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html) to the chassis or to get a list of existing modules.

**Accessing this Class**

- [CreateSCXIChassis(out Error)](nationalinstruments-veristand-systemdefinitionapi-daqdevice-createscxichassis__out.1.html)
- [GetSCXIChassisSection](nationalinstruments-veristand-systemdefinitionapi-daqdevice-getscxichassissection.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddSCXIModule(SCXIModule, out Error) | Adds the specified SCXIModule to the SCXI chassis. |
| AddSCXIModule(SCXIModule) | Adds the specified SCXIModule to the SCXI chassis. |
| GetSCXIModules() | Gets an array that contains the SCXIModule elements from the current SCXIChassis. This method gets the modules in the chassis. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scximodule-getanaloginputs.html language=enus -->
## TOPIC 03663: GetAnalogInputs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scximodule-getanaloginputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scximodule-getanaloginputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQAnalogInput elements from the current SCXIModule. This method gets the analog input channels of the module. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInput[] GetAnalogInputs()RemarksModifications you make to the contents of t

### GetAnalogInputs()

Gets an array that contains the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) elements from the current [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html). This method gets the analog input channels of the module.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html)[] GetAnalogInputs()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQAnalogInput](nationalinstruments-veristand-systemdefinitionapi-daqanaloginput.html) elements from the current [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html).

Parent topic:

SCXIModule Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scximodule-getanalogoutputs.html language=enus -->
## TOPIC 03664: GetAnalogOutputs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scximodule-getanalogoutputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scximodule-getanalogoutputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQAnalogOutput elements from the current SCXIModule. This method gets the analog output channels of the module. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutput[] GetAnalogOutputs()RemarksModifications you make to the contents

### GetAnalogOutputs()

Gets an array that contains the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) elements from the current [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html). This method gets the analog output channels of the module.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html)[] GetAnalogOutputs()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) elements from the current [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html).

Parent topic:

SCXIModule Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scximodule-getdioports.html language=enus -->
## TOPIC 03665: GetDIOPorts()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scximodule-getdioports.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scximodule-getdioports.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQDIOPort elements from the current SCXIModule. This method gets the digital I/O ports of the module. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDIOPort[] GetDIOPorts()RemarksModifications you make to the contents of this list apply t

### GetDIOPorts()

Gets an array that contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) elements from the current [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html). This method gets the digital I/O ports of the module.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html)[] GetDIOPorts()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) elements from the current [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html).

Parent topic:

SCXIModule Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scximodule-scximodule__string-string-ushort.html language=enus -->
## TOPIC 03666: SCXIModule(string, string, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scximodule-scximodule__string-string-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scximodule-scximodule__string-string-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SCXIModule with the specified name. All channels are populated based on the SCXI module Type specified by TypeGUID . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXIModule(string Name, string TypeGUID, ushort numInternalChannels)ParametersNa

### SCXIModule(string, string, ushort)

Initializes a new instance of [SCXIModule](nationalinstruments-veristand-systemdefinitionapi-scximodule.html) with the specified name. All channels are populated based on the SCXI module Type specified by *TypeGUID* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SCXIModule(string Name, string TypeGUID, ushort numInternalChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the SCXI module. |
| TypeGUID | string | The GUID specifying the module type. |
| numInternalChannels | ushort | The number of internal channels to add to the SCXI module. |

Parent topic:

SCXIModule Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scximodule-scximoduletype.html language=enus -->
## TOPIC 03667: SCXIModuleType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scximodule-scximoduletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scximodule-scximoduletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of the SCXI module. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string SCXIModuleType { get; }ReturnsThe module type.

### SCXIModuleType

Gets the type of the SCXI module.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string SCXIModuleType { get; }

#### Returns

The module type.

Parent topic:

SCXIModule Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-scximodule.html language=enus -->
## TOPIC 03668: SCXIModule Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-scximodule.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-scximodule.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SCXI module under an SCXIChassis. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SCXIModule : SectionRemarksUse the members of this class to get the type of the SCXI module and its inputs and outputs. Accessing this ClassGetSCXIModules

### SCXIModule Class

Represents an SCXI module under an [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SCXIModule : Section

#### Remarks

Use the members of this class to get the type of the SCXI module and its inputs and outputs.

**Accessing this Class**

- [GetSCXIModules](nationalinstruments-veristand-systemdefinitionapi-scxichassis-getscximodules.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SCXIModule(string, string, ushort) | Initializes a new instance of SCXIModule with the specified name. All channels are populated based on the SCXI module Type specified by TypeGUID . |

#### Properties

| Name | Description |
| --- | --- |
| SCXIModuleType | Gets the type of the SCXI module. |

#### Methods

| Name | Description |
| --- | --- |
| GetAnalogInputs() | Gets an array that contains the DAQAnalogInput elements from the current SCXIModule. This method gets the analog input channels of the module. |
| GetAnalogOutputs() | Gets an array that contains the DAQAnalogOutput elements from the current SCXIModule. This method gets the analog output channels of the module. |
| GetDIOPorts() | Gets an array that contains the DAQDIOPort elements from the current SCXIModule. This method gets the digital I/O ports of the module. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-section.html language=enus -->
## TOPIC 03669: Section Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-section.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-section.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a section or node in the system definition. A section represents any node that contains additional nodes. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Section : BaseNodeRemarksAccessing this ClassYou cannot explicitly construct a Secti

### Section Class

Represents a section or node in the system definition. A section represents any node that contains additional nodes.

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Section : BaseNode

#### Remarks

**Accessing this Class**

You cannot explicitly construct a Section object. Use an object of a type that inherits this class to access its members.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-channels.html language=enus -->
## TOPIC 03670: Channels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-channels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channels to set to the specified values. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode[] Channels { get; set; }ReturnsAn array of BaseNode references to the channels.

### Channels

Gets or sets the channels to set to the specified values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html)[] Channels { get; set; }

#### Returns

An array of [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) references to the channels.

Parent topic:

SetMultipleVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-setchannelsandvalues__basenode_arr1-double_arr1.html language=enus -->
## TOPIC 03671: SetChannelsAndValues(BaseNode[], double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-setchannelsandvalues__basenode_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-setchannelsandvalues__basenode_arr1-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the channel values to constant values. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetChannelsAndValues(BaseNode[] Channels, double[] Values)ParametersNameTypeDescriptionChannelsBaseNode[]The channels to convert to constant values.Valuesdouble[]The constant val

### SetChannelsAndValues(BaseNode[], double[])

Sets the channel values to constant values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetChannelsAndValues(BaseNode[] Channels, double[] Values)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Channels | BaseNode[] | The channels to convert to constant values. |
| Values | double[] | The constant values to set the channels to. |

Parent topic:

SetMultipleVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-setmultiplevariables__string-string-basenode_arr1-double_arr1.html language=enus -->
## TOPIC 03672: SetMultipleVariables(string, string, BaseNode[], double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-setmultiplevariables__string-string-basenode_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-setmultiplevariables__string-string-basenode_arr1-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetMultipleVariables with the specified name, description, channels, and values. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SetMultipleVariables(string Name, string Description, BaseNode[] Channels, double[] Values)ParametersNameTypeDescrip

### SetMultipleVariables(string, string, BaseNode[], double[])

Initializes a new instance of [SetMultipleVariables](nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables.html) with the specified name, description, channels, and values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SetMultipleVariables(string Name, string Description, BaseNode[] Channels, double[] Values)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Channels | BaseNode[] | The channels to convert to constant values. |
| Values | double[] | The constant values to set the channels to. |

Parent topic:

SetMultipleVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-values.html language=enus -->
## TOPIC 03673: Values

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-values.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-values.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the values to which this step sets the specified Channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double[] Values { get; }RemarksThis property is read-only. Use the constructor for this class or the SetChannelsAndValues method to set the channels this step conf

### Values

Gets the values to which this step sets the specified [Channels](nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-channels.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double[] Values { get; }

#### Remarks

This property is read-only. Use the constructor for this class or the [SetChannelsAndValues](nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-setchannelsandvalues__basenode_arr1-double_arr1.html) method to set the channels this step configures.

#### Returns

The array of constant values applied to the [Channels](nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables-channels.html).

Parent topic:

SetMultipleVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables.html language=enus -->
## TOPIC 03674: SetMultipleVariables Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setmultiplevariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Set Multiple Variables step that you can add to a procedure. This step sets the values of multiple channels to constant values. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SetMultipleVariables : CommandRemarksUse the members of this

### SetMultipleVariables Class

Represents a **Set Multiple Variables** step that you can add to a procedure. This step sets the values of multiple channels to constant values.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SetMultipleVariables : Command

#### Remarks

Use the members of this class to get and set the channels to configure and the values to apply to the channels.

**Accessing this Class**

- SetMultipleVariables Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SetMultipleVariables(string, string, BaseNode[], double[]) | Initializes a new instance of SetMultipleVariables with the specified name, description, channels, and values. |

#### Properties

| Name | Description |
| --- | --- |
| Channels | Gets or sets the channels to set to the specified values. |
| Values | Gets the values to which this step sets the specified Channels. |

#### Methods

| Name | Description |
| --- | --- |
| SetChannelsAndValues(BaseNode[], double[]) | Sets the channel values to constant values. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html language=enus -->
## TOPIC 03675: Function

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the Variable channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SetVariableStepFunction Function { get; set; }ReturnsAn enumeration value of SetVa

### Function

Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the [Variable](nationalinstruments-veristand-systemdefinitionapi-setvariable-variable.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SetVariableStepFunction](nationalinstruments-veristand-systemdefinitionapi-setvariablestepfunction.html) Function { get; set; }

#### Returns

An enumeration value of [SetVariableStepFunction](nationalinstruments-veristand-systemdefinitionapi-setvariablestepfunction.html).

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue1__basenode.html language=enus -->
## TOPIC 03676: SetValue1(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue1__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue1__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Value1 in the Function operation to a channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetValue1(BaseNode Value1)ParametersNameTypeDescriptionValue1BaseNodeThe channel that specifies the value of Value1.Returnstrue if the value was set successfully.

### SetValue1(BaseNode)

Sets *Value1* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation to a channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetValue1(BaseNode Value1)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Value1 | BaseNode | The channel that specifies the value of Value1. |

#### Returns

true if the value was set successfully.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue1__double.html language=enus -->
## TOPIC 03677: SetValue1(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue1__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue1__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Value1 in the Function operation to a constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetValue1(double Value1)ParametersNameTypeDescriptionValue1doubleThe constant value of Value1.Returnstrue if the value was set successfully.

### SetValue1(double)

Sets *Value1* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation to a constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetValue1(double Value1)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Value1 | double | The constant value of Value1. |

#### Returns

true if the value was set successfully.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue2__basenode.html language=enus -->
## TOPIC 03678: SetValue2(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue2__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue2__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Value2 in the Function operation to a channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetValue2(BaseNode Value2)ParametersNameTypeDescriptionValue2BaseNodeThe channel that specifies the value of Value1.Returnstrue if the value was set successfully.

### SetValue2(BaseNode)

Sets *Value2* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation to a channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetValue2(BaseNode Value2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Value2 | BaseNode | The channel that specifies the value of Value1. |

#### Returns

true if the value was set successfully.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue2__double.html language=enus -->
## TOPIC 03679: SetValue2(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue2__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvalue2__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets Value2 in the Function operation to a constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetValue2(double Value2)ParametersNameTypeDescriptionValue2doubleThe constant value of Value1.Returnstrue if the value was set successfully.

### SetValue2(double)

Sets *Value2* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation to a constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetValue2(double Value2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Value2 | double | The constant value of Value1. |

#### Returns

true if the value was set successfully.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-basenode.html language=enus -->
## TOPIC 03680: SetVariable(string, string, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetVariable and sets the value of the Variable channel to the value of the Value channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SetVariable(string Name, string Description, BaseNode Variable, BaseNode Value)ParametersNameTypeDescriptio

### SetVariable(string, string, BaseNode, BaseNode)

Initializes a new instance of [SetVariable](nationalinstruments-veristand-systemdefinitionapi-setvariable.html) and sets the value of the *Variable*  channel to the value of the *Value*  channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SetVariable(string Name, string Description, BaseNode Variable, BaseNode Value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Variable | BaseNode | The channel in the system whose value you want to set. |
| Value | BaseNode | The channel that specifies the value to set on Variable. |

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-double.html language=enus -->
## TOPIC 03681: SetVariable(string, string, BaseNode, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetVariable and sets the value of the Variable channel to the constant Value . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SetVariable(string Name, string Description, BaseNode Variable, double Value)ParametersNameTypeDescriptionNamestringTh

### SetVariable(string, string, BaseNode, double)

Initializes a new instance of [SetVariable](nationalinstruments-veristand-systemdefinitionapi-setvariable.html) and sets the value of the *Variable*  channel to the constant *Value* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SetVariable(string Name, string Description, BaseNode Variable, double Value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Variable | BaseNode | The channel in the system whose value you want to set. |
| Value | double | The constant value to set on Variable. |

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-basenode-basenode.html language=enus -->
## TOPIC 03682: SetVariable(string, string, BaseNode, SetVariableStepFunction, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses channels for the values of Value1 and Value2 . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Set

### SetVariable(string, string, BaseNode, SetVariableStepFunction, BaseNode, BaseNode)

Initializes a new instance of [SetVariable](nationalinstruments-veristand-systemdefinitionapi-setvariable.html) that performs the *Function*  you specify on *Value1*  and *Value2*  and sets the value of the *Variable*  channel to the result. This method uses channels for the values of *Value1*  and *Value2* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SetVariable(string Name, string Description, BaseNode Variable, SetVariableStepFunction Function, BaseNode Value1, BaseNode Value2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Variable | BaseNode | The channel in the system whose value you want to set. |
| Function | SetVariableStepFunction | The function to apply to Value1 and Value2 . |
| Value1 | BaseNode | The channel that specifies the value of Value1 . |
| Value2 | BaseNode | The channel that specifies the value of Value2 . |

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-basenode-double.html language=enus -->
## TOPIC 03683: SetVariable(string, string, BaseNode, SetVariableStepFunction, BaseNode, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-basenode-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-basenode-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses a channel for the value of Value1 and a constant for Value2 . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefiniti

### SetVariable(string, string, BaseNode, SetVariableStepFunction, BaseNode, double)

Initializes a new instance of [SetVariable](nationalinstruments-veristand-systemdefinitionapi-setvariable.html) that performs the *Function*  you specify on *Value1*  and *Value2*  and sets the value of the *Variable*  channel to the result. This method uses a channel for the value of *Value1*  and a constant for *Value2* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SetVariable(string Name, string Description, BaseNode Variable, SetVariableStepFunction Function, BaseNode Value1, double Value2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Variable | BaseNode | The channel in the system whose value you want to set. |
| Function | SetVariableStepFunction | The function to apply to Value1 and Value2 . |
| Value1 | BaseNode | The channel that specifies the value of Value1 . |
| Value2 | double | The constant value of Value2 . |

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-double-basenode.html language=enus -->
## TOPIC 03684: SetVariable(string, string, BaseNode, SetVariableStepFunction, double, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-double-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-double-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses a constant for the value of Value1 and a channel value for Value2 . SyntaxNamespace: NationalInstruments.VeriStand.SystemDe

### SetVariable(string, string, BaseNode, SetVariableStepFunction, double, BaseNode)

Initializes a new instance of [SetVariable](nationalinstruments-veristand-systemdefinitionapi-setvariable.html) that performs the *Function*  you specify on *Value1*  and *Value2*  and sets the value of the *Variable*  channel to the result. This method uses a constant for the value of *Value1*  and a channel value for *Value2* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SetVariable(string Name, string Description, BaseNode Variable, SetVariableStepFunction Function, double Value1, BaseNode Value2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Variable | BaseNode | The channel in the system whose value you want to set. |
| Function | SetVariableStepFunction | The function to apply to Value1 and Value2 . |
| Value1 | double | The constant value of Value1 . |
| Value2 | BaseNode | The channel that specifies the value of Value2 . |

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-double-double.html language=enus -->
## TOPIC 03685: SetVariable(string, string, BaseNode, SetVariableStepFunction, double, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-double-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-setvariable__string-string-basenode-setvariablestepfunction-double-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses constants for the values of Value1 and Value2 . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Se

### SetVariable(string, string, BaseNode, SetVariableStepFunction, double, double)

Initializes a new instance of [SetVariable](nationalinstruments-veristand-systemdefinitionapi-setvariable.html) that performs the *Function*  you specify on *Value1*  and *Value2*  and sets the value of the *Variable*  channel to the result. This method uses constants for the values of *Value1*  and *Value2* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SetVariable(string Name, string Description, BaseNode Variable, SetVariableStepFunction Function, double Value1, double Value2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Variable | BaseNode | The channel in the system whose value you want to set. |
| Function | SetVariableStepFunction | The function to apply to Value1 and Value2 . |
| Value1 | double | The constant value of Value1 . |
| Value2 | double | The constant value of Value2 . |

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-value1channel.html language=enus -->
## TOPIC 03686: Value1Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-value1channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-value1channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that determines the value of Value1 in the Function operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Value1Channel { get; }ReturnsA BaseNode reference to the channel.

### Value1Channel

Gets the channel that determines the value of *Value1* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Value1Channel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-value1constant.html language=enus -->
## TOPIC 03687: Value1Constant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-value1constant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-value1constant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of Value1 in the Function operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Value1Constant { get; }ReturnsThe constant value.

### Value1Constant

Gets the constant value of *Value1* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Value1Constant { get; }

#### Returns

The constant value.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-value1isconstant.html language=enus -->
## TOPIC 03688: Value1IsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-value1isconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-value1isconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value of Value1 in the Function operation is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Value1IsConstant { get; }Returnstrue if the value is a constant. false if the value is a channel.

### Value1IsConstant

Gets whether the value of *Value1* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Value1IsConstant { get; }

#### Returns

true if the value is a constant. false if the value is a channel.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-value2channel.html language=enus -->
## TOPIC 03689: Value2Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-value2channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-value2channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that determines the value of Value2 in the Function operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Value2Channel { get; }ReturnsA BaseNode reference to the channel.

### Value2Channel

Gets the channel that determines the value of *Value2* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Value2Channel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-value2constant.html language=enus -->
## TOPIC 03690: Value2Constant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-value2constant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-value2constant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of Value2 in the Function operation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Value2Constant { get; }ReturnsThe constant value.

### Value2Constant

Gets the constant value of *Value2* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Value2Constant { get; }

#### Returns

The constant value.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-value2isconstant.html language=enus -->
## TOPIC 03691: Value2IsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-value2isconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-value2isconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value of Value2 in the Function operation is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Value2IsConstant { get; }Returnstrue if the value is a constant. false if the value is a channel.

### Value2IsConstant

Gets whether the value of *Value2* in the [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) operation is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Value2IsConstant { get; }

#### Returns

true if the value is a constant. false if the value is a channel.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable-variable.html language=enus -->
## TOPIC 03692: Variable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable-variable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable-variable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel in the system whose value the Set Variable step sets. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Variable { get; set; }ReturnsA BaseNode reference to the channel.

### Variable

Gets or sets the channel in the system whose value the **Set Variable** step sets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Variable { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

SetVariable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariable.html language=enus -->
## TOPIC 03693: SetVariable Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Set Variable step that you can add to a procedure. This step sets a channel, Variable, to a certain value. The value can be a constant or the result of a calculation using a Function you specify. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### SetVariable Class

Represents a **Set Variable** step that you can add to a procedure. This step sets a channel, [Variable](nationalinstruments-veristand-systemdefinitionapi-setvariable-variable.html), to a certain value. The value can be a constant or the result of a calculation using a [Function](nationalinstruments-veristand-systemdefinitionapi-setvariable-function.html) you specify.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SetVariable : Command

#### Remarks

Use the members of this class to specify the channel to set and the values to set it to.

**Accessing this Class**

- SetVariable Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SetVariable(string, string, BaseNode, SetVariableStepFunction, double, BaseNode) | Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses a constant for the value of Value1 and a channel value for Value2 . |
| SetVariable(string, string, BaseNode, SetVariableStepFunction, BaseNode, double) | Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses a channel for the value of Value1 and a constant for Value2 . |
| SetVariable(string, string, BaseNode, SetVariableStepFunction, BaseNode, BaseNode) | Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses channels for the values of Value1 and Value2 . |
| SetVariable(string, string, BaseNode, double) | Initializes a new instance of SetVariable and sets the value of the Variable channel to the constant Value . |
| SetVariable(string, string, BaseNode, BaseNode) | Initializes a new instance of SetVariable and sets the value of the Variable channel to the value of the Value channel. |
| SetVariable(string, string, BaseNode, SetVariableStepFunction, double, double) | Initializes a new instance of SetVariable that performs the Function you specify on Value1 and Value2 and sets the value of the Variable channel to the result. This method uses constants for the values of Value1 and Value2 . |

#### Properties

| Name | Description |
| --- | --- |
| Function | Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the Variable channel. |
| Value1Channel | Gets the channel that determines the value of Value1 in the Function operation. |
| Value1Constant | Gets the constant value of Value1 in the Function operation. |
| Value1IsConstant | Gets whether the value of Value1 in the Function operation is specified by a constant or a channel. |
| Value2Channel | Gets the channel that determines the value of Value2 in the Function operation. |
| Value2Constant | Gets the constant value of Value2 in the Function operation. |
| Value2IsConstant | Gets whether the value of Value2 in the Function operation is specified by a constant or a channel. |
| Variable | Gets or sets the channel in the system whose value the Set Variable step sets. |

#### Methods

| Name | Description |
| --- | --- |
| SetValue1(BaseNode) | Sets Value1 in the Function operation to a channel value. |
| SetValue1(double) | Sets Value1 in the Function operation to a constant value. |
| SetValue2(BaseNode) | Sets Value2 in the Function operation to a channel value. |
| SetValue2(double) | Sets Value2 in the Function operation to a constant value. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-setvariablestepfunction.html language=enus -->
## TOPIC 03694: SetVariableStepFunction Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-setvariablestepfunction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-setvariablestepfunction.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the function to use on Value1 and Value2 of a SetVariable procedure step. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum SetVariableStepFunctionMembersNameValueDescriptionNone0None. AddAddition. SubtractSubtraction. MultiplyMultiplication. DivideDivision.

### SetVariableStepFunction Enumeration

Specifies the function to use on *Value1* and *Value2* of a [SetVariable](nationalinstruments-veristand-systemdefinitionapi-setvariable.html) procedure step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum SetVariableStepFunction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | None. |
| Add |  | Addition. |
| Subtract |  | Subtraction. |
| Multiply |  | Multiplication. |
| Divide |  | Division. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-clustername.html language=enus -->
## TOPIC 03695: ClusterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-clustername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-clustername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the cluster in the XNET database that contains the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ClusterName { get; set; }ReturnsThe cluster name.

### ClusterName

Gets or sets the name of the cluster in the XNET database that contains the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ClusterName { get; set; }

#### Returns

The cluster name.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createautomaticframeprocessing__out.1.html language=enus -->
## TOPIC 03696: CreateAutomaticFrameProcessing(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createautomaticframeprocessing__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createautomaticframeprocessing__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AutomaticFrameProcessing section under the frame, which contains sections to add a cyclic redundancy check (CRC) and counter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AutomaticFrameProcessing CreateAutomaticFrameProcessing(out Error error)RemarksThis method

### CreateAutomaticFrameProcessing(out Error)

Creates an [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section under the frame, which contains sections to add a cyclic redundancy check (CRC) and counter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) CreateAutomaticFrameProcessing(out Error error)

#### Remarks

This method is only valid for outgoing CAN/LIN frames. This method does not create a section if the frame is not an outgoing frame of a CAN/LIN port, or if an [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section already exists under the frame.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Upon return, contains a reference to the [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createautomaticframeprocessing__out.html language=enus -->
## TOPIC 03697: CreateAutomaticFrameProcessing(out AutomaticFrameProcessing)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createautomaticframeprocessing__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createautomaticframeprocessing__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an AutomaticFrameProcessing section under the frame, which contains sections to add a cyclic redundancy check (CRC) and counter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateAutomaticFrameProcessing(out AutomaticFrameProcessing automaticFrameProcessing)

### CreateAutomaticFrameProcessing(out AutomaticFrameProcessing)

Creates an [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section under the frame, which contains sections to add a cyclic redundancy check (CRC) and counter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateAutomaticFrameProcessing(out AutomaticFrameProcessing automaticFrameProcessing)

#### Remarks

This method is only valid for outgoing CAN/LIN frames. This method does not create a section if the frame is not an outgoing frame of a CAN/LIN port, or if an [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section already exists under the frame.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| automaticFrameProcessing | out AutomaticFrameProcessing | Upon return, contains a reference to the AutomaticFrameProcessing section. |

#### Returns

true if the section is created.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframefaulting__bool-bool-out.1.html language=enus -->
## TOPIC 03698: CreateFrameFaulting(bool, bool, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframefaulting__bool-bool-out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframefaulting__bool-bool-out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a FrameFaulting section under the frame, which contains channels you can use to control the transmission of outgoing cyclic frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FrameFaulting CreateFrameFaulting(bool CreateSkipCyclicFrames, bool CreateTransmitTime,

### CreateFrameFaulting(bool, bool, out Error)

Creates a [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) section under the frame, which contains channels you can use to control the transmission of outgoing cyclic frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) CreateFrameFaulting(bool CreateSkipCyclicFrames, bool CreateTransmitTime, out Error error)

#### Remarks

This method is only valid for outgoing cyclic frames under CAN ports. This method does not create a section if the frame is not an outgoing cyclic frame of a CAN port, or if a [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) section already exists under the frame.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| CreateSkipCyclicFrames | bool | If true, creates a SkipCyclicFrames channel under the section. |
| CreateTransmitTime | bool | If true, creates a TransmitTime channel under the section. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Upon return, contains a reference to the [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) section.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframefaulting__bool-bool-out.html language=enus -->
## TOPIC 03699: CreateFrameFaulting(bool, bool, out FrameFaulting)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframefaulting__bool-bool-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframefaulting__bool-bool-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a FrameFaulting section under the frame, which contains channels you can use to control the transmission of outgoing cyclic frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateFrameFaulting(bool CreateSkipCyclicFrames, bool CreateTransmitTime, out Fram

### CreateFrameFaulting(bool, bool, out FrameFaulting)

Creates a [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) section under the frame, which contains channels you can use to control the transmission of outgoing cyclic frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateFrameFaulting(bool CreateSkipCyclicFrames, bool CreateTransmitTime, out FrameFaulting frameFaulting)

#### Remarks

This method is only valid for outgoing cyclic frames under CAN ports. This method does not create a section if the frame is not an outgoing cyclic frame of a CAN port, or if a [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) section already exists under the frame.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| CreateSkipCyclicFrames | bool | If true, creates a SkipCyclicFrames channel under the section. |
| CreateTransmitTime | bool | If true, creates a TransmitTime channel under the section. |
| frameFaulting | out FrameFaulting | Upon return, contains a reference to the FrameFaulting section. |

#### Returns

true if the section is created.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframeinformation__out.1.html language=enus -->
## TOPIC 03700: CreateFrameInformation(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframeinformation__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframeinformation__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a FrameInformation section under the frame, which contains channels with timing and ID information for incoming frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FrameInformation CreateFrameInformation(out Error error)RemarksThis method is only valid for incomi

### CreateFrameInformation(out Error)

Creates a [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) section under the frame, which contains channels with timing and ID information for incoming frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) CreateFrameInformation(out Error error)

#### Remarks

This method is only valid for incoming frames. This method does not create a section if the frame is not an incoming frame, or if a [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) section already exists under the frame.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Reference to the [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) section.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframeinformation__out.html language=enus -->
## TOPIC 03701: CreateFrameInformation(out FrameInformation)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframeinformation__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframeinformation__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a FrameInformation section under the frame, which contains channels with timing and ID information for incoming frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateFrameInformation(out FrameInformation frameInformation)RemarksThis method is only valid

### CreateFrameInformation(out FrameInformation)

Creates a [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) section under the frame, which contains channels with timing and ID information for incoming frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateFrameInformation(out FrameInformation frameInformation)

#### Remarks

This method is only valid for incoming frames. This method does not create a section if the frame is not an incoming frame, or if a [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) section already exists under the frame.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| frameInformation | out FrameInformation | Upon return, contains a reference to the FrameInformation section. |

#### Returns

true if the section is created.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmode__int-string-string-string-double-out.1.html language=enus -->
## TOPIC 03702: CreateMode(int, string, string, string, double, out Mode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmode__int-string-string-string-double-out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmode__int-string-string-string-double-out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Mode section under the frame, which organizes multiplexed signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateMode(int MultiplexerValue, string SignalName, string Description, string Units, double DefaultValue, out Mode mode)RemarksThis method is on

### CreateMode(int, string, string, string, double, out Mode)

Creates a [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html) section under the frame, which organizes multiplexed signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateMode(int MultiplexerValue, string SignalName, string Description, string Units, double DefaultValue, out Mode mode)

#### Remarks

This method is only valid for frames under CAN ports.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| MultiplexerValue | int | The value of the multiplexer signal, which determines the dynamic signals transmitted in the frame. This method creates a section named "Mode MultiplexerValue". |
| SignalName | string | The name of a dynamic, or multiplexed, signal to add under the Mode section. |
| Description | string | A description of the multiplexed SignalName . |
| Units | string | The units associated with SignalName . |
| DefaultValue | double | The default value of SignalName . |
| mode | out Mode | Upon return, contains a reference to the Mode class. |

#### Returns

true if the section is created.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmode__int-string-string-string-double-out.html language=enus -->
## TOPIC 03703: CreateMode(int, string, string, string, double, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmode__int-string-string-string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmode__int-string-string-string-double-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Mode section under the frame, which organizes multiplexed signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Mode CreateMode(int MultiplexerValue, string SignalName, string Description, string Units, double DefaultValue, out Error error)RemarksThis method is

### CreateMode(int, string, string, string, double, out Error)

Creates a [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html) section under the frame, which organizes multiplexed signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html) CreateMode(int MultiplexerValue, string SignalName, string Description, string Units, double DefaultValue, out Error error)

#### Remarks

This method is only valid for frames under CAN ports.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| MultiplexerValue | int | The value of the multiplexer signal, which determines the dynamic signals transmitted in the frame. This method creates a section named "Mode MultiplexerValue". |
| SignalName | string | The name of a dynamic, or multiplexed, signal to add under the Mode section. |
| Description | string | A description of the multiplexed SignalName . |
| Units | string | The units associated with SignalName . |
| DefaultValue | double | The default value of SignalName . |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Upon return, contains a reference to the [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html) class.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-out.1.html language=enus -->
## TOPIC 03704: CreateMultiplexer(int, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Multiplexer signal under the frame. A single frame can contain only one Multiplexer signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Multiplexer CreateMultiplexer(int MultiplexerValue, out Error error)RemarksThis method is only valid for frames under CAN por

### CreateMultiplexer(int, out Error)

Creates a [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) signal under the frame. A single frame can contain only one [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) CreateMultiplexer(int MultiplexerValue, out Error error)

#### Remarks

This method is only valid for frames under CAN ports.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| MultiplexerValue | int | The value of the Multiplexer signal, which defines the dynamic, or multiplexed, signals to transmit. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Upon return, contains a reference to the [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) class.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-out.html language=enus -->
## TOPIC 03705: CreateMultiplexer(int, out Multiplexer)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Multiplexer signal under the frame. A single frame can contain only one Multiplexer signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateMultiplexer(int MultiplexerValue, out Multiplexer multiplexer)RemarksThis method is only valid for frames under CA

### CreateMultiplexer(int, out Multiplexer)

Creates a [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) signal under the frame. A single frame can contain only one [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateMultiplexer(int MultiplexerValue, out Multiplexer multiplexer)

#### Remarks

This method is only valid for frames under CAN ports.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| MultiplexerValue | int | The value of the Multiplexer signal, which defines the dynamic, or multiplexed, signals to transmit. |
| multiplexer | out Multiplexer | Upon return, contains a reference to the Multiplexer class. |

#### Returns

true if the signal is created.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-string-out.html language=enus -->
## TOPIC 03706: CreateMultiplexer(int, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmultiplexer__int-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Multiplexer signal under the frame. A single frame can contain only one Multiplexer signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Multiplexer CreateMultiplexer(int multiplexerValue, string signalName, out Error error)RemarksThis method is only valid for f

### CreateMultiplexer(int, string, out Error)

Creates a [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) signal under the frame. A single frame can contain only one [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) CreateMultiplexer(int multiplexerValue, string signalName, out Error error)

#### Remarks

This method is only valid for frames under CAN ports.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| multiplexerValue | int | The value of the Multiplexer signal, which defines the dynamic, or multiplexed, signals to transmit. |
| signalName | string | The name of the Multiplexer signal, which defines the dynamic, or multiplexed, signals to transmit. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Upon return, contains a reference to the [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) class.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createsignalbasedsignal__string-string-string-double-out.1.html language=enus -->
## TOPIC 03707: CreateSignalBasedSignal(string, string, string, double, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createsignalbasedsignal__string-string-string-double-out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createsignalbasedsignal__string-string-string-double-out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SignalBasedSignal under the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedSignal CreateSignalBasedSignal(string Name, string Description, string Units, double DefaultValue, out Error error)ParametersNameTypeDescriptionNamestringThe name of the S

### CreateSignalBasedSignal(string, string, string, double, out Error)

Creates a [SignalBasedSignal](nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html) under the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedSignal](nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html) CreateSignalBasedSignal(string Name, string Description, string Units, double DefaultValue, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the SignalBasedSignal. |
| Description | string | The description of the SignalBasedSignal. |
| Units | string | The units associated with the SignalBasedSignal. |
| DefaultValue | double | The default value of the SignalBasedSignal. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Upon return, contains a reference to the [SignalBasedSignal](nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html) class.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createsignalbasedsignal__string-string-string-double-out.html language=enus -->
## TOPIC 03708: CreateSignalBasedSignal(string, string, string, double, out SignalBasedSignal)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createsignalbasedsignal__string-string-string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createsignalbasedsignal__string-string-string-double-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SignalBasedSignal under the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateSignalBasedSignal(string Name, string Description, string Units, double DefaultValue, out SignalBasedSignal signal)ParametersNameTypeDescriptionNamestringThe name of the S

### CreateSignalBasedSignal(string, string, string, double, out SignalBasedSignal)

Creates a [SignalBasedSignal](nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html) under the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateSignalBasedSignal(string Name, string Description, string Units, double DefaultValue, out SignalBasedSignal signal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the SignalBasedSignal. |
| Description | string | The description of the SignalBasedSignal. |
| Units | string | The units associated with the SignalBasedSignal. |
| DefaultValue | double | The default value of the SignalBasedSignal. |
| signal | out SignalBasedSignal | Upon return, contains a reference to the SignalBasedSignal class. |

#### Returns

true if the signal is created.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-databasealias.html language=enus -->
## TOPIC 03709: DatabaseAlias

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-databasealias.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-databasealias.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the alias for the XNET database that contains the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string DatabaseAlias { get; set; }ReturnsThe default value is the filename of the XNET database file, without the file extension.

### DatabaseAlias

Gets or sets the alias for the XNET database that contains the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string DatabaseAlias { get; set; }

#### Returns

The default value is the filename of the XNET database file, without the file extension.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disablechannel.html language=enus -->
## TOPIC 03710: DisableChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disablechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disablechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode DisableChannel { get; }ReturnsA BaseNode reference

### DisableChannel

Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) DisableChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disabled.html language=enus -->
## TOPIC 03711: Disabled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disabled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disabled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether transmission of the outgoing frame is disabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Disabled { get; }Returnstrue if transmission is disabled.

### Disabled

Gets whether transmission of the outgoing frame is disabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Disabled { get; }

#### Returns

true if transmission is disabled.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disabletransmission__basenode.html language=enus -->
## TOPIC 03712: DisableTransmission(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disabletransmission__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-disabletransmission__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables transmission of the outgoing frame when the value of DisableChannel is non-zero. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void DisableTransmission(BaseNode DisableChannel)RemarksThis method is only valid for outgoing frames. ParametersNameTypeDescriptionDisab

### DisableTransmission(BaseNode)

Disables transmission of the outgoing frame when the value of *DisableChannel*  is non-zero.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void DisableTransmission(BaseNode DisableChannel)

#### Remarks

This method is only valid for outgoing frames.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| DisableChannel | BaseNode | The channel to check for a non-zero value. |

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enable64bit.html language=enus -->
## TOPIC 03713: Enable64Bit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enable64bit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enable64bit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether U64 bitfield representation is enabled for the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Enable64Bit { get; set; }Returnstrue if U64 bitfield representation is enabled.

### Enable64Bit

Gets or sets whether U64 bitfield representation is enabled for the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Enable64Bit { get; set; }

#### Returns

true if U64 bitfield representation is enabled.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enableframecyclictrigger.html language=enus -->
## TOPIC 03714: EnableFrameCyclicTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enableframecyclictrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enableframecyclictrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when TriggerChannel has a non-zero value, is enabled for the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool EnableFrameCyclicTrigger { get; set; }RemarksThis property is valid only for

### EnableFrameCyclicTrigger

Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when [TriggerChannel](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-triggerchannel.html) has a non-zero value, is enabled for the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool EnableFrameCyclicTrigger { get; set; }

#### Remarks

This property is valid only for outgoing cyclic frames.

#### Returns

true if a frame cyclic trigger is enabled.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enablesoftwarecyclictrigger.html language=enus -->
## TOPIC 03715: EnableSoftwareCyclicTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enablesoftwarecyclictrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enablesoftwarecyclictrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by TransmitTime, is enabled for the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool EnableSoftwareCyclicTrigger { get; set; }RemarksThis property is val

### EnableSoftwareCyclicTrigger

Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by [TransmitTime](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittime.html), is enabled for the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool EnableSoftwareCyclicTrigger { get; set; }

#### Remarks

This property is valid only for outgoing cyclic frames.

#### Returns

true if a software cyclic trigger is enabled.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enabletransmission.html language=enus -->
## TOPIC 03716: EnableTransmission()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enabletransmission.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enabletransmission.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables transmission of the outgoing frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void EnableTransmission()RemarksThis method is only valid for outgoing frames.

### EnableTransmission()

Enables transmission of the outgoing frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void EnableTransmission()

#### Remarks

This method is only valid for outgoing frames.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-frametype.html language=enus -->
## TOPIC 03717: FrameType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-frametype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-frametype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FrameType FrameType { get; set; }ReturnsAn enumeration value of FrameType.

### FrameType

Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FrameType](nationalinstruments-veristand-systemdefinitionapi-frametype.html) FrameType { get; set; }

#### Returns

An enumeration value of [FrameType](nationalinstruments-veristand-systemdefinitionapi-frametype.html).

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getautomaticframeprocessing.html language=enus -->
## TOPIC 03718: GetAutomaticFrameProcessing()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getautomaticframeprocessing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getautomaticframeprocessing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Automatic Frame Processing section of a frame, which contains the CRC and Counter sections for the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AutomaticFrameProcessing GetAutomaticFrameProcessing()RemarksThis method is only valid for outgoing CAN frames.

### GetAutomaticFrameProcessing()

Gets the **Automatic Frame Processing** section of a frame, which contains the [CRC](nationalinstruments-veristand-systemdefinitionapi-crc.html) and [Counter](nationalinstruments-veristand-systemdefinitionapi-counter.html) sections for the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) GetAutomaticFrameProcessing()

#### Remarks

This method is only valid for outgoing CAN frames.

#### Returns

An [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) object.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getframefaulting.html language=enus -->
## TOPIC 03719: GetFrameFaulting()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getframefaulting.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getframefaulting.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Frame Faulting section of the frame, which contains the SkipCyclicFrames and TransmitTime channels for the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FrameFaulting GetFrameFaulting()RemarksThis method is only valid for outgoing cyclic CAN frames. Returns

### GetFrameFaulting()

Gets the **Frame Faulting** section of the frame, which contains the [SkipCyclicFrames](nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html) and [TransmitTime](nationalinstruments-veristand-systemdefinitionapi-transmittime.html) channels for the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) GetFrameFaulting()

#### Remarks

This method is only valid for outgoing cyclic CAN frames.

#### Returns

A [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) object.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getframeinformation.html language=enus -->
## TOPIC 03720: GetFrameInformation()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getframeinformation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getframeinformation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Frame Information section of the frame, which contains the ReceiveTime and TimeDifference channels for the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FrameInformation GetFrameInformation()RemarksThis method is only valid for incoming frames. ReturnsA Fra

### GetFrameInformation()

Gets the **Frame Information** section of the frame, which contains the [ReceiveTime](nationalinstruments-veristand-systemdefinitionapi-receivetime.html) and [TimeDifference](nationalinstruments-veristand-systemdefinitionapi-timedifference.html) channels for the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) GetFrameInformation()

#### Remarks

This method is only valid for incoming frames.

#### Returns

A [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) object.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getmodelist.html language=enus -->
## TOPIC 03721: GetModeList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getmodelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getmodelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Mode elements from the current SignalBasedFrame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Mode[] GetModeList()RemarksThis method is only valid for CAN frames. In NI VeriStand, Mode nodes simply organize dynamic (multiplexed) signals acc

### GetModeList()

Gets an array that contains the [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html) elements from the current [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html)[] GetModeList()

#### Remarks

Mode

CreateMode(int, string, string, string, double, out Error)

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Mode](nationalinstruments-veristand-systemdefinitionapi-mode.html) elements from the current [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html).

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getmultiplexer.html language=enus -->
## TOPIC 03722: GetMultiplexer()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getmultiplexer.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getmultiplexer.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Multiplexer signal for the frame, which defines an area within the frame that contains different dynamic signals based on the multiplexer signal value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Multiplexer GetMultiplexer()RemarksThis method is only valid for f

### GetMultiplexer()

Gets the [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) signal for the frame, which defines an area within the frame that contains different dynamic signals based on the multiplexer signal value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) GetMultiplexer()

#### Remarks

This method is only valid for frames under CAN ports.

#### Returns

A [Multiplexer](nationalinstruments-veristand-systemdefinitionapi-multiplexer.html) object.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getsignalbasedsignallist.html language=enus -->
## TOPIC 03723: GetSignalBasedSignalList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getsignalbasedsignallist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getsignalbasedsignallist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SignalBasedSignal elements from the current SignalBasedFrame. This method gets all the signal format signals in the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedSignal[] GetSignalBasedSignalList()RemarksModifications you m

### GetSignalBasedSignalList()

Gets an array that contains the [SignalBasedSignal](nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html) elements from the current [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html). This method gets all the signal format signals in the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedSignal](nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html)[] GetSignalBasedSignalList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SignalBasedSignal](nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html) elements from the current [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html).

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-id.html language=enus -->
## TOPIC 03724: ID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-id.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-id.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint ID { get; set; }Return

### ID

Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint ID { get; set; }

#### Returns

The frame ID.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-md5.html language=enus -->
## TOPIC 03725: MD5

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-md5.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-md5.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the MD5 message digest for the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic byte[] MD5 { get; }ReturnsA byte array containing the MD5 message digest.

### MD5

Gets the MD5 message digest for the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public byte[] MD5 { get; }

#### Returns

A byte array containing the MD5 message digest.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-owningdatabase.html language=enus -->
## TOPIC 03726: OwningDatabase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-owningdatabase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-owningdatabase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a reference to the XNET database that contains the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode OwningDatabase { get; set; }ReturnsA BaseNode reference to the database.

### OwningDatabase

Gets or sets a reference to the XNET database that contains the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) OwningDatabase { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the database.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-payloadlength.html language=enus -->
## TOPIC 03727: PayloadLength

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-payloadlength.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-payloadlength.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of bytes in the payload of the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PayloadLength { get; set; }ReturnsThe payload length.

### PayloadLength

Gets or sets the number of bytes in the payload of the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PayloadLength { get; set; }

#### Returns

The payload length.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-phase.html language=enus -->
## TOPIC 03728: Phase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-phase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-phase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to reset the timer after TransmitTime elapses when EnableSoftwareCyclicTrigger is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FramePhaseType Phase { get; set; }ReturnsAn enumeration value of FramePhaseType.

### Phase

Gets or sets whether to reset the timer after [TransmitTime](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittime.html) elapses when [EnableSoftwareCyclicTrigger](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enablesoftwarecyclictrigger.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FramePhaseType](nationalinstruments-veristand-systemdefinitionapi-framephasetype.html) Phase { get; set; }

#### Returns

An enumeration value of [FramePhaseType](nationalinstruments-veristand-systemdefinitionapi-framephasetype.html).

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-settransmittrigger__frametriggertype-basenode.html language=enus -->
## TOPIC 03729: SetTransmitTrigger(FrameTriggerType, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-settransmittrigger__frametriggertype-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-settransmittrigger__frametriggertype-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets event-triggered frame transmission on the frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetTransmitTrigger(FrameTriggerType TriggerType, BaseNode TriggerChannel)RemarksThis method is only valid for outgoing frames. ParametersNameTypeDescriptionTriggerTypeF

### SetTransmitTrigger(FrameTriggerType, BaseNode)

Sets event-triggered frame transmission on the frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetTransmitTrigger(FrameTriggerType TriggerType, BaseNode TriggerChannel)

#### Remarks

This method is only valid for outgoing frames.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| TriggerType | FrameTriggerType | The FrameTriggerType condition TriggerChannel must meet to trigger transmission of the outgoing frame. |
| TriggerChannel | BaseNode | The channel to check for the FrameTriggerType condition. |

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-signalbasedframe__string-uint-database-string-uint-double-bool-string_arr1.html language=enus -->
## TOPIC 03730: SignalBasedFrame(string, uint, Database, string, uint, double, bool, string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-signalbasedframe__string-uint-database-string-uint-double-bool-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-signalbasedframe__string-uint-database-string-uint-double-bool-string_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SignalBasedFrame class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedFrame(string Name, uint ID, Database OwningDatabase, string ClusterName, uint PayloadLength, double StartTimeOffset, bool Enable64Bit, string[] SignalNames)Pa

### SignalBasedFrame(string, uint, Database, string, uint, double, bool, string[])

Initializes a new instance of the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SignalBasedFrame(string Name, uint ID, Database OwningDatabase, string ClusterName, uint PayloadLength, double StartTimeOffset, bool Enable64Bit, string[] SignalNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the frame. |
| ID | uint | The identifier number of the frame. |
| OwningDatabase | Database | The XNET database that contains the frame. |
| ClusterName | string | The name of the cluster that contains the frame. |
| PayloadLength | uint | The number of bytes in the frame payload. |
| StartTimeOffset | double | The amount of time, in seconds, that elapses between the session start and the first transmission of the outgoing frame. |
| Enable64Bit | bool | true to enable U64 bitfield representation for the frame. |
| SignalNames | string[] | The names of the signals in the frame. |

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-starttimeoffset.html language=enus -->
## TOPIC 03731: StartTimeOffset

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-starttimeoffset.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-starttimeoffset.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time that elapses between the session start and the transmission of the first frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double StartTimeOffset { get; set; }RemarksThis property is only valid for outgoing cyclic CAN frames. Use this pro

### StartTimeOffset

Gets or sets the amount of time that elapses between the session start and the transmission of the first frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double StartTimeOffset { get; set; }

#### Remarks

This property is only valid for outgoing cyclic CAN frames. Use this property to have more control over the schedule of frames on the bus, and to offer more determinism by configuring cyclic frames to be spaced evenly. If this field contains a negative number, NI-XNET chooses the start time offset based on the arbitration identifier and periodic transmit time.

#### Returns

The start time offset, in seconds.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittime.html language=enus -->
## TOPIC 03732: TransmitTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when EnableSoftwareCyclicTrigger is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double TransmitTime { get; set; }ReturnsThe transmit time, in seconds.

### TransmitTime

Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when [EnableSoftwareCyclicTrigger](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enablesoftwarecyclictrigger.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double TransmitTime { get; set; }

#### Returns

The transmit time, in seconds.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittrigger.html language=enus -->
## TOPIC 03733: TransmitTrigger

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittrigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-transmittrigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FrameTriggerType TransmitTrigger { get; }ReturnsAn enumeration value of FrameTriggerType.

### TransmitTrigger

Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FrameTriggerType](nationalinstruments-veristand-systemdefinitionapi-frametriggertype.html) TransmitTrigger { get; }

#### Returns

An enumeration value of [FrameTriggerType](nationalinstruments-veristand-systemdefinitionapi-frametriggertype.html).

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-triggerchannel.html language=enus -->
## TOPIC 03734: TriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-triggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-triggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the channel that is checked for a non-zero value when EnableFrameCyclicTrigger is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode TriggerChannel { get; }ReturnsA BaseNode reference to the channel.

### TriggerChannel

Gets a reference to the channel that is checked for a non-zero value when [EnableFrameCyclicTrigger](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-enableframecyclictrigger.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) TriggerChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

SignalBasedFrame Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html language=enus -->
## TOPIC 03735: SignalBasedFrame Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a signal format frame under an NI-XNET LIN, FlexRay, or CAN port. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SignalBasedFrame : SectionRemarksUse the members of this class get or set information about the frame, such as the XNET datab

### SignalBasedFrame Class

Represents a signal format frame under an NI-XNET LIN, FlexRay, or CAN port.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SignalBasedFrame : Section

#### Remarks

Use the members of this class get or set information about the frame, such as the XNET database and cluster that contain it, its frame ID number, and any transmission triggers (outgoing frames only).

**Accessing this Class**

- [GetSignalBasedFrameList](nationalinstruments-veristand-systemdefinitionapi-cyclic-getsignalbasedframelist.html)
- [GetSignalBasedFrameList](nationalinstruments-veristand-systemdefinitionapi-eventtriggered-getsignalbasedframelist.html)
- [GetSignalBasedFrameList](nationalinstruments-veristand-systemdefinitionapi-singlepoint-getsignalbasedframelist.html)
- [GetSignalBasedFrameList](nationalinstruments-veristand-systemdefinitionapi-sporadic-getsignalbasedframelist.html)
- [GetSignalBasedFrameList](nationalinstruments-veristand-systemdefinitionapi-unconditional-getsignalbasedframelist.html)
- SignalBasedFrame Constructor

For example code and more information about this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SignalBasedFrame(string, uint, Database, string, uint, double, bool, string[]) | Initializes a new instance of the SignalBasedFrame class. |

#### Properties

| Name | Description |
| --- | --- |
| ClusterName | Gets or sets the name of the cluster in the XNET database that contains the frame. |
| DatabaseAlias | Gets or sets the alias for the XNET database that contains the frame. |
| DisableChannel | Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero. |
| Disabled | Gets whether transmission of the outgoing frame is disabled. |
| Enable64Bit | Gets or sets whether U64 bitfield representation is enabled for the frame. |
| EnableFrameCyclicTrigger | Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when TriggerChannel has a non-zero value, is enabled for the frame. |
| EnableSoftwareCyclicTrigger | Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by TransmitTime, is enabled for the frame. |
| FrameType | Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port. |
| ID | Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent. |
| MD5 | Gets the MD5 message digest for the frame. |
| OwningDatabase | Gets or sets a reference to the XNET database that contains the frame. |
| PayloadLength | Gets or sets the number of bytes in the payload of the frame. |
| Phase | Gets or sets whether to reset the timer after TransmitTime elapses when EnableSoftwareCyclicTrigger is true. |
| StartTimeOffset | Gets or sets the amount of time that elapses between the session start and the transmission of the first frame. |
| TransmitTime | Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when EnableSoftwareCyclicTrigger is true. |
| TransmitTrigger | Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame. |
| TriggerChannel | Gets a reference to the channel that is checked for a non-zero value when EnableFrameCyclicTrigger is true. |

#### Methods

| Name | Description |
| --- | --- |
| CreateAutomaticFrameProcessing(out Error) | Creates an AutomaticFrameProcessing section under the frame, which contains sections to add a cyclic redundancy check (CRC) and counter. |
| CreateAutomaticFrameProcessing(out AutomaticFrameProcessing) | Creates an AutomaticFrameProcessing section under the frame, which contains sections to add a cyclic redundancy check (CRC) and counter. |
| CreateFrameFaulting(bool, bool, out FrameFaulting) | Creates a FrameFaulting section under the frame, which contains channels you can use to control the transmission of outgoing cyclic frames. |
| CreateFrameFaulting(bool, bool, out Error) | Creates a FrameFaulting section under the frame, which contains channels you can use to control the transmission of outgoing cyclic frames. |
| CreateFrameInformation(out FrameInformation) | Creates a FrameInformation section under the frame, which contains channels with timing and ID information for incoming frames. |
| CreateFrameInformation(out Error) | Creates a FrameInformation section under the frame, which contains channels with timing and ID information for incoming frames. |
| CreateMode(int, string, string, string, double, out Error) | Creates a Mode section under the frame, which organizes multiplexed signals. |
| CreateMode(int, string, string, string, double, out Mode) | Creates a Mode section under the frame, which organizes multiplexed signals. |
| CreateMultiplexer(int, out Multiplexer) | Creates a Multiplexer signal under the frame. A single frame can contain only one Multiplexer signal. |
| CreateMultiplexer(int, out Error) | Creates a Multiplexer signal under the frame. A single frame can contain only one Multiplexer signal. |
| CreateMultiplexer(int, string, out Error) | Creates a Multiplexer signal under the frame. A single frame can contain only one Multiplexer signal. |
| CreateSignalBasedSignal(string, string, string, double, out Error) | Creates a SignalBasedSignal under the frame. |
| CreateSignalBasedSignal(string, string, string, double, out SignalBasedSignal) | Creates a SignalBasedSignal under the frame. |
| DisableTransmission(BaseNode) | Disables transmission of the outgoing frame when the value of DisableChannel is non-zero. |
| EnableTransmission() | Enables transmission of the outgoing frame. |
| GetAutomaticFrameProcessing() | Gets the Automatic Frame Processing section of a frame, which contains the CRC and Counter sections for the frame. |
| GetFrameFaulting() | Gets the Frame Faulting section of the frame, which contains the SkipCyclicFrames and TransmitTime channels for the frame. |
| GetFrameInformation() | Gets the Frame Information section of the frame, which contains the ReceiveTime and TimeDifference channels for the frame. |
| GetModeList() | Gets an array that contains the Mode elements from the current SignalBasedFrame. |
| GetMultiplexer() | Gets the Multiplexer signal for the frame, which defines an area within the frame that contains different dynamic signals based on the multiplexer signal value. |
| GetSignalBasedSignalList() | Gets an array that contains the SignalBasedSignal elements from the current SignalBasedFrame. This method gets all the signal format signals in the frame. |
| SetTransmitTrigger(FrameTriggerType, BaseNode) | Sets event-triggered frame transmission on the frame. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal-md5.html language=enus -->
## TOPIC 03736: MD5

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal-md5.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal-md5.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the MD5 message-digest for the signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic byte[] MD5 { get; }ReturnsThe message-digest, as a byte array.

### MD5

Gets the MD5 message-digest for the signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public byte[] MD5 { get; }

#### Returns

The message-digest, as a byte array.

Parent topic:

SignalBasedSignal Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html language=enus -->
## TOPIC 03737: SignalBasedSignal Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-signalbasedsignal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a signal format signal under an NI-XNET SignalBasedFrame. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SignalBasedSignal : ChannelRemarksUse the members of this class to get and configure settings for a signal format signal, including i

### SignalBasedSignal Class

Represents a signal format signal under an NI-XNET [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html).

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SignalBasedSignal : Channel

#### Remarks

Use the members of this class to get and configure settings for a signal format signal, including its name, default value, and data source.

**Accessing this Class**

- [CreateSignalBasedSignal(string, string, string, double, out Error)](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createsignalbasedsignal__string-string-string-double-out.1.html)
- [GetSignalBasedSignalList](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getsignalbasedsignallist.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| MD5 | Gets the MD5 message-digest for the signal. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-applyparameterfile.html language=enus -->
## TOPIC 03738: ApplyParameterFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-applyparameterfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-applyparameterfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to apply the parameter values defined in the ParameterFile when you deploy a system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ApplyParameterFile { get; set; }ReturnsTrue to apply the ParameterFile.

### ApplyParameterFile

Gets or sets a value indicating whether to apply the parameter values defined in the [ParameterFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html) when you deploy a system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ApplyParameterFile { get; set; }

#### Returns

True to apply the [ParameterFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html).

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-getexecutionorder.html language=enus -->
## TOPIC 03739: GetExecutionOrder()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-getexecutionorder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-getexecutionorder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Execution Order section, which contains information about the order in which your models execute relative to each other in the VeriStand Engine. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ExecutionOrder GetExecutionOrder()ReturnsAn ExecutionOrder object.

### GetExecutionOrder()

Gets the **Execution Order** section, which contains information about the order in which your models execute relative to each other in the VeriStand Engine.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ExecutionOrder](nationalinstruments-veristand-systemdefinitionapi-executionorder.html) GetExecutionOrder()

#### Returns

An [ExecutionOrder](nationalinstruments-veristand-systemdefinitionapi-executionorder.html) object.

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-getmodels.html language=enus -->
## TOPIC 03740: GetModels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-getmodels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-getmodels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Models section, which contains any compiled or uncompiled models you add to the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Models GetModels()ReturnsA Models object.

### GetModels()

Gets the [Models](nationalinstruments-veristand-systemdefinitionapi-models.html) section, which contains any compiled or uncompiled models you add to the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Models](nationalinstruments-veristand-systemdefinitionapi-models.html) GetModels()

#### Returns

A [Models](nationalinstruments-veristand-systemdefinitionapi-models.html) object.

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameteraccess.html language=enus -->
## TOPIC 03741: ParameterAccess

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameteraccess.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameteraccess.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the flag used to allow or deny reading and writing non-imported parameters. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ParameterAccess ParameterAccess { get; set; }

### ParameterAccess

Gets or sets the flag used to allow or deny reading and writing non-imported parameters.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ParameterAccess](nationalinstruments-veristand-systemdefinitionapi-parameteraccess.html) ParameterAccess { get; set; }

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameteraliasfile.html language=enus -->
## TOPIC 03742: ParameterAliasFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameteraliasfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameteraliasfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the parameter alias file to use with the ParameterFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ParameterAliasFile { get; set; }RemarksThe alias file must have a .txt file extension and use the same delimiter as the ParameterFile with which it cor

### ParameterAliasFile

Gets or sets the parameter alias file to use with the [ParameterFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ParameterAliasFile { get; set; }

#### Remarks

Note

The alias file must have a .txt file extension and use the same delimiter as the [ParameterFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html) with which it corresponds.

Aliasing Parameter Names in a Model Parameter File

NI VeriStand Help

#### Returns

The path of the alias file.

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html language=enus -->
## TOPIC 03743: ParameterFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the parameter calibration .txt file to apply when you deploy a system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ParameterFile { get; set; }RemarksFor more information about valid syntax in model parameter files, refer to the Support

### ParameterFile

Gets or sets the parameter calibration .txt file to apply when you deploy a system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ParameterFile { get; set; }

#### Remarks

For more information about valid syntax in model parameter files, refer to the *Supported Syntax in Model Parameter Files* topic of the *NI VeriStand Help*.

#### Returns

The path of the model parameter file.

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfileallowtempvariable.html language=enus -->
## TOPIC 03744: ParameterFileAllowTempVariable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfileallowtempvariable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfileallowtempvariable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the ParameterFile allows temporary variables. Temporary variables are always local to the file in which you define them. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ParameterFileAllowTempVariable { get; set; }RemarksFor more i

### ParameterFileAllowTempVariable

Gets or sets a value indicating whether the [ParameterFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html) allows temporary variables. Temporary variables are always local to the file in which you define them.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ParameterFileAllowTempVariable { get; set; }

#### Remarks

For more information about declaring temporary variables in a model parameter file, refer to the *Declaring Temporary Variables in a Model Parameter File* topic of the *NI VeriStand Help*.

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfiledelimiter.html language=enus -->
## TOPIC 03745: ParameterFileDelimiter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfiledelimiter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfiledelimiter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the delimiter used to separate parameter-value pairs in the ParameterFile. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Delimiter ParameterFileDelimiter { get; set; }ReturnsAn enumeration of Delimiter.

### ParameterFileDelimiter

Gets or sets the delimiter used to separate parameter-value pairs in the [ParameterFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameterfile.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Delimiter](nationalinstruments-veristand-systemdefinitionapi-delimiter.html) ParameterFileDelimiter { get; set; }

#### Returns

An enumeration of [Delimiter](nationalinstruments-veristand-systemdefinitionapi-delimiter.html).

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels-removeparameteraliasfile.html language=enus -->
## TOPIC 03746: RemoveParameterAliasFile()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels-removeparameteraliasfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels-removeparameteraliasfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the ParameterAliasFile property. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveParameterAliasFile()

### RemoveParameterAliasFile()

Removes the [ParameterAliasFile](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-parameteraliasfile.html) property.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveParameterAliasFile()

Parent topic:

SimulationModels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html language=enus -->
## TOPIC 03747: SimulationModels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Simulation Models section of a Target, which contains any models you import and information about the order in which they execute. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SimulationModels : SectionRemarksUse the members of this

### SimulationModels Class

Represents the **Simulation Models** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html), which contains any models you import and information about the order in which they execute.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SimulationModels : Section

#### Remarks

Use the members of this class to get the imported models and their execution order. You also can configure NI VeriStand to automatically apply initial values for model parameters when you deploy a system definition file.

**Accessing this Class**

- [GetSimulationModels](nationalinstruments-veristand-systemdefinitionapi-target-getsimulationmodels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ApplyParameterFile | Gets or sets a value indicating whether to apply the parameter values defined in the ParameterFile when you deploy a system definition file. |
| ParameterAccess | Gets or sets the flag used to allow or deny reading and writing non-imported parameters. |
| ParameterAliasFile | Gets or sets the parameter alias file to use with the ParameterFile. |
| ParameterFile | Gets or sets the parameter calibration .txt file to apply when you deploy a system definition file. |
| ParameterFileAllowTempVariable | Gets or sets a value indicating whether the ParameterFile allows temporary variables. Temporary variables are always local to the file in which you define them. |
| ParameterFileDelimiter | Gets or sets the delimiter used to separate parameter-value pairs in the ParameterFile. |

#### Methods

| Name | Description |
| --- | --- |
| GetExecutionOrder() | Gets the Execution Order section, which contains information about the order in which your models execute relative to each other in the VeriStand Engine. |
| GetModels() | Gets the Models section, which contains any compiled or uncompiled models you add to the system definition. |
| RemoveParameterAliasFile() | Removes the ParameterAliasFile property. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-singlepoint-addrawdatabasedframe__rawdatabasedframe-out.html language=enus -->
## TOPIC 03748: AddRawDataBasedFrame(RawDataBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-singlepoint-addrawdatabasedframe__rawdatabasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-singlepoint-addrawdatabasedframe__rawdatabasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified rawDataBasedFrame to the Single-Point section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe raw data format

### AddRawDataBasedFrame(RawDataBasedFrame, out Error)

Adds the specified *rawDataBasedFrame*  to the **Single-Point** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The raw data format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-singlepoint-addrawdatabasedframe__rawdatabasedframe.html language=enus -->
## TOPIC 03749: AddRawDataBasedFrame(RawDataBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-singlepoint-addrawdatabasedframe__rawdatabasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-singlepoint-addrawdatabasedframe__rawdatabasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified rawDataBasedFrame to the Single-Point section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe raw data format frame to add. Re

### AddRawDataBasedFrame(RawDataBasedFrame)

Adds the specified *rawDataBasedFrame*  to the **Single-Point** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The raw data format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-singlepoint-addsignalbasedframe__signalbasedframe-out.html language=enus -->
## TOPIC 03750: AddSignalBasedFrame(SignalBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-singlepoint-addsignalbasedframe__signalbasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-singlepoint-addsignalbasedframe__signalbasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signalBasedFrame to the Single-Point section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)RemarksFor example code and more information about this method, refer to one of the fo

### AddSignalBasedFrame(SignalBasedFrame, out Error)

Adds the specified *signalBasedFrame*  to the **Single-Point** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The signal format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

SinglePoint Class
