# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=2751 end=3000 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexray-addflexrayport__flexrayport-out.html language=enus -->
## TOPIC 02751: AddFlexRayPort(FlexRayPort, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexray-addflexrayport__flexrayport-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexray-addflexrayport__flexrayport-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified FlexRayPort under the FlexRay section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFlexRayPort(FlexRayPort flexRayPort, out Error error)ParametersNameTypeDescriptionflexRayPortFlexRayPortThe port to add.errorout ErrorReturns an NationalInstrume

### AddFlexRayPort(FlexRayPort, out Error)

Adds the specified [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html) under the **FlexRay** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFlexRayPort(FlexRayPort flexRayPort, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| flexRayPort | FlexRayPort | The port to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the port was added successfully.

Parent topic:

FlexRay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexray-addflexrayport__flexrayport.html language=enus -->
## TOPIC 02752: AddFlexRayPort(FlexRayPort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexray-addflexrayport__flexrayport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexray-addflexrayport__flexrayport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified FlexRayPort under the FlexRay section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFlexRayPort(FlexRayPort flexRayPort)ParametersNameTypeDescriptionflexRayPortFlexRayPortThe port to add.Returnstrue if the port was added successfully.

### AddFlexRayPort(FlexRayPort)

Adds the specified [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html) under the **FlexRay** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFlexRayPort(FlexRayPort flexRayPort)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| flexRayPort | FlexRayPort | The port to add. |

#### Returns

true if the port was added successfully.

Parent topic:

FlexRay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexray-getflexrayportlist.html language=enus -->
## TOPIC 02753: GetFlexRayPortList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexray-getflexrayportlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexray-getflexrayportlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the FlexRayPort elements from the current FlexRay section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FlexRayPort[] GetFlexRayPortList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifi

### GetFlexRayPortList()

Gets an array that contains the [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html) elements from the current [FlexRay](nationalinstruments-veristand-systemdefinitionapi-flexray.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html)[] GetFlexRayPortList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html) elements from the current [FlexRay](nationalinstruments-veristand-systemdefinitionapi-flexray.html) section.

Parent topic:

FlexRay Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexray.html language=enus -->
## TOPIC 02754: FlexRay Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexray.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexray.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the FlexRay section under XNET in the system definition. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FlexRay : SectionRemarksUse the members of this class to add a FlexRay port or get a list of existing FlexRay ports. Accessing this Cl

### FlexRay Class

Represents the **FlexRay** section under [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) in the system definition.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FlexRay : Section

#### Remarks

Use the members of this class to add a FlexRay port or get a list of existing FlexRay ports.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET.GetFlexRay

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddFlexRayPort(FlexRayPort, out Error) | Adds the specified FlexRayPort under the FlexRay section. |
| AddFlexRayPort(FlexRayPort) | Adds the specified FlexRayPort under the FlexRay section. |
| GetFlexRayPortList() | Gets an array that contains the FlexRayPort elements from the current FlexRay section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createchannelasleepchannel__out.html language=enus -->
## TOPIC 02755: CreateChannelASleepChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createchannelasleepchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createchannelasleepchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Channel A Sleep status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateChannelASleepChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error ob

### CreateChannelASleepChannel(out Error)

Creates the Channel A Sleep status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateChannelASleepChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createchannelbsleepchannel__out.html language=enus -->
## TOPIC 02756: CreateChannelBSleepChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createchannelbsleepchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createchannelbsleepchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Channel B Sleep status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateChannelBSleepChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error ob

### CreateChannelBSleepChannel(out Error)

Creates the Channel B Sleep status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateChannelBSleepChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createclockcorrectionfailedchannel__out.html language=enus -->
## TOPIC 02757: CreateClockCorrectionFailedChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createclockcorrectionfailedchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createclockcorrectionfailedchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Clock Correction Failed status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateClockCorrectionFailedChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.Ve

### CreateClockCorrectionFailedChannel(out Error)

Creates the Clock Correction Failed status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateClockCorrectionFailedChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createfaultchannel__out.html language=enus -->
## TOPIC 02758: CreateFaultChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createfaultchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createfaultchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Fault? status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateFaultChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error

### CreateFaultChannel(out Error)

Creates the Fault? status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateFaultChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createfaultcodechannel__out.html language=enus -->
## TOPIC 02759: CreateFaultCodeChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createfaultcodechannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createfaultcodechannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Fault Code status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateFaultCodeChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If

### CreateFaultCodeChannel(out Error)

Creates the Fault Code status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateFaultCodeChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createpassivetoactivecountchannel__out.html language=enus -->
## TOPIC 02760: CreatePassiveToActiveCountChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createpassivetoactivecountchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createpassivetoactivecountchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Passive To Active Count status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreatePassiveToActiveCountChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.Ver

### CreatePassiveToActiveCountChannel(out Error)

Creates the Passive To Active Count status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreatePassiveToActiveCountChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createpocstatechannel__out.html language=enus -->
## TOPIC 02761: CreatePOCStateChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createpocstatechannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-createpocstatechannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the POC State status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreatePOCStateChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no

### CreatePOCStateChannel(out Error)

Creates the POC State status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreatePOCStateChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getchannelasleepchannel.html language=enus -->
## TOPIC 02762: GetChannelASleepChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getchannelasleepchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getchannelasleepchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Channel A Sleep status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetChannelASleepChannel()

### GetChannelASleepChannel()

Gets the Channel A Sleep status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetChannelASleepChannel()

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getchannelbsleepchannel.html language=enus -->
## TOPIC 02763: GetChannelBSleepChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getchannelbsleepchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getchannelbsleepchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Channel B Sleep status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetChannelBSleepChannel()

### GetChannelBSleepChannel()

Gets the Channel B Sleep status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetChannelBSleepChannel()

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getclockcorrectionfailedchannel.html language=enus -->
## TOPIC 02764: GetClockCorrectionFailedChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getclockcorrectionfailedchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getclockcorrectionfailedchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Clock Correction Failed status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetClockCorrectionFailedChannel()

### GetClockCorrectionFailedChannel()

Gets the Clock Correction Failed status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetClockCorrectionFailedChannel()

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getfaultchannel.html language=enus -->
## TOPIC 02765: GetFaultChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getfaultchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getfaultchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Fault? status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetFaultChannel()

### GetFaultChannel()

Gets the Fault? status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetFaultChannel()

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getfaultcodechannel.html language=enus -->
## TOPIC 02766: GetFaultCodeChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getfaultcodechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getfaultcodechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Fault Code status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetFaultCodeChannel()

### GetFaultCodeChannel()

Gets the Fault Code status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetFaultCodeChannel()

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getpassivetoactivecountchannel.html language=enus -->
## TOPIC 02767: GetPassiveToActiveCountChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getpassivetoactivecountchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getpassivetoactivecountchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Passive To Active Count status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetPassiveToActiveCountChannel()

### GetPassiveToActiveCountChannel()

Gets the Passive To Active Count status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetPassiveToActiveCountChannel()

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getpocstatechannel.html language=enus -->
## TOPIC 02768: GetPOCStateChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getpocstatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels-getpocstatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the POC State status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetPOCStateChannel()

### GetPOCStateChannel()

Gets the POC State status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetPOCStateChannel()

Parent topic:

FlexRayInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels.html language=enus -->
## TOPIC 02769: FlexRayInterfaceChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Interface section under an NI-XNET FlexRay port. This section contains the port-specific channels which provide status information. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FlexRayInterfaceChannels : SectionMethodsNameDescriptio

### FlexRayInterfaceChannels Class

Represents the **Interface** section under an NI-XNET FlexRay port. This section contains the port-specific channels which provide status information.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FlexRayInterfaceChannels : Section

#### Methods

| Name | Description |
| --- | --- |
| CreateChannelASleepChannel(out Error) | Creates the Channel A Sleep status channel for the interface, if it does not exist. |
| CreateChannelBSleepChannel(out Error) | Creates the Channel B Sleep status channel for the interface, if it does not exist. |
| CreateClockCorrectionFailedChannel(out Error) | Creates the Clock Correction Failed status channel for the interface, if it does not exist. |
| CreateFaultChannel(out Error) | Creates the Fault? status channel for the interface, if it does not exist. |
| CreateFaultCodeChannel(out Error) | Creates the Fault Code status channel for the interface, if it does not exist. |
| CreatePassiveToActiveCountChannel(out Error) | Creates the Passive To Active Count status channel for the interface, if it does not exist. |
| CreatePOCStateChannel(out Error) | Creates the POC State status channel for the interface, if it does not exist. |
| GetChannelASleepChannel() | Gets the Channel A Sleep status channel for the interface. |
| GetChannelBSleepChannel() | Gets the Channel B Sleep status channel for the interface. |
| GetClockCorrectionFailedChannel() | Gets the Clock Correction Failed status channel for the interface. |
| GetFaultChannel() | Gets the Fault? status channel for the interface. |
| GetFaultCodeChannel() | Gets the Fault Code status channel for the interface. |
| GetPassiveToActiveCountChannel() | Gets the Passive To Active Count status channel for the interface. |
| GetPOCStateChannel() | Gets the POC State status channel for the interface. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-baudrate.html language=enus -->
## TOPIC 02770: BaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-baudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-baudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the baud rate that all cluster nodes use. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint BaudRate { get; set; }ReturnsThe baud rate. For FlexRay interfaces, this rate must be 2500000, 5000000, or 10000000.

### BaudRate

Gets or sets the baud rate that all cluster nodes use.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint BaudRate { get; set; }

#### Returns

The baud rate. For FlexRay interfaces, this rate must be 2500000, 5000000, or 10000000.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-clustername.html language=enus -->
## TOPIC 02771: ClusterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-clustername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-clustername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the cluster in LinkedDatabase that is associated with the FlexRayPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ClusterName { get; set; }ReturnsThe cluster name.

### ClusterName

