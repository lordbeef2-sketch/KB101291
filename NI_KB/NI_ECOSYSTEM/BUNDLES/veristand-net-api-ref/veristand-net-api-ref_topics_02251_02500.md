# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=2251 end=2500 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-daqmeasurementtype-double.html language=enus -->
## TOPIC 02251: DAQAnalogOutput(string, uint, DAQMeasurementType, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-daqmeasurementtype-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-daqmeasurementtype-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutput(string name, uint channel, DAQMeasurementType measurementType, double initialValue)ParametersNameTypeDescriptionnamestringThe name of the analog output ch

### DAQAnalogOutput(string, uint, DAQMeasurementType, double)

Initializes a new instance of the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogOutput(string name, uint channel, DAQMeasurementType measurementType, double initialValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog output channel. |
| channel | uint | The channel number of the analog output channel. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |
| initialValue | double | The initial value of the analog output channel. |

Parent topic:

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-daqmeasurementtype.html language=enus -->
## TOPIC 02252: DAQAnalogOutput(string, uint, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutput(string name, uint channel, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringThe name of the analog output channel.channeluintThe

### DAQAnalogOutput(string, uint, DAQMeasurementType)

Initializes a new instance of the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogOutput(string name, uint channel, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog output channel. |
| channel | uint | The channel number of the analog output channel. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |

Parent topic:

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-string-double.html language=enus -->
## TOPIC 02253: DAQAnalogOutput(string, uint, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutput(string name, uint channel, string pluginGUID, double initialValue)RemarksUse this constructor to create channels with a measurement type defined in a cust

### DAQAnalogOutput(string, uint, string, double)

Initializes a new instance of the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogOutput(string name, uint channel, string pluginGUID, double initialValue)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog output channel. |
| channel | uint | The channel number of the analog output channel. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |
| initialValue | double | The initial value of the analog output channel. |

Parent topic:

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-string.html language=enus -->
## TOPIC 02254: DAQAnalogOutput(string, uint, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-daqanalogoutput__string-uint-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQAnalogOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutput(string name, uint channel, string pluginGUID)RemarksUse this constructor to create channels with a measurement type defined in a custom DAQ measurement ty

### DAQAnalogOutput(string, uint, string)

Initializes a new instance of the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQAnalogOutput(string name, uint channel, string pluginGUID)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the analog output channel. |
| channel | uint | The channel number of the analog output channel. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |

Parent topic:

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-highlevel.html language=enus -->
## TOPIC 02255: HighLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-highlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-highlevel.html
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

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-initialvalue.html language=enus -->
## TOPIC 02256: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the analog output channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InitialValue { get; set; }ReturnsThe initial value of the channel.

### InitialValue

Gets or sets the initial value of the analog output channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InitialValue { get; set; }

#### Returns

The initial value of the channel.

Parent topic:

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-isscxi.html language=enus -->
## TOPIC 02257: IsSCXI

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-isscxi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-isscxi.html
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

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-lowlevel.html language=enus -->
## TOPIC 02258: LowLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-lowlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-lowlevel.html
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

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-scximoduletype.html language=enus -->
## TOPIC 02259: SCXIModuleType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-scximoduletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput-scximoduletype.html
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

DAQAnalogOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html language=enus -->
## TOPIC 02260: DAQAnalogOutput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ analog output channel. Derives fromDAQChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQAnalogOutput : DAQChannelRemarksUse the members of this class to get and set properties of the channel, such as its high and low level and whether it belong

### DAQAnalogOutput Class

Represents a DAQ analog output channel.

#### Derives from

- DAQChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQAnalogOutput : DAQChannel

#### Remarks

Use the members of this class to get and set properties of the channel, such as its high and low level and whether it belongs to an SCXI module.

**Accessing this Class**

- [GetAnalogOutputList](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-getanalogoutputlist.html)
- [GetAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-scximodule-getanalogoutputs.html)
- DAQAnalogOutput Constructor

National Instruments recommends that you use a version of the DAQAnalogOutput constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQAnalogOutput(string, uint, DAQMeasurementType, double) | Initializes a new instance of the DAQAnalogOutput class. |
| DAQAnalogOutput(string, string, double, double, double, uint, DAQAnalogChannelType) | Initializes a new instance of DAQAnalogOutput with the name and configuration that you specify. |
| DAQAnalogOutput(string, uint, DAQMeasurementType) | Initializes a new instance of the DAQAnalogOutput class. |
| DAQAnalogOutput(string, uint, string) | Initializes a new instance of the DAQAnalogOutput class. |
| DAQAnalogOutput(string, uint, string, double) | Initializes a new instance of the DAQAnalogOutput class. |

#### Properties

| Name | Description |
| --- | --- |
| Channel | Gets or sets the channel number. |
| ChannelType | Gets or sets the measurement type of the channel (Current or Voltage). |
| HighLevel | Gets or sets the maximum value of the channel. |
| InitialValue | Gets or sets the initial value of the analog output channel. |
| IsSCXI | Gets whether the channel belongs to an SCXI module. |
| LowLevel | Gets or sets the minimum value of the channel. |
| SCXIModuleType | Gets the specific type of SCXI module to which the channel belongs. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-addanalogoutput__daqanalogoutput-out.html language=enus -->
## TOPIC 02261: AddAnalogOutput(DAQAnalogOutput, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-addanalogoutput__daqanalogoutput-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-addanalogoutput__daqanalogoutput-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQAnalogOutput channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAnalogOutput(DAQAnalogOutput analogOutput, out Error error)ParametersNameTypeDescriptionanalogOutputDAQAnalogOutputThe DAQAnalogOutput channel to add.errorout ErrorReturns an

### AddAnalogOutput(DAQAnalogOutput, out Error)

Adds the specified [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAnalogOutput(DAQAnalogOutput analogOutput, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| analogOutput | DAQAnalogOutput | The DAQAnalogOutput channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) channel was added successfully.

Parent topic:

DAQAnalogOutputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-addanalogoutput__daqanalogoutput.html language=enus -->
## TOPIC 02262: AddAnalogOutput(DAQAnalogOutput)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-addanalogoutput__daqanalogoutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-addanalogoutput__daqanalogoutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQAnalogOutput channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAnalogOutput(DAQAnalogOutput analogOutput)ParametersNameTypeDescriptionanalogOutputDAQAnalogOutputThe DAQAnalogOutput channel to add.Returnstrue if the DAQAnalogOutput channel

### AddAnalogOutput(DAQAnalogOutput)

Adds the specified [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAnalogOutput(DAQAnalogOutput analogOutput)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| analogOutput | DAQAnalogOutput | The DAQAnalogOutput channel to add. |

#### Returns

true if the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) channel was added successfully.

Parent topic:

DAQAnalogOutputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-getanalogoutputlist.html language=enus -->
## TOPIC 02263: GetAnalogOutputList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-getanalogoutputlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs-getanalogoutputlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQAnalogOutput elements from the current DAQAnalogOutputs section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutput[] GetAnalogOutputList()RemarksModifications you make to the contents of this list apply to the system definitio

### GetAnalogOutputList()

Gets an array that contains the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) elements from the current [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html)[] GetAnalogOutputList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) elements from the current [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) section.

Parent topic:

DAQAnalogOutputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html language=enus -->
## TOPIC 02264: DAQAnalogOutputs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Analog Output section under a DAQDevice, which contains all DAQAnalogOutput channels you add for the device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQAnalogOutputs : SectionRemarksUse the members of this class to add analog ou

### DAQAnalogOutputs Class

Represents an **Analog Output** section under a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html), which contains all [DAQAnalogOutput](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutput.html) channels you add for the device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQAnalogOutputs : Section

#### Remarks

Note

You can improve performance by only adding the channels the system interacts with, as opposed to all the channels your hardware supports.

**Accessing this Class**

- [CreateAnalogOutputs(out Error)](nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanalogoutputs__out.1.html)
- [GetAnalogOutputSection](nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanalogoutputsection.html)

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddAnalogOutput(DAQAnalogOutput, out Error) | Adds the specified DAQAnalogOutput channel. |
| AddAnalogOutput(DAQAnalogOutput) | Adds the specified DAQAnalogOutput channel. |
| GetAnalogOutputList() | Gets an array that contains the DAQAnalogOutput elements from the current DAQAnalogOutputs section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getbooleanproperty__string-out.html language=enus -->
## TOPIC 02265: GetBooleanProperty(string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getbooleanproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getbooleanproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the Boolean property specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetBooleanProperty(string propertyName, out bool value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method t

### GetBooleanProperty(string, out bool)