Gets or sets the name of the cluster in [LinkedDatabase](nationalinstruments-veristand-systemdefinitionapi-flexrayport-linkeddatabase.html) that is associated with the [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ClusterName { get; set; }

#### Returns

The cluster name.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-createinterfacesection__out.html language=enus -->
## TOPIC 02772: CreateInterfaceSection(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-createinterfacesection__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-createinterfacesection__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the FlexRayInterfaceChannels section of the current FlexRayPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FlexRayInterfaceChannels CreateInterfaceSection(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error

### CreateInterfaceSection(out Error)

Creates the [FlexRayInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels.html) section of the current [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FlexRayInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels.html) CreateInterfaceSection(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-disabled.html language=enus -->
## TOPIC 02773: Disabled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-disabled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-disabled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the port is disabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Disabled { get; set; }

### Disabled

Gets or sets whether the port is disabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Disabled { get; set; }

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-echo.html language=enus -->
## TOPIC 02774: Echo

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-echo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-echo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Echo { get; set

### Echo

Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Echo { get; set; }

#### Returns

true it outgoing frames are echoed back as incoming frames.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-enablecoldstart.html language=enus -->
## TOPIC 02775: EnableColdStart

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-enablecoldstart.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-enablecoldstart.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool EnableColdStart { get; set; }Returnstrue if the interface operates as a cold-start node.

### EnableColdStart

Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool EnableColdStart { get; set; }

#### Returns

true if the interface operates as a cold-start node.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-enablepassivetoactive.html language=enus -->
## TOPIC 02776: EnablePassiveToActive

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-enablepassivetoactive.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-enablepassivetoactive.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Corresponds to the Interface:FlexRay:Allow Passive to Active property for the FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint EnablePassiveToActive { get; set; }

### EnablePassiveToActive

Corresponds to the Interface:FlexRay:Allow Passive to Active property for the FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint EnablePassiveToActive { get; set; }

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-flexrayport__string-ushort-database-string-uint.html language=enus -->
## TOPIC 02777: FlexRayPort(string, ushort, Database, string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-flexrayport__string-ushort-database-string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-flexrayport__string-ushort-database-string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FlexRayPort class and creates a port with the specified Name , PortNumber , and so on. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FlexRayPort(string Name, ushort PortNumber, Database LinkedDatabase, string ClusterName, uint BaudRate)Par

### FlexRayPort(string, ushort, Database, string, uint)

Initializes a new instance of the [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html) class and creates a port with the specified *Name* , *PortNumber* , and so on.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public FlexRayPort(string Name, ushort PortNumber, Database LinkedDatabase, string ClusterName, uint BaudRate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the port. |
| PortNumber | ushort | The physical address of the port. |
| LinkedDatabase | Database | The XNET database associated with the port. |
| ClusterName | string | The cluster in LinkedDatabase that is associated with the port. |
| BaudRate | uint | The baud rate all cluster nodes under the port use. This rate can be 2500000, 5000000, or 10000000. |

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-getincoming.html language=enus -->
## TOPIC 02778: GetIncoming()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-getincoming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-getincoming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the Incoming section of the port, which includes incoming single-point frames and raw frame data logging files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Incoming GetIncoming()ReturnsAn Incoming object.

### GetIncoming()

Accesses the [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) section of the port, which includes incoming single-point frames and raw frame data logging files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) GetIncoming()

#### Returns

An [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) object.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-getinterfacesection.html language=enus -->
## TOPIC 02779: GetInterfaceSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-getinterfacesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-getinterfacesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FlexRayInterfaceChannels section of the current FlexRayPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FlexRayInterfaceChannels GetInterfaceSection()

### GetInterfaceSection()

Gets the [FlexRayInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels.html) section of the current [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FlexRayInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-flexrayinterfacechannels.html) GetInterfaceSection()

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-getoutgoing.html language=enus -->
## TOPIC 02780: GetOutgoing()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-getoutgoing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-getoutgoing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the Outgoing section of the port, which includes outgoing event-triggered and cyclic frames and data replay files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Outgoing GetOutgoing()ReturnsAn Outgoing object.

### GetOutgoing()

Accesses the [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) section of the port, which includes outgoing event-triggered and cyclic frames and data replay files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) GetOutgoing()

#### Returns

An [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) object.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-incomingrate.html language=enus -->
## TOPIC 02781: IncomingRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-incomingrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-incomingrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processing rate for incoming frames in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint IncomingRate { get; set; }RemarksIf InlineIncoming is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the incoming frame sess

### IncomingRate

Gets or sets the processing rate for incoming frames in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint IncomingRate { get; set; }

#### Remarks

If [InlineIncoming](nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineincoming.html) is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the incoming frame session loop. For example, if the PCL execution rate is 1000 Hz, setting this rate to 100 Hz calls the frame session loop on every 10th iteration of the PCL.

#### Returns

An integer representing the processing rate in hertz.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineincoming.html language=enus -->
## TOPIC 02782: InlineIncoming

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineincoming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineincoming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### InlineIncoming

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InlineIncoming { get; set; }

#### Remarks

By default, NI VeriStand runs incoming and outgoing frame sessions as asynchronous custom devices that execute in separate loops from the PCL. Therefore, there is a 1-cycle delay when reading and writing channel values between the frame session loops and the rest of the system. You can inline frames to eliminate this delay by running the session loops as inline hardware interface custom devices, where NI VeriStand uses the loop rate to calculate the decimation factor for calls to the session loop.

Inlining frames is useful if you need to reduce latency when getting XNET data from your system, or if you want to correlate frame data with channel data. However, it can increase CPU usage and, if the XNET loops take too long to execute, delay the execution of the Primary Control Loop.

#### Returns

true if incoming frames are processed inline with the PCL. false if they are processed asynchronously.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineoutgoing.html language=enus -->
## TOPIC 02783: InlineOutgoing

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineoutgoing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineoutgoing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### InlineOutgoing

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InlineOutgoing { get; set; }

#### Remarks

By default, NI VeriStand runs incoming and outgoing frame sessions as asynchronous custom devices that execute in separate loops from the PCL. Therefore, there is a 1-cycle delay when reading and writing channel values between the frame session loops and the rest of the system. You can inline frames to eliminate this delay by running the session loops as inline hardware interface custom devices, where NI VeriStand uses the loop rate to calculate the decimation factor for calls to the session loop.

Inlining frames is useful if you need to reduce latency when getting XNET data from your system, or if you want to correlate frame data with channel data. However, it can increase CPU usage and, if the XNET loops take too long to execute, delay the execution of the Primary Control Loop.

#### Returns

true if outgoing frames are processed inline with the PCL. false if they are processed asynchronously.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-inputstreamqueuesize.html language=enus -->
## TOPIC 02784: InputStreamQueueSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-inputstreamqueuesize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-inputstreamqueuesize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint InputStreamQueueSize { get; s

### InputStreamQueueSize

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint InputStreamQueueSize { get; set; }

#### Returns

An integer representing the queue size.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-inputstreamreadtime.html language=enus -->
## TOPIC 02785: InputStreamReadTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-inputstreamreadtime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-inputstreamreadtime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InputStrea

### InputStreamReadTime

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InputStreamReadTime { get; set; }

#### Returns

A double representing the read time in seconds.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-keyslot.html language=enus -->
## TOPIC 02786: KeySlot

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-keyslot.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-keyslot.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint KeySlot { get; set; }ReturnsAn integer representing the slot

### KeySlot

Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint KeySlot { get; set; }

#### Returns

An integer representing the slot number.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-linkeddatabase.html language=enus -->
## TOPIC 02787: LinkedDatabase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-linkeddatabase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-linkeddatabase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET database associated with the FlexRayPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode LinkedDatabase { get; set; }ReturnsA BaseNode reference to the XNET database.

### LinkedDatabase

Gets or sets the XNET database associated with the [FlexRayPort](nationalinstruments-veristand-systemdefinitionapi-flexrayport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) LinkedDatabase { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the XNET database.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-outgoingrate.html language=enus -->
## TOPIC 02788: OutgoingRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-outgoingrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-outgoingrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processing rate for outgoing frames in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint OutgoingRate { get; set; }RemarksIf InlineOutgoing is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the outgoing frame sess

### OutgoingRate

Gets or sets the processing rate for outgoing frames in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint OutgoingRate { get; set; }

#### Remarks

If [InlineOutgoing](nationalinstruments-veristand-systemdefinitionapi-flexrayport-inlineoutgoing.html) is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the outgoing frame session loop. For example, if the PCL execution rate is 1000 Hz, setting this rate to 100 Hz calls the frame session loop on every 10th iteration of the PCL.

#### Returns

An integer representing the processing rate in hertz.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-portnumber.html language=enus -->
## TOPIC 02789: PortNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-portnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-portnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the physical address of the FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ushort PortNumber { get; set; }ReturnsThe physical address of the port.

### PortNumber

Gets or sets the physical address of the FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ushort PortNumber { get; set; }

#### Returns

The physical address of the port.

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport-termination.html language=enus -->
## TOPIC 02790: Termination

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport-termination.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport-termination.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the onboard XNETTermination. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic XNETTermination Termination { get; set; }ReturnsAn enumeration value of XNETTermination.

### Termination

Gets or sets the onboard [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html). This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) Termination { get; set; }

#### Returns

An enumeration value of [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html).

Parent topic:

FlexRayPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-flexrayport.html language=enus -->
## TOPIC 02791: FlexRayPort Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-flexrayport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-flexrayport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a port under an NI-XNET FlexRay device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FlexRayPort : SectionRemarksUse the members of this class to add a port under a FlexRay device, access incoming and outgoing frames, and set various pr

### FlexRayPort Class

Represents a port under an NI-XNET [FlexRay](nationalinstruments-veristand-systemdefinitionapi-flexray.html) device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FlexRayPort : Section

#### Remarks

Use the members of this class to add a port under a FlexRay device, access incoming and outgoing frames, and set various properties of the port, such as the associated XNET database.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRay.GetFlexRayPortList
- FlexRayPort Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| FlexRayPort(string, ushort, Database, string, uint) | Initializes a new instance of the FlexRayPort class and creates a port with the specified Name , PortNumber , and so on. |

#### Properties

| Name | Description |
| --- | --- |
| BaudRate | Gets or sets the baud rate that all cluster nodes use. |
| ClusterName | Gets or sets the name of the cluster in LinkedDatabase that is associated with the FlexRayPort. |
| Disabled | Gets or sets whether the port is disabled. |
| Echo | Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session. |
| EnableColdStart | Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster. |
| EnablePassiveToActive | Corresponds to the Interface:FlexRay:Allow Passive to Active property for the FlexRay port. |
| IncomingRate | Gets or sets the processing rate for incoming frames in hertz. |
| InlineIncoming | Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. |
| InlineOutgoing | Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. |
| InputStreamQueueSize | Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored. |
| InputStreamReadTime | Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read. |
| KeySlot | Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes. |
| LinkedDatabase | Gets or sets the XNET database associated with the FlexRayPort. |
| OutgoingRate | Gets or sets the processing rate for outgoing frames in hertz. |
| PortNumber | Gets or sets the physical address of the FlexRay port. |
| Termination | Gets or sets the onboard XNETTermination. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface. |

#### Methods

| Name | Description |
| --- | --- |
| CreateInterfaceSection(out Error) | Creates the FlexRayInterfaceChannels section of the current FlexRayPort. |
| GetIncoming() | Accesses the Incoming section of the port, which includes incoming single-point frames and raw frame data logging files. |
| GetInterfaceSection() | Gets the FlexRayInterfaceChannels section of the current FlexRayPort. |
| GetOutgoing() | Accesses the Outgoing section of the port, which includes outgoing event-triggered and cyclic frames and data replay files. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-formula-formula__string-string-string-string_arr1-basenode_arr1.html language=enus -->
## TOPIC 02792: Formula(string, string, string, string[], BaseNode[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-formula-formula__string-string-string-string_arr1-basenode_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-formula-formula__string-string-string-string_arr1-basenode_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Formula with the specified name, description, formula string, and variables. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Formula(string Name, string Description, string Formula, string[] VariableNames, BaseNode[] Variables)ParametersNameType

### Formula(string, string, string, string[], BaseNode[])

Initializes a new instance of [Formula](nationalinstruments-veristand-systemdefinitionapi-formula.html) with the specified name, description, formula string, and variables.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Formula(string Name, string Description, string Formula, string[] VariableNames, BaseNode[] Variables)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| Formula | string | The formula for which the channel calculates the result. |
| VariableNames | string[] | A list of names to display in the formula for the Variables. |
| Variables | BaseNode[] | A list of channels to assign as variables in the formula. |

Parent topic:

Formula Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-formula-formula__string-string.html language=enus -->
## TOPIC 02793: Formula(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-formula-formula__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-formula-formula__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Formula with the specified name, and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Formula(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the calculated channel.DescriptionstringThe description

### Formula(string, string)

Initializes a new instance of [Formula](nationalinstruments-veristand-systemdefinitionapi-formula.html) with the specified name, and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Formula(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |

Parent topic:

Formula Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-formula-formulastring.html language=enus -->
## TOPIC 02794: FormulaString

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-formula-formulastring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-formula-formulastring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the formula for which the channel calculates the result. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string FormulaString { get; }ReturnsThe formula.

### FormulaString

Gets the formula for which the channel calculates the result.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string FormulaString { get; }

#### Returns

The formula.

Parent topic:

Formula Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-formula-resetformula.html language=enus -->
## TOPIC 02795: ResetFormula()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-formula-resetformula.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-formula-resetformula.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the formula string and removes all variables. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ResetFormula()

### ResetFormula()

Clears the formula string and removes all variables.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ResetFormula()

Parent topic:

Formula Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-formula-setformula__string-string_arr1-basenode_arr1.html language=enus -->
## TOPIC 02796: SetFormula(string, string[], BaseNode[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-formula-setformula__string-string_arr1-basenode_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-formula-setformula__string-string_arr1-basenode_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the formula string and adds the specified variables. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetFormula(string Formula, string[] VariableNames, BaseNode[] Variables)ParametersNameTypeDescriptionFormulastringThe formula for which the channel calculates the r

### SetFormula(string, string[], BaseNode[])

Sets the formula string and adds the specified variables.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetFormula(string Formula, string[] VariableNames, BaseNode[] Variables)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Formula | string | The formula for which the channel calculates the result. |
| VariableNames | string[] | A list of names to display in the formula for the Variables. |
| Variables | BaseNode[] | A list of channels to assign as variables in the formula. |

Parent topic:

Formula Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-formula.html language=enus -->
## TOPIC 02797: Formula Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-formula.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-formula.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a calculated channel with the formula function. This function calculates the result of a formula you specify. Derives fromCalculatedChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Formula : CalculatedChannelRemarksUse the members of this class to get

### Formula Class

Represents a calculated channel with the formula function. This function calculates the result of a formula you specify.

#### Derives from

- CalculatedChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Formula : CalculatedChannel

#### Remarks

Use the members of this class to get or set the formula that the channel calculates.

**Accessing this Class**

- Formula Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Formula(string, string) | Initializes a new instance of Formula with the specified name, and description. |
| Formula(string, string, string, string[], BaseNode[]) | Initializes a new instance of Formula with the specified name, description, formula string, and variables. |

#### Properties

| Name | Description |
| --- | --- |
| FormulaString | Gets the formula for which the channel calculates the result. |

#### Methods

| Name | Description |
| --- | --- |
| ResetFormula() | Clears the formula string and removes all variables. |
| SetFormula(string, string[], BaseNode[]) | Sets the formula string and adds the specified variables. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice.html language=enus -->
## TOPIC 02798: AddFPGADevice()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an FPGA target to the FPGA section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFPGADevice()Returnstrue if the target was added successfully.

### AddFPGADevice()

Adds an FPGA target to the **FPGA** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFPGADevice()

#### Returns

true if the target was added successfully.

Parent topic:

FPGA Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__out.html language=enus -->
## TOPIC 02799: AddFPGADevice(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an FPGA target to the FPGA section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGADevice AddFPGADevice(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Er

### AddFPGADevice(out Error)

Adds an FPGA target to the **FPGA** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html) AddFPGADevice(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the target was added successfully.

Parent topic:

FPGA Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__string-out.html language=enus -->
## TOPIC 02800: AddFPGADevice(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an FPGA target with the specified FPGA configuration file to the FPGA section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGADevice AddFPGADevice(string FPGAConfigFile, out Error error)ParametersNameTypeDescriptionFPGAConfigFilestringThe FPGA configuration (.fpgac

### AddFPGADevice(string, out Error)

Adds an FPGA target with the specified FPGA configuration file to the **FPGA** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html) AddFPGADevice(string FPGAConfigFile, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| FPGAConfigFile | string | The FPGA configuration (.fpgaconfig) file that defines the target to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The FPGA device that was added

Parent topic:

FPGA Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__string.html language=enus -->
## TOPIC 02801: AddFPGADevice(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpga-addfpgadevice__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an FPGA target with the specified FPGA configuration file to the FPGA section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFPGADevice(string FPGAConfigFile)ParametersNameTypeDescriptionFPGAConfigFilestringThe FPGA configuration (.fpgaconfig) file that define

### AddFPGADevice(string)

Adds an FPGA target with the specified FPGA configuration file to the **FPGA** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFPGADevice(string FPGAConfigFile)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| FPGAConfigFile | string | The FPGA configuration (.fpgaconfig) file that defines the target to add. |

#### Returns

true if the target was added successfully.

Parent topic:

FPGA Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpga-getfpgadevicelist.html language=enus -->
## TOPIC 02802: GetFPGADeviceList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpga-getfpgadevicelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpga-getfpgadevicelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the FPGADevice elements from the FPGA section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGADevice[] GetFPGADeviceList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications you ma

### GetFPGADeviceList()

Gets an array that contains the [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html) elements from the [FPGA](nationalinstruments-veristand-systemdefinitionapi-fpga.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html)[] GetFPGADeviceList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html) elements from the [FPGA](nationalinstruments-veristand-systemdefinitionapi-fpga.html) section.

Parent topic:

FPGA Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpga.html language=enus -->
## TOPIC 02803: FPGA Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpga.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpga.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the FPGA section of a Chassis in the system definition. This section contains all the FPGA devices you add under the chassis. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGA : SectionRemarksUse the members of this class to add a new o

### FPGA Class

Represents the **FPGA** section of a [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) in the system definition. This section contains all the FPGA devices you add under the chassis.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGA : Section

#### Remarks

Use the members of this class to add a new or get a list of existing FPGA targets.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis.GetFPGA

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddFPGADevice() | Adds an FPGA target to the FPGA section. |
| AddFPGADevice(out Error) | Adds an FPGA target to the FPGA section. |
| AddFPGADevice(string) | Adds an FPGA target with the specified FPGA configuration file to the FPGA section. |
| AddFPGADevice(string, out Error) | Adds an FPGA target with the specified FPGA configuration file to the FPGA section. |
| GetFPGADeviceList() | Gets an array that contains the FPGADevice elements from the FPGA section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpga_support.html language=enus -->
## TOPIC 02804: NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpga_support.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpga_support.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNoneInterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support

#### Classes

None

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgaaicategory.html language=enus -->
## TOPIC 02805: FPGAAICategory Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgaaicategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgaaicategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Input » Analog section under an FPGADevice. Derives fromFPGACategorySyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAAICategory : FPGACategoryRemarksYou cannot directly call this class. Use the FPGACategory class to access sections under an FPGA devic

### FPGAAICategory Class

Represents the **Input » Analog** section under an [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

#### Derives from

- FPGACategory

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAAICategory : FPGACategory

#### Remarks

You cannot directly call this class. Use the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) class to access sections under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgaanaloginput.html language=enus -->
## TOPIC 02806: FPGAAnalogInput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgaanaloginput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgaanaloginput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FPGA analog input channel. Derives fromFPGAChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAAnalogInput : FPGAChannelRemarksYou cannot directly call this class. Use the FPGAChannel class to access channels under an FPGA device. Thread SafetyAny

### FPGAAnalogInput Class

Represents an FPGA analog input channel.

#### Derives from

- FPGAChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAAnalogInput : FPGAChannel

#### Remarks

You cannot directly call this class. Use the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) class to access channels under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgaanalogoutput.html language=enus -->
## TOPIC 02807: FPGAAnalogOutput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgaanalogoutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgaanalogoutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FPGA analog output channel. Derives fromFPGAChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAAnalogOutput : FPGAChannelRemarksYou cannot directly call this class. Use the FPGAChannel class to access channels under an FPGA device. Thread SafetyAn

### FPGAAnalogOutput Class

Represents an FPGA analog output channel.

#### Derives from

- FPGAChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAAnalogOutput : FPGAChannel

#### Remarks

You cannot directly call this class. Use the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) class to access channels under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgaaocategory.html language=enus -->
## TOPIC 02808: FPGAAOCategory Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgaaocategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgaaocategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Output » Analog section under an FPGADevice. Derives fromFPGACategorySyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAAOCategory : FPGACategoryRemarksYou cannot directly call this class. Use the FPGACategory class to access sections under an FPGA devi

### FPGAAOCategory Class

Represents the **Output » Analog** section under an [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

#### Derives from

- FPGACategory

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAAOCategory : FPGACategory

#### Remarks

You cannot directly call this class. Use the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) class to access sections under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgacategory-getcategorylist.html language=enus -->
## TOPIC 02809: GetCategoryList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgacategory-getcategorylist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgacategory-getcategorylist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the FPGACategory elements from the current FPGACategory. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGACategory[] GetCategoryList()RemarksModifications you make to the contents of this list apply to the system definition. However, modificati

### GetCategoryList()

Gets an array that contains the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) elements from the current [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html)[] GetCategoryList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) elements from the current [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html).

Parent topic:

FPGACategory Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgacategory-getchannellist.html language=enus -->
## TOPIC 02810: GetChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgacategory-getchannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgacategory-getchannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the FPGAChannel elements from the current FPGACategory. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGAChannel[] GetChannelList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications

### GetChannelList()

Gets an array that contains the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) elements from the current [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html)[] GetChannelList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) elements from the current [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html).

Parent topic:

FPGACategory Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html language=enus -->
## TOPIC 02811: FPGACategory Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a section under an FPGA device. Sections organize channels according to type. For example, Input » Analog, Output » Digital, and so on. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGACategory : SectionRemarksUse the members of this cl

### FPGACategory Class

Represents a section under an FPGA device. Sections organize channels according to type. For example, **Input » Analog**, **Output » Digital**, and so on.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGACategory : Section

#### Remarks

Use the members of this class to get a list of sections or channels under an FPGA device.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice.GetCategoryList
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGACategory.GetCategoryList

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetCategoryList() | Gets an array that contains the FPGACategory elements from the current FPGACategory. |
| GetChannelList() | Gets an array that contains the FPGAChannel elements from the current FPGACategory. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-channelbitoffset.html language=enus -->
## TOPIC 02812: ChannelBitOffset

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-channelbitoffset.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-channelbitoffset.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bit offset of the FPGA channel in the DMA packet. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint ChannelBitOffset { get; }ReturnsThe bit offset, as an integer.

### ChannelBitOffset

Gets the bit offset of the FPGA channel in the DMA packet.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint ChannelBitOffset { get; }

#### Returns

The bit offset, as an integer.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-fxpiwl.html language=enus -->
## TOPIC 02813: FXPIWL

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-fxpiwl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-fxpiwl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the integer word length of a fixed-point FPGA channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int FXPIWL { get; }ReturnsThe integer word length.

### FXPIWL

Gets the integer word length of a fixed-point FPGA channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int FXPIWL { get; }

#### Returns

The integer word length.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-fxpwl.html language=enus -->
## TOPIC 02814: FXPWL

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-fxpwl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-fxpwl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the word length of a fixed-point FPGA channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint FXPWL { get; }ReturnsThe word length.

### FXPWL

Gets the word length of a fixed-point FPGA channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint FXPWL { get; }

#### Returns

The word length.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-initialvalue.html language=enus -->
## TOPIC 02815: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the FPGA channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InitialValue { get; set; }ReturnsThe initial value of the channel.

### InitialValue

Gets or sets the initial value of the FPGA channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InitialValue { get; set; }

#### Returns

The initial value of the channel.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-offset.html language=enus -->
## TOPIC 02816: Offset

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-offset.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-offset.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the offset of the FPGA channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Offset { get; set; }ReturnsThe offset, in engineering units.

### Offset

Gets or sets the offset of the FPGA channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Offset { get; set; }

#### Returns

The offset, in engineering units.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-packetindex.html language=enus -->
## TOPIC 02817: PacketIndex

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-packetindex.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-packetindex.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the index of the packet in the DMA FIFO that defines the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PacketIndex { get; }ReturnsThe packet index.

### PacketIndex

Gets the index of the packet in the DMA FIFO that defines the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PacketIndex { get; }

#### Returns

The packet index.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-periodpwm.html language=enus -->
## TOPIC 02818: PeriodPWM

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-periodpwm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-periodpwm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse width modulation (PWM) period for an output channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PeriodPWM { get; set; }ReturnsThe PWM period.

### PeriodPWM

Gets or sets the pulse width modulation (PWM) period for an output channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PeriodPWM { get; set; }

#### Returns

The PWM period.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-representation.html language=enus -->
## TOPIC 02819: Representation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-representation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-representation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the data type of the FPGA channel as it is represented in the DMA packet. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint Representation { get; }RemarksThis property can return the following values:ValueData Type0Boolean1U82I83U164I165U326I327U648I649FXPU3210FXPI32

### Representation

Gets the data type of the FPGA channel as it is represented in the DMA packet.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint Representation { get; }

#### Remarks

This property can return the following values:

| Value | Data Type |
| --- | --- |
| 0 | Boolean |
| 1 | U8 |
| 2 | I8 |
| 3 | U16 |
| 4 | I16 |
| 5 | U32 |
| 6 | I32 |
| 7 | U64 |
| 8 | I64 |
| 9 | FXPU32 |
| 10 | FXPI32 |
| 11 | FXPU64 |
| 12 | FXPI64 |
| 13 | PWM |
| 14 | Void |
| 15 | Invalid |

#### Returns

The data type of the FPGA channel.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel-scaling.html language=enus -->
## TOPIC 02820: Scaling

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel-scaling.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel-scaling.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the scaling value applied to a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Scaling { get; set; }ReturnsThe range of the scale in engineering units.

### Scaling

Gets or sets the scaling value applied to a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Scaling { get; set; }

#### Returns

The range of the scale in engineering units.

Parent topic:

FPGAChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html language=enus -->
## TOPIC 02821: FPGAChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a channel of an FPGA device. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAChannel : ChannelRemarksUse the members of this class to configure properties of the channel, such as its offset, initial value, representation, and so on. Ac

### FPGAChannel Class

Represents a channel of an FPGA device.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAChannel : Channel

#### Remarks

Use the members of this class to configure properties of the channel, such as its offset, initial value, representation, and so on.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGACategory.GetChannelList

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ChannelBitOffset | Gets the bit offset of the FPGA channel in the DMA packet. |
| FXPIWL | Gets the integer word length of a fixed-point FPGA channel. |
| FXPWL | Gets the word length of a fixed-point FPGA channel. |
| InitialValue | Gets or sets the initial value of the FPGA channel. |
| Offset | Gets or sets the offset of the FPGA channel. |
| PacketIndex | Gets the index of the packet in the DMA FIFO that defines the channel. |
| PeriodPWM | Gets or sets the pulse width modulation (PWM) period for an output channel. |
| Representation | Gets the data type of the FPGA channel as it is represented in the DMA packet. |
| Scaling | Gets or sets the scaling value applied to a channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-changerioaddress__int-out.html language=enus -->
## TOPIC 02822: ChangeRIOAddress(int, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-changerioaddress__int-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-changerioaddress__int-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the RIO address of the FPGA target to RIOx, where x is the address number you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ChangeRIOAddress(int AddressNumber, out Error error)ParametersNameTypeDescriptionAddressNumberintThe address number you want to

### ChangeRIOAddress(int, out Error)

Changes the RIO address of the FPGA target to RIO*x*, where *x* is the address number you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ChangeRIOAddress(int AddressNumber, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| AddressNumber | int | The address number you want to assign to the RIO. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the RIO address was changed successfully.

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-changerioaddress__int.html language=enus -->
## TOPIC 02823: ChangeRIOAddress(int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-changerioaddress__int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-changerioaddress__int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the RIO address of the FPGA target to RIOx, where x is the address number you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ChangeRIOAddress(int AddressNumber)ParametersNameTypeDescriptionAddressNumberintThe address number you want to assign to the RI

### ChangeRIOAddress(int)

Changes the RIO address of the FPGA target to RIO*x*, where *x* is the address number you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ChangeRIOAddress(int AddressNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| AddressNumber | int | The address number you want to assign to the RIO. |

#### Returns

true if the RIO address was changed successfully.

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgabitfile.html language=enus -->
## TOPIC 02824: FPGABitfile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgabitfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgabitfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the FPGA bitfile used for the FPGA target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile FPGABitfile { get; }ReturnsA DependentFile reference to the bitfile.

### FPGABitfile

Gets the name of the FPGA bitfile used for the FPGA target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) FPGABitfile { get; }

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the bitfile.

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgaconfigfile.html language=enus -->
## TOPIC 02825: FPGAConfigFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgaconfigfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgaconfigfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the FPGA configuration file used to define the FPGA target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile FPGAConfigFile { get; }ReturnsA DependentFile reference to the configuration file.

### FPGAConfigFile

Gets the FPGA configuration file used to define the FPGA target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) FPGAConfigFile { get; }

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the configuration file.

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgadevice__string.html language=enus -->
## TOPIC 02826: FPGADevice(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgadevice__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-fpgadevice__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FPGADevice class for the device specified by Name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGADevice(string Name)ParametersNameTypeDescriptionNamestringThe name of the new FPGADevice object.

### FPGADevice(string)

Initializes a new instance of the [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html) class for the device specified by *Name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public FPGADevice(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the new FPGADevice object. |

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-getcategorylist.html language=enus -->
## TOPIC 02827: GetCategoryList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-getcategorylist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-getcategorylist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the FPGACategory elements from the current FPGADevice. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FPGACategory[] GetCategoryList()RemarksModifications you make to the contents of this list apply to the system definition. However, modification

### GetCategoryList()

Gets an array that contains the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) elements from the current [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html)[] GetCategoryList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) elements from the current [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-latestrefresh.html language=enus -->
## TOPIC 02828: LatestRefresh

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-latestrefresh.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-latestrefresh.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a timestamp indicating the last date and time that the FPGA configuration file, which specifies the content of the DMA FIFOs and how the device appears in System Explorer, was refreshed. Refreshing the configuration file essentially re-creates the device. SyntaxNamespace: NationalInstruments.Ve

### LatestRefresh

Gets a timestamp indicating the last date and time that the FPGA configuration file, which specifies the content of the DMA FIFOs and how the device appears in System Explorer, was refreshed. Refreshing the configuration file essentially re-creates the device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string LatestRefresh { get; }

#### Returns

The time of the latest refresh.

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-readpackets.html language=enus -->
## TOPIC 02829: ReadPackets

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-readpackets.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-readpackets.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of DMA read packets. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ReadPackets { get; }ReturnsThe number of packets.

### ReadPackets

Gets the number of DMA read packets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ReadPackets { get; }

#### Returns

The number of packets.

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice-writepackets.html language=enus -->
## TOPIC 02830: WritePackets

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice-writepackets.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice-writepackets.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of DMA write packets. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int WritePackets { get; }ReturnsThe number of packets.

### WritePackets

Gets the number of DMA write packets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int WritePackets { get; }

#### Returns

The number of packets.

Parent topic:

FPGADevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html language=enus -->
## TOPIC 02831: FPGADevice Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FPGA target under the FPGA section. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGADevice : SectionRemarksUse the members of this class to get information about the target, such as its associated bitfile, configuration file, and DM

### FPGADevice Class

Represents an FPGA target under the [FPGA](nationalinstruments-veristand-systemdefinitionapi-fpga.html) section.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGADevice : Section

#### Remarks

Use the members of this class to get information about the target, such as its associated bitfile, configuration file, and DMA read/write packets.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA.GetFPGADeviceList
- FPGADevice Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| FPGADevice(string) | Initializes a new instance of the FPGADevice class for the device specified by Name . |

#### Properties

| Name | Description |
| --- | --- |
| FPGABitfile | Gets the name of the FPGA bitfile used for the FPGA target. |
| FPGAConfigFile | Gets the FPGA configuration file used to define the FPGA target. |
| LatestRefresh | Gets a timestamp indicating the last date and time that the FPGA configuration file, which specifies the content of the DMA FIFOs and how the device appears in System Explorer, was refreshed. Refreshing the configuration file essentially re-creates the device. |
| ReadPackets | Gets the number of DMA read packets. |
| WritePackets | Gets the number of DMA write packets. |

#### Methods

| Name | Description |
| --- | --- |
| ChangeRIOAddress(int, out Error) | Changes the RIO address of the FPGA target to RIOx, where x is the address number you specify. |
| ChangeRIOAddress(int) | Changes the RIO address of the FPGA target to RIOx, where x is the address number you specify. |
| GetCategoryList() | Gets an array that contains the FPGACategory elements from the current FPGADevice. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadicategory.html language=enus -->
## TOPIC 02832: FPGADICategory Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadicategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadicategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Input » Digital section under an FPGADevice. Derives fromFPGACategorySyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGADICategory : FPGACategoryRemarksYou cannot directly call this class. Use the FPGACategory class to access sections under an FPGA devi

### FPGADICategory Class

Represents the **Input » Digital** section under an [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

#### Derives from

- FPGACategory

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGADICategory : FPGACategory

#### Remarks

You cannot directly call this class. Use the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) class to access sections under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadigitalinput.html language=enus -->
## TOPIC 02833: FPGADigitalInput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadigitalinput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadigitalinput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FPGA digital input channel. Derives fromFPGAChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGADigitalInput : FPGAChannelRemarksYou cannot directly call this class. Use the FPGAChannel class to access channels under an FPGA device. Thread SafetyAn

### FPGADigitalInput Class

Represents an FPGA digital input channel.

#### Derives from

- FPGAChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGADigitalInput : FPGAChannel

#### Remarks

You cannot directly call this class. Use the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) class to access channels under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadigitaloutput.html language=enus -->
## TOPIC 02834: FPGADigitalOutput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadigitaloutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadigitaloutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FPGA digital output channel. Derives fromFPGAChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGADigitalOutput : FPGAChannelRemarksYou cannot directly call this class. Use the FPGAChannel class to access channels under an FPGA device. Thread Safety

### FPGADigitalOutput Class

Represents an FPGA digital output channel.

#### Derives from

- FPGAChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGADigitalOutput : FPGAChannel

#### Remarks

You cannot directly call this class. Use the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) class to access channels under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgadocategory.html language=enus -->
## TOPIC 02835: FPGADOCategory Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgadocategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgadocategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Output » Digital section under an FPGADevice. Derives fromFPGACategorySyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGADOCategory : FPGACategoryRemarksYou cannot directly call this class. Use the FPGACategory class to access sections under an FPGA dev

### FPGADOCategory Class

Represents the **Output » Digital** section under an [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

#### Derives from

- FPGACategory

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGADOCategory : FPGACategory

#### Remarks

You cannot directly call this class. Use the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) class to access sections under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgapwmincategory.html language=enus -->
## TOPIC 02836: FPGAPWMInCategory Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgapwmincategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgapwmincategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Input » PWM section under an FPGADevice. Derives fromFPGACategorySyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAPWMInCategory : FPGACategoryRemarksYou cannot directly call this class. Use the FPGACategory class to access sections under an FPGA devic

### FPGAPWMInCategory Class

Represents the **Input » PWM** section under an [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

#### Derives from

- FPGACategory

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAPWMInCategory : FPGACategory

#### Remarks

You cannot directly call this class. Use the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) class to access sections under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgapwminput.html language=enus -->
## TOPIC 02837: FPGAPWMInput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgapwminput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgapwminput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FPGA PWM input channel. Derives fromFPGAChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAPWMInput : FPGAChannelRemarksYou cannot directly call this class. Use the FPGAChannel class to access channels under an FPGA device. Thread SafetyAny member

### FPGAPWMInput Class

Represents an FPGA PWM input channel.

#### Derives from

- FPGAChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAPWMInput : FPGAChannel

#### Remarks

You cannot directly call this class. Use the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) class to access channels under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgapwmoutcategory.html language=enus -->
## TOPIC 02838: FPGAPWMOutCategory Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgapwmoutcategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgapwmoutcategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Output » PWM section under an FPGADevice. Derives fromFPGACategorySyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAPWMOutCategory : FPGACategoryRemarksYou cannot directly call this class. Use the FPGACategory class to access sections under an FPGA dev

### FPGAPWMOutCategory Class

Represents the **Output » PWM** section under an [FPGADevice](nationalinstruments-veristand-systemdefinitionapi-fpgadevice.html).

#### Derives from

- FPGACategory

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAPWMOutCategory : FPGACategory

#### Remarks

You cannot directly call this class. Use the [FPGACategory](nationalinstruments-veristand-systemdefinitionapi-fpgacategory.html) class to access sections under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-fpgapwmoutput.html language=enus -->
## TOPIC 02839: FPGAPWMOutput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-fpgapwmoutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-fpgapwmoutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FPGA PWM output channel. Derives fromFPGAChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FPGAPWMOutput : FPGAChannelRemarksYou cannot directly call this class. Use the FPGAChannel class to access channels under an FPGA device. Thread SafetyAny memb

### FPGAPWMOutput Class

Represents an FPGA PWM output channel.

#### Derives from

- FPGAChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FPGAPWMOutput : FPGAChannel

#### Remarks

You cannot directly call this class. Use the [FPGAChannel](nationalinstruments-veristand-systemdefinitionapi-fpgachannel.html) class to access channels under an FPGA device.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-framefaulting-getskipcyclicframes.html language=enus -->
## TOPIC 02840: GetSkipCyclicFrames()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-framefaulting-getskipcyclicframes.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-framefaulting-getskipcyclicframes.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the SkipCyclicFrames channel under the Frame Faulting section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SkipCyclicFrames GetSkipCyclicFrames()ReturnsA SkipCyclicFrames reference.

### GetSkipCyclicFrames()

Gets a reference to the [SkipCyclicFrames](nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html) channel under the Frame Faulting section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SkipCyclicFrames](nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html) GetSkipCyclicFrames()

#### Returns

A [SkipCyclicFrames](nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html) reference.

Parent topic:

FrameFaulting Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-framefaulting-gettransmittime.html language=enus -->
## TOPIC 02841: GetTransmitTime()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-framefaulting-gettransmittime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-framefaulting-gettransmittime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the TransmitTime channel under the Frame Faulting section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TransmitTime GetTransmitTime()ReturnsA TransmitTime reference.

### GetTransmitTime()

Gets a reference to the [TransmitTime](nationalinstruments-veristand-systemdefinitionapi-transmittime.html) channel under the Frame Faulting section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TransmitTime](nationalinstruments-veristand-systemdefinitionapi-transmittime.html) GetTransmitTime()

#### Returns

A [TransmitTime](nationalinstruments-veristand-systemdefinitionapi-transmittime.html) reference.

Parent topic:

FrameFaulting Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-framefaulting.html language=enus -->
## TOPIC 02842: FrameFaulting Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-framefaulting.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-framefaulting.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Frame Faulting section under an outgoing cyclic frame of an NI-XNET CAN port. This section contains channels you can use to configure the transmission of cyclic frames. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FrameFaulting : Sect

### FrameFaulting Class

Represents a **Frame Faulting** section under an outgoing cyclic frame of an NI-XNET CAN port. This section contains channels you can use to configure the transmission of cyclic frames.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FrameFaulting : Section

#### Remarks

Use the members of this class to access the [SkipCyclicFrames](nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html) and [TransmitTime](nationalinstruments-veristand-systemdefinitionapi-transmittime.html) channels for an outgoing cyclic frame.

**Accessing this Class**

- [CreateFrameFaulting(bool, bool, out Error)](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe-createframefaulting__bool-bool-out.1.html)
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.GetFrameFaulting
- [GetFrameFaulting](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getframefaulting.html)
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.GetFrameFaulting

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetSkipCyclicFrames() | Gets a reference to the SkipCyclicFrames channel under the Frame Faulting section. |
| GetTransmitTime() | Gets a reference to the TransmitTime channel under the Frame Faulting section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frameid-id.html language=enus -->
## TOPIC 02843: ID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frameid-id.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frameid-id.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ID number of the current incoming frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint ID { get; }ReturnsThe frame ID.

### ID

Gets the ID number of the current incoming frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint ID { get; }

#### Returns

The frame ID.

Parent topic:

FrameID Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frameid.html language=enus -->
## TOPIC 02844: FrameID Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frameid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frameid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Frame ID channel under the FrameInformation section of an incoming, raw data format NI-XNET frame. This channel contains the ID number that identifies the frame. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class FrameID : ChannelRemarksUse

### FrameID Class

Represents a **Frame ID** channel under the [FrameInformation](nationalinstruments-veristand-systemdefinitionapi-frameinformation.html) section of an incoming, raw data format NI-XNET frame. This channel contains the ID number that identifies the frame.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FrameID : Channel

#### Remarks

Use the members of this class to get information about a **Frame ID** channel, including the ID number of the current incoming frame. Only incoming, event-triggered, raw data format frames can have associated Frame ID channels.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.FrameInformation.GetFrameID

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ID | Gets the ID number of the current incoming frame. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frameinformation-getframeid.html language=enus -->
## TOPIC 02845: GetFrameID()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frameinformation-getframeid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frameinformation-getframeid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Frame ID channel under the current Frame Information section. The Frame ID channel contains the ID number that identifies an incoming, raw data format NI-XNET frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FrameID GetFrameID()ReturnsA FrameID reference.

### GetFrameID()

Gets the Frame ID channel under the current Frame Information section. The Frame ID channel contains the ID number that identifies an incoming, raw data format NI-XNET frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FrameID](nationalinstruments-veristand-systemdefinitionapi-frameid.html) GetFrameID()

#### Returns

A [FrameID](nationalinstruments-veristand-systemdefinitionapi-frameid.html) reference.

Parent topic:

FrameInformation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frameinformation-getreceivetime.html language=enus -->
## TOPIC 02846: GetReceiveTime()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frameinformation-getreceivetime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frameinformation-getreceivetime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Receive Time channel under the current Frame Information section. The Receive Time channel contains the timestamp of the most recently received frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ReceiveTime GetReceiveTime()ReturnsA ReceiveTime reference.

### GetReceiveTime()

Gets the Receive Time channel under the current Frame Information section. The Receive Time channel contains the timestamp of the most recently received frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ReceiveTime](nationalinstruments-veristand-systemdefinitionapi-receivetime.html) GetReceiveTime()

#### Returns

A [ReceiveTime](nationalinstruments-veristand-systemdefinitionapi-receivetime.html) reference.

Parent topic:

FrameInformation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frameinformation-gettimedifference.html language=enus -->
## TOPIC 02847: GetTimeDifference()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frameinformation-gettimedifference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frameinformation-gettimedifference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Time Difference channel under the current Frame Information section. The Time Difference channel contains the difference between the two most recent ReceiveTime timestamps. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TimeDifference GetTimeDifference()ReturnsA Ti

### GetTimeDifference()

Gets the Time Difference channel under the current Frame Information section. The Time Difference channel contains the difference between the two most recent [ReceiveTime](nationalinstruments-veristand-systemdefinitionapi-receivetime.html) timestamps.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TimeDifference](nationalinstruments-veristand-systemdefinitionapi-timedifference.html) GetTimeDifference()

#### Returns

A [TimeDifference](nationalinstruments-veristand-systemdefinitionapi-timedifference.html) reference.

Parent topic:

FrameInformation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frameinformation.html language=enus -->
## TOPIC 02848: FrameInformation Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frameinformation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frameinformation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Frame Information section under an incoming NI-XNET frame. This section contains channels that store information about the frame, such as the timestamp at which it was received and the ID number of the current frame. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.Syst

### FrameInformation Class

Represents a **Frame Information** section under an incoming NI-XNET frame. This section contains channels that store information about the frame, such as the timestamp at which it was received and the ID number of the current frame.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class FrameInformation : Section