Gets the value of the Boolean property specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetBooleanProperty(string propertyName, out bool value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out bool | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getdoubleproperty__string-out.html language=enus -->
## TOPIC 02266: GetDoubleProperty(string, out double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getdoubleproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getdoubleproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the Double property specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetDoubleProperty(string propertyName, out double value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method t

### GetDoubleProperty(string, out double)

Gets the value of the Double property specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetDoubleProperty(string propertyName, out double value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out double | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getenumproperty__string-out-out.html language=enus -->
## TOPIC 02267: GetEnumProperty(string, out string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getenumproperty__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getenumproperty__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string and integer values of the Enum property specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetEnumProperty(string propertyName, out string enumString, out int enumValue)RemarksTo find valid propertyName values, refer to the list

### GetEnumProperty(string, out string, out int)

Gets the string and integer values of the Enum property specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetEnumProperty(string propertyName, out string enumString, out int enumValue)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| enumString | out string | The string value of the enum. |
| enumValue | out int | The integer value of the enum. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti16property__string-out.html language=enus -->
## TOPIC 02268: GetI16Property(string, out short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti16property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti16property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the I16 property specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI16Property(string propertyName, out short value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throws a

### GetI16Property(string, out short)

Gets the value of the I16 property specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI16Property(string propertyName, out short value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out short | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti32property__string-out.html language=enus -->
## TOPIC 02269: GetI32Property(string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the I32 property specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI32Property(string propertyName, out int value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throws an

### GetI32Property(string, out int)

Gets the value of the I32 property specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI32Property(string propertyName, out int value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out int | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti64property__string-out.html language=enus -->
## TOPIC 02270: GetI64Property(string, out long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti64property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-geti64property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a property of type I64 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI64Property(string propertyName, out long value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method thr

### GetI64Property(string, out long)

Gets the value of a property of type I64 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI64Property(string propertyName, out long value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out long | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getproperties__out-out.html language=enus -->
## TOPIC 02271: GetProperties(out string[], out ValueDataType[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getproperties__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getproperties__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of all properties specified by the DAQ plugin for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetProperties(out string[] propertyNames, out ValueDataType[] propertyTypes)ParametersNameTypeDescriptionpropertyNamesout string[]The names of t

### GetProperties(out string[], out ValueDataType[])

Returns a list of all properties specified by the DAQ plugin for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetProperties(out string[] propertyNames, out ValueDataType[] propertyTypes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyNames | out string[] | The names of the properties. |
| propertyTypes | out ValueDataType[] | An enum defining the data type of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getstringproperty__string-out.html language=enus -->
## TOPIC 02272: GetStringProperty(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getstringproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getstringproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a property of type string specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetStringProperty(string propertyName, out string value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This me

### GetStringProperty(string, out string)

Gets the value of a property of type string specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetStringProperty(string propertyName, out string value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out string | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu16property__string-out.html language=enus -->
## TOPIC 02273: GetU16Property(string, out ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu16property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu16property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a property of type U16 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU16Property(string propertyName, out ushort value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method t

### GetU16Property(string, out ushort)

Gets the value of a property of type U16 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU16Property(string propertyName, out ushort value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out ushort | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu32property__string-out.html language=enus -->
## TOPIC 02274: GetU32Property(string, out uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a property of type U32 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU32Property(string propertyName, out uint value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method thr

### GetU32Property(string, out uint)

Gets the value of a property of type U32 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU32Property(string propertyName, out uint value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out uint | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu64property__string-out.html language=enus -->
## TOPIC 02275: GetU64Property(string, out ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu64property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-getu64property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a property of type U64 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU64Property(string propertyName, out ulong value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method th

### GetU64Property(string, out ulong)

Gets the value of a property of type U64 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU64Property(string propertyName, out ulong value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | out ulong | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-measurementtype.html language=enus -->
## TOPIC 02276: MeasurementType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-measurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-measurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of measurement or generation the DAQ channel performs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQMeasurementType MeasurementType { get; }ReturnsAn enumeration of DAQMeasurementType.

### MeasurementType

Gets the type of measurement or generation the DAQ channel performs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html) MeasurementType { get; }

#### Returns

An enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-pluginguid.html language=enus -->
## TOPIC 02277: PluginGUID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-pluginguid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-pluginguid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the GUID that corresponds to the type of measurement or generation the channel performs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string PluginGUID { get; set; }

### PluginGUID

Gets the GUID that corresponds to the type of measurement or generation the channel performs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string PluginGUID { get; set; }

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-resetpropertyvalues.html language=enus -->
## TOPIC 02278: ResetPropertyValues()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-resetpropertyvalues.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-resetpropertyvalues.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reset all properties specified in the DAQ Plugin XML to their defaults. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ResetPropertyValues()

### ResetPropertyValues()

Reset all properties specified in the DAQ Plugin XML to their defaults.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ResetPropertyValues()

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setbooleanproperty__string-bool.html language=enus -->
## TOPIC 02279: SetBooleanProperty(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setbooleanproperty__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setbooleanproperty__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type Boolean specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetBooleanProperty(string propertyName, bool value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method

### SetBooleanProperty(string, bool)

Sets the value of a property of type Boolean specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetBooleanProperty(string propertyName, bool value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | bool | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setdoubleproperty__string-double.html language=enus -->
## TOPIC 02280: SetDoubleProperty(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setdoubleproperty__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setdoubleproperty__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type double specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetDoubleProperty(string propertyName, double value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method

### SetDoubleProperty(string, double)

Sets the value of a property of type double specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetDoubleProperty(string propertyName, double value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | double | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setenumproperty__string-int.html language=enus -->
## TOPIC 02281: SetEnumProperty(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setenumproperty__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setenumproperty__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type enum specified by propertyName , where the enum value is an integer. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetEnumProperty(string propertyName, int value)RemarksTo find valid propertyName and enum values, refer to the list

### SetEnumProperty(string, int)

Sets the value of a property of type enum specified by *propertyName* , where the enum value is an integer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetEnumProperty(string propertyName, int value)

#### Remarks

To find valid *propertyName*  and enum values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel, or if the *value*  is invalid.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | int | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setenumproperty__string-string.html language=enus -->
## TOPIC 02282: SetEnumProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setenumproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setenumproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type enum specified by propertyName , where the enum value is a string. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetEnumProperty(string propertyName, string enumString)RemarksTo find valid propertyName and enumString values, refer

### SetEnumProperty(string, string)

Sets the value of a property of type enum specified by *propertyName* , where the enum value is a string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetEnumProperty(string propertyName, string enumString)

#### Remarks

To find valid *propertyName*  and *enumString*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel, or if the *enumString*  is invalid.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| enumString | string | The value of the enum as a string. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti16property__string-short.html language=enus -->
## TOPIC 02283: SetI16Property(string, short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti16property__string-short.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti16property__string-short.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type I16 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI16Property(string propertyName, short value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throws

### SetI16Property(string, short)

Sets the value of a property of type I16 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI16Property(string propertyName, short value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | short | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti32property__string-int.html language=enus -->
## TOPIC 02284: SetI32Property(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti32property__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti32property__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type I32 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI32Property(string propertyName, int value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throws a

### SetI32Property(string, int)

Sets the value of a property of type I32 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI32Property(string propertyName, int value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | int | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti64property__string-long.html language=enus -->
## TOPIC 02285: SetI64Property(string, long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti64property__string-long.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-seti64property__string-long.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type I64 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI64Property(string propertyName, long value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throws

### SetI64Property(string, long)

Sets the value of a property of type I64 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI64Property(string propertyName, long value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | long | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setstringproperty__string-string.html language=enus -->
## TOPIC 02286: SetStringProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setstringproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setstringproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type string specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetStringProperty(string propertyName, string value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method

### SetStringProperty(string, string)

Sets the value of a property of type string specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetStringProperty(string propertyName, string value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | string | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu16property__string-ushort.html language=enus -->
## TOPIC 02287: SetU16Property(string, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu16property__string-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu16property__string-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type U16 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU16Property(string propertyName, ushort value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throw

### SetU16Property(string, ushort)

Sets the value of a property of type U16 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU16Property(string propertyName, ushort value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | ushort | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu32property__string-uint.html language=enus -->
## TOPIC 02288: SetU32Property(string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu32property__string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu32property__string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type U32 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU32Property(string propertyName, uint value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throws

### SetU32Property(string, uint)

Sets the value of a property of type U32 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU32Property(string propertyName, uint value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | uint | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu64property__string-ulong.html language=enus -->
## TOPIC 02289: SetU64Property(string, ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu64property__string-ulong.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel-setu64property__string-ulong.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a property of type U64 specified by propertyName . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU64Property(string propertyName, ulong value)RemarksTo find valid propertyName values, refer to the list of DAQ channel properties. This method throws

### SetU64Property(string, ulong)

Sets the value of a property of type U64 specified by *propertyName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU64Property(string propertyName, ulong value)

#### Remarks

To find valid *propertyName*  values, refer to the list of DAQ channel properties

.

This method throws an exception if the *propertyName*  does not exist in the plug-in XML file that defines the measurement type of the channel.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | The name of the property. |
| value | ulong | The value of the property. |

Parent topic:

DAQChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqchannel.html language=enus -->
## TOPIC 02290: DAQChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides an abstract base class for implementing DAQ device channels and their measurement types based on DAQ plug-in XML files. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQChannel : ChannelPropertiesNameDescriptionMeasurementTypeGets the type

### DAQChannel Class

Provides an abstract base class for implementing DAQ device channels and their measurement types based on DAQ plug-in XML files.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQChannel : Channel

#### Properties

| Name | Description |
| --- | --- |
| MeasurementType | Gets the type of measurement or generation the DAQ channel performs. |
| PluginGUID | Gets the GUID that corresponds to the type of measurement or generation the channel performs. |

#### Methods

| Name | Description |
| --- | --- |
| GetBooleanProperty(string, out bool) | Gets the value of the Boolean property specified by propertyName . |
| GetDoubleProperty(string, out double) | Gets the value of the Double property specified by propertyName . |
| GetEnumProperty(string, out string, out int) | Gets the string and integer values of the Enum property specified by propertyName . |
| GetI16Property(string, out short) | Gets the value of the I16 property specified by propertyName . |
| GetI32Property(string, out int) | Gets the value of the I32 property specified by propertyName . |
| GetI64Property(string, out long) | Gets the value of a property of type I64 specified by propertyName . |
| GetProperties(out string[], out ValueDataType[]) | Returns a list of all properties specified by the DAQ plugin for the channel. |
| GetStringProperty(string, out string) | Gets the value of a property of type string specified by propertyName . |
| GetU16Property(string, out ushort) | Gets the value of a property of type U16 specified by propertyName . |
| GetU32Property(string, out uint) | Gets the value of a property of type U32 specified by propertyName . |
| GetU64Property(string, out ulong) | Gets the value of a property of type U64 specified by propertyName . |
| ResetPropertyValues() | Reset all properties specified in the DAQ Plugin XML to their defaults. |
| SetBooleanProperty(string, bool) | Sets the value of a property of type Boolean specified by propertyName . |
| SetDoubleProperty(string, double) | Sets the value of a property of type double specified by propertyName . |
| SetEnumProperty(string, int) | Sets the value of a property of type enum specified by propertyName , where the enum value is an integer. |
| SetEnumProperty(string, string) | Sets the value of a property of type enum specified by propertyName , where the enum value is a string. |
| SetI16Property(string, short) | Sets the value of a property of type I16 specified by propertyName . |
| SetI32Property(string, int) | Sets the value of a property of type I32 specified by propertyName . |
| SetI64Property(string, long) | Sets the value of a property of type I64 specified by propertyName . |
| SetStringProperty(string, string) | Sets the value of a property of type string specified by propertyName . |
| SetU16Property(string, ushort) | Sets the value of a property of type U16 specified by propertyName . |
| SetU32Property(string, uint) | Sets the value of a property of type U32 specified by propertyName . |
| SetU64Property(string, ulong) | Sets the value of a property of type U64 specified by propertyName . |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_active_edge.html language=enus -->
## TOPIC 02291: DAQCM_Active_Edge Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_active_edge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_active_edge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge on which the sample clock pulses to acquire or generate samples. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_Active_EdgeMembersNameValueDescriptionRising10280The sample clock pulses to acquire or generate samples on the rising edge. Falling1

### DAQCM_Active_Edge Enumeration

Specifies the edge on which the sample clock pulses to acquire or generate samples.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Active_Edge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | The sample clock pulses to acquire or generate samples on the rising edge. |
| Falling | 10171 | The sample clock pulses to acquire or generate samples on the falling edge. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_clock_source.html language=enus -->
## TOPIC 02292: DAQCM_Clock_Source Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_clock_source.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_clock_source.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the sample clock. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_Clock_SourceRemarksThe PXI trigger bus is the timing bus that connects PXI DAQ devices directly. The RTSI bus is the timing bus that connects PCI DAQ devices directly. These

### DAQCM_Clock_Source Enumeration

Specifies the source of the sample clock.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Clock_Source

#### Remarks

Note

The PXI trigger bus is the timing bus that connects PXI DAQ devices directly. The RTSI bus is the timing bus that connects PCI DAQ devices directly. These buses are functionally equivalent.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Onboard10MHzClock | 0 | The device's onboard 10 MHz clock. |
| PFI_0 |  | The PFI 0 terminal. |
| PFI_1 |  | The PFI 1 terminal. |
| PFI_2 |  | The PFI 2 terminal. |
| PFI_3 |  | The PFI 3 terminal. |
| PFI_4 |  | The PFI 4 terminal. |
| PFI_5 |  | The PFI 5 terminal. |
| PFI_6 |  | The PFI 6 terminal. |
| PFI_7 |  | The PFI 7 terminal. |
| PFI_8 |  | The PFI 8 terminal. |
| PFI_9 |  | The PFI 9 terminal. |
| PFI_10 |  | The PFI 10 terminal. |
| PFI_11 |  | The PFI 11 terminal. |
| PFI_12 |  | The PFI 12 terminal. |
| PFI_13 |  | The PFI 13 terminal. |
| PFI_14 |  | The PFI 14 terminal. |
| PFI_15 |  | The PFI 15 terminal. |
| RTSI_PXI_TRIG_0 |  | The RTSI 0 or PXI Trigger 0 terminal. |
| RTSI_PXI_TRIG_1 |  | The RTSI 1 or PXI Trigger 1 terminal. |
| RTSI_PXI_TRIG_2 |  | The RTSI 2 or PXI Trigger 2 terminal. |
| RTSI_PXI_TRIG_3 |  | The RTSI 3 or PXI Trigger 3 terminal. |
| RTSI_PXI_TRIG_4 |  | The RTSI 4 or PXI Trigger 4 terminal. |
| RTSI_PXI_TRIG_5 |  | The RTSI 5 or PXI Trigger 5 terminal. |
| RTSI_PXI_TRIG_6 |  | The RTSI 6 or PXI Trigger 6 terminal. |
| RTSI_PXI_TRIG_7 |  | The RTSI 7 or PXI Trigger 7 terminal. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_export_clk_on_line.html language=enus -->
## TOPIC 02293: DAQCM_Export_Clk_On_Line Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_export_clk_on_line.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_export_clk_on_line.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the line that receives the pulse from the sample clock. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_Export_Clk_On_LineRemarksThe PXI trigger bus is the timing bus that connects PXI DAQ devices directly. The RTSI bus is the timing bus that connects PC

### DAQCM_Export_Clk_On_Line Enumeration

Specifies the line that receives the pulse from the sample clock.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Export_Clk_On_Line

#### Remarks

Note

The PXI trigger bus is the timing bus that connects PXI DAQ devices directly. The RTSI bus is the timing bus that connects PCI DAQ devices directly. These buses are functionally equivalent.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Default_RTSI_PXI_TRIG_0 | 0 | The RTSI 0 or PXI Trigger 0 line. This is the default setting. |
| PFI_0 |  | The PFI 0 line. |
| PFI_1 |  | The PFI 1 line. |
| PFI_2 |  | The PFI 2 line. |
| PFI_3 |  | The PFI 3 line. |
| PFI_4 |  | The PFI 4 line. |
| PFI_5 |  | The PFI 5 line. |
| PFI_6 |  | The PFI 6 line. |
| PFI_7 |  | The PFI 7 line. |
| PFI_8 |  | The PFI 8 line. |
| PFI_9 |  | The PFI 9 line. |
| PFI_10 |  | The PFI 10 line. |
| PFI_11 |  | The PFI 11 line. |
| PFI_12 |  | The PFI 12 line. |
| PFI_13 |  | The PFI 13 line. |
| PFI_14 |  | The PFI 14 line. |
| PFI_15 |  | The PFI 15 line. |
| RTSI_PXI_TRIG_0 |  | The RTSI 0 or PXI Trigger 0 line. |
| RTSI_PXI_TRIG_1 |  | The RTSI 1 or PXI Trigger 1 line. |
| RTSI_PXI_TRIG_2 |  | The RTSI 2 or PXI Trigger 2 line. |
| RTSI_PXI_TRIG_3 |  | The RTSI 3 or PXI Trigger 3 line. |
| RTSI_PXI_TRIG_4 |  | The RTSI 4 or PXI Trigger 4 line. |
| RTSI_PXI_TRIG_5 |  | The RTSI 5 or PXI Trigger 5 line. |
| RTSI_PXI_TRIG_6 |  | The RTSI 6 or PXI Trigger 6 line. |
| RTSI_PXI_TRIG_7 |  | The RTSI 7 or PXI Trigger 7 line. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_export_sample_clock.html language=enus -->
## TOPIC 02294: DAQCM_Export_Sample_Clock Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_export_sample_clock.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_export_sample_clock.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sample clock to export. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_Export_Sample_ClockMembersNameValueDescriptionaiSampleClock0The AI sample clock. aoSampleClockThe AO sample clock.

### DAQCM_Export_Sample_Clock Enumeration

Specifies the sample clock to export.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Export_Sample_Clock

#### Members

| Name | Value | Description |
| --- | --- | --- |
| aiSampleClock | 0 | The AI sample clock. |
| aoSampleClock |  | The AO sample clock. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_export_start_trigger.html language=enus -->
## TOPIC 02295: DAQCM_Export_Start_Trigger Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_export_start_trigger.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_export_start_trigger.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start trigger to export. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_Export_Start_TriggerMembersNameValueDescriptionaiStartTrigger0The AI Start Trigger. aoStartTriggerThe AO Start Trigger.

### DAQCM_Export_Start_Trigger Enumeration

Specifies the start trigger to export.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Export_Start_Trigger

#### Members

| Name | Value | Description |
| --- | --- | --- |
| aiStartTrigger | 0 | The AI Start Trigger. |
| aoStartTrigger |  | The AO Start Trigger. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_export_starttrigger_on_line.html language=enus -->
## TOPIC 02296: DAQCM_Export_StartTrigger_On_Line Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_export_starttrigger_on_line.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_export_starttrigger_on_line.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the line that exports the Start Trigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_Export_StartTrigger_On_LineMembersNameValueDescriptionNone0No line is assigned to export the Start Trigger. PFI_0The PFI 0 line. PFI_1The PFI 1 line. PFI_2The PFI 2

### DAQCM_Export_StartTrigger_On_Line Enumeration

Specifies the line that exports the Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Export_StartTrigger_On_Line

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No line is assigned to export the Start Trigger. |
| PFI_0 |  | The PFI 0 line. |
| PFI_1 |  | The PFI 1 line. |
| PFI_2 |  | The PFI 2 line. |
| PFI_3 |  | The PFI 3 line. |
| PFI_4 |  | The PFI 4 line. |
| PFI_5 |  | The PFI 5 line. |
| PFI_6 |  | The PFI 6 line. |
| PFI_7 |  | The PFI 7 line. |
| PFI_8 |  | The PFI 8 line. |
| PFI_9 |  | The PFI 9 line. |
| PFI_10 |  | The PFI 10 line. |
| PFI_11 |  | The PFI 11 line. |
| PFI_12 |  | The PFI 12 line. |
| PFI_13 |  | The PFI 13 line. |
| PFI_14 |  | The PFI 14 line. |
| PFI_15 |  | The PFI 15 line. |
| RTSI_PXI_TRIG_0 |  | The RTSI 0 or PXI Trigger 0 line. |
| RTSI_PXI_TRIG_1 |  | The RTSI 1 or PXI Trigger 1 line. |
| RTSI_PXI_TRIG_2 |  | The RTSI 2 or PXI Trigger 2 line. |
| RTSI_PXI_TRIG_3 |  | The RTSI 3 or PXI Trigger 3 line. |
| RTSI_PXI_TRIG_4 |  | The RTSI 4 or PXI Trigger 4 line. |
| RTSI_PXI_TRIG_5 |  | The RTSI 5 or PXI Trigger 5 line. |
| RTSI_PXI_TRIG_6 |  | The RTSI 6 or PXI Trigger 6 line. |
| RTSI_PXI_TRIG_7 |  | The RTSI 7 or PXI Trigger 7 line. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_slope.html language=enus -->
## TOPIC 02297: DAQCM_Slope Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_slope.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_slope.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge on which to trigger the device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_SlopeMembersNameValueDescriptionRising10280The device triggers on the rising edge. Falling10171The device triggers on the falling edge.

### DAQCM_Slope Enumeration

Specifies the edge on which to trigger the device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Slope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 10280 | The device triggers on the rising edge. |
| Falling | 10171 | The device triggers on the falling edge. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcm_trigger_line.html language=enus -->
## TOPIC 02298: DAQCM_Trigger_Line Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcm_trigger_line.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcm_trigger_line.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the line that triggers the acquisition or generation of samples. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCM_Trigger_LineMembersNameValueDescriptionNone0No trigger line is assigned. PFI_0The PFI 0 line. PFI_1The PFI 1 line. PFI_2The PFI 2 line. PFI_3

### DAQCM_Trigger_Line Enumeration

Specifies the line that triggers the acquisition or generation of samples.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCM_Trigger_Line

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No trigger line is assigned. |
| PFI_0 |  | The PFI 0 line. |
| PFI_1 |  | The PFI 1 line. |
| PFI_2 |  | The PFI 2 line. |
| PFI_3 |  | The PFI 3 line. |
| PFI_4 |  | The PFI 4 line. |
| PFI_5 |  | The PFI 5 line. |
| PFI_6 |  | The PFI 6 line. |
| PFI_7 |  | The PFI 7 line. |
| PFI_8 |  | The PFI 8 line. |
| PFI_9 |  | The PFI 9 line. |
| PFI_10 |  | The PFI 10 line. |
| PFI_11 |  | The PFI 11 line. |
| PFI_12 |  | The PFI 12 line. |
| PFI_13 |  | The PFI 13 line. |
| PFI_14 |  | The PFI 14 line. |
| PFI_15 |  | The PFI 15 line. |
| RTSI_PXI_TRIG_0 |  | The RTSI 0 or PXI Trigger 0 line. |
| RTSI_PXI_TRIG_1 |  | The RTSI 1 or PXI Trigger 1 line. |
| RTSI_PXI_TRIG_2 |  | The RTSI 2 or PXI Trigger 2 line. |
| RTSI_PXI_TRIG_3 |  | The RTSI 3 or PXI Trigger 3 line. |
| RTSI_PXI_TRIG_4 |  | The RTSI 4 or PXI Trigger 4 line. |
| RTSI_PXI_TRIG_5 |  | The RTSI 5 or PXI Trigger 5 line. |
| RTSI_PXI_TRIG_6 |  | The RTSI 6 or PXI Trigger 6 line. |
| RTSI_PXI_TRIG_7 |  | The RTSI 7 or PXI Trigger 7 line. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqconversionrate.html language=enus -->
## TOPIC 02299: DAQConversionRate Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqconversionrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqconversionrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate used to run the analog-digital converters (ADCs) on a DAQ device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQConversionRateMembersNameValueDescriptionDefault0The default rate. Maximum1The maximum rate the device supports.

### DAQConversionRate Enumeration

Specifies the rate used to run the analog-digital converters (ADCs) on a DAQ device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQConversionRate

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Default | 0 | The default rate. |
| Maximum | 1 | The maximum rate the device supports. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-counter.html language=enus -->
## TOPIC 02300: Counter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-counter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-counter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the counter channel number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Counter { get; }ReturnsThe channel number.

### Counter

Gets the counter channel number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Counter { get; }

#### Returns

The channel number.

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-daqmeasurementtype-double.html language=enus -->
## TOPIC 02301: DAQCounter(string, uint, DAQMeasurementType, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-daqmeasurementtype-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-daqmeasurementtype-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQCounter class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounter(string name, uint index, DAQMeasurementType measurementType, double initialValue)ParametersNameTypeDescriptionnamestringThe name of the counter.indexuintThe counter

### DAQCounter(string, uint, DAQMeasurementType, double)

Initializes a new instance of the DAQCounter class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQCounter(string name, uint index, DAQMeasurementType measurementType, double initialValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the counter. |
| index | uint | The counter index. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |
| initialValue | double | The initial value of counter. |

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-daqmeasurementtype.html language=enus -->
## TOPIC 02302: DAQCounter(string, uint, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQCounter class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounter(string name, uint index, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringThe name of counter.indexuintThe counter indexmeasurementTypeDAQM

### DAQCounter(string, uint, DAQMeasurementType)

Initializes a new instance of the DAQCounter class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQCounter(string name, uint index, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of counter. |
| index | uint | The counter index |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-string-double.html language=enus -->
## TOPIC 02303: DAQCounter(string, uint, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQCounter class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounter(string name, uint index, string pluginGUID, double initialValue)RemarksUse this constructor to create channels with a measurement type defined in a custom DAQ measu

### DAQCounter(string, uint, string, double)

Initializes a new instance of the DAQCounter class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQCounter(string name, uint index, string pluginGUID, double initialValue)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the counter. |
| index | uint | The counter index. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |
| initialValue | double | The initial value of the counter. |

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-string.html language=enus -->
## TOPIC 02304: DAQCounter(string, uint, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-daqcounter__string-uint-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQCounter class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounter(string name, uint index, string pluginGUID)RemarksUse this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in X

### DAQCounter(string, uint, string)

Initializes a new instance of the DAQCounter class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQCounter(string name, uint index, string pluginGUID)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the counter. |
| index | uint | The counter index. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-datatask.html language=enus -->
## TOPIC 02305: DataTask

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-datatask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-datatask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of task the counter performs (frequency measurement, period measurement, count up/down, or position measurement). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterType DataTask { get; }ReturnsAn enumeration value of DAQCounterType.

### DataTask

Gets the type of task the counter performs (frequency measurement, period measurement, count up/down, or position measurement).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterType](nationalinstruments-veristand-systemdefinitionapi-daqcountertype.html) DataTask { get; }

#### Returns

An enumeration value of [DAQCounterType](nationalinstruments-veristand-systemdefinitionapi-daqcountertype.html).

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html language=enus -->
## TOPIC 02306: DefaultTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the DAQmx default terminal for this counter will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static readonly string DefaultTerminal

### DefaultTerminal

Indicates that the DAQmx default terminal for this counter will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static readonly string DefaultTerminal

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-downcast.html language=enus -->
## TOPIC 02307: Downcast()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-downcast.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-downcast.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Casts DAQCounter to a more specific type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounter Downcast()ReturnsA reference to the downcast DAQCounter object.

### Downcast()

Casts [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) to a more specific type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) Downcast()

#### Returns

A reference to the downcast [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) object.

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-initialvalue.html language=enus -->
## TOPIC 02308: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the counter channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InitialValue { get; set; }ReturnsThe initial value of the channel.

### InitialValue

Gets or sets the initial value of the counter channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InitialValue { get; set; }

#### Returns

The initial value of the channel.

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter-setcounterindex__uint.html language=enus -->
## TOPIC 02309: SetCounterIndex(uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter-setcounterindex__uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter-setcounterindex__uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the index value of the counter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetCounterIndex(uint Index)ParametersNameTypeDescriptionIndexuintThe index value of the channel.Returnstrue if the counter was set successfully.

### SetCounterIndex(uint)

Sets the index value of the counter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetCounterIndex(uint Index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Index | uint | The index value of the channel. |

#### Returns

true if the counter was set successfully.

Parent topic:

DAQCounter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounter.html language=enus -->
## TOPIC 02310: DAQCounter Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ counter channel. Derives fromDAQChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQCounter : DAQChannelRemarksUse the members of this class to get and set properties of the channel, such as its task type and initial value. Accessing this ClassGe

### DAQCounter Class

Represents a DAQ counter channel.

#### Derives from

- DAQChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQCounter : DAQChannel

#### Remarks

Use the members of this class to get and set properties of the channel, such as its task type and initial value.

**Accessing this Class**

- [GetCounterList](nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounterlist.html)
- DAQCounter Constructor

National Instruments recommends that you use a version of the DAQCounter constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQCounter(string, uint, DAQMeasurementType) | Initializes a new instance of the DAQCounter class. |
| DAQCounter(string, uint, DAQMeasurementType, double) | Initializes a new instance of the DAQCounter class. |
| DAQCounter(string, uint, string) | Initializes a new instance of the DAQCounter class. |
| DAQCounter(string, uint, string, double) | Initializes a new instance of the DAQCounter class. |

#### Fields

| Name | Description |
| --- | --- |
| DefaultTerminal | Indicates that the DAQmx default terminal for this counter will be used. |

#### Properties

| Name | Description |
| --- | --- |
| Counter | Gets the counter channel number. |
| DataTask | Gets the type of task the counter performs (frequency measurement, period measurement, count up/down, or position measurement). |
| InitialValue | Gets or sets the initial value of the counter channel. |

#### Methods

| Name | Description |
| --- | --- |
| Downcast() | Casts DAQCounter to a more specific type. |
| SetCounterIndex(uint) | Sets the index value of the counter. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountercountmode.html language=enus -->
## TOPIC 02311: DAQCounterCountMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountercountmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountercountmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode of the count direction. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCounterCountModeMembersNameValueDescriptionUp10128Increments the counter. Down10124Decrements the counter. ExternallyControlled10326The state of a digital line controls the cou

### DAQCounterCountMode Enumeration

Specifies the mode of the count direction.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCounterCountMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Up | 10128 | Increments the counter. |
| Down | 10124 | Decrements the counter. |
| ExternallyControlled | 10326 | The state of a digital line controls the count direction. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounterdecoding.html language=enus -->
## TOPIC 02312: DAQCounterDecoding Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounterdecoding.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounterdecoding.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used to count and interpret the pulses the encoder generates on signal A and signal B. Decoding1X, Decoding2X, and Decoding4X are valid for quadrature encoders only. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCounterDecodingMembersNameValueD

### DAQCounterDecoding Enumeration

Specifies the method used to count and interpret the pulses the encoder generates on signal A and signal B. **Decoding1X**, **Decoding2X**, and **Decoding4X** are valid for quadrature encoders only.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCounterDecoding

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Decoding1X | 10090 | If signal A leads signal B, counts the rising edges of signal A. If signal B leads signal A, counts the falling edges of signal A. |
| Decoding2X | 10091 | Counts the rising and falling edges of signal A. |
| Decoding4X | 10092 | Counts the rising and falling edges of signal A and signal B. |
| DecodingPulseCounting | 10313 | Increments the count on rising edges of signal A. Decrements the count on rising edges of signal B. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html language=enus -->
## TOPIC 02313: DAQCounterEdge Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode the counter uses to count the edge. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCounterEdgeMembersNameValueDescriptionFalling10171The counter measures the time from one falling edge to the next falling edge. Rising10280The counter measures the

### DAQCounterEdge Enumeration

Specifies the mode the counter uses to count the edge.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCounterEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Falling | 10171 | The counter measures the time from one falling edge to the next falling edge. |
| Rising | 10280 | The counter measures the time from one rising edge to the next rising edge. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html language=enus -->
## TOPIC 02314: DAQCounterInput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQCounterInput class. Derives fromDAQSectionTypeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQCounterInput : DAQSectionType

### DAQCounterInput Class

Initializes a new instance of the DAQCounterInput class.

#### Derives from

- DAQSectionType

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQCounterInput : DAQSectionType

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html language=enus -->
## TOPIC 02315: DAQCounterOutput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQCounterOutput class. Derives fromDAQSectionTypeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQCounterOutput : DAQSectionType

### DAQCounterOutput Class

Initializes a new instance of the DAQCounterOutput class.

#### Derives from

- DAQSectionType

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQCounterOutput : DAQSectionType

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounter__daqcounter-out.html language=enus -->
## TOPIC 02316: AddCounter(DAQCounter, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounter__daqcounter-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounter__daqcounter-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQCounter to the Counter section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCounter(DAQCounter counter, out Error error)ParametersNameTypeDescriptioncounterDAQCounterThe DAQCounter to add.errorout ErrorReturns an NationalInstruments.VeriStan

### AddCounter(DAQCounter, out Error)

Adds the specified [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) to the **Counter** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCounter(DAQCounter counter, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| counter | DAQCounter | The DAQCounter to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) was added successfully.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounter__daqcounter.html language=enus -->
## TOPIC 02317: AddCounter(DAQCounter)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounter__daqcounter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounter__daqcounter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQCounter to the Counter section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCounter(DAQCounter counter)ParametersNameTypeDescriptioncounterDAQCounterThe DAQCounter to add.Returnstrue if the DAQCounter was added successfully.

### AddCounter(DAQCounter)

Adds the specified [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) to the **Counter** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCounter(DAQCounter counter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| counter | DAQCounter | The DAQCounter to add. |

#### Returns

true if the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) was added successfully.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounterinput__daqcounterinput-out.html language=enus -->
## TOPIC 02318: AddCounterInput(DAQCounterInput, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounterinput__daqcounterinput-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounterinput__daqcounterinput-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQCounterInput to the Counter section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCounterInput(DAQCounterInput counter, out Error error)ParametersNameTypeDescriptioncounterDAQCounterInputThe DAQCounter to add.errorout ErrorReturns an National

### AddCounterInput(DAQCounterInput, out Error)

Adds the specified [DAQCounterInput](nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html) to the **Counter** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCounterInput(DAQCounterInput counter, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| counter | DAQCounterInput | The DAQCounter to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) was added successfully.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounterinput__daqcounterinput.html language=enus -->
## TOPIC 02319: AddCounterInput(DAQCounterInput)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounterinput__daqcounterinput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounterinput__daqcounterinput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQCounterInput to the Counter section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCounterInput(DAQCounterInput counter)ParametersNameTypeDescriptioncounterDAQCounterInputThe DAQCounter to add.Returnstrue if the DAQCounter was added successful

### AddCounterInput(DAQCounterInput)

Adds the specified [DAQCounterInput](nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html) to the **Counter** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCounterInput(DAQCounterInput counter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| counter | DAQCounterInput | The DAQCounter to add. |

#### Returns

true if the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) was added successfully.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounteroutput__daqcounteroutput-out.html language=enus -->
## TOPIC 02320: AddCounterOutput(DAQCounterOutput, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounteroutput__daqcounteroutput-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounteroutput__daqcounteroutput-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQCounterOutput to the Counter section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCounterOutput(DAQCounterOutput counter, out Error error)ParametersNameTypeDescriptioncounterDAQCounterOutputThe DAQCounter to add.errorout ErrorReturns an Nati

### AddCounterOutput(DAQCounterOutput, out Error)

Adds the specified [DAQCounterOutput](nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html) to the **Counter** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCounterOutput(DAQCounterOutput counter, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| counter | DAQCounterOutput | The DAQCounter to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) was added successfully.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounteroutput__daqcounteroutput.html language=enus -->
## TOPIC 02321: AddCounterOutput(DAQCounterOutput)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounteroutput__daqcounteroutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-addcounteroutput__daqcounteroutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQCounterOutput to the Counter section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCounterOutput(DAQCounterOutput counter)ParametersNameTypeDescriptioncounterDAQCounterOutputThe DAQCounter to add.Returnstrue if the DAQCounter was added succes

### AddCounterOutput(DAQCounterOutput)

Adds the specified [DAQCounterOutput](nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html) to the **Counter** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCounterOutput(DAQCounterOutput counter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| counter | DAQCounterOutput | The DAQCounter to add. |

#### Returns

true if the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) was added successfully.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounterinputs.html language=enus -->
## TOPIC 02322: GetCounterInputs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounterinputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounterinputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQCounterInput elements from the current DAQCounters section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterInput[] GetCounterInputs()RemarksModifications you make to the contents of this list apply to the system definition. Howev

### GetCounterInputs()

Gets an array that contains the [DAQCounterInput](nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html) elements from the current [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterInput](nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html)[] GetCounterInputs()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQCounterInput](nationalinstruments-veristand-systemdefinitionapi-daqcounterinput.html) elements from the current [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) section.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounterlist.html language=enus -->
## TOPIC 02323: GetCounterList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounterlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounterlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQCounter elements from the current DAQCounters section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounter[] GetCounterList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifica

### GetCounterList()

Gets an array that contains the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) elements from the current [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html)[] GetCounterList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) elements from the current [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) section.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounteroutputs.html language=enus -->
## TOPIC 02324: GetCounterOutputs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounteroutputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters-getcounteroutputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQCounterOutput elements from the current DAQCounters section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterOutput[] GetCounterOutputs()RemarksModifications you make to the contents of this list apply to the system definition. Ho

### GetCounterOutputs()

Gets an array that contains the [DAQCounterOutput](nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html) elements from the current [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterOutput](nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html)[] GetCounterOutputs()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQCounterOutput](nationalinstruments-veristand-systemdefinitionapi-daqcounteroutput.html) elements from the current [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) section.

Parent topic:

DAQCounters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounters.html language=enus -->
## TOPIC 02325: DAQCounters Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Counter section under a DAQDevice, which contains all DAQCounter channels you add for the device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQCounters : SectionRemarksUse the members of this class to add counter channels or to get

### DAQCounters Class

Represents a **Counter** section under a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html), which contains all [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) channels you add for the device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQCounters : Section

#### Remarks

Use the members of this class to add counter channels or to get a list of existing counter channels.

**Accessing this Class**

- [CreateCounters(out Error)](nationalinstruments-veristand-systemdefinitionapi-daqdevice-createcounters__out.html)
- [GetCounterSection](nationalinstruments-veristand-systemdefinitionapi-daqdevice-getcountersection.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddCounter(DAQCounter) | Adds the specified DAQCounter to the Counter section. |
| AddCounter(DAQCounter, out Error) | Adds the specified DAQCounter to the Counter section. |
| AddCounterInput(DAQCounterInput) | Adds the specified DAQCounterInput to the Counter section. |
| AddCounterInput(DAQCounterInput, out Error) | Adds the specified DAQCounterInput to the Counter section. |
| AddCounterOutput(DAQCounterOutput) | Adds the specified DAQCounterOutput to the Counter section. |
| AddCounterOutput(DAQCounterOutput, out Error) | Adds the specified DAQCounterOutput to the Counter section. |
| GetCounterInputs() | Gets an array that contains the DAQCounterInput elements from the current DAQCounters section. |
| GetCounterList() | Gets an array that contains the DAQCounter elements from the current DAQCounters section. |
| GetCounterOutputs() | Gets an array that contains the DAQCounterOutput elements from the current DAQCounters section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountertype.html language=enus -->
## TOPIC 02326: DAQCounterType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of task the DAQ counter performs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQCounterTypeMembersNameValueDescriptionFrequencyMeasurement0Measures the frequency in Hz of a signal connected to a channel. PeriodMeasurementMeasures the period in se

### DAQCounterType Enumeration

Specifies the type of task the DAQ counter performs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCounterType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FrequencyMeasurement | 0 | Measures the frequency in Hz of a signal connected to a channel. |
| PeriodMeasurement |  | Measures the period in seconds of a signal connected to a channel. |
| CountUpDown |  | Counts the rising or falling edges. |
| PositionMeasurement |  | Measures position with quadrature encoders. A quadrature encoder can have up to three channels- channels A, B, and Z. |
| Other |  | Measurement Type introduced after NI VeriStand 2011 SP1. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcounterzindexmode.html language=enus -->
## TOPIC 02327: DAQCounterZIndexMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcounterzindexmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcounterzindexmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than AHighBHigh. When signal Z transitions to high and how long it st

### DAQCounterZIndexMode Enumeration

Specifies the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than **AHighBHigh**. When signal Z transitions to high and how long it stays high varies from encoder to encoder. Refer to the documentation for the encoder to determine the timing of signal Z with respect to signal A and signal B.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQCounterZIndexMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AHighBHigh | 10040 | Resets the measurement when signal A and signal B are high. |
| AHighBLow | 10041 | Resets the measurement when signal A is high and signal B is low. |
| ALowBHigh | 10042 | Resets the measurement when signal A is low and signal B high. |
| ALowBLow | 10043 | Resets the measurement when signal A and signal B are low. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-countdirection.html language=enus -->
## TOPIC 02328: CountDirection

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-countdirection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-countdirection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the direction of the count (up, down, or externally controlled). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterCountMode CountDirection { get; set; }ReturnsAn enumeration value of DAQCounterCountMode.

### CountDirection

Gets or sets the direction of the count (up, down, or externally controlled).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterCountMode](nationalinstruments-veristand-systemdefinitionapi-daqcountercountmode.html) CountDirection { get; set; }

#### Returns

An enumeration value of [DAQCounterCountMode](nationalinstruments-veristand-systemdefinitionapi-daqcountercountmode.html).

Parent topic:

DAQCountUpDown Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-daqcountupdown__string-string-uint-double-daqcountercountmode-daqcounteredge-basenode.html language=enus -->
## TOPIC 02329: DAQCountUpDown(string, string, uint, double, DAQCounterCountMode, DAQCounterEdge, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-daqcountupdown__string-string-uint-double-daqcountercountmode-daqcounteredge-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-daqcountupdown__string-string-uint-double-daqcountercountmode-daqcounteredge-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQCountUpDown with the specified name, description, and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCountUpDown(string Name, string Description, uint Index, double DefaultValue, DAQCounterCountMode CountDirection, DAQCount

### DAQCountUpDown(string, string, uint, double, DAQCounterCountMode, DAQCounterEdge, BaseNode)

Initializes a new instance of [DAQCountUpDown](nationalinstruments-veristand-systemdefinitionapi-daqcountupdown.html) with the specified name, description, and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQCountUpDown(string Name, string Description, uint Index, double DefaultValue, DAQCounterCountMode CountDirection, DAQCounterEdge Edge, BaseNode ResetVariable)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |
| Description | string | The description of the channel. |
| Index | uint | The index value of the channel. |
| DefaultValue | double | The initial value of the channel. |
| CountDirection | DAQCounterCountMode | The direction of the count (up, down, or externally controlled). |
| Edge | DAQCounterEdge | The edge on which to count (rising or falling). |
| ResetVariable | BaseNode | The channel whose value the counter must reach before it resets. |

Parent topic:

DAQCountUpDown Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-edge.html language=enus -->
## TOPIC 02330: Edge

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-edge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-edge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the edge on which to count (rising or falling). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterEdge Edge { get; set; }ReturnsAn enumeration value of DAQCounterEdge.

### Edge

Gets or sets the edge on which to count (rising or falling).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterEdge](nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html) Edge { get; set; }

#### Returns

An enumeration value of [DAQCounterEdge](nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html).

Parent topic:

DAQCountUpDown Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-inputterminal.html language=enus -->
## TOPIC 02331: InputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-inputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string InputTerminal { get; set; }

### InputTerminal

Gets or sets the input terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string InputTerminal { get; set; }

Parent topic:

DAQCountUpDown Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-resetvariable.html language=enus -->
## TOPIC 02332: ResetVariable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-resetvariable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountupdown-resetvariable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel whose value the counter must reach before it resets. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode ResetVariable { get; set; }ReturnsA BaseNode reference to the channel.

### ResetVariable

Gets or sets the channel whose value the counter must reach before it resets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) ResetVariable { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

DAQCountUpDown Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqcountupdown.html language=enus -->
## TOPIC 02333: DAQCountUpDown Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqcountupdown.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqcountupdown.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQCounter channel with the count up/down task type. Derives fromDAQCounterSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQCountUpDown : DAQCounterRemarksUse the members of this class to get or set set the count direction, the edge on which to count, an

### DAQCountUpDown Class

Represents a [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) channel with the count up/down task type.

#### Derives from

- DAQCounter

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQCountUpDown : DAQCounter

#### Remarks

Use the members of this class to get or set set the count direction, the edge on which to count, and the value at which the counter resets.

**Accessing this Class**

- DAQCountUpDown Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQCountUpDown(string, string, uint, double, DAQCounterCountMode, DAQCounterEdge, BaseNode) | Initializes a new instance of DAQCountUpDown with the specified name, description, and configuration. |

#### Properties

| Name | Description |
| --- | --- |
| CountDirection | Gets or sets the direction of the count (up, down, or externally controlled). |
| Edge | Gets or sets the edge on which to count (rising or falling). |
| InputTerminal | Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |
| ResetVariable | Gets or sets the channel whose value the counter must reach before it resets. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdatachanneltype.html language=enus -->
## TOPIC 02334: DAQDataChannelType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdatachanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdatachanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of data channel in a DAQ measurement DAQSectionType section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQDataChannelTypeMembersNameValueDescriptionFrequencyFrequency channel. DutyCycleDuty cycle channel.

### DAQDataChannelType Enumeration

Specifies the type of data channel in a DAQ measurement [DAQSectionType](nationalinstruments-veristand-systemdefinitionapi-daqsectiontype.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQDataChannelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Frequency |  | Frequency channel. |
| DutyCycle |  | Duty cycle channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-backplanereferenceclock.html language=enus -->
## TOPIC 02335: BackplaneReferenceClock

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-backplanereferenceclock.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-backplanereferenceclock.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the DAQDevice synchronizes its timing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic PXIBackplaneReferenceClock BackplaneReferenceClock { get; set; }ReturnsAn enumeration of PXIBackplaneReferenceCl

### BackplaneReferenceClock

Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) synchronizes its timing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [PXIBackplaneReferenceClock](nationalinstruments-veristand-systemdefinitionapi-pxibackplanereferenceclock.html) BackplaneReferenceClock { get; set; }

#### Returns

An enumeration of [PXIBackplaneReferenceClock](nationalinstruments-veristand-systemdefinitionapi-pxibackplanereferenceclock.html). If the device or its chassis do not support reference clock synchronization, select None or Automatic.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out-samplemode.html language=enus -->
## TOPIC 02336: CreateAnalogInputs(out DAQAnalogInputs, SampleMode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out-samplemode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out-samplemode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateAnalogInputs(out DAQAnalogInp

### CreateAnalogInputs(out DAQAnalogInputs, SampleMode)

Creates a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateAnalogInputs(out DAQAnalogInputs analogInputs, SampleMode mode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| analogInputs | out DAQAnalogInputs | The new or existing DAQAnalogInputs object. |
| mode | SampleMode | The mode of the acquisition. |

#### Returns

true if [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) was added successfully. false if [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out.1.html language=enus -->
## TOPIC 02337: CreateAnalogInputs(out DAQAnalogInputs)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateAnalogInputs(out DAQAnalogInp

### CreateAnalogInputs(out DAQAnalogInputs)

Creates a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateAnalogInputs(out DAQAnalogInputs analogInputs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| analogInputs | out DAQAnalogInputs | The new or existing DAQAnalogInputs object. |

#### Returns

true if [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) was added successfully. false if [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out.html language=enus -->
## TOPIC 02338: CreateAnalogInputs(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInputs CreateAnalogInputs(out E

### CreateAnalogInputs(out Error)

Creates a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) CreateAnalogInputs(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new or existing [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__samplemode-out.html language=enus -->
## TOPIC 02339: CreateAnalogInputs(SampleMode, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__samplemode-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanaloginputs__samplemode-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInputs CreateAnalogInputs(Sampl

### CreateAnalogInputs(SampleMode, out Error)

Creates a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) CreateAnalogInputs(SampleMode mode, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| mode | SampleMode | The mode of the acquisition. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new or existing [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanalogoutputs__out.1.html language=enus -->
## TOPIC 02340: CreateAnalogOutputs(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanalogoutputs__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanalogoutputs__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQAnalogOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogOutputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutputs CreateAnalogOutputs(o

### CreateAnalogOutputs(out Error)

Creates a [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) CreateAnalogOutputs(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new or existing [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanalogoutputs__out.html language=enus -->
## TOPIC 02341: CreateAnalogOutputs(out DAQAnalogOutputs)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanalogoutputs__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createanalogoutputs__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQAnalogOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogOutputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateAnalogOutputs(out DAQAnalog

### CreateAnalogOutputs(out DAQAnalogOutputs)

Creates a [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateAnalogOutputs(out DAQAnalogOutputs analogOutputs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| analogOutputs | out DAQAnalogOutputs | The new or existing DAQAnalogOutputs object. |

#### Returns

true if [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) was added successfully. false if [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createcounters__out.1.html language=enus -->
## TOPIC 02342: CreateCounters(out DAQCounters)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createcounters__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createcounters__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQCounters object, if one does not already exist, and adds it to the DAQDevice. If a DAQCounters object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateCounters(out DAQCounters counters)Par

### CreateCounters(out DAQCounters)

Creates a [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateCounters(out DAQCounters counters)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| counters | out DAQCounters | The new or existing DAQCounters object. |

#### Returns

true if [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) was added successfully. false if [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createcounters__out.html language=enus -->
## TOPIC 02343: CreateCounters(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createcounters__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createcounters__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQCounters object, if one does not already exist, and adds it to the DAQDevice. If a DAQCounters object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounters CreateCounters(out Error error)Param

### CreateCounters(out Error)

Creates a [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) CreateCounters(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new or existing [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitalinputs__out.1.html language=enus -->
## TOPIC 02344: CreateDigitalInputs(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitalinputs__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitalinputs__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQDigitalInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalInputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInputs CreateDigitalInputs(o

### CreateDigitalInputs(out Error)

Creates a [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) CreateDigitalInputs(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new or existing [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitalinputs__out.html language=enus -->
## TOPIC 02345: CreateDigitalInputs(out DAQDigitalInputs)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitalinputs__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitalinputs__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQDigitalInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalInputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateDigitalInputs(out DAQDigita

### CreateDigitalInputs(out DAQDigitalInputs)

Creates a [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateDigitalInputs(out DAQDigitalInputs digitalInputs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| digitalInputs | out DAQDigitalInputs | The new or existing DAQDigitalInputs object. |

#### Returns

true if [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) was added successfully. false if [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitaloutputs__out.1.html language=enus -->
## TOPIC 02346: CreateDigitalOutputs(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitaloutputs__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitaloutputs__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQDigitalOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalOutputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutputs CreateDigitalOutpu

### CreateDigitalOutputs(out Error)

Creates a [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) CreateDigitalOutputs(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) was added successfully. false if [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitaloutputs__out.html language=enus -->
## TOPIC 02347: CreateDigitalOutputs(out DAQDigitalOutputs)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitaloutputs__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitaloutputs__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQDigitalOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalOutputs object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateDigitalOutputs(out DAQDig

### CreateDigitalOutputs(out DAQDigitalOutputs)

Creates a [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateDigitalOutputs(out DAQDigitalOutputs digitalOutputs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| digitalOutputs | out DAQDigitalOutputs | The new or existing DAQDigitalOutputs object. |

#### Returns

true if [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) was added successfully. false if [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createinternalchannels__out.1.html language=enus -->
## TOPIC 02348: CreateInternalChannels(out DAQInternalChannels)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createinternalchannels__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createinternalchannels__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQInternalChannels object, if one does not already exist, and adds it to the DAQDevice. If a DAQInternalChannels object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateInternalChannels(out

### CreateInternalChannels(out DAQInternalChannels)

Creates a [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateInternalChannels(out DAQInternalChannels internalChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| internalChannels | out DAQInternalChannels | The new or existing DAQInternalChannels object. |

#### Returns

true if [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) was added successfully. false if [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createinternalchannels__out.html language=enus -->
## TOPIC 02349: CreateInternalChannels(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createinternalchannels__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createinternalchannels__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a DAQInternalChannels object, if one does not already exist, and adds it to the DAQDevice. If a DAQInternalChannels object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQInternalChannels CreateIntern

### CreateInternalChannels(out Error)

Creates a [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) CreateInternalChannels(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new or existing [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createscxichassis__out.1.html language=enus -->
## TOPIC 02350: CreateSCXIChassis(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createscxichassis__out.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createscxichassis__out.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SCXIChassis object, if one does not already exist, and adds it to the DAQDevice. If a SCXIChassis object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXIChassis CreateSCXIChassis(out Error error)Pa

### CreateSCXIChassis(out Error)

Creates a [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) CreateSCXIChassis(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new or existing [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-createscxichassis__out.html language=enus -->
## TOPIC 02351: CreateSCXIChassis(out SCXIChassis)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-createscxichassis__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-createscxichassis__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SCXIChassis object, if one does not already exist, and adds it to the DAQDevice. If a SCXIChassis object already exists, this method returns a reference to this object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CreateSCXIChassis(out SCXIChassis scxiChass

### CreateSCXIChassis(out SCXIChassis)

Creates a [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) object, if one does not already exist, and adds it to the [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html). If a [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) object already exists, this method returns a reference to this object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CreateSCXIChassis(out SCXIChassis scxiChassis)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scxiChassis | out SCXIChassis | The new or existing SCXIChassis object. |

#### Returns

true if [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) was added successfully. false if [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) already exists.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqconversionrateoption.html language=enus -->
## TOPIC 02352: DAQConversionRateOption

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqconversionrateoption.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqconversionrateoption.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the rate used to run the analog-digital converters on the DAQ device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQConversionRate DAQConversionRateOption { get; set; }ReturnsAn enumeration value of DAQConversionRate.

### DAQConversionRateOption

Gets or sets the rate used to run the analog-digital converters on the DAQ device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQConversionRate](nationalinstruments-veristand-systemdefinitionapi-daqconversionrate.html) DAQConversionRateOption { get; set; }

#### Returns

An enumeration value of [DAQConversionRate](nationalinstruments-veristand-systemdefinitionapi-daqconversionrate.html).

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration-uint-uint-uint-uint-ushort-daqcountertype_arr1-uint.html language=enus -->
## TOPIC 02353: DAQDevice(string, string, DAQDeviceInputConfiguration, uint, uint, uint, uint, ushort, DAQCounterType[], uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration-uint-uint-uint-uint-ushort-daqcountertype_arr1-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration-uint-uint-uint-uint-ushort-daqcountertype_arr1-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQDevice with the specified name, description, input configuration, number of channels, port width, counter types, and number of internal channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDevice(string Name, string Description, DAQDe

### DAQDevice(string, string, DAQDeviceInputConfiguration, uint, uint, uint, uint, ushort, DAQCounterType[], uint)

Initializes a new instance of [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) with the specified name, description, input configuration, number of channels, port width, counter types, and number of internal channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDevice(string Name, string Description, DAQDeviceInputConfiguration InputConfiguration, uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, ushort PortWidth, DAQCounterType[] CounterTypes, uint NumInternalChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the device. |
| Description | string | The description of the device. |
| InputConfiguration | DAQDeviceInputConfiguration | The input terminal configuration. |
| NumAIChannels | uint | The number of analog input channels. |
| NumAOChannels | uint | The number of analog output channels. |
| NumDIChannels | uint | The number of digital input channels. |
| NumDOChannels | uint | The number of digital output channels. |
| PortWidth | ushort | The total number of lines per port. |
| CounterTypes | DAQCounterType[] | The types of tasks the DAQ counter channels perform. |
| NumInternalChannels | uint | The number of internal channels. |

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration-uint-uint-uint-uint-ushort.html language=enus -->
## TOPIC 02354: DAQDevice(string, string, DAQDeviceInputConfiguration, uint, uint, uint, uint, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration-uint-uint-uint-uint-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration-uint-uint-uint-uint-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQDevice with the specified name, description, input configuration, number of channels, and port width. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDevice(string Name, string Description, DAQDeviceInputConfiguration InputConfiguration, u

### DAQDevice(string, string, DAQDeviceInputConfiguration, uint, uint, uint, uint, ushort)

Initializes a new instance of [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) with the specified name, description, input configuration, number of channels, and port width.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDevice(string Name, string Description, DAQDeviceInputConfiguration InputConfiguration, uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, ushort PortWidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the device. |
| Description | string | The description of the device. |
| InputConfiguration | DAQDeviceInputConfiguration | The input terminal configuration. |
| NumAIChannels | uint | The number of analog input channels. |
| NumAOChannels | uint | The number of analog output channels. |
| NumDIChannels | uint | The number of digital input channels. |
| NumDOChannels | uint | The number of digital output channels. |
| PortWidth | ushort | The total number of lines per port. |

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration.html language=enus -->
## TOPIC 02355: DAQDevice(string, string, DAQDeviceInputConfiguration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-daqdevice__string-string-daqdeviceinputconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQDevice with the specified name, description, and input configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDevice(string Name, string Description, DAQDeviceInputConfiguration InputConfiguration)ParametersNameTypeDescriptionNames

### DAQDevice(string, string, DAQDeviceInputConfiguration)

Initializes a new instance of [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) with the specified name, description, and input configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDevice(string Name, string Description, DAQDeviceInputConfiguration InputConfiguration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the device. |
| Description | string | The description of the device. |
| InputConfiguration | DAQDeviceInputConfiguration | The input terminal configuration. |

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanaloginputsection.html language=enus -->
## TOPIC 02356: GetAnalogInputSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanaloginputsection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanaloginputsection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQAnalogInputs class, which you can use to add or get a list of analog input channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogInputs GetAnalogInputSection()ReturnsA DAQAnalogInputs object.

### GetAnalogInputSection()

Gets the [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) class, which you can use to add or get a list of analog input channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) GetAnalogInputSection()

#### Returns

A [DAQAnalogInputs](nationalinstruments-veristand-systemdefinitionapi-daqanaloginputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanalogoutputsection.html language=enus -->
## TOPIC 02357: GetAnalogOutputSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanalogoutputsection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-getanalogoutputsection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQAnalogOutputs class, which you can use to add or get a list of analog output channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQAnalogOutputs GetAnalogOutputSection()ReturnsA DAQAnalogOutputs object.

### GetAnalogOutputSection()

Gets the [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) class, which you can use to add or get a list of analog output channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) GetAnalogOutputSection()

#### Returns

A [DAQAnalogOutputs](nationalinstruments-veristand-systemdefinitionapi-daqanalogoutputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-getcountersection.html language=enus -->
## TOPIC 02358: GetCounterSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-getcountersection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-getcountersection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQCounters class, which you can use to add or get a list of counters. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounters GetCounterSection()ReturnsA DAQCounters object.

### GetCounterSection()

Gets the [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) class, which you can use to add or get a list of counters.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) GetCounterSection()

#### Returns

A [DAQCounters](nationalinstruments-veristand-systemdefinitionapi-daqcounters.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-getdigitalinputsection.html language=enus -->
## TOPIC 02359: GetDigitalInputSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-getdigitalinputsection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-getdigitalinputsection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQDigitalInputs class, which you can use to add or get a list of digital input channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInputs GetDigitalInputSection()ReturnsA DAQDigitalInputs object.

### GetDigitalInputSection()

Gets the [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) class, which you can use to add or get a list of digital input channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) GetDigitalInputSection()

#### Returns

A [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-getdigitaloutputsection.html language=enus -->
## TOPIC 02360: GetDigitalOutputSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-getdigitaloutputsection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-getdigitaloutputsection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQDigitalOutputs class, which you can use to add or get a list of DAQ digital output ports. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutputs GetDigitalOutputSection()ReturnsA DAQDigitalOutputs object.

### GetDigitalOutputSection()

Gets the [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) class, which you can use to add or get a list of DAQ digital output ports.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) GetDigitalOutputSection()

#### Returns

A [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-getinternalchannelssection.html language=enus -->
## TOPIC 02361: GetInternalChannelsSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-getinternalchannelssection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-getinternalchannelssection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DAQInternalChannels class, which you can use to add or get a list of internal channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQInternalChannels GetInternalChannelsSection()ReturnsA DAQInternalChannels object.

### GetInternalChannelsSection()

Gets the [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) class, which you can use to add or get a list of internal channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) GetInternalChannelsSection()

#### Returns

A [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-getscxichassissection.html language=enus -->
## TOPIC 02362: GetSCXIChassisSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-getscxichassissection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-getscxichassissection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the SCXIChassis class, which you can use to add or get a list of SCXI modules. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SCXIChassis GetSCXIChassisSection()ReturnsAn SCXIChassis object.

### GetSCXIChassisSection()

Get the [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) class, which you can use to add or get a list of SCXI modules.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) GetSCXIChassisSection()

#### Returns

An [SCXIChassis](nationalinstruments-veristand-systemdefinitionapi-scxichassis.html) object.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-inputconfiguration.html language=enus -->
## TOPIC 02363: InputConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-inputconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-inputconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal configuration applied to device channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDeviceInputConfiguration InputConfiguration { get; set; }ReturnsAn enumeration value of DAQDeviceInputConfiguration.

### InputConfiguration

Gets or sets the input terminal configuration applied to device channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDeviceInputConfiguration](nationalinstruments-veristand-systemdefinitionapi-daqdeviceinputconfiguration.html) InputConfiguration { get; set; }

#### Returns

An enumeration value of [DAQDeviceInputConfiguration](nationalinstruments-veristand-systemdefinitionapi-daqdeviceinputconfiguration.html).

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint-daqcountertype_arr1-uint-out.html language=enus -->
## TOPIC 02364: PopulateDevice(uint, uint, uint, uint, uint, DAQCounterType[], uint, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint-daqcountertype_arr1-uint-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint-daqcountertype_arr1-uint-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all existing channels from the DAQ device and repopulates the device with the specified channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void PopulateDevice(uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, uint PortWidth, DAQCo

### PopulateDevice(uint, uint, uint, uint, uint, DAQCounterType[], uint, out Error)

Removes all existing channels from the DAQ device and repopulates the device with the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void PopulateDevice(uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, uint PortWidth, DAQCounterType[] CounterTypes, uint NumInternalChannels, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| NumAIChannels | uint | The number of analog input channels. |
| NumAOChannels | uint | The number of analog output channels. |
| NumDIChannels | uint | The number of digital input channels. |
| NumDOChannels | uint | The number of digital output channels. |
| PortWidth | uint | The total number of lines per port. |
| CounterTypes | DAQCounterType[] | The types of tasks the DAQ counter channels perform. |
| NumInternalChannels | uint | The number of internal channels. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint-daqcountertype_arr1-uint.html language=enus -->
## TOPIC 02365: PopulateDevice(uint, uint, uint, uint, uint, DAQCounterType[], uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint-daqcountertype_arr1-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint-daqcountertype_arr1-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all existing channels from the DAQ device and repopulates the device with the specified channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void PopulateDevice(uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, uint PortWidth, DAQCo

### PopulateDevice(uint, uint, uint, uint, uint, DAQCounterType[], uint)

Removes all existing channels from the DAQ device and repopulates the device with the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void PopulateDevice(uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, uint PortWidth, DAQCounterType[] CounterTypes, uint NumInternalChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| NumAIChannels | uint | The number of analog input channels. |
| NumAOChannels | uint | The number of analog output channels. |
| NumDIChannels | uint | The number of digital input channels. |
| NumDOChannels | uint | The number of digital output channels. |
| PortWidth | uint | The total number of lines per port. |
| CounterTypes | DAQCounterType[] | The types of tasks the DAQ counter channels perform. |
| NumInternalChannels | uint | The number of internal channels. |

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint.html language=enus -->
## TOPIC 02366: PopulateDevice(uint, uint, uint, uint, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-populatedevice__uint-uint-uint-uint-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all existing channels from the DAQ device and repopulates the device with the specified channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void PopulateDevice(uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, uint PortWidth)Parame

### PopulateDevice(uint, uint, uint, uint, uint)

Removes all existing channels from the DAQ device and repopulates the device with the specified channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void PopulateDevice(uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, uint PortWidth)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| NumAIChannels | uint | The number of analog input channels. |
| NumAOChannels | uint | The number of analog output channels. |
| NumDIChannels | uint | The number of digital input channels. |
| NumDOChannels | uint | The number of digital output channels. |
| PortWidth | uint | The total number of lines per port. |

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-portwidth.html language=enus -->
## TOPIC 02367: PortWidth

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-portwidth.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-portwidth.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the total number of lines per port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ushort PortWidth { get; set; }ReturnsThe port width.

### PortWidth

Gets or sets the total number of lines per port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ushort PortWidth { get; set; }

#### Returns

The port width.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-productcategory.html language=enus -->
## TOPIC 02368: ProductCategory

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-productcategory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-productcategory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Public, always writable version of DAQ Product Category. Unique identifier for each DAQ Product category. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ProductCategory { get; set; }

### ProductCategory

Public, always writable version of DAQ Product Category. Unique identifier for each DAQ Product category.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ProductCategory { get; set; }

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-productid.html language=enus -->
## TOPIC 02369: ProductID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-productid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-productid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Public, always writable version of DAQ Product ID DAQ Product ID is the unique numeric identifier for a DAQ device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ulong ProductID { get; set; }

### ProductID

Public, always writable version of DAQ Product ID DAQ Product ID is the unique numeric identifier for a DAQ device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong ProductID { get; set; }

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-productname.html language=enus -->
## TOPIC 02370: ProductName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-productname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-productname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Public, always writable version of DAQ Product Name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ProductName { get; set; }

### ProductName

Public, always writable version of DAQ Product Name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ProductName { get; set; }

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-turnoffhwtimedsinglepointai.html language=enus -->
## TOPIC 02371: TurnOffHWTimedSinglePointAI

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-turnoffhwtimedsinglepointai.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-turnoffhwtimedsinglepointai.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether hardware-timed single-point support is disabled for analog input tasks. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool TurnOffHWTimedSinglePointAI { get; set; }RemarksC Series devices, USB devices, and any other devices that include a hardware AI f

### TurnOffHWTimedSinglePointAI

Gets or sets whether hardware-timed single-point support is disabled for analog input tasks.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool TurnOffHWTimedSinglePointAI { get; set; }

#### Remarks

Note

C Series devices, USB devices, and any other devices that include a hardware AI filter do not support hardware-timed single-point sample mode.

Note

Enabling hardware-timed single-point support can drastically slow the Primary Control Loop rate.

#### Returns

true if hardware-timed single-point support is disabled. false if it is enabled.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice-turnoffhwtimedsinglepointao.html language=enus -->
## TOPIC 02372: TurnOffHWTimedSinglePointAO

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice-turnoffhwtimedsinglepointao.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice-turnoffhwtimedsinglepointao.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether hardware-timed single-point support is disabled for analog output tasks. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool TurnOffHWTimedSinglePointAO { get; set; }RemarksC Series devices, USB devices, and any other devices that include a hardware AI

### TurnOffHWTimedSinglePointAO

Gets or sets whether hardware-timed single-point support is disabled for analog output tasks.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool TurnOffHWTimedSinglePointAO { get; set; }

#### Remarks

Note

C Series devices, USB devices, and any other devices that include a hardware AI filter do not support hardware-timed single-point sample mode.

Note

Enabling hardware-timed single-point support can drastically slow the Primary Control Loop rate.

#### Returns

true if hardware-timed single-point support is disabled. false if it is enabled.

Parent topic:

DAQDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdevice.html language=enus -->
## TOPIC 02373: DAQDevice Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQDevice : SectionRemarksUse the members of this class to access channel sections and to configure device-level settings, such as port width and support for hardware-timed sing

### DAQDevice Class

Represents a DAQ device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQDevice : Section

#### Remarks

Use the members of this class to access channel sections and to configure device-level settings, such as port width and support for hardware-timed single-point sample mode.

**Accessing this Class**

- DAQDevice Constructor

DAQTimingDevice

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQDevice(string, string, DAQDeviceInputConfiguration) | Initializes a new instance of DAQDevice with the specified name, description, and input configuration. |
| DAQDevice(string, string, DAQDeviceInputConfiguration, uint, uint, uint, uint, ushort) | Initializes a new instance of DAQDevice with the specified name, description, input configuration, number of channels, and port width. |
| DAQDevice(string, string, DAQDeviceInputConfiguration, uint, uint, uint, uint, ushort, DAQCounterType[], uint) | Initializes a new instance of DAQDevice with the specified name, description, input configuration, number of channels, port width, counter types, and number of internal channels. |

#### Properties

| Name | Description |
| --- | --- |
| BackplaneReferenceClock | Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the DAQDevice synchronizes its timing. |
| DAQConversionRateOption | Gets or sets the rate used to run the analog-digital converters on the DAQ device. |
| InputConfiguration | Gets or sets the input terminal configuration applied to device channels. |
| PortWidth | Gets or sets the total number of lines per port. |
| ProductCategory | Public, always writable version of DAQ Product Category. Unique identifier for each DAQ Product category. |
| ProductID | Public, always writable version of DAQ Product ID DAQ Product ID is the unique numeric identifier for a DAQ device. |
| ProductName | Public, always writable version of DAQ Product Name. |
| TurnOffHWTimedSinglePointAI | Gets or sets whether hardware-timed single-point support is disabled for analog input tasks. |
| TurnOffHWTimedSinglePointAO | Gets or sets whether hardware-timed single-point support is disabled for analog output tasks. |

#### Methods

| Name | Description |
| --- | --- |
| CreateAnalogInputs(out DAQAnalogInputs, SampleMode) | Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. |
| CreateAnalogInputs(SampleMode, out Error) | Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. |
| CreateAnalogInputs(out DAQAnalogInputs) | Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. |
| CreateAnalogInputs(out Error) | Creates a DAQAnalogInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogInputs object already exists, this method returns a reference to this object. |
| CreateAnalogOutputs(out Error) | Creates a DAQAnalogOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogOutputs object already exists, this method returns a reference to this object. |
| CreateAnalogOutputs(out DAQAnalogOutputs) | Creates a DAQAnalogOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQAnalogOutputs object already exists, this method returns a reference to this object. |
| CreateCounters(out Error) | Creates a DAQCounters object, if one does not already exist, and adds it to the DAQDevice. If a DAQCounters object already exists, this method returns a reference to this object. |
| CreateCounters(out DAQCounters) | Creates a DAQCounters object, if one does not already exist, and adds it to the DAQDevice. If a DAQCounters object already exists, this method returns a reference to this object. |
| CreateDigitalInputs(out Error) | Creates a DAQDigitalInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalInputs object already exists, this method returns a reference to this object. |
| CreateDigitalInputs(out DAQDigitalInputs) | Creates a DAQDigitalInputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalInputs object already exists, this method returns a reference to this object. |
| CreateDigitalOutputs(out Error) | Creates a DAQDigitalOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalOutputs object already exists, this method returns a reference to this object. |
| CreateDigitalOutputs(out DAQDigitalOutputs) | Creates a DAQDigitalOutputs object, if one does not already exist, and adds it to the DAQDevice. If a DAQDigitalOutputs object already exists, this method returns a reference to this object. |
| CreateInternalChannels(out DAQInternalChannels) | Creates a DAQInternalChannels object, if one does not already exist, and adds it to the DAQDevice. If a DAQInternalChannels object already exists, this method returns a reference to this object. |
| CreateInternalChannels(out Error) | Creates a DAQInternalChannels object, if one does not already exist, and adds it to the DAQDevice. If a DAQInternalChannels object already exists, this method returns a reference to this object. |
| CreateSCXIChassis(out SCXIChassis) | Creates a SCXIChassis object, if one does not already exist, and adds it to the DAQDevice. If a SCXIChassis object already exists, this method returns a reference to this object. |
| CreateSCXIChassis(out Error) | Creates a SCXIChassis object, if one does not already exist, and adds it to the DAQDevice. If a SCXIChassis object already exists, this method returns a reference to this object. |
| GetAnalogInputSection() | Gets the DAQAnalogInputs class, which you can use to add or get a list of analog input channels. |
| GetAnalogOutputSection() | Gets the DAQAnalogOutputs class, which you can use to add or get a list of analog output channels. |
| GetCounterSection() | Gets the DAQCounters class, which you can use to add or get a list of counters. |
| GetDigitalInputSection() | Gets the DAQDigitalInputs class, which you can use to add or get a list of digital input channels. |
| GetDigitalOutputSection() | Gets the DAQDigitalOutputs class, which you can use to add or get a list of DAQ digital output ports. |
| GetInternalChannelsSection() | Gets the DAQInternalChannels class, which you can use to add or get a list of internal channels. |
| GetSCXIChassisSection() | Get the SCXIChassis class, which you can use to add or get a list of SCXI modules. |
| PopulateDevice(uint, uint, uint, uint, uint, DAQCounterType[], uint, out Error) | Removes all existing channels from the DAQ device and repopulates the device with the specified channels. |
| PopulateDevice(uint, uint, uint, uint, uint) | Removes all existing channels from the DAQ device and repopulates the device with the specified channels. |
| PopulateDevice(uint, uint, uint, uint, uint, DAQCounterType[], uint) | Removes all existing channels from the DAQ device and repopulates the device with the specified channels. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdeviceinputconfiguration.html language=enus -->
## TOPIC 02374: DAQDeviceInputConfiguration Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdeviceinputconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdeviceinputconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration to apply to the device channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQDeviceInputConfigurationMembersNameValueDescriptionDefault-1The default configuration of the DAQ device, or the configuration you specify in Me

### DAQDeviceInputConfiguration Enumeration

Specifies the input terminal configuration to apply to the device channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQDeviceInputConfiguration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Default | -1 | The default configuration of the DAQ device, or the configuration you specify in Measurement and Automation Explorer (MAX). |
| RSE | 10083 | The analog input channels are reference single-ended (RSE). A referenced single-ended (RSE) measurement system measures voltage with respect to the ground, which is directly connected to the measurement system ground. |
| NRSE | 10078 | The analog input channels are non-referenced single-ended (NRSE). In a NRSE measurements system, all measurements are still made with respect to a single-node analog input, AISENSE, but the potential at this node can vary with respect to the measurement system ground. |
| Differential | 10106 | The analog input channels are differential. A differential measurement system has neither of its inputs tied to a fixed reference, such as earth or building ground. A differential measurement system is similar to a floating signal source in that the measurement is made with respect to a floating ground that is different from the measurement system ground. Hand-held, battery-powered instruments and DAQ devices with instrumentation amplifiers are examples of differential measurement systems. This mode measures potential between two inputs and therefore reduces channel count by 2. |
| Pseudodifferential | 12529 | The analog input channels are pseudodifferential. A pseudodifferential measurement system combines some characteristics of a differential input channel and a referenced single-ended (RSE) input channel. Like a differential input channel, a pseudodifferential measurement system exposes both the positive and negative sides of the channel. You connect the positive and negative inputs to the respective outputs of the unit under test. The negative input is tied to system ground through a relatively small impedance. The impedance between the negative input and ground may include both resistive and capacitive components. The positive and negative sides of the input channel are separated by a larger impedance. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-bool-uint-uint.html language=enus -->
## TOPIC 02375: DAQDigitalInput(string, bool, uint, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-bool-uint-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-bool-uint-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQDigitalInput with the specified name and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInput(string Name, bool InitialValue, uint DigitalLine, uint PortNumber)ParametersNameTypeDescriptionNamestringThe name of the c

### DAQDigitalInput(string, bool, uint, uint)

Initializes a new instance of [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html) with the specified name and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalInput(string Name, bool InitialValue, uint DigitalLine, uint PortNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |
| InitialValue | bool | The initial value of the channel. |
| DigitalLine | uint | The digital line for the channel. |
| PortNumber | uint | The port to which the channel belongs. |

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-bool-daqmeasurementtype.html language=enus -->
## TOPIC 02376: DAQDigitalInput(string, uint, uint, bool, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-bool-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-bool-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInput(string name, uint digitalLine, uint portNumber, bool initialValue, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringThe name of t

### DAQDigitalInput(string, uint, uint, bool, DAQMeasurementType)

Initializes a new instance of the DAQDigitalInput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalInput(string name, uint digitalLine, uint portNumber, bool initialValue, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. |
| digitalLine | uint | The digital line number. |
| portNumber | uint | The digital port number. |
| initialValue | bool | The initial value of the digital input line. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-bool-string.html language=enus -->
## TOPIC 02377: DAQDigitalInput(string, uint, uint, bool, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-bool-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInput(string name, uint digitalLine, uint portNumber, bool initialValue, string pluginGUID)RemarksUse this constructor to create channels with a measurement typ

### DAQDigitalInput(string, uint, uint, bool, string)

Initializes a new instance of the DAQDigitalInput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalInput(string name, uint digitalLine, uint portNumber, bool initialValue, string pluginGUID)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. |
| digitalLine | uint | The digital line number. |
| portNumber | uint | The digital port number. |
| initialValue | bool | The initial value of the digital input line. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-daqmeasurementtype.html language=enus -->
## TOPIC 02378: DAQDigitalInput(string, uint, uint, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInput(string name, uint digitalLine, uint portNumber, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringThe name of the channel.digitalL

### DAQDigitalInput(string, uint, uint, DAQMeasurementType)

Initializes a new instance of the DAQDigitalInput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalInput(string name, uint digitalLine, uint portNumber, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. |
| digitalLine | uint | The digital line number. |
| portNumber | uint | The digital port number. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-string.html language=enus -->
## TOPIC 02379: DAQDigitalInput(string, uint, uint, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-daqdigitalinput__string-uint-uint-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalInput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInput(string name, uint digitalLine, uint portNumber, string pluginGUID)RemarksUse this constructor to create channels with a measurement type defined in a cust

### DAQDigitalInput(string, uint, uint, string)

Initializes a new instance of the DAQDigitalInput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalInput(string name, uint digitalLine, uint portNumber, string pluginGUID)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. |
| digitalLine | uint | The digital line number. |
| portNumber | uint | The digital port number. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-digitalline.html language=enus -->
## TOPIC 02380: DigitalLine

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-digitalline.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-digitalline.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the digital line for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint DigitalLine { get; set; }ReturnsThe digital line.

### DigitalLine

Gets or sets the digital line for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint DigitalLine { get; set; }

#### Returns

The digital line.

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-initalvalue.html language=enus -->
## TOPIC 02381: InitalValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-initalvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-initalvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the digital input channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool InitalValue { get; set; }ReturnsThe initial value.

### InitalValue

Gets or sets the initial value of the digital input channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InitalValue { get; set; }

#### Returns

The initial value.

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-isscxi.html language=enus -->
## TOPIC 02382: IsSCXI

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-isscxi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-isscxi.html
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

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-portnumber.html language=enus -->
## TOPIC 02383: PortNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-portnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput-portnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the port to which the channel belongs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PortNumber { get; set; }ReturnsThe port number.

### PortNumber

Gets or sets the port to which the channel belongs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PortNumber { get; set; }

#### Returns

The port number.

Parent topic:

DAQDigitalInput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html language=enus -->
## TOPIC 02384: DAQDigitalInput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ digital input channel. Derives fromDAQChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQDigitalInput : DAQChannelRemarksUse the members of this class to get and set properties of the channel such as the port it belongs to and its digital line.

### DAQDigitalInput Class

Represents a DAQ digital input channel.

#### Derives from

- DAQChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQDigitalInput : DAQChannel

#### Remarks

Use the members of this class to get and set properties of the channel such as the port it belongs to and its digital line.

**Accessing this Class**

- [GetDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitalinputs.html)
- DAQDigitalInput Constructor

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQDigitalInput(string, uint, uint, bool, DAQMeasurementType) | Initializes a new instance of the DAQDigitalInput class. |
| DAQDigitalInput(string, bool, uint, uint) | Initializes a new instance of DAQDigitalInput with the specified name and configuration. |
| DAQDigitalInput(string, uint, uint, DAQMeasurementType) | Initializes a new instance of the DAQDigitalInput class. |
| DAQDigitalInput(string, uint, uint, string) | Initializes a new instance of the DAQDigitalInput class. |
| DAQDigitalInput(string, uint, uint, bool, string) | Initializes a new instance of the DAQDigitalInput class. |

#### Properties

| Name | Description |
| --- | --- |
| DigitalLine | Gets or sets the digital line for the channel. |
| InitalValue | Gets or sets the initial value of the digital input channel. |
| IsSCXI | Gets whether the channel belongs to an SCXI module. |
| PortNumber | Gets or sets the port to which the channel belongs. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-adddioport__daqdioport-out.html language=enus -->
## TOPIC 02385: AddDIOPort(DAQDIOPort, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-adddioport__daqdioport-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-adddioport__daqdioport-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDIOPort to the Digital Input section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDIOPort(DAQDIOPort dioPort, out Error error)ParametersNameTypeDescriptiondioPortDAQDIOPortThe DIO port to add.errorout ErrorReturns an NationalInstruments.Veri

### AddDIOPort(DAQDIOPort, out Error)

Adds the specified [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) to the **Digital Input** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDIOPort(DAQDIOPort dioPort, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dioPort | DAQDIOPort | The DIO port to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the port was added successfully.

Parent topic:

DAQDigitalInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-adddioport__daqdioport.html language=enus -->
## TOPIC 02386: AddDIOPort(DAQDIOPort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-adddioport__daqdioport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-adddioport__daqdioport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDIOPort to the Digital Input section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDIOPort(DAQDIOPort dioPort)ParametersNameTypeDescriptiondioPortDAQDIOPortThe DIO port to add.Returnstrue if the port was added successfully.

### AddDIOPort(DAQDIOPort)

Adds the specified [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) to the **Digital Input** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDIOPort(DAQDIOPort dioPort)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dioPort | DAQDIOPort | The DIO port to add. |

#### Returns

true if the port was added successfully.

Parent topic:

DAQDigitalInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-getdioports.html language=enus -->
## TOPIC 02387: GetDIOPorts()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-getdioports.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-getdioports.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQDIOPort elements from the current DAQDigitalInputs section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDIOPort[] GetDIOPorts()RemarksModifications you make to the contents of this list apply to the system definition. However, modifi

### GetDIOPorts()

Gets an array that contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) elements from the current [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html)[] GetDIOPorts()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) elements from the current [DAQDigitalInputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html) section.

Parent topic:

DAQDigitalInputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html language=enus -->
## TOPIC 02388: DAQDigitalInputs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Digital Input section under a DAQDevice, which contains the DAQDIOPort ports for DAQDigitalInput channels. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQDigitalInputs : SectionRemarksUse the members of this class to add or get a lis

### DAQDigitalInputs Class

Represents a **Digital Input** section under a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html), which contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) ports for [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html) channels.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQDigitalInputs : Section

#### Remarks

Use the members of this class to add or get a list of existing DAQ DIO ports for the current device.

**Accessing this Class**

- [CreateDigitalInputs(out Error)](nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitalinputs__out.1.html)
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice.GetDigitalInputSection

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddDIOPort(DAQDIOPort, out Error) | Adds the specified DAQDIOPort to the Digital Input section. |
| AddDIOPort(DAQDIOPort) | Adds the specified DAQDIOPort to the Digital Input section. |
| GetDIOPorts() | Gets an array that contains the DAQDIOPort elements from the current DAQDigitalInputs section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-bool-uint-uint.html language=enus -->
## TOPIC 02389: DAQDigitalOutput(string, bool, uint, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-bool-uint-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-bool-uint-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQDigitalOutput with the specified name and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutput(string Name, bool InitialValue, uint DigitalLine, uint PortNumber)ParametersNameTypeDescriptionNamestringThe name of the

### DAQDigitalOutput(string, bool, uint, uint)

Initializes a new instance of [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html) with the specified name and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalOutput(string Name, bool InitialValue, uint DigitalLine, uint PortNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |
| InitialValue | bool | The initial value of the channel. |
| DigitalLine | uint | The digital line for the channel. |
| PortNumber | uint | The port to which the channel belongs. |

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-bool-daqmeasurementtype.html language=enus -->
## TOPIC 02390: DAQDigitalOutput(string, uint, uint, bool, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-bool-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-bool-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutput(string name, uint digitalLine, uint portNumber, bool initialValue, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringName of DI

### DAQDigitalOutput(string, uint, uint, bool, DAQMeasurementType)

Initializes a new instance of the DAQDigitalOutput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalOutput(string name, uint digitalLine, uint portNumber, bool initialValue, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Name of DI Channel |
| digitalLine | uint | Digital line number |
| portNumber | uint | Digital port Number |
| initialValue | bool | Initial value of Digital Input Line |
| measurementType | DAQMeasurementType | DAQ Measurement Type |

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-bool-string.html language=enus -->
## TOPIC 02391: DAQDigitalOutput(string, uint, uint, bool, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-bool-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutput(string name, uint digitalLine, uint portNumber, bool initialValue, string pluginGUID)RemarksUse this constructor to create channels with a measurement t

### DAQDigitalOutput(string, uint, uint, bool, string)

Initializes a new instance of the DAQDigitalOutput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalOutput(string name, uint digitalLine, uint portNumber, bool initialValue, string pluginGUID)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. |
| digitalLine | uint | The digital line number. |
| portNumber | uint | The digital port number. |
| initialValue | bool | The initial value of the digital output line. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-daqmeasurementtype.html language=enus -->
## TOPIC 02392: DAQDigitalOutput(string, uint, uint, DAQMeasurementType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutput(string name, uint digitalLine, uint portNumber, DAQMeasurementType measurementType)ParametersNameTypeDescriptionnamestringThe name of the channel.digita

### DAQDigitalOutput(string, uint, uint, DAQMeasurementType)

Initializes a new instance of the DAQDigitalOutput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalOutput(string name, uint digitalLine, uint portNumber, DAQMeasurementType measurementType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. |
| digitalLine | uint | The digital line number. |
| portNumber | uint | The digital port number. |
| measurementType | DAQMeasurementType | An enumeration of DAQMeasurementType. |

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-string.html language=enus -->
## TOPIC 02393: DAQDigitalOutput(string, uint, uint, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-daqdigitaloutput__string-uint-uint-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQDigitalOutput class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutput(string name, uint digitalLine, uint portNumber, string pluginGUID)RemarksUse this constructor to create channels with a measurement type defined in a cu

### DAQDigitalOutput(string, uint, uint, string)

Initializes a new instance of the DAQDigitalOutput class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDigitalOutput(string name, uint digitalLine, uint portNumber, string pluginGUID)

#### Remarks

Use this constructor to create channels with a measurement type defined in a custom DAQ measurement type plug-in XML file. You can locate the *pluginGUID* value in the <GUID> tags within the plug-in XML file.

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the channel. |
| digitalLine | uint | The digital line number. |
| portNumber | uint | The digital port number. |
| pluginGUID | string | The GUID for the DAQ measurement type plug-in. |

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-digitalline.html language=enus -->
## TOPIC 02394: DigitalLine

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-digitalline.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-digitalline.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the digital line for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint DigitalLine { get; set; }ReturnsThe digital line.

### DigitalLine

Gets or sets the digital line for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint DigitalLine { get; set; }

#### Returns

The digital line.

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-initalvalue.html language=enus -->
## TOPIC 02395: InitalValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-initalvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-initalvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the digital output channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool InitalValue { get; set; }ReturnsThe initial value.

### InitalValue

Gets or sets the initial value of the digital output channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InitalValue { get; set; }

#### Returns

The initial value.

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-isscxi.html language=enus -->
## TOPIC 02396: IsSCXI

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-isscxi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-isscxi.html
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

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-portnumber.html language=enus -->
## TOPIC 02397: PortNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-portnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput-portnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the port to which the channel belongs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PortNumber { get; set; }ReturnsThe port number.

### PortNumber

Gets or sets the port to which the channel belongs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PortNumber { get; set; }

#### Returns

The port number.

Parent topic:

DAQDigitalOutput Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html language=enus -->
## TOPIC 02398: DAQDigitalOutput Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ digital output channel. Derives fromDAQChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQDigitalOutput : DAQChannelRemarksUse the members of this class to get and set properties of the channel such as the port it belongs to and its digital line

### DAQDigitalOutput Class

Represents a DAQ digital output channel.

#### Derives from

- DAQChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQDigitalOutput : DAQChannel

#### Remarks

Use the members of this class to get and set properties of the channel such as the port it belongs to and its digital line.

**Accessing this Class**

- [GetDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitaloutputs.html)
- DAQDigitalOutput Constructor

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQDigitalOutput(string, uint, uint, bool, DAQMeasurementType) | Initializes a new instance of the DAQDigitalOutput class. |
| DAQDigitalOutput(string, bool, uint, uint) | Initializes a new instance of DAQDigitalOutput with the specified name and configuration. |
| DAQDigitalOutput(string, uint, uint, DAQMeasurementType) | Initializes a new instance of the DAQDigitalOutput class. |
| DAQDigitalOutput(string, uint, uint, string) | Initializes a new instance of the DAQDigitalOutput class. |
| DAQDigitalOutput(string, uint, uint, bool, string) | Initializes a new instance of the DAQDigitalOutput class. |

#### Properties

| Name | Description |
| --- | --- |
| DigitalLine | Gets or sets the digital line for the channel. |
| InitalValue | Gets or sets the initial value of the digital output channel. |
| IsSCXI | Gets whether the channel belongs to an SCXI module. |
| PortNumber | Gets or sets the port to which the channel belongs. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-adddioport__daqdioport-out.html language=enus -->
## TOPIC 02399: AddDIOPort(DAQDIOPort, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-adddioport__daqdioport-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-adddioport__daqdioport-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDIOPort to the Digital Output section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDIOPort(DAQDIOPort dioPort, out Error error)ParametersNameTypeDescriptiondioPortDAQDIOPortThe DIO port to add.errorout ErrorReturns an NationalInstruments.Ver

### AddDIOPort(DAQDIOPort, out Error)

Adds the specified [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) to the **Digital Output** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDIOPort(DAQDIOPort dioPort, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dioPort | DAQDIOPort | The DIO port to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the port was added successfully.

Parent topic:

DAQDigitalOutputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-adddioport__daqdioport.html language=enus -->
## TOPIC 02400: AddDIOPort(DAQDIOPort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-adddioport__daqdioport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-adddioport__daqdioport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDIOPort to the Digital Output section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDIOPort(DAQDIOPort dioPort)ParametersNameTypeDescriptiondioPortDAQDIOPortThe DIO port to add.Returnstrue if the port was added successfully.

### AddDIOPort(DAQDIOPort)

Adds the specified [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) to the **Digital Output** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDIOPort(DAQDIOPort dioPort)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dioPort | DAQDIOPort | The DIO port to add. |

#### Returns

true if the port was added successfully.

Parent topic:

DAQDigitalOutputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-getdioports.html language=enus -->
## TOPIC 02401: GetDIOPorts()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-getdioports.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-getdioports.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQDIOPort elements from the current DAQDigitalOutputs section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDIOPort[] GetDIOPorts()RemarksModifications you make to the contents of this list apply to the system definition. However, modif

### GetDIOPorts()

Gets an array that contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) elements from the current [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html)[] GetDIOPorts()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) elements from the current [DAQDigitalOutputs](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html) section.

Parent topic:

DAQDigitalOutputs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html language=enus -->
## TOPIC 02402: DAQDigitalOutputs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Digital Output section under a DAQDevice, which contains the DAQDIOPort ports for DAQDigitalOutput channels. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQDigitalOutputs : SectionRemarksUse the members of this class to add or get a

### DAQDigitalOutputs Class

Represents a **Digital Output** section under a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html), which contains the [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) ports for [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html) channels.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQDigitalOutputs : Section

#### Remarks

Use the members of this class to add or get a list of existing DAQ DIO ports for the current device.

**Accessing this Class**

- [CreateDigitalOutputs(out Error)](nationalinstruments-veristand-systemdefinitionapi-daqdevice-createdigitaloutputs__out.1.html)
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice.GetDigitalOutputSection

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddDIOPort(DAQDIOPort, out Error) | Adds the specified DAQDIOPort to the Digital Output section. |
| AddDIOPort(DAQDIOPort) | Adds the specified DAQDIOPort to the Digital Output section. |
| GetDIOPorts() | Gets an array that contains the DAQDIOPort elements from the current DAQDigitalOutputs section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitalinput__daqdigitalinput-out.html language=enus -->
## TOPIC 02403: AddDigitalInput(DAQDigitalInput, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitalinput__daqdigitalinput-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitalinput__daqdigitalinput-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDigitalInput channel to the port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDigitalInput(DAQDigitalInput digitalInput, out Error error)ParametersNameTypeDescriptiondigitalInputDAQDigitalInputThe digital input channel to add.errorout ErrorR

### AddDigitalInput(DAQDigitalInput, out Error)

Adds the specified [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html) channel to the port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDigitalInput(DAQDigitalInput digitalInput, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| digitalInput | DAQDigitalInput | The digital input channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the channel was added successfully.

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitalinput__daqdigitalinput.html language=enus -->
## TOPIC 02404: AddDigitalInput(DAQDigitalInput)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitalinput__daqdigitalinput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitalinput__daqdigitalinput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDigitalInput channel to the port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDigitalInput(DAQDigitalInput digitalInput)ParametersNameTypeDescriptiondigitalInputDAQDigitalInputThe digital input channel to add.Returnstrue if the channel was a

### AddDigitalInput(DAQDigitalInput)

Adds the specified [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html) channel to the port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDigitalInput(DAQDigitalInput digitalInput)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| digitalInput | DAQDigitalInput | The digital input channel to add. |

#### Returns

true if the channel was added successfully.

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitaloutput__daqdigitaloutput-out.html language=enus -->
## TOPIC 02405: AddDigitalOutput(DAQDigitalOutput, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitaloutput__daqdigitaloutput-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitaloutput__daqdigitaloutput-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDigitalOutput channel to the port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDigitalOutput(DAQDigitalOutput digitalOutput, out Error error)ParametersNameTypeDescriptiondigitalOutputDAQDigitalOutputThe digital output channel to add.errorout

### AddDigitalOutput(DAQDigitalOutput, out Error)

Adds the specified [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html) channel to the port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDigitalOutput(DAQDigitalOutput digitalOutput, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| digitalOutput | DAQDigitalOutput | The digital output channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the channel was added successfully.

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitaloutput__daqdigitaloutput.html language=enus -->
## TOPIC 02406: AddDigitalOutput(DAQDigitalOutput)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitaloutput__daqdigitaloutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-adddigitaloutput__daqdigitaloutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQDigitalOutput channel to the port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDigitalOutput(DAQDigitalOutput digitalOutput)ParametersNameTypeDescriptiondigitalOutputDAQDigitalOutputThe digital output channel to add.Returnstrue if the channe

### AddDigitalOutput(DAQDigitalOutput)

Adds the specified [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html) channel to the port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDigitalOutput(DAQDigitalOutput digitalOutput)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| digitalOutput | DAQDigitalOutput | The digital output channel to add. |

#### Returns

true if the channel was added successfully.

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-daqdioport__uint-bool.html language=enus -->
## TOPIC 02407: DAQDIOPort(uint, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-daqdioport__uint-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-daqdioport__uint-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQDIOPort with the specified configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDIOPort(uint portNumber, bool Inverted)ParametersNameTypeDescriptionportNumberuintThe number for the port.Invertedbooltrue to invert the digital line

### DAQDIOPort(uint, bool)

Initializes a new instance of [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html) with the specified configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQDIOPort(uint portNumber, bool Inverted)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| portNumber | uint | The number for the port. |
| Inverted | bool | true to invert the digital lines. |

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitalinputs.html language=enus -->
## TOPIC 02408: GetDigitalInputs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitalinputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitalinputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQDigitalInput elements from the current DAQDIOPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalInput[] GetDigitalInputs()RemarksModifications you make to the contents of this list apply to the system definition. However, modif

### GetDigitalInputs()

Gets an array that contains the [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html) elements from the current [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html)[] GetDigitalInputs()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html) elements from the current [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html).

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitaloutputs.html language=enus -->
## TOPIC 02409: GetDigitalOutputs()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitaloutputs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-getdigitaloutputs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQDigitalOutput elements from the current DAQDIOPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDigitalOutput[] GetDigitalOutputs()RemarksModifications you make to the contents of this list apply to the system definition. However, mo

### GetDigitalOutputs()

Gets an array that contains the [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html) elements from the current [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html)[] GetDigitalOutputs()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html) elements from the current [DAQDIOPort](nationalinstruments-veristand-systemdefinitionapi-daqdioport.html)..

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport-inverted.html language=enus -->
## TOPIC 02410: Inverted

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport-inverted.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport-inverted.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the digital lines are inverted. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Inverted { get; set; }Returnstrue if digital lines are inverted. Otherwise false.

### Inverted

Gets or sets whether the digital lines are inverted.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Inverted { get; set; }

#### Returns

true if digital lines are inverted. Otherwise false.

Parent topic:

DAQDIOPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqdioport.html language=enus -->
## TOPIC 02411: DAQDIOPort Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqdioport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqdioport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ DIO port, which contains DAQDigitalInput and/or DAQDigitalOutput channels. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQDIOPort : SectionRemarksUse the members of this class to add new or get a list of existing digital input an

### DAQDIOPort Class

Represents a DAQ DIO port, which contains [DAQDigitalInput](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinput.html) and/or [DAQDigitalOutput](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutput.html) channels.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQDIOPort : Section

#### Remarks

Use the members of this class to add new or get a list of existing digital input and output channels, and to invert digital lines on the port.

**Accessing this Class**

- [GetDIOPorts](nationalinstruments-veristand-systemdefinitionapi-daqdigitalinputs-getdioports.html)
- [GetDIOPorts](nationalinstruments-veristand-systemdefinitionapi-daqdigitaloutputs-getdioports.html)
- DAQDIOPort Constructor

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a DAQ Device in a System Definition File

C# Walkthrough: Modifying a DAQ Device in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQDIOPort(uint, bool) | Initializes a new instance of DAQDIOPort with the specified configuration. |

#### Properties

| Name | Description |
| --- | --- |
| Inverted | Gets or sets whether the digital lines are inverted. |

#### Methods

| Name | Description |
| --- | --- |
| AddDigitalInput(DAQDigitalInput, out Error) | Adds the specified DAQDigitalInput channel to the port. |
| AddDigitalInput(DAQDigitalInput) | Adds the specified DAQDigitalInput channel to the port. |
| AddDigitalOutput(DAQDigitalOutput) | Adds the specified DAQDigitalOutput channel to the port. |
| AddDigitalOutput(DAQDigitalOutput, out Error) | Adds the specified DAQDigitalOutput channel to the port. |
| GetDigitalInputs() | Gets an array that contains the DAQDigitalInput elements from the current DAQDIOPort. |
| GetDigitalOutputs() | Gets an array that contains the DAQDigitalOutput elements from the current DAQDIOPort. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-daqfrequencymeasurement__string-string-uint-double-double-double-daqcounteredge.html language=enus -->
## TOPIC 02412: DAQFrequencyMeasurement(string, string, uint, double, double, double, DAQCounterEdge)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-daqfrequencymeasurement__string-string-uint-double-double-double-daqcounteredge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-daqfrequencymeasurement__string-string-uint-double-double-double-daqcounteredge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQFrequencyMeasurement with the specified name, description, and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQFrequencyMeasurement(string Name, string Description, uint Index, double DefaultValue, double Maximum, double Min

### DAQFrequencyMeasurement(string, string, uint, double, double, double, DAQCounterEdge)

Initializes a new instance of [DAQFrequencyMeasurement](nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement.html) with the specified name, description, and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQFrequencyMeasurement(string Name, string Description, uint Index, double DefaultValue, double Maximum, double Minimum, DAQCounterEdge Edge)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |
| Description | string | The description of the channel. |
| Index | uint | The index value of the channel. A value of 1 represents CTR1. 2 represents CTR2, and so on. |
| DefaultValue | double | The initial value of the channel. |
| Maximum | double | The maximum value of the channel. |
| Minimum | double | The minimum value of the channel. |
| Edge | DAQCounterEdge | The edge on which to count (rising or falling). |

Parent topic:

DAQFrequencyMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-edge.html language=enus -->
## TOPIC 02413: Edge

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-edge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-edge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the edge on which to count (rising or falling). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterEdge Edge { get; set; }ReturnsAn enumeration value of DAQCounterEdge.

### Edge

Gets or sets the edge on which to count (rising or falling).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterEdge](nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html) Edge { get; set; }

#### Returns

An enumeration value of [DAQCounterEdge](nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html).

Parent topic:

DAQFrequencyMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-inputterminal.html language=enus -->
## TOPIC 02414: InputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-inputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string InputTerminal { get; set; }

### InputTerminal

Gets or sets the input terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string InputTerminal { get; set; }

Parent topic:

DAQFrequencyMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-max.html language=enus -->
## TOPIC 02415: Max

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-max.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-max.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum value of the channel in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Max { get; set; }ReturnsThe maximum value of the channel in hertz.

### Max

Gets or sets the maximum value of the channel in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Max { get; set; }

#### Returns

The maximum value of the channel in hertz.

Parent topic:

DAQFrequencyMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-min.html language=enus -->
## TOPIC 02416: Min

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-min.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement-min.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the minimum value of the channel in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Min { get; set; }ReturnsThe minimum value of the channel in hertz.

### Min

Gets or sets the minimum value of the channel in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Min { get; set; }

#### Returns

The minimum value of the channel in hertz.

Parent topic:

DAQFrequencyMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement.html language=enus -->
## TOPIC 02417: DAQFrequencyMeasurement Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqfrequencymeasurement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQCounter channel with the frequency measurement task type. Derives fromDAQCounterSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQFrequencyMeasurement : DAQCounterRemarksUse the members of this class to get or set the maximum and minimum value of the c

### DAQFrequencyMeasurement Class

Represents a [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) channel with the frequency measurement task type.

#### Derives from

- DAQCounter

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQFrequencyMeasurement : DAQCounter

#### Remarks

Use the members of this class to get or set the maximum and minimum value of the channel and the edge on which to count.

**Accessing this Class**

- DAQFrequencyMeasurement Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQFrequencyMeasurement(string, string, uint, double, double, double, DAQCounterEdge) | Initializes a new instance of DAQFrequencyMeasurement with the specified name, description, and configuration. |

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets the edge on which to count (rising or falling). |
| InputTerminal | Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |
| Max | Gets or sets the maximum value of the channel in hertz. |
| Min | Gets or sets the minimum value of the channel in hertz. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-channel.html language=enus -->
## TOPIC 02418: Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the physical name for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Channel { get; set; }ReturnsThe physical name of the internal channel. Valid values vary by device. Refer to your hardware documentation for a list of valid internal channe

### Channel

Gets or sets the physical name for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Channel { get; set; }

#### Returns

The physical name of the internal channel. Valid values vary by device. Refer to your hardware documentation for a list of valid internal channel names.

Parent topic:

DAQInternalChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-daqinternalchannel__string-double.html language=enus -->
## TOPIC 02419: DAQInternalChannel(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-daqinternalchannel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-daqinternalchannel__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQInternalChannel with the specified name and default value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQInternalChannel(string Name, double DefaultValue)ParametersNameTypeDescriptionNamestringThe name of the channel.DefaultValuedoubleTh

### DAQInternalChannel(string, double)

Initializes a new instance of [DAQInternalChannel](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html) with the specified name and default value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQInternalChannel(string Name, double DefaultValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |
| DefaultValue | double | The default value of the channel. |

Parent topic:

DAQInternalChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-highlevel.html language=enus -->
## TOPIC 02420: HighLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-highlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-highlevel.html
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

DAQInternalChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-lowlevel.html language=enus -->
## TOPIC 02421: LowLevel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-lowlevel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel-lowlevel.html
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

DAQInternalChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html language=enus -->
## TOPIC 02422: DAQInternalChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ internal channel. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQInternalChannel : ChannelRemarksUse the members of this class to get and set properties of the channel, such as its maximum and minimum values and its physical chan

### DAQInternalChannel Class

Represents a DAQ internal channel.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQInternalChannel : Channel

#### Remarks

Use the members of this class to get and set properties of the channel, such as its maximum and minimum values and its physical channel name.

**Accessing this Class**

- [GetInternalChannelList](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-getinternalchannellist.html)
- DAQInternalChannel Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQInternalChannel(string, double) | Initializes a new instance of DAQInternalChannel with the specified name and default value. |

#### Properties

| Name | Description |
| --- | --- |
| Channel | Gets or sets the physical name for the channel. |
| HighLevel | Gets or sets the maximum value of the channel. |
| LowLevel | Gets or sets the minimum value of the channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-addinternalchannel__daqinternalchannel-out.html language=enus -->
## TOPIC 02423: AddInternalChannel(DAQInternalChannel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-addinternalchannel__daqinternalchannel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-addinternalchannel__daqinternalchannel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQInternalChannel to the Internal Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddInternalChannel(DAQInternalChannel internalChannel, out Error error)ParametersNameTypeDescriptioninternalChannelDAQInternalChannelThe channel to ad

### AddInternalChannel(DAQInternalChannel, out Error)

Adds the specified [DAQInternalChannel](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html) to the **Internal Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddInternalChannel(DAQInternalChannel internalChannel, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| internalChannel | DAQInternalChannel | The channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the channel was added successfully.

Parent topic:

DAQInternalChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-addinternalchannel__daqinternalchannel.html language=enus -->
## TOPIC 02424: AddInternalChannel(DAQInternalChannel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-addinternalchannel__daqinternalchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-addinternalchannel__daqinternalchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified DAQInternalChannel to the Internal Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddInternalChannel(DAQInternalChannel internalChannel)ParametersNameTypeDescriptioninternalChannelDAQInternalChannelThe channel to add.Returnstrue if

### AddInternalChannel(DAQInternalChannel)

Adds the specified [DAQInternalChannel](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html) to the **Internal Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddInternalChannel(DAQInternalChannel internalChannel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| internalChannel | DAQInternalChannel | The channel to add. |

#### Returns

true if the channel was added successfully.

Parent topic:

DAQInternalChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-getinternalchannellist.html language=enus -->
## TOPIC 02425: GetInternalChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-getinternalchannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels-getinternalchannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the DAQInternalChannel elements from the current DAQInternalChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQInternalChannel[] GetInternalChannelList()RemarksModifications you make to the contents of this list apply to the syst

### GetInternalChannelList()

Gets an array that contains the [DAQInternalChannel](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html) elements from the current [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQInternalChannel](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html)[] GetInternalChannelList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [DAQInternalChannel](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html) elements from the current [DAQInternalChannels](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html) section.

Parent topic:

DAQInternalChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html language=enus -->
## TOPIC 02426: DAQInternalChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqinternalchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Internal Channels section under a DAQDevice, which contains any DAQInternalChannel objects to add to the device. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQInternalChannels : SectionRemarksUse the members of this class to add or

### DAQInternalChannels Class

Represents an **Internal Channels** section under a [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html), which contains any [DAQInternalChannel](nationalinstruments-veristand-systemdefinitionapi-daqinternalchannel.html) objects to add to the device.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQInternalChannels : Section

#### Remarks

Use the members of this class to add or get a list of existing internal channels for the current device.

**Accessing this Class**

- [CreateInternalChannels(out Error)](nationalinstruments-veristand-systemdefinitionapi-daqdevice-createinternalchannels__out.html)
- M:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice.GetInternalChannelsSection

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddInternalChannel(DAQInternalChannel, out Error) | Adds the specified DAQInternalChannel to the Internal Channels section. |
| AddInternalChannel(DAQInternalChannel) | Adds the specified DAQInternalChannel to the Internal Channels section. |
| GetInternalChannelList() | Gets an array that contains the DAQInternalChannel elements from the current DAQInternalChannels section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-actiononnew.html language=enus -->
## TOPIC 02427: ActionOnNew

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-actiononnew.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-actiononnew.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the location to log data when the DAQTaskAI begins a new acquisition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ActionOnNew ActionOnNew { get; set; }ReturnsAn enumeration of ActionOnNew. The default value is NewGroup.

### ActionOnNew

Gets or sets the location to log data when the [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) begins a new acquisition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ActionOnNew](nationalinstruments-veristand-systemdefinitionapi-actiononnew.html) ActionOnNew { get; set; }

#### Returns

An enumeration of [ActionOnNew](nationalinstruments-veristand-systemdefinitionapi-actiononnew.html). The default value is [NewGroup](nationalinstruments-veristand-systemdefinitionapi-actiononnew.html).

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-filenamebase.html language=enus -->
## TOPIC 02428: FilenameBase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-filenamebase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-filenamebase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the base string used in log filenames. Use this property when UseTaskAsFilename is false to specify a filename base other than the task name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string FilenameBase { get; set; }ReturnsThe string to use as filename ba

### FilenameBase

Gets or sets the base string used in log filenames. Use this property when [UseTaskAsFilename](nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasfilename.html) is false to specify a filename base other than the task name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string FilenameBase { get; set; }

#### Returns

The string to use as filename base. The default value is the task name.

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsFilename

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-getloggingenabledchannel.html language=enus -->
## TOPIC 02429: GetLoggingEnabledChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-getloggingenabledchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-getloggingenabledchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Logging Enabled channel under the current DAQTaskAI. This reference is valid only if the LoggingEnabled property is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTaskCommand GetLoggingEnabledChannel()ReturnsA DAQTaskCommand reference to the Logging Enable

### GetLoggingEnabledChannel()

Gets the Logging Enabled channel under the current [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html). This reference is valid only if the [LoggingEnabled](nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingenabled.html) property is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) GetLoggingEnabledChannel()

#### Returns

A [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) reference to the Logging Enabled channel.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-getstartnewfilechannel.html language=enus -->
## TOPIC 02430: GetStartNewFileChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-getstartnewfilechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-getstartnewfilechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Start New File channel under the current DAQTaskAI. This reference is valid only if the LoggingEnabled property is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQTaskCommand GetStartNewFileChannel()ReturnsA DAQTaskCommand reference to the Start New File ch

### GetStartNewFileChannel()

Gets the Start New File channel under the current [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html). This reference is valid only if the [LoggingEnabled](nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingenabled.html) property is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) GetStartNewFileChannel()

#### Returns

A [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) reference to the Start New File channel.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-groupname.html language=enus -->
## TOPIC 02431: GroupName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-groupname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-groupname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the group name to which the task logs data in the TDMS file. Use this property when UseTaskAsGroupName is false to specify a group name other than the task name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string GroupName { get; set; }RemarksIf the specifie

### GroupName

Gets or sets the group name to which the task logs data in the TDMS file. Use this property when [UseTaskAsGroupName](nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasgroupname.html) is false to specify a group name other than the task name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string GroupName { get; set; }

#### Remarks

If the specified group already exists, NI VeriStand appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist.

#### Returns

The string to use as group name. The default value is the task name.

#### See Also

- NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsGroupName

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-logdirectory.html language=enus -->
## TOPIC 02432: LogDirectory

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-logdirectory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-logdirectory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the directory in which to save log files on the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string LogDirectory { get; set; }ReturnsThe path of the directory in which to save log files. The default is c:\logs.

### LogDirectory

Gets or sets the directory in which to save log files on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string LogDirectory { get; set; }

#### Returns

The path of the directory in which to save log files. The default is c:\logs.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingenabled.html language=enus -->
## TOPIC 02433: LoggingEnabled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingenabled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingenabled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the Logging Enabled DAQTaskCommand channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Logging

### LoggingEnabled

Gets or sets a value indicating whether the Logging Enabled [DAQTaskCommand](nationalinstruments-veristand-systemdefinitionapi-daqtaskcommand.html) channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool LoggingEnabled { get; set; }

#### Remarks

To improve system performance, set this property to false if you do not plan to log data from a task.

#### Returns

true if logging is allowed to be enabled. The default value is false.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingmode.html language=enus -->
## TOPIC 02434: LoggingMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether data is available to components in the NI VeriStand system while you log it. This property valid only if LoggingEnabled is true. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic LogMode LoggingMode { get; set; }ReturnsAn enumeration of LogMode. The defaul

### LoggingMode

Gets or sets whether data is available to components in the NI VeriStand system while you log it. This property valid only if [LoggingEnabled](nationalinstruments-veristand-systemdefinitionapi-daqlogging-loggingenabled.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [LogMode](nationalinstruments-veristand-systemdefinitionapi-logmode.html) LoggingMode { get; set; }

#### Returns

An enumeration of [LogMode](nationalinstruments-veristand-systemdefinitionapi-logmode.html). The default value is [LogAndRead](nationalinstruments-veristand-systemdefinitionapi-logmode.html).

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-samplesperfile.html language=enus -->
## TOPIC 02435: SamplesPerFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-samplesperfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-samplesperfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a limit to the number of samples per channel to log to the current file when SpanMultipleFiles is true. This property not active if SpanMultipleFiles is false because NI VeriStand logs to the current file without limiting the number of samples. SyntaxNamespace: NationalInstruments.VeriS

### SamplesPerFile

Gets or sets a limit to the number of samples per channel to log to the current file when [SpanMultipleFiles](nationalinstruments-veristand-systemdefinitionapi-daqlogging-spanmultiplefiles.html) is true. This property not active if [SpanMultipleFiles](nationalinstruments-veristand-systemdefinitionapi-daqlogging-spanmultiplefiles.html) is false because NI VeriStand logs to the current file without limiting the number of samples.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong SamplesPerFile { get; set; }

#### Returns

The maximum number of samples per channel to log to the current file. The default value is 100000.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-spanmultiplefiles.html language=enus -->
## TOPIC 02436: SpanMultipleFiles

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-spanmultiplefiles.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-spanmultiplefiles.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to create a new log file when you reach the SamplesPerFile limit. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SpanMultipleFiles { get; set; }RemarksWhen this property is true and the SamplesPerFile limit is reached, NI VeriSta

### SpanMultipleFiles

Gets or sets a value indicating whether to create a new log file when you reach the [SamplesPerFile](nationalinstruments-veristand-systemdefinitionapi-daqlogging-samplesperfile.html) limit.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SpanMultipleFiles { get; set; }

#### Remarks

When this property is true and the [SamplesPerFile](nationalinstruments-veristand-systemdefinitionapi-daqlogging-samplesperfile.html) limit is reached, NI VeriStand creates new files with the naming convention of *filename_####*.tdms, where *####* starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\data.tdms, the next filename used is C:\data_0001.tdms.

#### Returns

true if a new file is created when the [SamplesPerFile](nationalinstruments-veristand-systemdefinitionapi-daqlogging-samplesperfile.html) limit is reached. The default value is false.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-timestampfilename.html language=enus -->
## TOPIC 02437: TimestampFilename

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-timestampfilename.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-timestampfilename.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to append timestamps to the log filenames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool TimestampFilename { get; set; }Returnstrue to append timestamps to filenames. The default value is false.

### TimestampFilename

Gets or sets a value indicating whether to append timestamps to the log filenames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool TimestampFilename { get; set; }

#### Returns

true to append timestamps to filenames. The default value is false.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasfilename.html language=enus -->
## TOPIC 02438: UseTaskAsFilename

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasfilename.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasfilename.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to use the DAQTask name from the system definition as the base of log filenames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UseTaskAsFilename { get; set; }Returnstrue to use the DAQTask name as the base of log filenames. fals

### UseTaskAsFilename

Gets or sets a value indicating whether to use the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) name from the system definition as the base of log filenames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UseTaskAsFilename { get; set; }

#### Returns

true to use the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) name as the base of log filenames. false to use a custom [FilenameBase](nationalinstruments-veristand-systemdefinitionapi-daqlogging-filenamebase.html). The default value is true.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasgroupname.html language=enus -->
## TOPIC 02439: UseTaskAsGroupName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasgroupname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging-usetaskasgroupname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to use the DAQTask name from the system definition as the group name under which data is logged in the TDMS file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UseTaskAsGroupName { get; set; }Returnstrue to use the DAQTask name

### UseTaskAsGroupName

Gets or sets a value indicating whether to use the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) name from the system definition as the group name under which data is logged in the TDMS file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UseTaskAsGroupName { get; set; }

#### Returns

true to use the [DAQTask](nationalinstruments-veristand-systemdefinitionapi-daqtask.html) name as the TDMS group name. false to use a custom [GroupName](nationalinstruments-veristand-systemdefinitionapi-daqlogging-groupname.html). The default value is true.

Parent topic:

DAQLogging Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqlogging.html language=enus -->
## TOPIC 02440: DAQLogging Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqlogging.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqlogging.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Logging section of a DAQTaskAI. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQLogging : SectionRemarksUse the members of this class to enable and configure how a DAQTaskAI implements embedded logging of waveform data to .tdms file

### DAQLogging Class

Represents the **Logging** section of a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQLogging : Section

#### Remarks

Use the members of this class to enable and configure how a [DAQTaskAI](nationalinstruments-veristand-systemdefinitionapi-daqtaskai.html) implements embedded logging of waveform data to .tdms files. When a task runs with logging enabled, NI VeriStand streams data directly from the device buffer to the hard disk of the target to which the DAQ device is connected.

**Accessing this Class**

- [GetLogging](nationalinstruments-veristand-systemdefinitionapi-daqtaskai-getlogging.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ActionOnNew | Gets or sets the location to log data when the DAQTaskAI begins a new acquisition. |
| FilenameBase | Gets or sets the base string used in log filenames. Use this property when UseTaskAsFilename is false to specify a filename base other than the task name. |
| GroupName | Gets or sets the group name to which the task logs data in the TDMS file. Use this property when UseTaskAsGroupName is false to specify a group name other than the task name. |
| LogDirectory | Gets or sets the directory in which to save log files on the target. |
| LoggingEnabled | Gets or sets a value indicating whether the Logging Enabled DAQTaskCommand channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging. |
| LoggingMode | Gets or sets whether data is available to components in the NI VeriStand system while you log it. This property valid only if LoggingEnabled is true. |
| SamplesPerFile | Gets or sets a limit to the number of samples per channel to log to the current file when SpanMultipleFiles is true. This property not active if SpanMultipleFiles is false because NI VeriStand logs to the current file without limiting the number of samples. |
| SpanMultipleFiles | Gets or sets a value indicating whether to create a new log file when you reach the SamplesPerFile limit. |
| TimestampFilename | Gets or sets a value indicating whether to append timestamps to the log filenames. |
| UseTaskAsFilename | Gets or sets a value indicating whether to use the DAQTask name from the system definition as the base of log filenames. |
| UseTaskAsGroupName | Gets or sets a value indicating whether to use the DAQTask name from the system definition as the group name under which data is logged in the TDMS file. |

#### Methods

| Name | Description |
| --- | --- |
| GetLoggingEnabledChannel() | Gets the Logging Enabled channel under the current DAQTaskAI. This reference is valid only if the LoggingEnabled property is true. |
| GetStartNewFileChannel() | Gets the Start New File channel under the current DAQTaskAI. This reference is valid only if the LoggingEnabled property is true. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html language=enus -->
## TOPIC 02441: DAQMeasurementType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement type of a DAQ channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum DAQMeasurementTypeRemarksFor information about the channel properties that belong to each enumeration value and information about accessing them, refer to the list of DAQ ch

### DAQMeasurementType Enumeration

Specifies the measurement type of a DAQ channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum DAQMeasurementType

#### Remarks

For information about the channel properties that belong to each enumeration value and information about accessing them, refer to the list of DAQ channel properties

.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AnalogInputVoltage | 0 | An analog input channel that measures voltage. |
| AnalogInputCurrent | 1 | An analog input channel that measures current. |
| AnalogInputTemperatureThermocouple | 2 | An analog input channel that measures temperature using a thermocouple. |
| AnalogInputTemperatureThermistorVex | 3 | An analog input channel that measures temperature using a thermistor that requires voltage excitation. |
| AnalogInputTemperatureThermistorIex | 4 | An analog input channel that measures temperature using a thermistor that requires current excitation. |
| AnalogInputTemperatureRTD | 5 | An analog input channel that measures temperature from an RTD. |
| AnalogInputStrainGage | 6 | An analog input channel that measures strain. |
| AnalogInputAccelerometer | 7 | An analog input channel that measures acceleration from an accelerometer. |
| AnalogInputBridge | 8 | An analog input channel that measures Voltage ratios from a Wheatstone bridge. |
| AnalogInputForce | 9 | An analog input channel that uses a Wheatstone bridge to measure force or load. |
| AnalogInputPressure | 10 | An analog input channel that uses a Wheatstone bridge to measure pressure. |
| AnalogInputTorque | 11 | An analog input channel that uses a Wheatstone bridge to measure torque. |
| AnalogInputPositionLVDT | 12 | An analog input channel that measures linear position. |
| AnalogInputPositionRVDT | 13 | An analog input channel that measures rotary position. |
| AnalogOutputVoltage | 20 | An analog output channel that measures voltage. |
| AnalogOutputCurrent | 21 | An analog output channel that measures current. |
| DigitalInput | 40 | A digital input channel that measures digital signals. |
| DigitalOutput | 60 | A digital output channel that generates digital signals. |
| CounterInputCountEdges | 80 | A counter input channel that counts the number of rising or falling edges of a digital signal. |
| CounterInputFrequency | 81 | A counter input channel that measures the frequency of a digital signal. |
| CounterInputPeriod | 82 | A counter input channel that measures the period of a digital signal. |
| CounterInputPositionLinearEncoder | 83 | A counter input channel that uses a linear encoder to measure linear position. |
| CounterInputPulseMeasurement | 84 | A counter input channel that measures pulse specifications. Note that only X Series DAQ devices support this measurement type. The pairing of high time and low time pair is a pulse specification. NI VeriStand returns these measurements as pairs of frequency and duty cycle values. |
| CounterOutputPulseGeneration | 85 | A counter output channel that generates digital pulses. To assign this measurement type to channels on a non-X Series DAQ device, use the SetBooleanProperty method to set the isHWTSP property for the counter output channelto false. If isHWTSP is true, only X Series DAQ devices support this measurement type. NI VeriStand generates pulses that are defined by pairs of frequency and duty cycle values. |
| UserDefined | -1 | A channel that implements a user-defined measurement type. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-daqperiodmeasurement__string-string-uint-double-double-double-daqcounteredge.html language=enus -->
## TOPIC 02442: DAQPeriodMeasurement(string, string, uint, double, double, double, DAQCounterEdge)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-daqperiodmeasurement__string-string-uint-double-double-double-daqcounteredge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-daqperiodmeasurement__string-string-uint-double-double-double-daqcounteredge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQPeriodMeasurement with the specified name, description, and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQPeriodMeasurement(string Name, string Description, uint Index, double DefaultValue, double Maximum, double Minimum,

### DAQPeriodMeasurement(string, string, uint, double, double, double, DAQCounterEdge)

Initializes a new instance of [DAQPeriodMeasurement](nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement.html) with the specified name, description, and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQPeriodMeasurement(string Name, string Description, uint Index, double DefaultValue, double Maximum, double Minimum, DAQCounterEdge Edge)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |
| Description | string | The description of the channel. |
| Index | uint | The index value of the channel. |
| DefaultValue | double | The initial value of the channel. |
| Maximum | double | The maximum value of the channel. |
| Minimum | double | The minimum value of the channel. |
| Edge | DAQCounterEdge | The edge on which to count (rising or falling). |

Parent topic:

DAQPeriodMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-edge.html language=enus -->
## TOPIC 02443: Edge

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-edge.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-edge.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the edge on which to count (rising or falling). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterEdge Edge { get; set; }ReturnsAn enumeration value of DAQCounterEdge.

### Edge

Gets or sets the edge on which to count (rising or falling).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterEdge](nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html) Edge { get; set; }

#### Returns

An enumeration value of [DAQCounterEdge](nationalinstruments-veristand-systemdefinitionapi-daqcounteredge.html).

Parent topic:

DAQPeriodMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-inputterminal.html language=enus -->
## TOPIC 02444: InputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-inputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string InputTerminal { get; set; }

### InputTerminal

Gets or sets the input terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string InputTerminal { get; set; }

Parent topic:

DAQPeriodMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-max.html language=enus -->
## TOPIC 02445: Max

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-max.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-max.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum value of the channel in seconds. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Max { get; set; }ReturnsThe maximum value of the channel in seconds.

### Max

Gets or sets the maximum value of the channel in seconds.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Max { get; set; }

#### Returns

The maximum value of the channel in seconds.

Parent topic:

DAQPeriodMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-min.html language=enus -->
## TOPIC 02446: Min

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-min.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement-min.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the minimum value of the channel in seconds. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Min { get; set; }ReturnsThe minimum value of the channel in seconds.

### Min

Gets or sets the minimum value of the channel in seconds.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Min { get; set; }

#### Returns

The minimum value of the channel in seconds.

Parent topic:

DAQPeriodMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement.html language=enus -->
## TOPIC 02447: DAQPeriodMeasurement Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqperiodmeasurement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQCounter channel with the period measurement task type. Derives fromDAQCounterSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQPeriodMeasurement : DAQCounterRemarksUse the members of this class to get or set the maximum and minimum value of the channel

### DAQPeriodMeasurement Class

Represents a [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) channel with the period measurement task type.

#### Derives from

- DAQCounter

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQPeriodMeasurement : DAQCounter

#### Remarks

Use the members of this class to get or set the maximum and minimum value of the channel and the edge on which to count.

**Accessing this Class**

- DAQPeriodMeasurement Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQPeriodMeasurement(string, string, uint, double, double, double, DAQCounterEdge) | Initializes a new instance of DAQPeriodMeasurement with the specified name, description, and configuration. |

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets the edge on which to count (rising or falling). |
| InputTerminal | Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |
| Max | Gets or sets the maximum value of the channel in seconds. |
| Min | Gets or sets the minimum value of the channel in seconds. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-ainputterminal.html language=enus -->
## TOPIC 02448: AInputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-ainputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-ainputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the A input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string AInputTerminal { get; set; }

### AInputTerminal

Gets or sets the A input terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string AInputTerminal { get; set; }

Parent topic:

DAQPositionMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-binputterminal.html language=enus -->
## TOPIC 02449: BInputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-binputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-binputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the B input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string BInputTerminal { get; set; }

### BInputTerminal

Gets or sets the B input terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string BInputTerminal { get; set; }

Parent topic:

DAQPositionMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-daqpositionmeasurement__string-string-uint-double-daqcounterdecoding-daqcounterzindexmode.html language=enus -->
## TOPIC 02450: DAQPositionMeasurement(string, string, uint, double, DAQCounterDecoding, DAQCounterZIndexMode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-daqpositionmeasurement__string-string-uint-double-daqcounterdecoding-daqcounterzindexmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-daqpositionmeasurement__string-string-uint-double-daqcounterdecoding-daqcounterzindexmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DAQPositionMeasurement with the specified name, description, and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQPositionMeasurement(string Name, string Description, uint Index, double DefaultValue, DAQCounterDecoding Decoding,

### DAQPositionMeasurement(string, string, uint, double, DAQCounterDecoding, DAQCounterZIndexMode)

Initializes a new instance of [DAQPositionMeasurement](nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement.html) with the specified name, description, and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQPositionMeasurement(string Name, string Description, uint Index, double DefaultValue, DAQCounterDecoding Decoding, DAQCounterZIndexMode ZIndexMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the channel. |
| Description | string | The description of the channel. |
| Index | uint | The index value of the channel. |
| DefaultValue | double | The initial value of the channel. |
| Decoding | DAQCounterDecoding | The method used to count and interpret the pulses the encoder generates on signal A and signal B. |
| ZIndexMode | DAQCounterZIndexMode | The states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. |

Parent topic:

DAQPositionMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-decoding.html language=enus -->
## TOPIC 02451: Decoding

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-decoding.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-decoding.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterDecoding Decoding { get; set; }ReturnsAn enumeration value of DAQCounterDecoding.

### Decoding

Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterDecoding](nationalinstruments-veristand-systemdefinitionapi-daqcounterdecoding.html) Decoding { get; set; }

#### Returns

An enumeration value of [DAQCounterDecoding](nationalinstruments-veristand-systemdefinitionapi-daqcounterdecoding.html).

Parent topic:

DAQPositionMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-zindexmode.html language=enus -->
## TOPIC 02452: ZIndexMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-zindexmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-zindexmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQCounterZIndexMode ZIndexMode { get; set; }ReturnsAn enumeration value of DAQCounterZIndexMode.

### ZIndexMode

Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQCounterZIndexMode](nationalinstruments-veristand-systemdefinitionapi-daqcounterzindexmode.html) ZIndexMode { get; set; }

#### Returns

An enumeration value of [DAQCounterZIndexMode](nationalinstruments-veristand-systemdefinitionapi-daqcounterzindexmode.html).

Parent topic:

DAQPositionMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-zinputterminal.html language=enus -->
## TOPIC 02453: ZInputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-zinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement-zinputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Z input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ZInputTerminal { get; set; }

### ZInputTerminal

Gets or sets the Z input terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ZInputTerminal { get; set; }

Parent topic:

DAQPositionMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement.html language=enus -->
## TOPIC 02454: DAQPositionMeasurement Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpositionmeasurement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQCounter channel with the position measurement task type. Derives fromDAQCounterSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQPositionMeasurement : DAQCounterRemarksUse the members of this class to get or set the Z index mode for resetting the posit

### DAQPositionMeasurement Class

Represents a [DAQCounter](nationalinstruments-veristand-systemdefinitionapi-daqcounter.html) channel with the position measurement task type.

#### Derives from

- DAQCounter

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQPositionMeasurement : DAQCounter

#### Remarks

Use the members of this class to get or set the Z index mode for resetting the position measurement and the decoding mode for interpreting pulses from the encoder.

**Accessing this Class**

- DAQPositionMeasurement Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DAQPositionMeasurement(string, string, uint, double, DAQCounterDecoding, DAQCounterZIndexMode) | Initializes a new instance of DAQPositionMeasurement with the specified name, description, and configuration. |

#### Properties

| Name | Description |
| --- | --- |
| AInputTerminal | Gets or sets the A input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |
| BInputTerminal | Gets or sets the B input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |
| Decoding | Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B. |
| ZIndexMode | Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. |
| ZInputTerminal | Gets or sets the Z input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-counter.html language=enus -->
## TOPIC 02455: Counter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-counter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-counter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the counter channel number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Counter { get; private set; }ReturnsThe channel number.

### Counter

Gets the counter channel number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Counter { get; private set; }

#### Returns

The channel number.

Parent topic:

DAQPulseGeneration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-daqpulsegeneration__string-string-uint.html language=enus -->
## TOPIC 02456: DAQPulseGeneration(string, string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-daqpulsegeneration__string-string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-daqpulsegeneration__string-string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQPulseGeneration class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQPulseGeneration(string name, string description, uint index)ParametersNameTypeDescriptionnamestringName of CounterdescriptionstringSection descriptionindexuintCount

### DAQPulseGeneration(string, string, uint)

Initializes a new instance of the [DAQPulseGeneration](nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQPulseGeneration(string name, string description, uint index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Name of Counter |
| description | string | Section description |
| index | uint | Counter Index |

Parent topic:

DAQPulseGeneration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-getdatachannel__daqdatachanneltype.html language=enus -->
## TOPIC 02457: GetDataChannel(DAQDataChannelType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-getdatachannel__daqdatachanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-getdatachannel__daqdatachanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a Channel referencing to the desired measurement data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override Channel GetDataChannel(DAQDataChannelType type)ParametersNameTypeDescriptiontypeDAQDataChannelTypeThe data channel typeReturnsReturns a channel referencing

### GetDataChannel(DAQDataChannelType)

Returns a [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) referencing to the desired measurement data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetDataChannel(DAQDataChannelType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| type | DAQDataChannelType | The data channel type |

#### Returns

Returns a channel referencing to the desired measurement data.

Parent topic:

DAQPulseGeneration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-initchannels.html language=enus -->
## TOPIC 02458: InitChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-initchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-initchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initialize the data channels array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected override Channel[] InitChannels()ReturnsReturns an array of data channels specific to this measurement type

### InitChannels()

Initialize the data channels array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected override [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html)[] InitChannels()

#### Returns

Returns an array of data channels specific to this measurement type

Parent topic:

DAQPulseGeneration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-outputterminal.html language=enus -->
## TOPIC 02459: OutputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-outputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string OutputTerminal { get; set; }

### OutputTerminal

Gets or sets the output terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string OutputTerminal { get; set; }

Parent topic:

DAQPulseGeneration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-setcounterindex__uint.html language=enus -->
## TOPIC 02460: SetCounterIndex(uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-setcounterindex__uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration-setcounterindex__uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the index value of the counter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetCounterIndex(uint index)ParametersNameTypeDescriptionindexuintThe index value of the channel.

### SetCounterIndex(uint)

Sets the index value of the counter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetCounterIndex(uint index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | uint | The index value of the channel. |

Parent topic:

DAQPulseGeneration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration.html language=enus -->
## TOPIC 02461: DAQPulseGeneration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsegeneration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ Counter measurement section of input channels. Derives fromDAQCounterOutputSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQPulseGeneration : DAQCounterOutputConstructorsNameDescriptionDAQPulseGeneration(string, string, uint)Initializes a new instanc

### DAQPulseGeneration Class

Represents a DAQ Counter measurement section of input channels.

#### Derives from

- DAQCounterOutput

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQPulseGeneration : DAQCounterOutput

#### Constructors

| Name | Description |
| --- | --- |
| DAQPulseGeneration(string, string, uint) | Initializes a new instance of the DAQPulseGeneration class. |

#### Properties

| Name | Description |
| --- | --- |
| Counter | Gets the counter channel number. |
| OutputTerminal | Gets or sets the output terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |

#### Methods

| Name | Description |
| --- | --- |
| GetDataChannel(DAQDataChannelType) | Returns a Channel referencing to the desired measurement data. |
| SetCounterIndex(uint) | Sets the index value of the counter. |
| InitChannels() | Initialize the data channels array. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-counter.html language=enus -->
## TOPIC 02462: Counter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-counter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-counter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the counter channel number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Counter { get; private set; }ReturnsThe channel number.

### Counter

Gets the counter channel number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Counter { get; private set; }

#### Returns

The channel number.

Parent topic:

DAQPulseMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-daqpulsemeasurement__string-string-uint.html language=enus -->
## TOPIC 02463: DAQPulseMeasurement(string, string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-daqpulsemeasurement__string-string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-daqpulsemeasurement__string-string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DAQPulseMeasurement class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQPulseMeasurement(string name, string description, uint index)ParametersNameTypeDescriptionnamestringName of CounterdescriptionstringSection descriptionindexuintCou

### DAQPulseMeasurement(string, string, uint)

Initializes a new instance of the [DAQPulseMeasurement](nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DAQPulseMeasurement(string name, string description, uint index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Name of Counter |
| description | string | Section description |
| index | uint | Counter Index |

Parent topic:

DAQPulseMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-getdatachannel__daqdatachanneltype.html language=enus -->
## TOPIC 02464: GetDataChannel(DAQDataChannelType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-getdatachannel__daqdatachanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-getdatachannel__daqdatachanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a Channel referencing to the desired measurement data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override Channel GetDataChannel(DAQDataChannelType type)ParametersNameTypeDescriptiontypeDAQDataChannelTypeThe data channel typeReturnsReturns a channel referencing

### GetDataChannel(DAQDataChannelType)

Returns a [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) referencing to the desired measurement data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetDataChannel(DAQDataChannelType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| type | DAQDataChannelType | The data channel type |

#### Returns

Returns a channel referencing to the desired measurement data.

Parent topic:

DAQPulseMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-initchannels.html language=enus -->
## TOPIC 02465: InitChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-initchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-initchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initialize the data channels array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected override Channel[] InitChannels()ReturnsReturns an array of data channels specific to this measurement type

### InitChannels()

Initialize the data channels array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected override [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html)[] InitChannels()

#### Returns

Returns an array of data channels specific to this measurement type

Parent topic:

DAQPulseMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-inputterminal.html language=enus -->
## TOPIC 02466: InputTerminal

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-inputterminal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-inputterminal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string InputTerminal { get; set; }

### InputTerminal

Gets or sets the input terminal for the counter. A value of [DefaultTerminal](nationalinstruments-veristand-systemdefinitionapi-daqcounter-defaultterminal.html) indicates the default terminal will be used.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string InputTerminal { get; set; }

Parent topic:

DAQPulseMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-setcounterindex__uint.html language=enus -->
## TOPIC 02467: SetCounterIndex(uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-setcounterindex__uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement-setcounterindex__uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the index value of the counter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetCounterIndex(uint index)ParametersNameTypeDescriptionindexuintThe index value of the channel.

### SetCounterIndex(uint)

Sets the index value of the counter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetCounterIndex(uint index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | uint | The index value of the channel. |

Parent topic:

DAQPulseMeasurement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement.html language=enus -->
## TOPIC 02468: DAQPulseMeasurement Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqpulsemeasurement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DAQ Counter measurement section of input channels. Derives fromDAQCounterInputSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQPulseMeasurement : DAQCounterInputConstructorsNameDescriptionDAQPulseMeasurement(string, string, uint)Initializes a new instanc

### DAQPulseMeasurement Class

Represents a DAQ Counter measurement section of input channels.

#### Derives from

- DAQCounterInput

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQPulseMeasurement : DAQCounterInput

#### Constructors

| Name | Description |
| --- | --- |
| DAQPulseMeasurement(string, string, uint) | Initializes a new instance of the DAQPulseMeasurement class. |

#### Properties

| Name | Description |
| --- | --- |
| Counter | Gets the counter channel number. |
| InputTerminal | Gets or sets the input terminal for the counter. A value of DefaultTerminal indicates the default terminal will be used. |

#### Methods

| Name | Description |
| --- | --- |
| GetDataChannel(DAQDataChannelType) | Returns a Channel referencing to the desired measurement data. |
| SetCounterIndex(uint) | Sets the index value of the counter. |
| InitChannels() | Initialize the data channels array. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-datachannels.html language=enus -->
## TOPIC 02469: DataChannels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-datachannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-datachannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all registered data channels for a measurement type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel[] DataChannels { get; }

### DataChannels

Gets all registered data channels for a measurement type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html)[] DataChannels { get; }

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getbooleanproperty__string-out.html language=enus -->
## TOPIC 02470: GetBooleanProperty(string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getbooleanproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getbooleanproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetBooleanProperty(string propertyName, out bool value)ParametersNameTypeDescri

### GetBooleanProperty(string, out bool)

Get value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetBooleanProperty(string propertyName, out bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out bool | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getdatachannel__daqdatachanneltype.html language=enus -->
## TOPIC 02471: GetDataChannel(DAQDataChannelType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getdatachannel__daqdatachanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getdatachannel__daqdatachanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a Channel referencing to the desired measurement data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetDataChannel(DAQDataChannelType type)ParametersNameTypeDescriptiontypeDAQDataChannelTypeThe data channel typeReturnsReturns a channel referencing to the d

### GetDataChannel(DAQDataChannelType)

Returns a [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) referencing to the desired measurement data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetDataChannel(DAQDataChannelType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| type | DAQDataChannelType | The data channel type |

#### Returns

Returns a channel referencing to the desired measurement data.

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getdoubleproperty__string-out.html language=enus -->
## TOPIC 02472: GetDoubleProperty(string, out double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getdoubleproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getdoubleproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetDoubleProperty(string propertyName, out double value)ParametersNameTypeDescri

### GetDoubleProperty(string, out double)

Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetDoubleProperty(string propertyName, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out double | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getenumproperty__string-out-out.html language=enus -->
## TOPIC 02473: GetEnumProperty(string, out string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getenumproperty__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getenumproperty__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type enum specified by propertyName. This gets the enum value as a string as well as the underlying integer value. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetE

### GetEnumProperty(string, out string, out int)

Get value of a property of type enum specified by propertyName. This gets the enum value as a string as well as the underlying integer value. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetEnumProperty(string propertyName, out string enumString, out int enumValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| enumString | out string | String value of the enum |
| enumValue | out int | Integer value of the enum |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti16property__string-out.html language=enus -->
## TOPIC 02474: GetI16Property(string, out short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti16property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti16property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI16Property(string propertyName, out short value)ParametersNameTypeDescriptionpr

### GetI16Property(string, out short)

Get value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI16Property(string propertyName, out short value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out short | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti32property__string-out.html language=enus -->
## TOPIC 02475: GetI32Property(string, out int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI32Property(string propertyName, out int value)ParametersNameTypeDescriptionprop

### GetI32Property(string, out int)

Get value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI32Property(string propertyName, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out int | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti64property__string-out.html language=enus -->
## TOPIC 02476: GetI64Property(string, out long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti64property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-geti64property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetI64Property(string propertyName, out long value)ParametersNameTypeDescriptionpro

### GetI64Property(string, out long)

Get value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetI64Property(string propertyName, out long value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out long | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getproperties__out-out.html language=enus -->
## TOPIC 02477: GetProperties(out string[], out ValueDataType[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getproperties__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getproperties__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of all properties specified by the DAQ plugin for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetProperties(out string[] propertyNames, out ValueDataType[] propertyTypes)ParametersNameTypeDescriptionpropertyNamesout string[]The names of t

### GetProperties(out string[], out ValueDataType[])

Returns a list of all properties specified by the DAQ plugin for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetProperties(out string[] propertyNames, out ValueDataType[] propertyTypes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyNames | out string[] | The names of the properties. |
| propertyTypes | out ValueDataType[] | An enum defining the data type of the property. |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getstringproperty__string-out.html language=enus -->
## TOPIC 02478: GetStringProperty(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getstringproperty__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getstringproperty__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetStringProperty(string propertyName, out string value)ParametersNameTypeDescri

### GetStringProperty(string, out string)

Get value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetStringProperty(string propertyName, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out string | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu16property__string-out.html language=enus -->
## TOPIC 02479: GetU16Property(string, out ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu16property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu16property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU16Property(string propertyName, out ushort value)ParametersNameTypeDescriptionp

### GetU16Property(string, out ushort)

Get value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU16Property(string propertyName, out ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out ushort | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu32property__string-out.html language=enus -->
## TOPIC 02480: GetU32Property(string, out uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu32property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu32property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU32Property(string propertyName, out uint value)ParametersNameTypeDescriptionpro

### GetU32Property(string, out uint)

Get value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU32Property(string propertyName, out uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out uint | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu64property__string-out.html language=enus -->
## TOPIC 02481: GetU64Property(string, out ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu64property__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-getu64property__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void GetU64Property(string propertyName, out ulong value)ParametersNameTypeDescriptionpr

### GetU64Property(string, out ulong)

Get value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void GetU64Property(string propertyName, out ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | out ulong | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-initchannels.html language=enus -->
## TOPIC 02482: InitChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-initchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-initchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initialize the data channels array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIprotected Channel[] InitChannels()ReturnsReturns an array of data channels specific to this measurement type

### InitChannels()

Initialize the data channels array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

protected [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html)[] InitChannels()

#### Returns

Returns an array of data channels specific to this measurement type

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-measurementtype.html language=enus -->
## TOPIC 02483: MeasurementType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-measurementtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-measurementtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the enum specifying DAQ Measurement Type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQMeasurementType MeasurementType { get; }

### MeasurementType

Gets the enum specifying DAQ Measurement Type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQMeasurementType](nationalinstruments-veristand-systemdefinitionapi-daqmeasurementtype.html) MeasurementType { get; }

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-pluginguid.html language=enus -->
## TOPIC 02484: PluginGUID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-pluginguid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-pluginguid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the GUID specifying DAQPlugin XML/Measurement Type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string PluginGUID { get; set; }

### PluginGUID

Gets the GUID specifying DAQPlugin XML/Measurement Type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string PluginGUID { get; set; }

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-resetpropertyvalues.html language=enus -->
## TOPIC 02485: ResetPropertyValues()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-resetpropertyvalues.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-resetpropertyvalues.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reset all properties specified in the DAQ Plugin XML to their defaults. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ResetPropertyValues()

### ResetPropertyValues()

Reset all properties specified in the DAQ Plugin XML to their defaults.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ResetPropertyValues()

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setbooleanproperty__string-bool.html language=enus -->
## TOPIC 02486: SetBooleanProperty(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setbooleanproperty__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setbooleanproperty__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetBooleanProperty(string propertyName, bool value)ParametersNameTypeDescriptio

### SetBooleanProperty(string, bool)

Set value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetBooleanProperty(string propertyName, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | bool | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setdoubleproperty__string-double.html language=enus -->
## TOPIC 02487: SetDoubleProperty(string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setdoubleproperty__string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setdoubleproperty__string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetDoubleProperty(string propertyName, double value)ParametersNameTypeDescriptio

### SetDoubleProperty(string, double)

Set value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetDoubleProperty(string propertyName, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | double | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setenumproperty__string-int.html language=enus -->
## TOPIC 02488: SetEnumProperty(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setenumproperty__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setenumproperty__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type enum specified by propertyName. Enum is specified by integer value. Throws exception if property of this type does not exist in the Plugin XML, or if value is an invalid enumeration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetEnum

### SetEnumProperty(string, int)

Set value of a property of type enum specified by propertyName. Enum is specified by integer value. Throws exception if property of this type does not exist in the Plugin XML, or if value is an invalid enumeration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetEnumProperty(string propertyName, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | int | Integer value of enum |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setenumproperty__string-string.html language=enus -->
## TOPIC 02489: SetEnumProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setenumproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setenumproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type enum specified by propertyName. Enum is specified by a string. Throws exception if property of this type does not exist in the Plugin XML, or if enumString is an invalid enumeration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetEnum

### SetEnumProperty(string, string)

Set value of a property of type enum specified by propertyName. Enum is specified by a string. Throws exception if property of this type does not exist in the Plugin XML, or if enumString is an invalid enumeration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetEnumProperty(string propertyName, string enumString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| enumString | string | Value of enum as a string |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti16property__string-short.html language=enus -->
## TOPIC 02490: SetI16Property(string, short)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti16property__string-short.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti16property__string-short.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI16Property(string propertyName, short value)ParametersNameTypeDescriptionproper

### SetI16Property(string, short)

Set value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI16Property(string propertyName, short value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | short | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti32property__string-int.html language=enus -->
## TOPIC 02491: SetI32Property(string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti32property__string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti32property__string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI32Property(string propertyName, int value)ParametersNameTypeDescriptionproperty

### SetI32Property(string, int)

Set value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI32Property(string propertyName, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | int | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti64property__string-long.html language=enus -->
## TOPIC 02492: SetI64Property(string, long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti64property__string-long.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-seti64property__string-long.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetI64Property(string propertyName, long value)ParametersNameTypeDescriptionpropert

### SetI64Property(string, long)

Set value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetI64Property(string propertyName, long value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | long | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setstringproperty__string-string.html language=enus -->
## TOPIC 02493: SetStringProperty(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setstringproperty__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setstringproperty__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetStringProperty(string propertyName, string value)ParametersNameTypeDescriptio

### SetStringProperty(string, string)

Set value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetStringProperty(string propertyName, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | string | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu16property__string-ushort.html language=enus -->
## TOPIC 02494: SetU16Property(string, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu16property__string-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu16property__string-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU16Property(string propertyName, ushort value)ParametersNameTypeDescriptionprope

### SetU16Property(string, ushort)

Set value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU16Property(string propertyName, ushort value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | ushort | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu32property__string-uint.html language=enus -->
## TOPIC 02495: SetU32Property(string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu32property__string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu32property__string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU32Property(string propertyName, uint value)ParametersNameTypeDescriptionpropert

### SetU32Property(string, uint)

Set value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU32Property(string propertyName, uint value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | uint | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu64property__string-ulong.html language=enus -->
## TOPIC 02496: SetU64Property(string, ulong)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu64property__string-ulong.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype-setu64property__string-ulong.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Set value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetU64Property(string propertyName, ulong value)ParametersNameTypeDescriptionproper

### SetU64Property(string, ulong)

Set value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetU64Property(string propertyName, ulong value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| propertyName | string | Name of Property |
| value | ulong | Value of property |

Parent topic:

DAQSectionType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqsectiontype.html language=enus -->
## TOPIC 02497: DAQSectionType Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqsectiontype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqsectiontype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a generic DAQ data section. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQSectionType : SectionRemarksAbstract class implementing constructors and methods for creating/modifying DAQ data sections based on DAQ Plugin XMLs PropertiesNam

### DAQSectionType Class

Represents a generic DAQ data section.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQSectionType : Section

#### Remarks

Abstract class implementing constructors and methods for creating/modifying DAQ data sections based on DAQ Plugin XMLs

#### Properties

| Name | Description |
| --- | --- |
| DataChannels | Gets all registered data channels for a measurement type. |
| MeasurementType | Gets the enum specifying DAQ Measurement Type. |
| PluginGUID | Gets the GUID specifying DAQPlugin XML/Measurement Type. |

#### Methods

| Name | Description |
| --- | --- |
| GetBooleanProperty(string, out bool) | Get value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetDataChannel(DAQDataChannelType) | Returns a Channel referencing to the desired measurement data. |
| GetDoubleProperty(string, out double) | Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetEnumProperty(string, out string, out int) | Get value of a property of type enum specified by propertyName. This gets the enum value as a string as well as the underlying integer value. Throws exception if property of this type does not exist in the Plugin XML. |
| GetI16Property(string, out short) | Get value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetI32Property(string, out int) | Get value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetI64Property(string, out long) | Get value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetProperties(out string[], out ValueDataType[]) | Returns a list of all properties specified by the DAQ plugin for the channel. |
| GetStringProperty(string, out string) | Get value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetU16Property(string, out ushort) | Get value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetU32Property(string, out uint) | Get value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| GetU64Property(string, out ulong) | Get value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| ResetPropertyValues() | Reset all properties specified in the DAQ Plugin XML to their defaults. |
| SetBooleanProperty(string, bool) | Set value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetDoubleProperty(string, double) | Set value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetEnumProperty(string, string) | Set value of a property of type enum specified by propertyName. Enum is specified by a string. Throws exception if property of this type does not exist in the Plugin XML, or if enumString is an invalid enumeration. |
| SetEnumProperty(string, int) | Set value of a property of type enum specified by propertyName. Enum is specified by integer value. Throws exception if property of this type does not exist in the Plugin XML, or if value is an invalid enumeration. |
| SetI16Property(string, short) | Set value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetI32Property(string, int) | Set value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetI64Property(string, long) | Set value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetStringProperty(string, string) | Set value of a property of type string specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetU16Property(string, ushort) | Set value of a property of type U16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetU32Property(string, uint) | Set value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| SetU64Property(string, ulong) | Set value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML. |
| InitChannels() | Initialize the data channels array. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtask-tasktype.html language=enus -->
## TOPIC 02498: TaskType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtask-tasktype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtask-tasktype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the task type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TaskType TaskType { get; }ReturnsAn enumeration of TaskType.

### TaskType

Gets the task type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TaskType](nationalinstruments-veristand-systemdefinitionapi-tasktype.html) TaskType { get; }

#### Returns

An enumeration of [TaskType](nationalinstruments-veristand-systemdefinitionapi-tasktype.html).

Parent topic:

DAQTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtask.html language=enus -->
## TOPIC 02499: DAQTask Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides an abstract base class for different types of tasks you can assign to DAQ channels. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class DAQTask : SectionThread SafetyAny members of this type are not guaranteed to be thread safe.PropertiesNameDes

### DAQTask Class

Provides an abstract base class for different types of tasks you can assign to DAQ channels.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class DAQTask : Section

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| TaskType | Gets the task type. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionmode.html language=enus -->
## TOPIC 02500: AcquisitionMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-daqtaskai-acquisitionmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of acquisition the task performs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AcquisitionMode AcquisitionMode { get; set; }ReturnsAn enumeration of AcquisitionMode.

### AcquisitionMode

Gets or sets the type of acquisition the task performs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AcquisitionMode](nationalinstruments-veristand-systemdefinitionapi-acquisitionmode.html) AcquisitionMode { get; set; }

#### Returns

An enumeration of [AcquisitionMode](nationalinstruments-veristand-systemdefinitionapi-acquisitionmode.html).

Parent topic:

DAQTaskAI Class