#### Remarks

Use the members of this class to access [FrameID](nationalinstruments-veristand-systemdefinitionapi-frameid.html), [ReceiveTime](nationalinstruments-veristand-systemdefinitionapi-receivetime.html), and [TimeDifference](nationalinstruments-veristand-systemdefinitionapi-timedifference.html) channels.

**Accessing this Class**

- [CreateFrameInformation(bool, bool, out Error)](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe-createframeinformation__bool-bool-out.1.html)
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.GetFrameInformation
- [CreateFrameInformation(out Error)](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createframeinformation__out.1.html)
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.GetFrameInformation

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetFrameID() | Gets the Frame ID channel under the current Frame Information section. The Frame ID channel contains the ID number that identifies an incoming, raw data format NI-XNET frame. |
| GetReceiveTime() | Gets the Receive Time channel under the current Frame Information section. The Receive Time channel contains the timestamp of the most recently received frame. |
| GetTimeDifference() | Gets the Time Difference channel under the current Frame Information section. The Time Difference channel contains the difference between the two most recent ReceiveTime timestamps. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-framephasetype.html language=enus -->
## TOPIC 02849: FramePhaseType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-framephasetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-framephasetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to reset the timer of a software cyclic trigger after each transmission of an outgoing frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum FramePhaseTypeRemarksSoftware cyclic triggers transmit outgoing event-triggered frames at regular intervals sp

### FramePhaseType Enumeration

Specifies whether to reset the timer of a software cyclic trigger after each transmission of an outgoing frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum FramePhaseType

#### Remarks

Software cyclic triggers transmit outgoing event-triggered frames at regular intervals specified by a TransmitTime property on the frame.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Unchanged | 0 | Leaves the timer unchanged after each transmission of an outgoing frame. |
| Reset | 1 | Resets the timer after each transmission of an outgoing frame. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frametriggertype.html language=enus -->
## TOPIC 02850: FrameTriggerType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frametriggertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frametriggertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a condition that a trigger channel must meet to trigger transmission of an outgoing frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum FrameTriggerTypeMembersNameValueDescriptionChannelValueChange0Triggers when the value of the frame changes. TriggerChanne

### FrameTriggerType Enumeration

Specifies a condition that a trigger channel must meet to trigger transmission of an outgoing frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum FrameTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ChannelValueChange | 0 | Triggers when the value of the frame changes. |
| TriggerChannelNotZero | 1 | Triggers when the value of the trigger channel is non-zero. |
| ChannelValueChangeOrTriggerChannelNotZero | 2 | Triggers when the value of the frame changes or when the value of trigger channel is non-zero. |
| TriggerChannelAnyValueChange | 3 | Triggers when the value of the trigger channel changes. |
| ChannelValueChangeOrTriggerChannelAnyValueChange | 4 | Triggers when the value of the frame changes or the value of the trigger channel changes. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-frametype.html language=enus -->
## TOPIC 02851: FrameType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-frametype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-frametype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of a CAN or FlexRay frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum FrameTypeMembersNameValueDescriptionCANDataFrame0A CAN data frame, which contains payload data. CANRemoteFrame1A CAN remote frame, which requests data for the corresponding fra

### FrameType Enumeration

Specifies the type of a CAN or FlexRay frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum FrameType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| CANDataFrame | 0 | A CAN data frame, which contains payload data. |
| CANRemoteFrame | 1 | A CAN remote frame, which requests data for the corresponding frame ID. |
| FlexRayDataFrame | 32 | A FlexRay data frame, which contains payload data. |
| FlexRayNullFrame | 33 | A FlexRay null frame, which indicates when the transmitting ECU does not have new data for the current cycle. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-generator-getstimuluschannellist.html language=enus -->
## TOPIC 02852: GetStimulusChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-generator-getstimuluschannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-generator-getstimuluschannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the StimulusChannel elements from the current Generator section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic StimulusChannel[] GetStimulusChannelList()RemarksThis method is obsolete in NI VeriStand 2011 and later and does not interact with the

### GetStimulusChannelList()

Gets an array that contains the [StimulusChannel](nationalinstruments-veristand-systemdefinitionapi-stimuluschannel.html) elements from the current [Generator](nationalinstruments-veristand-systemdefinitionapi-generator.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [StimulusChannel](nationalinstruments-veristand-systemdefinitionapi-stimuluschannel.html)[] GetStimulusChannelList()

#### Remarks

Note

This method is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [StimulusChannel](nationalinstruments-veristand-systemdefinitionapi-stimuluschannel.html) elements from the current [Generator](nationalinstruments-veristand-systemdefinitionapi-generator.html) section.

Parent topic:

Generator Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-generator.html language=enus -->
## TOPIC 02853: Generator Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-generator.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-generator.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a stimulus generator in the Legacy Stimulus Profile Editor, which produces simulated real-world signals that stimulus profiles use to perform tests on a system. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Generator : SectionRemarksThis

### Generator Class

Represents a stimulus generator in the Legacy Stimulus Profile Editor, which produces simulated real-world signals that stimulus profiles use to perform tests on a system.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Generator : Section

#### Remarks

Note

This class is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Stimulus.GetGeneratorList

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetStimulusChannelList() | Gets an array that contains the StimulusChannel elements from the current Generator section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-globalparameterscopes.html language=enus -->
## TOPIC 02854: GlobalParameterScopes Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-globalparameterscopes.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-globalparameterscopes.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether global parameters in a Model share their values with other models. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum GlobalParameterScopesMembersNameValueDescriptionTarget0Updates to a global parameter apply to the current model and to any global paramet

### GlobalParameterScopes Enumeration

Specifies whether global parameters in a [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) share their values with other models.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum GlobalParameterScopes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Target | 0 | Updates to a global parameter apply to the current model and to any global parameters with the same name and scope in other models on the target. |
| Model | 1 | Updates to a global parameter are restricted to the instance of the parameter in the current model. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-globalsequencecommand.html language=enus -->
## TOPIC 02855: GlobalSequenceCommand Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-globalsequencecommand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-globalsequencecommand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the command for all running sequences. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum GlobalSequenceCommandMembersNameValueDescriptionStopAllStops all running real-time sequences. AbortAllAborts all running real-time sequences. StopGroupStop all running real-

### GlobalSequenceCommand Enumeration

Specifies the command for all running sequences.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum GlobalSequenceCommand

#### Members

| Name | Value | Description |
| --- | --- | --- |
| StopAll |  | Stops all running real-time sequences. |
| AbortAll |  | Aborts all running real-time sequences. |
| StopGroup |  | Stop all running real-time sequences in the specified Group. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-gotolabel-gotolabel__string-string-basenode.html language=enus -->
## TOPIC 02856: GotoLabel(string, string, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-gotolabel-gotolabel__string-string-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-gotolabel-gotolabel__string-string-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of GotoLabel with the specified name, description, and label. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic GotoLabel(string Name, string Description, BaseNode Label)ParametersNameTypeDescriptionNamestringThe name of the step.DescriptionstringThe

### GotoLabel(string, string, BaseNode)

Initializes a new instance of [GotoLabel](nationalinstruments-veristand-systemdefinitionapi-gotolabel.html) with the specified name, description, and label.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public GotoLabel(string Name, string Description, BaseNode Label)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the step. |
| Description | string | The description of the step. |
| Label | BaseNode | The procedure step to jump to when the GotoLabel step executes. |

Parent topic:

GotoLabel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-gotolabel-label.html language=enus -->
## TOPIC 02857: Label

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-gotolabel-label.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-gotolabel-label.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the procedure step to execute when the GotoLabel step is executed. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Label { get; set; }ReturnsThe label of the procedure step to go to.

### Label

Gets or sets the procedure step to execute when the [GotoLabel](nationalinstruments-veristand-systemdefinitionapi-gotolabel.html) step is executed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Label { get; set; }

#### Returns

The label of the procedure step to go to.

Parent topic:

GotoLabel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-gotolabel.html language=enus -->
## TOPIC 02858: GotoLabel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-gotolabel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-gotolabel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Goto Label step that you can add to a procedure. When this step executes, the procedure jumps to the step specified by M:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel.Label. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class G

### GotoLabel Class

Represents a **Goto Label** step that you can add to a procedure. When this step executes, the procedure jumps to the step specified by M:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel.Label.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class GotoLabel : Command

#### Remarks

Use the members of this class to access the **Exit Subroutine** step.

**Accessing this Class**

- GotoLabel Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| GotoLabel(string, string, BaseNode) | Initializes a new instance of GotoLabel with the specified name, description, and label. |

#### Properties

| Name | Description |
| --- | --- |
| Label | Gets or sets the procedure step to execute when the GotoLabel step is executed. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-hardware-addchassis__chassis-out.html language=enus -->
## TOPIC 02859: AddChassis(Chassis, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-hardware-addchassis__chassis-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-hardware-addchassis__chassis-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Chassis to the Hardware section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddChassis(Chassis chassis, out Error error)ParametersNameTypeDescriptionchassisChassisThe chassis to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error obj

### AddChassis(Chassis, out Error)

Adds the specified [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) to the **Hardware** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddChassis(Chassis chassis, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| chassis | Chassis | The chassis to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) was added successfully.

Parent topic:

Hardware Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-hardware-addchassis__chassis.html language=enus -->
## TOPIC 02860: AddChassis(Chassis)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-hardware-addchassis__chassis.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-hardware-addchassis__chassis.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Chassis to the Hardware section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddChassis(Chassis chassis)ParametersNameTypeDescriptionchassisChassisThe chassis to add.Returnstrue if the Chassis was added successfully.

### AddChassis(Chassis)

Adds the specified [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) to the **Hardware** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddChassis(Chassis chassis)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| chassis | Chassis | The chassis to add. |

#### Returns

true if the [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) was added successfully.

Parent topic:

Hardware Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-hardware-addnewchassis__string-out.html language=enus -->
## TOPIC 02861: AddNewChassis(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-hardware-addnewchassis__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-hardware-addnewchassis__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Chassis with the specified name to the Hardware section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Chassis AddNewChassis(string Name, out Error error)ParametersNameTypeDescriptionNamestringThe name of the chassis.errorout ErrorReturns an NationalInstruments.

### AddNewChassis(string, out Error)

Adds a new [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) with the specified name to the **Hardware** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) AddNewChassis(string Name, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the chassis. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new Chassis.

Parent topic:

Hardware Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-hardware-addnewchassis__string.html language=enus -->
## TOPIC 02862: AddNewChassis(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-hardware-addnewchassis__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-hardware-addnewchassis__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Chassis with the specified name to the Hardware section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewChassis(string Name)ParametersNameTypeDescriptionNamestringThe name of the chassis.Returnstrue if the Chassis was added successfully.

### AddNewChassis(string)

Adds a new [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) with the specified name to the **Hardware** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewChassis(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the chassis. |

#### Returns

true if the [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) was added successfully.

Parent topic:

Hardware Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-hardware-getchassislist.html language=enus -->
## TOPIC 02863: GetChassisList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-hardware-getchassislist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-hardware-getchassislist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Chassis elements from the Hardware section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Chassis[] GetChassisList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications you make to

### GetChassisList()

Gets an array that contains the [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) elements from the [Hardware](nationalinstruments-veristand-systemdefinitionapi-hardware.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html)[] GetChassisList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

An array that contains the [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) elements from the [Hardware](nationalinstruments-veristand-systemdefinitionapi-hardware.html) section.

Parent topic:

Hardware Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-hardware-getslsc.html language=enus -->
## TOPIC 02864: GetSLSC()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-hardware-getslsc.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-hardware-getslsc.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the SLSC node instance associated to this Hardware section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSC GetSLSC()ReturnsThe SLSC element.

### GetSLSC()

Get the SLSC node instance associated to this Hardware section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSC](nationalinstruments-veristand-systemdefinitionapi-slsc.html) GetSLSC()

#### Returns

The [SLSC](nationalinstruments-veristand-systemdefinitionapi-slsc.html) element.

Parent topic:

Hardware Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-hardware.html language=enus -->
## TOPIC 02865: Hardware Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-hardware.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-hardware.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Hardware section of a Target, which contains any chassis you add. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Hardware : SectionRemarksUse the members of this class to add a new chassis or get a list of existing chassis. Accessing

### Hardware Class

Represents the **Hardware** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html), which contains any chassis you add.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Hardware : Section

#### Remarks

Use the members of this class to add a new chassis or get a list of existing chassis.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.GetHardware

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddChassis(Chassis, out Error) | Adds the specified Chassis to the Hardware section. |
| AddChassis(Chassis) | Adds the specified Chassis to the Hardware section. |
| AddNewChassis(string) | Adds a new Chassis with the specified name to the Hardware section. |
| AddNewChassis(string, out Error) | Adds a new Chassis with the specified name to the Hardware section. |
| GetChassisList() | Gets an array that contains the Chassis elements from the Hardware section. |
| GetSLSC() | Get the SLSC node instance associated to this Hardware section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-baudrate.html language=enus -->
## TOPIC 02866: BaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-baudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-baudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CAN baud rate. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ulong BaudRate { get; set; }

### BaudRate

Gets or sets the CAN baud rate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong BaudRate { get; set; }

Parent topic:

ICANConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-brsbaudrate.html language=enus -->
## TOPIC 02867: BRSBaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-brsbaudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-brsbaudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CAN-BRS baud rate. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ulong BRSBaudRate { get; set; }

### BRSBaudRate

Gets or sets the CAN-BRS baud rate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong BRSBaudRate { get; set; }

Parent topic:

ICANConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-fdisomode.html language=enus -->
## TOPIC 02868: FDISOMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-fdisomode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-fdisomode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CAN FDISOMode. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FDISOMode FDISOMode { get; set; }

### FDISOMode

Gets or sets the CAN [FDISOMode](nationalinstruments-veristand-systemdefinitionapi-fdisomode.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FDISOMode](nationalinstruments-veristand-systemdefinitionapi-fdisomode.html) FDISOMode { get; set; }

Parent topic:

ICANConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-iomode.html language=enus -->
## TOPIC 02869: IOMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-iomode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-iomode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CANIOMode. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANIOMode IOMode { get; set; }

### IOMode

Gets or sets the [CANIOMode](nationalinstruments-veristand-systemdefinitionapi-caniomode.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CANIOMode](nationalinstruments-veristand-systemdefinitionapi-caniomode.html) IOMode { get; set; }

Parent topic:

ICANConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-transceivertype.html language=enus -->
## TOPIC 02870: TransceiverType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-transceivertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-transceivertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CANTransceiverType. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANTransceiverType TransceiverType { get; set; }

### TransceiverType

Gets or sets the [CANTransceiverType](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CANTransceiverType](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html) TransceiverType { get; set; }

Parent topic:

ICANConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-xnetinterface.html language=enus -->
## TOPIC 02871: XNETInterface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-xnetinterface.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icanconfiguration-xnetinterface.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET Interface to be used to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string XNETInterface { get; set; }RemarksUse MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and in

### XNETInterface

Gets or sets the XNET Interface to be used to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string XNETInterface { get; set; }

#### Remarks

Use MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and interfaces.

Parent topic:

ICANConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icanconfiguration.html language=enus -->
## TOPIC 02872: ICANConfiguration Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icanconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icanconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for CAN communication. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic interface ICANConfigurationPropertiesNameDescriptionBaudRateGets or sets the CAN baud rate. BRSBaudRateGets or sets the CAN-BRS baud rate. FDISOModeGets or set

### ICANConfiguration Interface

Represents the configuration for CAN communication.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public interface ICANConfiguration

#### Properties

| Name | Description |
| --- | --- |
| BaudRate | Gets or sets the CAN baud rate. |
| BRSBaudRate | Gets or sets the CAN-BRS baud rate. |
| FDISOMode | Gets or sets the CAN FDISOMode. |
| IOMode | Gets or sets the CANIOMode. |
| TransceiverType | Gets or sets the CANTransceiverType. |
| XNETInterface | Gets or sets the XNET Interface to be used to connect to the real network. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-columndimensions.html language=enus -->
## TOPIC 02873: ColumnDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-columndimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-columndimensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of columns in the channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ColumnDimensions { get; }ReturnsThe number of columns.

### ColumnDimensions

Gets the number of columns in the channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ColumnDimensions { get; }

#### Returns

The number of columns.

Parent topic:

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-datasource.html language=enus -->
## TOPIC 02874: DataSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-datasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-datasource.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-getvaluetable__out-out.html language=enus -->
## TOPIC 02875: GetValueTable(out string[], out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-getvaluetable__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-getvaluetable__out-out.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-isreadable.html language=enus -->
## TOPIC 02876: IsReadable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-isreadable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-isreadable.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-iswritable.html language=enus -->
## TOPIC 02877: IsWritable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-iswritable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-iswritable.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-removedatasource.html language=enus -->
## TOPIC 02878: RemoveDataSource()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-removedatasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-removedatasource.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-rowdimensions.html language=enus -->
## TOPIC 02879: RowDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-rowdimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-rowdimensions.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-scaleunits.html language=enus -->
## TOPIC 02880: ScaleUnits

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-scaleunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-scaleunits.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel-units.html language=enus -->
## TOPIC 02881: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel-units.html
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

IChannel Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ichannel.html language=enus -->
## TOPIC 02882: IChannel Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ichannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ichannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: An interface defining system definition channel behavior. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic interface IChannelPropertiesNameDescriptionColumnDimensionsGets the number of columns in the channel value. DataSourceGets or sets the source channel tha

### IChannel Interface

An interface defining system definition channel behavior.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public interface IChannel

#### Properties

| Name | Description |
| --- | --- |
| ColumnDimensions | Gets the number of columns in the channel value. |
| DataSource | Gets or sets the source channel that maps to the current channel and provides it data. |
| IsReadable | Gets a value indicating whether the channel is readable. |
| IsWritable | Gets a value indicating whether the channel is writable. |
| RowDimensions | Gets the number of rows in the channel value. |
| ScaleUnits | Gets the units of the scale associated with the channel. |
| Units | Gets or sets the units associated with the channel. This can be any arbitrary string. |

#### Methods

| Name | Description |
| --- | --- |
| GetValueTable(out string[], out double[]) | Gets the value table for the channel. |
| RemoveDataSource() | Removes the source channel that maps to the current channel and provides it data. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icustomdevicepluginnodefactory-tryinitializebasenodetypetocustomdevice__basenodetype.html language=enus -->
## TOPIC 02883: TryInitializeBaseNodeTypeToCustomDevice(BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icustomdevicepluginnodefactory-tryinitializebasenodetypetocustomdevice__basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icustomdevicepluginnodefactory-tryinitializebasenodetypetocustomdevice__basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attempts to initialize a BaseNodeType to match the custom device structure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool TryInitializeBaseNodeTypeToCustomDevice(BaseNodeType node)ParametersNameTypeDescriptionnodeBaseNodeTypeThe BaseNodeType to initialize.ReturnsTrue

### TryInitializeBaseNodeTypeToCustomDevice(BaseNodeType)

Attempts to initialize a BaseNodeType to match the custom device structure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool TryInitializeBaseNodeTypeToCustomDevice(BaseNodeType node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BaseNodeType | The BaseNodeType to initialize. |

#### Returns

True if this factory can handle the node type and successfully initialized it; otherwise, false.

Parent topic:

ICustomDevicePluginNodeFactory Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-icustomdevicepluginnodefactory.html language=enus -->
## TOPIC 02884: ICustomDevicePluginNodeFactory Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-icustomdevicepluginnodefactory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-icustomdevicepluginnodefactory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a factory interface for creating and initializing custom device plugin nodes. Derives fromIPluginNodeFactorySyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic interface ICustomDevicePluginNodeFactory : IPluginNodeFactoryMethodsNameDescriptionTryInitializeBaseNodeTypeToC

### ICustomDevicePluginNodeFactory Interface

Defines a factory interface for creating and initializing custom device plugin nodes.

#### Derives from

- IPluginNodeFactory

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public interface ICustomDevicePluginNodeFactory : IPluginNodeFactory

#### Methods

| Name | Description |
| --- | --- |
| TryInitializeBaseNodeTypeToCustomDevice(BaseNodeType) | Attempts to initialize a BaseNodeType to match the custom device structure. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-addvirtualecu__string.html language=enus -->
## TOPIC 02885: AddVirtualECU(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-addvirtualecu__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-addvirtualecu__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new virtual ECU to the virtual ECU list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void AddVirtualECU(string virtualECUName)ParametersNameTypeDescriptionvirtualECUNamestringThe name of the Virtual ECU to be added.

### AddVirtualECU(string)

Adds a new virtual ECU to the virtual ECU list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void AddVirtualECU(string virtualECUName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualECUName | string | The name of the Virtual ECU to be added. |

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-canconfiguration.html language=enus -->
## TOPIC 02886: CANConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-canconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-canconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the protocol specific configuration when Protocol is set to CAN. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ICANConfiguration CANConfiguration { get; }

### CANConfiguration

Represents the protocol specific configuration when [Protocol](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html) is set to CAN.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ICANConfiguration](nationalinstruments-veristand-systemdefinitionapi-icanconfiguration.html) CANConfiguration { get; }

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-clustername.html language=enus -->
## TOPIC 02887: ClusterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-clustername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-clustername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the ECU Network Cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ClusterName { get; set; }RemarksSet the name of the silver virtual bus as cluster name when using virtual ECUs built using Synopsys Silver®.

### ClusterName

Gets or sets the name of the ECU Network Cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ClusterName { get; set; }

#### Remarks

Set the name of the silver virtual bus as cluster name when using virtual ECUs built using Synopsys Silver®.

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-ethernetconfiguration.html language=enus -->
## TOPIC 02888: EthernetConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-ethernetconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-ethernetconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the protocol specific configuration when Protocol is set to Ethernet. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic IEthernetConfiguration EthernetConfiguration { get; }

### EthernetConfiguration

Represents the protocol specific configuration when [Protocol](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html) is set to Ethernet.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [IEthernetConfiguration](nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration.html) EthernetConfiguration { get; }

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-getvirtualecus.html language=enus -->
## TOPIC 02889: GetVirtualECUs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-getvirtualecus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-getvirtualecus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of virtual ECUs that have been added to the cluster as an array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string[] GetVirtualECUs()ReturnsAn array of virtual ECU names as strings.

### GetVirtualECUs()

Returns the names of virtual ECUs that have been added to the cluster as an array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string[] GetVirtualECUs()

#### Returns

An array of virtual ECU names as strings.

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-linconfiguration.html language=enus -->
## TOPIC 02890: LINConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-linconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-linconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the protocol specific configuration when Protocol is set to LIN. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ILINConfiguration LINConfiguration { get; }

### LINConfiguration

Represents the protocol specific configuration when [Protocol](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster-protocol.html) is set to LIN.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ILINConfiguration](nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration.html) LINConfiguration { get; }

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-protocol.html language=enus -->
## TOPIC 02891: Protocol

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-protocol.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-protocol.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CommunicationProtocol used by the ECU network cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CommunicationProtocol Protocol { get; set; }

### Protocol

Gets or sets the [CommunicationProtocol](nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html) used by the ECU network cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CommunicationProtocol](nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html) Protocol { get; set; }

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-removevirtualecu__string.html language=enus -->
## TOPIC 02892: RemoveVirtualECU(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-removevirtualecu__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-removevirtualecu__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a virtual ECU from the virtual ECU list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveVirtualECU(string virtualECUName)ParametersNameTypeDescriptionvirtualECUNamestringThe name of the Virtual ECU to be removed.

### RemoveVirtualECU(string)

Removes a virtual ECU from the virtual ECU list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveVirtualECU(string virtualECUName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualECUName | string | The name of the Virtual ECU to be removed. |

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-timestep.html language=enus -->
## TOPIC 02893: TimeStep

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-timestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-timestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double TimeStep { get; set; }RemarksWhen using virtual ECUs built using Synopsys Silver, set the SVB

### TimeStep

Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double TimeStep { get; set; }

#### Remarks

When using virtual ECUs built using Synopsys Silver, set the SVB Step Size to this property.

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-virtualecutoolchain.html language=enus -->
## TOPIC 02894: VirtualECUToolchain

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-virtualecutoolchain.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration-virtualecutoolchain.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the VirtualECUToolchain that was used to build virtual ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic VirtualECUToolchain VirtualECUToolchain { get; set; }

### VirtualECUToolchain

Gets or sets the name of the [VirtualECUToolchain](nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html) that was used to build virtual ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [VirtualECUToolchain](nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html) VirtualECUToolchain { get; set; }

Parent topic:

IECUNetworkClusterConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration.html language=enus -->
## TOPIC 02895: IECUNetworkClusterConfiguration Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iecunetworkclusterconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface for an ECU network cluster configuration. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic interface IECUNetworkClusterConfigurationPropertiesNameDescriptionCANConfigurationRepresents the protocol specific configuration when Protocol is set to CAN. C

### IECUNetworkClusterConfiguration Interface

Interface for an ECU network cluster configuration.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public interface IECUNetworkClusterConfiguration

#### Properties

| Name | Description |
| --- | --- |
| CANConfiguration | Represents the protocol specific configuration when Protocol is set to CAN. |
| ClusterName | Gets or sets the name of the ECU Network Cluster. |
| EthernetConfiguration | Represents the protocol specific configuration when Protocol is set to Ethernet. |
| LINConfiguration | Represents the protocol specific configuration when Protocol is set to LIN. |
| Protocol | Gets or sets the CommunicationProtocol used by the ECU network cluster. |
| TimeStep | Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs. |
| VirtualECUToolchain | Gets or sets the name of the VirtualECUToolchain that was used to build virtual ECUs. |

#### Methods

| Name | Description |
| --- | --- |
| AddVirtualECU(string) | Adds a new virtual ECU to the virtual ECU list. |
| GetVirtualECUs() | Returns the names of virtual ECUs that have been added to the cluster as an array. |
| RemoveVirtualECU(string) | Removes a virtual ECU from the virtual ECU list. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-addvirtualecumacaddress__string.html language=enus -->
## TOPIC 02896: AddVirtualECUMACAddress(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-addvirtualecumacaddress__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-addvirtualecumacaddress__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new virtual ECU MAC address to the virtual ECU MAC addresses list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void AddVirtualECUMACAddress(string virtualECUMACAddress)ParametersNameTypeDescriptionvirtualECUMACAddressstringThe MAC address of the virtual ECU to be

### AddVirtualECUMACAddress(string)

Adds a new virtual ECU MAC address to the virtual ECU MAC addresses list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void AddVirtualECUMACAddress(string virtualECUMACAddress)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualECUMACAddress | string | The MAC address of the virtual ECU to be added. |

Parent topic:

IEthernetConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-getvirtualecumacaddresses.html language=enus -->
## TOPIC 02897: GetVirtualECUMACAddresses()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-getvirtualecumacaddresses.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-getvirtualecumacaddresses.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the virtual ECU MAC addresses that have been added to the cluster as an array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string[] GetVirtualECUMACAddresses()ReturnsAn array of virtual ECU MAC addresses as strings.

### GetVirtualECUMACAddresses()

Returns the virtual ECU MAC addresses that have been added to the cluster as an array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string[] GetVirtualECUMACAddresses()

#### Returns

An array of virtual ECU MAC addresses as strings.

Parent topic:

IEthernetConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-removevirtualecumacaddress__string.html language=enus -->
## TOPIC 02898: RemoveVirtualECUMACAddress(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-removevirtualecumacaddress__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-removevirtualecumacaddress__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a virtual ECU MAC address from the virtual ECU MAC addresses list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveVirtualECUMACAddress(string virtualECUMACAddress)ParametersNameTypeDescriptionvirtualECUMACAddressstringThe MAC address of the virtual ECU to

### RemoveVirtualECUMACAddress(string)

Removes a virtual ECU MAC address from the virtual ECU MAC addresses list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveVirtualECUMACAddress(string virtualECUMACAddress)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualECUMACAddress | string | The MAC address of the virtual ECU to be removed. |

Parent topic:

IEthernetConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-xnetinterface.html language=enus -->
## TOPIC 02899: XNETInterface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-xnetinterface.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration-xnetinterface.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET Interface to be used to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string XNETInterface { get; set; }RemarksUse MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and in

### XNETInterface

Gets or sets the XNET Interface to be used to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string XNETInterface { get; set; }

#### Remarks

Use MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and interfaces.

Parent topic:

IEthernetConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration.html language=enus -->
## TOPIC 02900: IEthernetConfiguration Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-iethernetconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for Ethernet communication. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic interface IEthernetConfigurationPropertiesNameDescriptionXNETInterfaceGets or sets the XNET Interface to be used to connect to the real network. MethodsNa

### IEthernetConfiguration Interface

Represents the configuration for Ethernet communication.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public interface IEthernetConfiguration

#### Properties

| Name | Description |
| --- | --- |
| XNETInterface | Gets or sets the XNET Interface to be used to connect to the real network. |

#### Methods

| Name | Description |
| --- | --- |
| AddVirtualECUMACAddress(string) | Adds a new virtual ECU MAC address to the virtual ECU MAC addresses list. |
| GetVirtualECUMACAddresses() | Returns the virtual ECU MAC addresses that have been added to the cluster as an array. |
| RemoveVirtualECUMACAddress(string) | Removes a virtual ECU MAC address from the virtual ECU MAC addresses list. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-addvirtualtxframeid__int.html language=enus -->
## TOPIC 02901: AddVirtualTxFrameID(int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-addvirtualtxframeid__int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-addvirtualtxframeid__int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new virtual Tx frame ID to the virtual Tx frame IDs list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void AddVirtualTxFrameID(int virtualTxFrameID)ParametersNameTypeDescriptionvirtualTxFrameIDintThe ID of the virtual Tx frame to be added.

### AddVirtualTxFrameID(int)

Adds a new virtual Tx frame ID to the virtual Tx frame IDs list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void AddVirtualTxFrameID(int virtualTxFrameID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualTxFrameID | int | The ID of the virtual Tx frame to be added. |

Parent topic:

ILINConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-baudrate.html language=enus -->
## TOPIC 02902: BaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-baudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-baudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the LIN baud rate. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ulong BaudRate { get; set; }

### BaudRate

Gets or sets the LIN baud rate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong BaudRate { get; set; }

Parent topic:

ILINConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-getvirtualtxframeids.html language=enus -->
## TOPIC 02903: GetVirtualTxFrameIDs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-getvirtualtxframeids.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-getvirtualtxframeids.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the virtual Tx frame IDs that have been added to the cluster as an array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int[] GetVirtualTxFrameIDs()ReturnsAn integer array of virtual Tx frame IDs.

### GetVirtualTxFrameIDs()

Returns the virtual Tx frame IDs that have been added to the cluster as an array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int[] GetVirtualTxFrameIDs()

#### Returns

An integer array of virtual Tx frame IDs.

Parent topic:

ILINConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-removevirtualtxframeid__int.html language=enus -->
## TOPIC 02904: RemoveVirtualTxFrameID(int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-removevirtualtxframeid__int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-removevirtualtxframeid__int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a virtual Tx Frame ID from the virtual Tx frame IDs list. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveVirtualTxFrameID(int virtualTxFrameID)ParametersNameTypeDescriptionvirtualTxFrameIDintThe ID of the virtual Tx frame to be removed.

### RemoveVirtualTxFrameID(int)

Removes a virtual Tx Frame ID from the virtual Tx frame IDs list.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveVirtualTxFrameID(int virtualTxFrameID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| virtualTxFrameID | int | The ID of the virtual Tx frame to be removed. |

Parent topic:

ILINConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-xnetinterface.html language=enus -->
## TOPIC 02905: XNETInterface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-xnetinterface.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration-xnetinterface.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET Interface to be used to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string XNETInterface { get; set; }RemarksUse MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and in

### XNETInterface

Gets or sets the XNET Interface to be used to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string XNETInterface { get; set; }

#### Remarks

Use MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and interfaces.

Parent topic:

ILINConfiguration Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration.html language=enus -->
## TOPIC 02906: ILINConfiguration Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ilinconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for LIN communication. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic interface ILINConfigurationPropertiesNameDescriptionBaudRateGets or sets the LIN baud rate. XNETInterfaceGets or sets the XNET Interface to be used to connect

### ILINConfiguration Interface

Represents the configuration for LIN communication.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public interface ILINConfiguration

#### Properties

| Name | Description |
| --- | --- |
| BaudRate | Gets or sets the LIN baud rate. |
| XNETInterface | Gets or sets the XNET Interface to be used to connect to the real network. |

#### Methods

| Name | Description |
| --- | --- |
| AddVirtualTxFrameID(int) | Adds a new virtual Tx frame ID to the virtual Tx frame IDs list. |
| GetVirtualTxFrameIDs() | Returns the virtual Tx frame IDs that have been added to the cluster as an array. |
| RemoveVirtualTxFrameID(int) | Removes a virtual Tx Frame ID from the virtual Tx frame IDs list. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-incoming-getrawframedatalogging.html language=enus -->
## TOPIC 02907: GetRawFrameDataLogging()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-incoming-getrawframedatalogging.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-incoming-getrawframedatalogging.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the RawFrameDataLogging class, which you can use to add or access files that log data under an NI-XNET CAN, LIN, or FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RawFrameDataLogging GetRawFrameDataLogging()ReturnsA RawFrameDataLogging object.

### GetRawFrameDataLogging()

Accesses the [RawFrameDataLogging](nationalinstruments-veristand-systemdefinitionapi-rawframedatalogging.html) class, which you can use to add or access files that log data under an NI-XNET CAN, LIN, or FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [RawFrameDataLogging](nationalinstruments-veristand-systemdefinitionapi-rawframedatalogging.html) GetRawFrameDataLogging()

#### Returns

A [RawFrameDataLogging](nationalinstruments-veristand-systemdefinitionapi-rawframedatalogging.html) object.

Parent topic:

Incoming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-incoming-getsinglepoint.html language=enus -->
## TOPIC 02908: GetSinglePoint()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-incoming-getsinglepoint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-incoming-getsinglepoint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the SinglePoint class, which you can use to add or access incoming single-point frames under an NI-XNET CAN, LIN, or FlexRay port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SinglePoint GetSinglePoint()ReturnsA SinglePoint object.

### GetSinglePoint()

Accesses the [SinglePoint](nationalinstruments-veristand-systemdefinitionapi-singlepoint.html) class, which you can use to add or access incoming single-point frames under an NI-XNET CAN, LIN, or FlexRay port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SinglePoint](nationalinstruments-veristand-systemdefinitionapi-singlepoint.html) GetSinglePoint()

#### Returns

A [SinglePoint](nationalinstruments-veristand-systemdefinitionapi-singlepoint.html) object.

Parent topic:

Incoming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-incoming.html language=enus -->
## TOPIC 02909: Incoming Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-incoming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-incoming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represent the Incoming section under an NI-XNET CAN, LIN, or FlexRay ports, which contains any incoming frames and data logging files . Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Incoming : SectionRemarksUse the members of this class to access i

### Incoming Class

Represent the **Incoming** section under an NI-XNET CAN, LIN, or FlexRay ports, which contains any incoming frames and data logging files .

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Incoming : Section

#### Remarks

Use the members of this class to access incoming frames or raw frame data logging files.

**Accessing this Class**

- [GetIncoming](nationalinstruments-veristand-systemdefinitionapi-canport-getincoming.html)
- [GetIncoming](nationalinstruments-veristand-systemdefinitionapi-flexrayport-getincoming.html)
- [GetIncoming](nationalinstruments-veristand-systemdefinitionapi-linport-getincoming.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetRawFrameDataLogging() | Accesses the RawFrameDataLogging class, which you can use to add or access files that log data under an NI-XNET CAN, LIN, or FlexRay port. |
| GetSinglePoint() | Accesses the SinglePoint class, which you can use to add or access incoming single-point frames under an NI-XNET CAN, LIN, or FlexRay port. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inport-index.html language=enus -->
## TOPIC 02910: Index

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inport-index.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inport-index.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the index of the inport in the inport vector (array). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int Index { get; }ReturnsThe index of the inport.

### Index

Gets the index of the inport in the inport vector (array).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Index { get; }

#### Returns

The index of the inport.

Parent topic:

Inport Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inport-initialvalue.html language=enus -->
## TOPIC 02911: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inport-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inport-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the model inport. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double[,] InitialValue { get; set; }ReturnsThe initial value of the inport.

### InitialValue

Gets or sets the initial value of the model inport.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double[,] InitialValue { get; set; }

#### Returns

The initial value of the inport.

Parent topic:

Inport Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inport.html language=enus -->
## TOPIC 02912: Inport Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a model inport, or input. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Inport : ChannelRemarksUse the members of this class to get the index of the inport in the inport vector (array). Accessing this ClassGetInports()GetInports() Thread

### Inport Class

Represents a model inport, or input.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Inport : Channel

#### Remarks

Use the members of this class to get the index of the inport in the inport vector (array).

**Accessing this Class**

- [GetInports()](nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinports.html)
- [GetInports()](nationalinstruments-veristand-systemdefinitionapi-inports-getinports.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Index | Gets the index of the inport in the inport vector (array). |
| InitialValue | Gets or sets the initial value of the model inport. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinportgroups.html language=enus -->
## TOPIC 02913: GetInportGroups()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinportgroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinportgroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the InportGroup elements from the current InportGroup. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic InportGroup[] GetInportGroups()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications

### GetInportGroups()

Gets an array that contains the [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html) elements from the current [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html)[] GetInportGroups()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html) elements from the current [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html).

Parent topic:

InportGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinports.html language=enus -->
## TOPIC 02914: GetInports()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinports.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinports.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Inport elements from the current InportGroup. This method gets the inports that are categorized under the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Inport[] GetInports()RemarksModifications you make to the contents of this

### GetInports()

Gets an array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html). This method gets the inports that are categorized under the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html)[] GetInports()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html).

Parent topic:

InportGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinports__bool.html language=enus -->
## TOPIC 02915: GetInports(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinports__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinports__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Inport elements from the current InportGroup. This method gets the inports that are categorized under the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Inport[] GetInports(bool deep)RemarksModifications you make to the content

### GetInports(bool)

Gets an array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html). This method gets the inports that are categorized under the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html)[] GetInports(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child Inport element of the InportGroup section. |

#### Returns

An array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html).

Parent topic:

InportGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inportgroup.html language=enus -->
## TOPIC 02916: InportGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inportgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inportgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a sub-section of the Inports section of a model. Inport groups provide organization within the model. Derives fromModelDefaultGroupSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class InportGroup : ModelDefaultGroupRemarksUse the members of this class to get a li

### InportGroup Class

Represents a sub-section of the [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section of a model. Inport groups provide organization within the model.

#### Derives from

- ModelDefaultGroup

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class InportGroup : ModelDefaultGroup

#### Remarks

Use the members of this class to get a list of inports or inport groups under the current section.

**Accessing this Class**

- [GetInportGroups](nationalinstruments-veristand-systemdefinitionapi-inports-getinportgroups.html)
- [GetInportGroups](nationalinstruments-veristand-systemdefinitionapi-inportgroup-getinportgroups.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetInportGroups() | Gets an array that contains the InportGroup elements from the current InportGroup. |
| GetInports(bool) | Gets an array that contains the Inport elements from the current InportGroup. This method gets the inports that are categorized under the current group. |
| GetInports() | Gets an array that contains the Inport elements from the current InportGroup. This method gets the inports that are categorized under the current group. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inports-getinportgroups.html language=enus -->
## TOPIC 02917: GetInportGroups()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inports-getinportgroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inports-getinportgroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the InportGroup elements from the current Inports section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic InportGroup[] GetInportGroups()RemarksModifications you make to the contents of this list apply to the system definition. However, modificat

### GetInportGroups()

Gets an array that contains the [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html) elements from the current [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html)[] GetInportGroups()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html) elements from the current [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section.

Parent topic:

Inports Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inports-getinports.html language=enus -->
## TOPIC 02918: GetInports()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inports-getinports.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inports-getinports.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Inport elements from the current Inports section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Inport[] GetInports()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications you make t

### GetInports()

Gets an array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html)[] GetInports()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section.

Parent topic:

Inports Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inports-getinports__bool.html language=enus -->
## TOPIC 02919: GetInports(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inports-getinports__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inports-getinports__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Inport elements from the current Inports section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Inport[] GetInports(bool deep)RemarksModifications you make to the contents of this list apply to the system definition. However, modifications y

### GetInports(bool)

Gets an array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html)[] GetInports(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child Inport element of the Inports section. |

#### Returns

An array that contains the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) elements from the current [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section.

Parent topic:

Inports Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inports.html language=enus -->
## TOPIC 02920: Inports Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inports.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inports.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the top-level Inports section under a Model. This section contains all the Inport and InportGroup objects for the model. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Inports : SectionRemarksUse the members of this class to get a list of

### Inports Class

Represents the top-level **Inports** section under a [Model](nationalinstruments-veristand-systemdefinitionapi-model.html). This section contains all the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) and [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html) objects for the model.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Inports : Section

#### Remarks

Use the members of this class to get a list of inports or inport groups under the **Inports** section.

**Accessing this Class**

- [GetInportsSection](nationalinstruments-veristand-systemdefinitionapi-model-getinportssection.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetInportGroups() | Gets an array that contains the InportGroup elements from the current Inports section. |
| GetInports() | Gets an array that contains the Inport elements from the current Inports section. |
| GetInports(bool) | Gets an array that contains the Inport elements from the current Inports section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inputoverflowchannel-inputoverflowchannel__string.html language=enus -->
## TOPIC 02921: InputOverflowChannel(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inputoverflowchannel-inputoverflowchannel__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inputoverflowchannel-inputoverflowchannel__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the InputOverflowChannel class and creates an input overflow count channel with the specified Name . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic InputOverflowChannel(string Name)ParametersNameTypeDescriptionNamestringThe name of the channel.

### InputOverflowChannel(string)

Initializes a new instance of the [InputOverflowChannel](nationalinstruments-veristand-systemdefinitionapi-inputoverflowchannel.html) class and creates an input overflow count channel with the specified *Name* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public InputOverflowChannel(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |

Parent topic:

InputOverflowChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-inputoverflowchannel.html language=enus -->
## TOPIC 02922: InputOverflowChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-inputoverflowchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-inputoverflowchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an input overflow count channel, which tracks the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A single custom device can have only one input overflow count channel. Derives fromCustomDeviceChannelSyntaxNamespace: NationalInstru

### InputOverflowChannel Class

Represents an input overflow count channel, which tracks the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A single custom device can have only one input overflow count channel.

#### Derives from

- CustomDeviceChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class InputOverflowChannel : CustomDeviceChannel

#### Remarks

Use the members of this class to create and configure an input overflow count channel.

**Accessing this Class**

- InputOverflowChannel Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| InputOverflowChannel(string) | Initializes a new instance of the InputOverflowChannel class and creates an input overflow count channel with the specified Name . |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ipluginnodefactory-trycreatebasenodefromsystemstoragenode__basenodetype-out.html language=enus -->
## TOPIC 02923: TryCreateBaseNodeFromSystemStorageNode(BaseNodeType, out BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ipluginnodefactory-trycreatebasenodefromsystemstoragenode__basenodetype-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ipluginnodefactory-trycreatebasenodefromsystemstoragenode__basenodetype-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attempts to create a BaseNode from a system storage node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool TryCreateBaseNodeFromSystemStorageNode(BaseNodeType storageNode, out BaseNode baseNode)ParametersNameTypeDescriptionstorageNodeBaseNodeTypeThe storage node containi

### TryCreateBaseNodeFromSystemStorageNode(BaseNodeType, out BaseNode)

Attempts to create a BaseNode from a system storage node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool TryCreateBaseNodeFromSystemStorageNode(BaseNodeType storageNode, out BaseNode baseNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| storageNode | BaseNodeType | The storage node containing the serialized node data. |
| baseNode | out BaseNode | When this method returns, contains the created BaseNode if successful; otherwise, null. |

#### Returns

True if the node was successfully created; otherwise, false.

Parent topic:

IPluginNodeFactory Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-ipluginnodefactory.html language=enus -->
## TOPIC 02924: IPluginNodeFactory Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-ipluginnodefactory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-ipluginnodefactory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a factory interface for creating plugin nodes from system storage data. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic interface IPluginNodeFactoryMethodsNameDescriptionTryCreateBaseNodeFromSystemStorageNode(BaseNodeType, out BaseNode)Attempts to cre

### IPluginNodeFactory Interface

Defines a factory interface for creating plugin nodes from system storage data.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public interface IPluginNodeFactory

#### Methods

| Name | Description |
| --- | --- |
| TryCreateBaseNodeFromSystemStorageNode(BaseNodeType, out BaseNode) | Attempts to create a BaseNode from a system storage node. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lin-addlinport__linport-out.html language=enus -->
## TOPIC 02925: AddLINPort(LINPort, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lin-addlinport__linport-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lin-addlinport__linport-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified LIN port to the LIN section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddLINPort(LINPort linPort, out Error error)ParametersNameTypeDescriptionlinPortLINPortThe LIN port to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object

### AddLINPort(LINPort, out Error)

Adds the specified LIN port to the **LIN** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddLINPort(LINPort linPort, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| linPort | LINPort | The LIN port to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the LIN port was added successfully.

Parent topic:

LIN Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lin-addlinport__linport.html language=enus -->
## TOPIC 02926: AddLINPort(LINPort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lin-addlinport__linport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lin-addlinport__linport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified LIN port to the LIN section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddLINPort(LINPort linPort)ParametersNameTypeDescriptionlinPortLINPortThe LIN port to add.Returnstrue if the LIN port was added successfully.

### AddLINPort(LINPort)

Adds the specified LIN port to the **LIN** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddLINPort(LINPort linPort)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| linPort | LINPort | The LIN port to add. |

#### Returns

true if the LIN port was added successfully.

Parent topic:

LIN Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lin-getlinportlist.html language=enus -->
## TOPIC 02927: GetLINPortList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lin-getlinportlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lin-getlinportlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the LINPort elements from the current LIN section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LINPort[] GetLINPortList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications you make

### GetLINPortList()

Gets an array that contains the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) elements from the current [LIN](nationalinstruments-veristand-systemdefinitionapi-lin.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html)[] GetLINPortList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) elements from the current [LIN](nationalinstruments-veristand-systemdefinitionapi-lin.html) section.

Parent topic:

LIN Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lin.html language=enus -->
## TOPIC 02928: LIN Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lin.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lin.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the LIN section under XNET in the system definition. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class LIN : SectionRemarksUse the members of this class to configure the section, add a LIN port, or get a list of LIN ports. Accessing this Cla

### LIN Class

Represents the **LIN** section under [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) in the system definition.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class LIN : Section

#### Remarks

Use the members of this class to configure the section, add a LIN port, or get a list of LIN ports.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET.GetLIN

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddLINPort(LINPort, out Error) | Adds the specified LIN port to the LIN section. |
| AddLINPort(LINPort) | Adds the specified LIN port to the LIN section. |
| GetLINPortList() | Gets an array that contains the LINPort elements from the current LIN section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createcommunicationstatechannel__out.html language=enus -->
## TOPIC 02929: CreateCommunicationStateChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createcommunicationstatechannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createcommunicationstatechannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Communication State status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateCommunicationStateChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand

### CreateCommunicationStateChannel(out Error)

Creates the Communication State status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateCommunicationStateChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createfaultchannel__out.html language=enus -->
## TOPIC 02930: CreateFaultChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createfaultchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createfaultchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Fault status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateFaultChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error

### CreateFaultChannel(out Error)

Creates the Fault status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateFaultChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createfaultcodechannel__out.html language=enus -->
## TOPIC 02931: CreateFaultCodeChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createfaultcodechannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createfaultcodechannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Fault Code status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateFaultCodeChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If

### CreateFaultCodeChannel(out Error)

Creates the Fault Code status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateFaultCodeChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorchannel__out.html language=enus -->
## TOPIC 02932: CreateLastErrorChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Last Error status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateLastErrorChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If

### CreateLastErrorChannel(out Error)

Creates the Last Error status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateLastErrorChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorexpectedchannel__out.html language=enus -->
## TOPIC 02933: CreateLastErrorExpectedChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorexpectedchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorexpectedchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Last Error Expected status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateLastErrorExpectedChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.

### CreateLastErrorExpectedChannel(out Error)

Creates the Last Error Expected status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateLastErrorExpectedChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterroridentifierchannel__out.html language=enus -->
## TOPIC 02934: CreateLastErrorIdentifierChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterroridentifierchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterroridentifierchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Last Error Identifier status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateLastErrorIdentifierChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriSt

### CreateLastErrorIdentifierChannel(out Error)

Creates the Last Error Identifier status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateLastErrorIdentifierChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorreceivedchannel__out.html language=enus -->
## TOPIC 02935: CreateLastErrorReceivedChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorreceivedchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrorreceivedchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Last Error Received status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateLastErrorReceivedChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.

### CreateLastErrorReceivedChannel(out Error)

Creates the Last Error Received status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateLastErrorReceivedChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrortimestampchannel__out.html language=enus -->
## TOPIC 02936: CreateLastErrorTimestampChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrortimestampchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createlasterrortimestampchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Last Error Timestamp status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateLastErrorTimestampChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStan

### CreateLastErrorTimestampChannel(out Error)

Creates the Last Error Timestamp status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateLastErrorTimestampChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createsleepchannel__out.html language=enus -->
## TOPIC 02937: CreateSleepChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createsleepchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createsleepchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Sleep status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateSleepChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error

### CreateSleepChannel(out Error)

Creates the Sleep status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateSleepChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createtransceiverstatechannel__out.html language=enus -->
## TOPIC 02938: CreateTransceiverStateChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createtransceiverstatechannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-createtransceiverstatechannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Transceiver State status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateTransceiverStateChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Err

### CreateTransceiverStateChannel(out Error)

Creates the Transceiver State status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateTransceiverStateChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getcommunicationstatechannel.html language=enus -->
## TOPIC 02939: GetCommunicationStateChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getcommunicationstatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getcommunicationstatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Communication State status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetCommunicationStateChannel()

### GetCommunicationStateChannel()

Gets the Communication State status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetCommunicationStateChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getfaultchannel.html language=enus -->
## TOPIC 02940: GetFaultChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getfaultchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getfaultchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Fault status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetFaultChannel()

### GetFaultChannel()

Gets the Fault status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetFaultChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getfaultcodechannel.html language=enus -->
## TOPIC 02941: GetFaultCodeChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getfaultcodechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getfaultcodechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Fault Code status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetFaultCodeChannel()

### GetFaultCodeChannel()

Gets the Fault Code status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetFaultCodeChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorchannel.html language=enus -->
## TOPIC 02942: GetLastErrorChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Last Error status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetLastErrorChannel()

### GetLastErrorChannel()

Gets the Last Error status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetLastErrorChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorexpectedchannel.html language=enus -->
## TOPIC 02943: GetLastErrorExpectedChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorexpectedchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorexpectedchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Last Error Expected status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetLastErrorExpectedChannel()

### GetLastErrorExpectedChannel()

Gets the Last Error Expected status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetLastErrorExpectedChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterroridentifierchannel.html language=enus -->
## TOPIC 02944: GetLastErrorIdentifierChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterroridentifierchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterroridentifierchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Last Error Identifier status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetLastErrorIdentifierChannel()

### GetLastErrorIdentifierChannel()

Gets the Last Error Identifier status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetLastErrorIdentifierChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorreceivedchannel.html language=enus -->
## TOPIC 02945: GetLastErrorReceivedChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorreceivedchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrorreceivedchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Last Error Received status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetLastErrorReceivedChannel()

### GetLastErrorReceivedChannel()

Gets the Last Error Received status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetLastErrorReceivedChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrortimestampchannel.html language=enus -->
## TOPIC 02946: GetLastErrorTimestampChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrortimestampchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getlasterrortimestampchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Last Error Timestamp status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetLastErrorTimestampChannel()

### GetLastErrorTimestampChannel()

Gets the Last Error Timestamp status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetLastErrorTimestampChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getsleepchannel.html language=enus -->
## TOPIC 02947: GetSleepChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getsleepchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-getsleepchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Sleep status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetSleepChannel()

### GetSleepChannel()

Gets the Sleep status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetSleepChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-gettransceiverreadychannel.html language=enus -->
## TOPIC 02948: GetTransceiverReadyChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-gettransceiverreadychannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels-gettransceiverreadychannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Transceiver Ready status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetTransceiverReadyChannel()

### GetTransceiverReadyChannel()

Gets the Transceiver Ready status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetTransceiverReadyChannel()

Parent topic:

LINInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels.html language=enus -->
## TOPIC 02949: LINInterfaceChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Interface section under an NI-XNET LIN port. This section contains the port-specific channels which provide status information. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class LINInterfaceChannels : SectionMethodsNameDescriptionCreateC

### LINInterfaceChannels Class

Represents the **Interface** section under an NI-XNET LIN port. This section contains the port-specific channels which provide status information.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class LINInterfaceChannels : Section

#### Methods

| Name | Description |
| --- | --- |
| CreateCommunicationStateChannel(out Error) | Creates the Communication State status channel for the interface, if it does not exist. |
| CreateFaultChannel(out Error) | Creates the Fault status channel for the interface, if it does not exist. |
| CreateFaultCodeChannel(out Error) | Creates the Fault Code status channel for the interface, if it does not exist. |
| CreateLastErrorChannel(out Error) | Creates the Last Error status channel for the interface, if it does not exist. |
| CreateLastErrorExpectedChannel(out Error) | Creates the Last Error Expected status channel for the interface, if it does not exist. |
| CreateLastErrorIdentifierChannel(out Error) | Creates the Last Error Identifier status channel for the interface, if it does not exist. |
| CreateLastErrorReceivedChannel(out Error) | Creates the Last Error Received status channel for the interface, if it does not exist. |
| CreateLastErrorTimestampChannel(out Error) | Creates the Last Error Timestamp status channel for the interface, if it does not exist. |
| CreateSleepChannel(out Error) | Creates the Sleep status channel for the interface, if it does not exist. |
| CreateTransceiverStateChannel(out Error) | Creates the Transceiver State status channel for the interface, if it does not exist. |
| GetCommunicationStateChannel() | Gets the Communication State status channel for the interface. |
| GetFaultChannel() | Gets the Fault status channel for the interface. |
| GetFaultCodeChannel() | Gets the Fault Code status channel for the interface. |
| GetLastErrorChannel() | Gets the Last Error status channel for the interface. |
| GetLastErrorExpectedChannel() | Gets the Last Error Expected status channel for the interface. |
| GetLastErrorIdentifierChannel() | Gets the Last Error Identifier status channel for the interface. |
| GetLastErrorReceivedChannel() | Gets the Last Error Received status channel for the interface. |
| GetLastErrorTimestampChannel() | Gets the Last Error Timestamp status channel for the interface. |
| GetSleepChannel() | Gets the Sleep status channel for the interface. |
| GetTransceiverReadyChannel() | Gets the Transceiver Ready status channel for the interface. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-afpbinaryfile.html language=enus -->
## TOPIC 02950: AFPBinaryFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-afpbinaryfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-afpbinaryfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the binary (.ini) file used for automatic frame processing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile AFPBinaryFile { get; set; }RemarksYou can use the BinaryFilePath parameter of SetAutomaticFrameProcessing to set this file. ReturnsA DependentFile r

### AFPBinaryFile

Gets the binary (.ini) file used for automatic frame processing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) AFPBinaryFile { get; set; }

#### Remarks

You can use the *BinaryFilePath* parameter of [SetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-linport-setautomaticframeprocessing__string-string-uint_arr1.html) to set this file.

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the .ini file.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-afpglobaldata.html language=enus -->
## TOPIC 02951: AFPGlobalData

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-afpglobaldata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-afpglobaldata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the global data used for automatic frame processing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint[] AFPGlobalData { get; set; }ReturnsThe array specified by the GlobalData parameter of SetAutomaticFrameProcessing.

### AFPGlobalData

Gets the global data used for automatic frame processing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint[] AFPGlobalData { get; set; }

#### Returns

The array specified by the *GlobalData* parameter of [SetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-linport-setautomaticframeprocessing__string-string-uint_arr1.html).

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-afpinifile.html language=enus -->
## TOPIC 02952: AFPINIFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-afpinifile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-afpinifile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the AFPBinaryFile used for automatic frame processing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string AFPINIFile { get; set; }ReturnsThe filename specified by the IniFileName parameter of SetAutomaticFrameProcessing.

### AFPINIFile

Gets the name of the [AFPBinaryFile](nationalinstruments-veristand-systemdefinitionapi-linport-afpbinaryfile.html) used for automatic frame processing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string AFPINIFile { get; set; }

#### Returns

The filename specified by the *IniFileName* parameter of [SetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-linport-setautomaticframeprocessing__string-string-uint_arr1.html).

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-baudrate.html language=enus -->
## TOPIC 02953: BaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-baudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-baudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the baud rate that all cluster nodes use. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint BaudRate { get; set; }ReturnsThe initial value is the value specified in the LinkedDatabase or the value specified by the M:NationalInstruments.VeriStand.SystemDefinit

### BaudRate

Gets or sets the baud rate that all cluster nodes use.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint BaudRate { get; set; }

#### Returns

The initial value is the value specified in the [LinkedDatabase](nationalinstruments-veristand-systemdefinitionapi-linport-linkeddatabase.html) or the value specified by the M:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort constructor. The rate can be any value between 2400 and 20000, inclusive.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-clustername.html language=enus -->
## TOPIC 02954: ClusterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-clustername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-clustername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the cluster in LinkedDatabase that is associated with the LINPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ClusterName { get; set; }ReturnsThe initial value is the ClusterName specified by the LINPort constructor.

### ClusterName

Gets or sets the name of the cluster in [LinkedDatabase](nationalinstruments-veristand-systemdefinitionapi-linport-linkeddatabase.html) that is associated with the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ClusterName { get; set; }

#### Returns

The initial value is the *ClusterName* specified by the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) constructor.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-createinterfacesection__out.html language=enus -->
## TOPIC 02955: CreateInterfaceSection(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-createinterfacesection__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-createinterfacesection__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the LINInterfaceChannels section of the current LINPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LINInterfaceChannels CreateInterfaceSection(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If n

### CreateInterfaceSection(out Error)

Creates the [LINInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels.html) section of the current [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [LINInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels.html) CreateInterfaceSection(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-disabled.html language=enus -->
## TOPIC 02956: Disabled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-disabled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-disabled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the port is disabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Disabled { get; set; }

### Disabled

Gets or sets whether the port is disabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Disabled { get; set; }

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-echo.html language=enus -->
## TOPIC 02957: Echo

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-echo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-echo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Echo { get; set

### Echo

Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Echo { get; set; }

#### Returns

A Boolean that indicates whether outgoing frames are echoed back as incoming frames.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-getincoming.html language=enus -->
## TOPIC 02958: GetIncoming()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-getincoming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-getincoming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the Incoming section of the port, which includes incoming single-point frames and raw frame data logging files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Incoming GetIncoming()ReturnsA reference to the Incoming class.

### GetIncoming()

Accesses the [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) section of the port, which includes incoming single-point frames and raw frame data logging files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) GetIncoming()

#### Returns

A reference to the [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) class.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-getinterfacesection.html language=enus -->
## TOPIC 02959: GetInterfaceSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-getinterfacesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-getinterfacesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the LINInterfaceChannels section of the current LINPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LINInterfaceChannels GetInterfaceSection()

### GetInterfaceSection()

Gets the [LINInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels.html) section of the current [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [LINInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-lininterfacechannels.html) GetInterfaceSection()

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-getlinscheduler.html language=enus -->
## TOPIC 02960: GetLINScheduler()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-getlinscheduler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-getlinscheduler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the LINScheduler section of the port, which specifies the active schedule to use to specify when to transmit frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LINScheduler GetLINScheduler()RemarksA LIN schedule is valid only if the port is configured as the ma

### GetLINScheduler()

Accesses the [LINScheduler](nationalinstruments-veristand-systemdefinitionapi-linscheduler.html) section of the port, which specifies the active schedule to use to specify when to transmit frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [LINScheduler](nationalinstruments-veristand-systemdefinitionapi-linscheduler.html) GetLINScheduler()

#### Remarks

Note

A LIN schedule is valid only if the port is configured as the master port ([IsMaster](nationalinstruments-veristand-systemdefinitionapi-linport-ismaster.html) is true).

#### Returns

A reference to the [LINScheduler](nationalinstruments-veristand-systemdefinitionapi-linscheduler.html) class.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-getoutgoing.html language=enus -->
## TOPIC 02961: GetOutgoing()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-getoutgoing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-getoutgoing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the Outgoing section of the port, which includes outgoing sporadic and unconditional frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Outgoing GetOutgoing()ReturnsA reference to the Outgoing class.

### GetOutgoing()

Accesses the [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) section of the port, which includes outgoing sporadic and unconditional frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) GetOutgoing()

#### Returns

A reference to the [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) class.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-incomingrate.html language=enus -->
## TOPIC 02962: IncomingRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-incomingrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-incomingrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processing rate for outgoing frames in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint IncomingRate { get; set; }RemarksIf InlineIncoming is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the incoming frame sess

### IncomingRate

Gets or sets the processing rate for outgoing frames in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint IncomingRate { get; set; }

#### Remarks

If [InlineIncoming](nationalinstruments-veristand-systemdefinitionapi-linport-inlineincoming.html) is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the incoming frame session loop. For example, if the PCL execution rate is 1000 Hz, setting this rate to 100 Hz calls the frame session loop on every 10th iteration of the PCL.

#### Returns

An integer representing the processing rate in hertz.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-inlineincoming.html language=enus -->
## TOPIC 02963: InlineIncoming

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-inlineincoming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-inlineincoming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### InlineIncoming

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InlineIncoming { get; set; }

#### Remarks

By default, NI VeriStand runs incoming and outgoing frame sessions as asynchronous custom devices that execute in separate loops from the PCL. Therefore, there is a 1-cycle delay when reading and writing channel values between the frame session loops and the rest of the system. You can inline frames to eliminate this delay by running the session loops as inline hardware interface custom devices, where NI VeriStand uses the loop rate to calculate the decimation factor for calls to the session loop.

Inlining frames is useful if you need to reduce latency when getting XNET data from your system, or if you want to correlate frame data with channel data. However, it can increase CPU usage and, if the XNET loops take too long to execute, delay the execution of the Primary Control Loop.

#### Returns

A Boolean that indicates whether incoming frames are processed inline with the PCL (true) or asynchronously (false).

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-inlineoutgoing.html language=enus -->
## TOPIC 02964: InlineOutgoing

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-inlineoutgoing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-inlineoutgoing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### InlineOutgoing

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InlineOutgoing { get; set; }

#### Remarks

By default, NI VeriStand runs incoming and outgoing frame sessions as asynchronous custom devices that execute in separate loops from the PCL. Therefore, there is a 1-cycle delay when reading and writing channel values between the frame session loops and the rest of the system. You can inline frames to eliminate this delay by running the session loops as inline hardware interface custom devices, where NI VeriStand uses the loop rate to calculate the decimation factor for calls to the session loop.

Inlining frames is useful if you need to reduce latency when getting XNET data from your system, or if you want to correlate frame data with channel data. However, it can increase CPU usage and, if the XNET loops take too long to execute, delay the execution of the Primary Control Loop.

#### Returns

A Boolean that indicates whether outgoing frames are processed inline with the PCL (true) or asynchronously (false).

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-inputstreamqueuesize.html language=enus -->
## TOPIC 02965: InputStreamQueueSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-inputstreamqueuesize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-inputstreamqueuesize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint InputStreamQueueSize { get; s

### InputStreamQueueSize

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint InputStreamQueueSize { get; set; }

#### Returns

An integer representing the queue size.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-inputstreamreadtime.html language=enus -->
## TOPIC 02966: InputStreamReadTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-inputstreamreadtime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-inputstreamreadtime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InputStrea

### InputStreamReadTime

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InputStreamReadTime { get; set; }

#### Returns

A double representing the read time in seconds.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-ismaster.html language=enus -->
## TOPIC 02967: IsMaster

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-ismaster.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-ismaster.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### IsMaster

Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsMaster { get; set; }

#### Returns

true if the port is the master.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-linkeddatabase.html language=enus -->
## TOPIC 02968: LinkedDatabase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-linkeddatabase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-linkeddatabase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET database associated with the LINPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode LinkedDatabase { get; set; }ReturnsThe initial value is the LinkedDatabase specified by the LINPort constructor.

### LinkedDatabase

Gets or sets the XNET database associated with the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) LinkedDatabase { get; set; }

#### Returns

The initial value is the *LinkedDatabase* specified by the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) constructor.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-linport__string-ushort-database-string-uint-string.html language=enus -->
## TOPIC 02969: LINPort(string, ushort, Database, string, uint, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-linport__string-ushort-database-string-uint-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-linport__string-ushort-database-string-uint-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LINPort class and creates a port with the specified Name , PortNumber , and so on. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LINPort(string Name, ushort PortNumber, Database LinkedDatabase, string ClusterName, uint BaudRate, string LIN

### LINPort(string, ushort, Database, string, uint, string)

Initializes a new instance of the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) class and creates a port with the specified *Name* , *PortNumber* , and so on.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public LINPort(string Name, ushort PortNumber, Database LinkedDatabase, string ClusterName, uint BaudRate, string LINSchedules)

#### Remarks

Note

A LIN schedule is valid only if the port is configured as the master port ([IsMaster](nationalinstruments-veristand-systemdefinitionapi-linport-ismaster.html) is true).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the port. |
| PortNumber | ushort | The physical address of the port. |
| LinkedDatabase | Database | The XNET database associated with the port. |
| ClusterName | string | The cluster in LinkedDatabase that is associated with the port. |
| BaudRate | uint | The baud rate all cluster nodes under the port use. The rate can be any value between 2400 and 20000, inclusive. |
| LINSchedules | string | The names of all the available LIN schedules. |

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-linschedules.html language=enus -->
## TOPIC 02970: LINSchedules

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-linschedules.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-linschedules.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the names of all the available LIN schedules. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string LINSchedules { get; set; }ReturnsThe initial value is the schedule names specified by the LinkedDatabase or the LINPort constructor.

### LINSchedules

Gets or sets the names of all the available LIN schedules.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string LINSchedules { get; set; }

#### Returns

The initial value is the schedule names specified by the [LinkedDatabase](nationalinstruments-veristand-systemdefinitionapi-linport-linkeddatabase.html) or the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) constructor.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-outgoingrate.html language=enus -->
## TOPIC 02971: OutgoingRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-outgoingrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-outgoingrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processing rate for outgoing frames in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint OutgoingRate { get; set; }RemarksIf InlineOutgoing is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the outgoing frame sess

### OutgoingRate

Gets or sets the processing rate for outgoing frames in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint OutgoingRate { get; set; }

#### Remarks

If [InlineOutgoing](nationalinstruments-veristand-systemdefinitionapi-linport-inlineoutgoing.html) is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the outgoing frame session loop. For example, if the PCL execution rate is 1000 Hz, setting this rate to 100 Hz calls the frame session loop on every 10th iteration of the PCL.

#### Returns

An integer representing the processing rate in hertz.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-portnumber.html language=enus -->
## TOPIC 02972: PortNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-portnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-portnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the physical address of the LIN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ushort PortNumber { get; set; }ReturnsThe initial value is the PortNumber specified by the LINPort constructor.

### PortNumber

Gets or sets the physical address of the LIN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ushort PortNumber { get; set; }

#### Returns

The initial value is the *PortNumber* specified by the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) constructor.

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-removeautomaticframeprocessing.html language=enus -->
## TOPIC 02973: RemoveAutomaticFrameProcessing()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-removeautomaticframeprocessing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-removeautomaticframeprocessing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes automatic frame processing from the LINPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveAutomaticFrameProcessing()

### RemoveAutomaticFrameProcessing()

Removes automatic frame processing from the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveAutomaticFrameProcessing()

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-setautomaticframeprocessing__string-string-uint_arr1.html language=enus -->
## TOPIC 02974: SetAutomaticFrameProcessing(string, string, uint[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-setautomaticframeprocessing__string-string-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-setautomaticframeprocessing__string-string-uint_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets automatic frame processing on the LINPort. You must set automatic frame processing on the port if you want to configure CRCs and counters on outgoing frames under the port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetAutomaticFrameProcessing(string iniFileNa

### SetAutomaticFrameProcessing(string, string, uint[])

Sets automatic frame processing on the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html). You must set automatic frame processing on the port if you want to configure CRCs and counters on outgoing frames under the port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetAutomaticFrameProcessing(string iniFileName, string binaryFilePath, uint[] globalData)

#### Remarks

NI VeriStand supports CRC-8 and CRC-16 length polynomials.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| iniFileName | string | The name of the binary file to use for automatic frame processing. |
| binaryFilePath | string | The path to the binary file to use for automatic frame processing. The CRC files installed with NI VeriStand are available in the < Application Data > \\National Instruments\\VeriStand\\System Explorer\\XNET\\AFP directory. |
| globalData | uint[] | An array that contains the following data:GlobalData[0] = Polynomial, or the generator polynomial for the CRC. This decimal value is converted to binary form to create the polynomial. For example, if you enter the decimal value 23, the value becomes 10111 in binary form, which translates to the following polynomial: 1x^4 + 0x^3 + 1x^2 + 1x + 1 GlobalData[1] = Initial CRC, or the initial value to use for the CRC calculation. This decimal value is converted to binary form. The value can be up to 8 bits long for CRC-8 and up to 16 bits long for CRC-16. GlobalData[2] = Final XOR, or the value to XOR with the calculated CRC. This decimal value is converted to binary form. The value can be up to 8 bits long for CRC-8 and up to 16 bits long for CRC-16. GlobalData[3] = Reflected, if a non-zero number, specifies to reverse the order of the bits in the CRC before writing the data in to the data stream. |

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport-termination.html language=enus -->
## TOPIC 02975: Termination

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport-termination.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport-termination.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the onboard XNETTermination. You can select Off (disabled) and On (enabled). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic XNETTermination Termination { get; set; }RemarksPer the LIN 2.1 standard, the master ECU has a ~1 k Ω termination resistor between Vbat a

### Termination

Gets or sets the onboard [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html). You can select [Off](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) (disabled) and [On](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) (enabled).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) Termination { get; set; }

#### Remarks

Per the LIN 2.1 standard, the master ECU has a ~1 k Ω termination resistor between Vbat and Vbus. Therefore, select [On](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) only if you are using your interface as the master and do not already have external termination.

#### Returns

An enumeration value of [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html).

Parent topic:

LINPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linport.html language=enus -->
## TOPIC 02976: LINPort Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a port under an NI-XNET LIN device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class LINPort : SectionRemarksUse the members of this class to configure port settings, such as the port name, physical address, processing rate for incoming and

### LINPort Class

Represents a port under an NI-XNET [LIN](nationalinstruments-veristand-systemdefinitionapi-lin.html) device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class LINPort : Section

#### Remarks

Use the members of this class to configure port settings, such as the port name, physical address, processing rate for incoming and outgoing frames, and so on.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.LIN.GetLINPortList
- LINPort Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| LINPort(string, ushort, Database, string, uint, string) | Initializes a new instance of the LINPort class and creates a port with the specified Name , PortNumber , and so on. |

#### Properties

| Name | Description |
| --- | --- |
| AFPBinaryFile | Gets the binary (.ini) file used for automatic frame processing. |
| AFPGlobalData | Gets the global data used for automatic frame processing. |
| AFPINIFile | Gets the name of the AFPBinaryFile used for automatic frame processing. |
| BaudRate | Gets or sets the baud rate that all cluster nodes use. |
| ClusterName | Gets or sets the name of the cluster in LinkedDatabase that is associated with the LINPort. |
| Disabled | Gets or sets whether the port is disabled. |
| Echo | Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session. |
| IncomingRate | Gets or sets the processing rate for outgoing frames in hertz. |
| InlineIncoming | Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. |
| InlineOutgoing | Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. |
| InputStreamQueueSize | Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored. |
| InputStreamReadTime | Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read. |
| IsMaster | Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs. |
| LinkedDatabase | Gets or sets the XNET database associated with the LINPort. |
| LINSchedules | Gets or sets the names of all the available LIN schedules. |
| OutgoingRate | Gets or sets the processing rate for outgoing frames in hertz. |
| PortNumber | Gets or sets the physical address of the LIN port. |
| Termination | Gets or sets the onboard XNETTermination. You can select Off (disabled) and On (enabled). |

#### Methods

| Name | Description |
| --- | --- |
| CreateInterfaceSection(out Error) | Creates the LINInterfaceChannels section of the current LINPort. |
| GetIncoming() | Accesses the Incoming section of the port, which includes incoming single-point frames and raw frame data logging files. |
| GetInterfaceSection() | Gets the LINInterfaceChannels section of the current LINPort. |
| GetLINScheduler() | Accesses the LINScheduler section of the port, which specifies the active schedule to use to specify when to transmit frames. |
| GetOutgoing() | Accesses the Outgoing section of the port, which includes outgoing sporadic and unconditional frames. |
| RemoveAutomaticFrameProcessing() | Removes automatic frame processing from the LINPort. |
| SetAutomaticFrameProcessing(string, string, uint[]) | Sets automatic frame processing on the LINPort. You must set automatic frame processing on the port if you want to configure CRCs and counters on outgoing frames under the port. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linscheduler-activeschedule.html language=enus -->
## TOPIC 02977: ActiveSchedule

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linscheduler-activeschedule.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linscheduler-activeschedule.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the active LIN schedule. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ActiveSchedule { get; set; }ReturnsThe name of the active LIN schedule.

### ActiveSchedule

Gets or sets the name of the active LIN schedule.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ActiveSchedule { get; set; }

#### Returns

The name of the active LIN schedule.

Parent topic:

LINScheduler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linscheduler-setactiveschedule__string_arr1-string.html language=enus -->
## TOPIC 02978: SetActiveSchedule(string[], string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linscheduler-setactiveschedule__string_arr1-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linscheduler-setactiveschedule__string_arr1-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the active schedule for the current LINPort by searching the LINSchedules array for the name specified by ActiveSchedule . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetActiveSchedule(string[] LINSchedules, string ActiveSchedule)ParametersNameTypeDescriptionLI

### SetActiveSchedule(string[], string)

Sets the active schedule for the current [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) by searching the *LINSchedules*  array for the name specified by *ActiveSchedule* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetActiveSchedule(string[] LINSchedules, string ActiveSchedule)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| LINSchedules | string[] | The array of all available LIN schedules. |
| ActiveSchedule | string | The name of the schedule to set as the active schedule. |

#### Returns

true if the active schedule was set successfully.

Parent topic:

LINScheduler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linscheduler-setactiveschedule__string_arr1-uint.html language=enus -->
## TOPIC 02979: SetActiveSchedule(string[], uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linscheduler-setactiveschedule__string_arr1-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linscheduler-setactiveschedule__string_arr1-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the active schedule for the current LINPort by searching the LINSchedules array for the schedule at the specified ActiveScheduleIndex . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetActiveSchedule(string[] LINSchedules, uint ActiveScheduleIndex)ParametersNameT

### SetActiveSchedule(string[], uint)

Sets the active schedule for the current [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) by searching the *LINSchedules*  array for the schedule at the specified *ActiveScheduleIndex* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetActiveSchedule(string[] LINSchedules, uint ActiveScheduleIndex)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| LINSchedules | string[] | The array of all available LIN schedules. |
| ActiveScheduleIndex | uint | The array index of the schedule to set as the active schedule. |

#### Returns

true if the active schedule was set successfully.

Parent topic:

LINScheduler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linscheduler-units.html language=enus -->
## TOPIC 02980: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linscheduler-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linscheduler-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units associated with the LIN Scheduler channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override string Units { get; }ReturnsThe units associated with the channel.

### Units

Gets the units associated with the LIN Scheduler channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override string Units { get; }

#### Returns

The units associated with the channel.

Parent topic:

LINScheduler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-linscheduler.html language=enus -->
## TOPIC 02981: LINScheduler Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-linscheduler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-linscheduler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the LIN Scheduler channel under an NI-XNET LINPort. The LIN Scheduler specifies which schedule to use to determine when to transmit frames. This channel is only valid if the LINPort to which is belongs is configured as the master port (IsMaster is true). Derives fromChannelSyntaxNamespace

### LINScheduler Class

Represents the **LIN Scheduler** channel under an NI-XNET [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html). The LIN Scheduler specifies which schedule to use to determine when to transmit frames. This channel is only valid if the [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html) to which is belongs is configured as the master port ([IsMaster](nationalinstruments-veristand-systemdefinitionapi-linport-ismaster.html) is true).

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class LINScheduler : Channel

#### Remarks

You can use the members of this class to get or set the active schedule for the master [LINPort](nationalinstruments-veristand-systemdefinitionapi-linport.html).

**Accessing this Class**

- [GetLINScheduler](nationalinstruments-veristand-systemdefinitionapi-linport-getlinscheduler.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ActiveSchedule | Gets or sets the name of the active LIN schedule. |
| Units | Gets the units associated with the LIN Scheduler channel. |

#### Methods

| Name | Description |
| --- | --- |
| SetActiveSchedule(string[], string) | Sets the active schedule for the current LINPort by searching the LINSchedules array for the name specified by ActiveSchedule . |
| SetActiveSchedule(string[], uint) | Sets the active schedule for the current LINPort by searching the LINSchedules array for the schedule at the specified ActiveScheduleIndex . |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-logmode.html language=enus -->
## TOPIC 02982: LogMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-logmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-logmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The logging mode that determines whether components in the NI VeriStand system can read data as you log it. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum LogModeMembersNameValueDescriptionLog15844Logs data but prevents components in the system from reading the data as

### LogMode Enumeration

The logging mode that determines whether components in the NI VeriStand system can read data as you log it.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum LogMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Log | 15844 | Logs data but prevents components in the system from reading the data as you log it. This option improves the performance of logging, but the data is not available to the rest of the system. For example, a waveform graph on the Workspace window cannot plot waveform data that a task acquires if you enable this mode. |
| LogAndRead | 15842 | Logs data and allows components in the system to read the data while logging occurs. For example, a waveform graph on a Workspace screen can plot data that the task acquires if you enable this mode. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__basenodetype.html language=enus -->
## TOPIC 02983: LookupTable(BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LookupTable class with the specified object. Throws an exception if the object's GUID is not that of LookupTable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LookupTable(BaseNodeType node)ParametersNameTypeDescriptionnodeBaseNodeTypeThe

### LookupTable(BaseNodeType)

Initializes a new instance of the LookupTable class with the specified object. Throws an exception if the object's GUID is not that of [LookupTable](nationalinstruments-veristand-systemdefinitionapi-lookuptable.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public LookupTable(BaseNodeType node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BaseNodeType | The BaseNodeType object. |

Parent topic:

LookupTable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__string-lutvalue_arr1-string.html language=enus -->
## TOPIC 02984: LookupTable(string, LUTValue[], string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__string-lutvalue_arr1-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__string-lutvalue_arr1-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LookupTable class with the specified name and properties. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LookupTable(string name, LUTValue[] lookupTableValues, string scaleUnit)ParametersNameTypeDescriptionnamestringThe name of the LookupTa

### LookupTable(string, LUTValue[], string)

Initializes a new instance of the LookupTable class with the specified name and properties.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public LookupTable(string name, LUTValue[] lookupTableValues, string scaleUnit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the LookupTable instance. |
| lookupTableValues | LUTValue[] | An array of LUTValue elements. |
| scaleUnit | string | The units of the scale. This can be any arbitrary string. |

Parent topic:

LookupTable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__string.html language=enus -->
## TOPIC 02985: LookupTable(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptable__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LookupTable class with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LookupTable(string name)RemarksThis constructor sets scaleUnit to V and the lookupTableValues to null. ParametersNameTypeDescriptionnamestringThe name

### LookupTable(string)

Initializes a new instance of the LookupTable class with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public LookupTable(string name)

#### Remarks

This constructor sets *scaleUnit* to V and the *lookupTableValues* to null.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the LookupTable instance. |

Parent topic:

LookupTable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptablevalues.html language=enus -->
## TOPIC 02986: LookupTableValues

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptablevalues.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lookuptable-lookuptablevalues.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the values of the LookupTable scale. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LUTValue[] LookupTableValues { get; set; }ReturnsAn array of LUTValue elements.

### LookupTableValues

Gets or sets the values of the LookupTable scale.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [LUTValue](nationalinstruments-veristand-systemdefinitionapi-lutvalue.html)[] LookupTableValues { get; set; }

#### Returns

An array of [LUTValue](nationalinstruments-veristand-systemdefinitionapi-lutvalue.html) elements.

Parent topic:

LookupTable Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lookuptable.html language=enus -->
## TOPIC 02987: LookupTable Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lookuptable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lookuptable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a lookup table Scale, which maps an array of pre-scaled values to an array of corresponding scaled values. Derives fromScaleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class LookupTable : ScaleRemarksNI VeriStand applies linear interpolation to values that fal

### LookupTable Class

Represents a lookup table [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html), which maps an array of pre-scaled values to an array of corresponding scaled values.

#### Derives from

- Scale

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class LookupTable : Scale

#### Remarks

- **Pre-Scaled Values:** 0, 5, 10
- **Scaled Values:** 0, 10, 20

**Values Outside the Lookup Table Range**

NI VeriStand clips samples that are outside the maximum and minimum scaled values found in the table. For example, suppose the following lookup table scale is mapped to an input channel that reads a pre-scaled value of 3:

- **Pre-Scaled Values:** 0, 1, 2
- **Scaled Values:** 0, 4, 10

#### Constructors

| Name | Description |
| --- | --- |
| LookupTable(BaseNodeType) | Initializes a new instance of the LookupTable class with the specified object. Throws an exception if the object's GUID is not that of LookupTable. |
| LookupTable(string, LUTValue[], string) | Initializes a new instance of the LookupTable class with the specified name and properties. |
| LookupTable(string) | Initializes a new instance of the LookupTable class with the specified name. |

#### Properties

| Name | Description |
| --- | --- |
| LookupTableValues | Gets or sets the values of the LookupTable scale. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-channeltofilter.html language=enus -->
## TOPIC 02988: ChannelToFilter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-channeltofilter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-channeltofilter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel to which to apply the filter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode ChannelToFilter { get; set; }ReturnsA BaseNode reference to the channel.

### ChannelToFilter

Gets or sets the channel to which to apply the filter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) ChannelToFilter { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

LowpassFilter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-filterorder.html language=enus -->
## TOPIC 02989: FilterOrder

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-filterorder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-filterorder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpubli

### FilterOrder

Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int FilterOrder { get; set; }

#### Returns

The order of the filter.

Parent topic:

LowpassFilter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-lowcutofffrequency.html language=enus -->
## TOPIC 02990: LowCutoffFrequency

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-lowcutofffrequency.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-lowcutofffrequency.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the low cutoff frequency, in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double LowCutoffFrequency { get; set; }ReturnsThe low cutoff frequency, in hertz.

### LowCutoffFrequency

Gets or sets the low cutoff frequency, in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double LowCutoffFrequency { get; set; }

#### Returns

The low cutoff frequency, in hertz.

Parent topic:

LowpassFilter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-lowpassfilter__string-string-channel-double-int.html language=enus -->
## TOPIC 02991: LowpassFilter(string, string, Channel, double, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-lowpassfilter__string-string-channel-double-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-lowpassfilter__string-string-channel-double-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of LowpassFilter with the specified name, description, and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LowpassFilter(string Name, string Description, Channel ChannelToFilter, double LowCutoffFrequency, int FilterOrder)ParametersN

### LowpassFilter(string, string, Channel, double, int)

Initializes a new instance of [LowpassFilter](nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html) with the specified name, description, and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public LowpassFilter(string Name, string Description, Channel ChannelToFilter, double LowCutoffFrequency, int FilterOrder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| ChannelToFilter | Channel | The channel to which to apply the filter. |
| LowCutoffFrequency | double | The low cutoff frequency in hertz. |
| FilterOrder | int | The order of the filter. |

Parent topic:

LowpassFilter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html language=enus -->
## TOPIC 02992: LowpassFilter Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a calculated channel with the Lowpass Filter function. This function applies a lowpass Butterworth filter to the value of the specified ChannelToFilter. Derives fromCalculatedChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class LowpassFilter : CalculatedCh

### LowpassFilter Class

Represents a calculated channel with the **Lowpass Filter** function. This function applies a lowpass Butterworth filter to the value of the specified [ChannelToFilter](nationalinstruments-veristand-systemdefinitionapi-lowpassfilter-channeltofilter.html).

#### Derives from

- CalculatedChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class LowpassFilter : CalculatedChannel

#### Remarks

Use the members of this class to configure the channel to apply the filter to, the filter order, and the low cutoff frequency.

**Accessing this Class**

- LowpassFilter Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| LowpassFilter(string, string, Channel, double, int) | Initializes a new instance of LowpassFilter with the specified name, description, and configuration. |

#### Properties

| Name | Description |
| --- | --- |
| ChannelToFilter | Gets or sets the channel to which to apply the filter. |
| FilterOrder | Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable. |
| LowCutoffFrequency | Gets or sets the low cutoff frequency, in hertz. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lutvalue-prescaled.html language=enus -->
## TOPIC 02993: PreScaled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lutvalue-prescaled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lutvalue-prescaled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pre-scaled LUTValue. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double PreScaled { get; set; }

### PreScaled

Gets or sets the pre-scaled LUTValue.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double PreScaled { get; set; }

Parent topic:

LUTValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lutvalue-scaled.html language=enus -->
## TOPIC 02994: Scaled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lutvalue-scaled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lutvalue-scaled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the scaled LUTValue. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Scaled { get; set; }

### Scaled

Gets or sets the scaled LUTValue.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Scaled { get; set; }

Parent topic:

LUTValue Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-lutvalue.html language=enus -->
## TOPIC 02995: LUTValue Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-lutvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-lutvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a pair of values in a LookupTable scale: a pre-scaled value and the corresponding scaled value. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class LUTValuePropertiesNameDescriptionPreScaledGets or sets the pre-scaled LUTValue. ScaledGets or sets

### LUTValue Class

Represents a pair of values in a [LookupTable](nationalinstruments-veristand-systemdefinitionapi-lookuptable.html) scale: a pre-scaled value and the corresponding scaled value.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class LUTValue

#### Properties

| Name | Description |
| --- | --- |
| PreScaled | Gets or sets the pre-scaled LUTValue. |
| Scaled | Gets or sets the scaled LUTValue. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-basenode-basenode.html language=enus -->
## TOPIC 02996: Maximum(string, string, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Maximum where the values of x and y are both channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Maximum(string Name, string Description, BaseNode XValue, BaseNode YValue)ParametersNameTypeDescriptionNamestringThe name of the calculated ch

### Maximum(string, string, BaseNode, BaseNode)

Initializes a new instance of [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) where the values of *x* and *y* are both channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Maximum(string Name, string Description, BaseNode XValue, BaseNode YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| XValue | BaseNode | The channel to be compared. |
| YValue | BaseNode | The channel value to which x is compared. |

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-basenode-double.html language=enus -->
## TOPIC 02997: Maximum(string, string, BaseNode, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-basenode-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-basenode-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Maximum where the value of x is a channel and the value of y is a constant. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Maximum(string Name, string Description, BaseNode XValue, double YValue)ParametersNameTypeDescriptionNamestringThe name o

### Maximum(string, string, BaseNode, double)

Initializes a new instance of [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) where the value of *x* is a channel and the value of *y* is a constant.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Maximum(string Name, string Description, BaseNode XValue, double YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| XValue | BaseNode | The channel to be compared. |
| YValue | double | The constant value to which x is compared. |

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-double-basenode.html language=enus -->
## TOPIC 02998: Maximum(string, string, double, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-double-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-double-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Maximum where the value of x is a constant and the value of y is a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Maximum(string Name, string Description, double XValue, BaseNode YValue)ParametersNameTypeDescriptionNamestringThe name o

### Maximum(string, string, double, BaseNode)

Initializes a new instance of [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) where the value of *x* is a constant and the value of *y* is a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Maximum(string Name, string Description, double XValue, BaseNode YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| XValue | double | The constant value to be compared. |
| YValue | BaseNode | The channel value to which x is compared. |

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-double-double.html language=enus -->
## TOPIC 02999: Maximum(string, string, double, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-maximum__string-string-double-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Maximum where the values of x and y are both constants. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Maximum(string Name, string Description, double XValue, double YValue)ParametersNameTypeDescriptionNamestringThe name of the Maximum calculat

### Maximum(string, string, double, double)

Initializes a new instance of [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) where the values of *x* and *y* are both constants.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Maximum(string Name, string Description, double XValue, double YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Maximum calculated channel. |
| Description | string | The description of the Maximum calculated channel. |
| XValue | double | The constant value to be compared. |
| YValue | double | The constant value to which x is compared. |

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-setxvalue__basenode.html language=enus -->
## TOPIC 03000: SetXValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-setxvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-setxvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of x in the comparison of x and y to the value of the specified channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetXValue(BaseNode XValue)ParametersNameTypeDescriptionXValueBaseNodeThe channel that specifies the value of x.

### SetXValue(BaseNode)

Sets the value of *x* in the comparison of *x* and *y* to the value of the specified channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetXValue(BaseNode XValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| XValue | BaseNode | The channel that specifies the value of x. |

Parent topic:

Maximum Class
