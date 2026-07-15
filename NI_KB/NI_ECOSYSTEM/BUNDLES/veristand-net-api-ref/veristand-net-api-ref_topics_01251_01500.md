# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=1251 end=1500 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-variables.html language=enus -->
## TOPIC 01251: Variables

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-variables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the array of defined parameter declarations for the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ParameterDeclaration[] Variables { get; set; }ReturnsAn array of ParameterDeclaration objects.

### Variables

Gets or sets the array of defined parameter declarations for the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html)[] Variables { get; set; }

#### Returns

An array of [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) objects.

Parent topic:

Parameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html language=enus -->
## TOPIC 01252: Parameters Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Parameters section of the real-time sequence definition, which contains the parameter declarations for the sequence. Derives fromBaseNodeIEquatable< Parameters >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class Parameters : BaseNode, IEquatable<

### Parameters Class

Represents the **Parameters** section of the real-time sequence definition, which contains the parameter declarations for the sequence.

#### Derives from

- BaseNode
- IEquatable< Parameters >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Parameters : BaseNode, IEquatable< Parameters >

#### Remarks

Use the members of this class to add, configure, or remove parameters from the real-time sequence.

**Accessing this Class:**

- [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-variables-parameters.html)
- Parameters Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Parameters() | Initializes a new instance of Parameters. |
| Parameters(Parameters) | Initializes a new instance of Parameters by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| Variables | Gets or sets the array of defined parameter declarations for the real-time sequence. |

#### Methods

| Name | Description |
| --- | --- |
| AddParameter(ParameterDeclaration) | Adds the specified parameter to the end of the Parameters section. |
| ClearParameters() | Clears all the currently declared parameters from the real-time sequence. |
| Equals(Parameters) | Determines whether the specified other object is equal to the current instance of Parameters. Equivalency is determined using Variables. |
| Equals(object) | Determines whether the specified obj , which must be a Parameters object, is equal to the current Parameters. Equivalency is determined using Variables. |
| GetHashCode() | Serves as a hash function for a Parameters object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-dotfileextension.html language=enus -->
## TOPIC 01253: DotFileExtension

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-dotfileextension.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-dotfileextension.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the default file extension for the path. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string DotFileExtension { get; }ReturnsThe file extension, including the preceding dot. For example: .txt

### DotFileExtension

Gets the default file extension for the path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string DotFileExtension { get; }

#### Returns

The file extension, including the preceding dot. For example: .txt

Parent topic:

PathStringAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-filetypename.html language=enus -->
## TOPIC 01254: FileTypeName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-filetypename.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-filetypename.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the file type name, such as Text Document, for the file at the file path. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string FileTypeName { get; }ReturnsThe file type name.

### FileTypeName

Gets the file type name, such as Text Document, for the file at the file path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string FileTypeName { get; }

#### Returns

The file type name.

Parent topic:

PathStringAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-issavedialogrequested.html language=enus -->
## TOPIC 01255: IsSaveDialogRequested

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-issavedialogrequested.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-issavedialogrequested.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the Save or Open dialog box is requested. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool IsSaveDialogRequested { get; }Returnstrue if the dialog box is requested. Otherwise false.

### IsSaveDialogRequested

Gets a value indicating whether the **Save** or **Open** dialog box is requested.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool IsSaveDialogRequested { get; }

#### Returns

true if the dialog box is requested. Otherwise false.

Parent topic:

PathStringAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-pathstringattribute__string-string-bool.html language=enus -->
## TOPIC 01256: PathStringAttribute(string, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-pathstringattribute__string-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-pathstringattribute__string-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the PathStringAttribute class with the specified fileTypeName and dotFileExtension class and specifies whether a Save or Open dialog is required. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic PathStringAttribute(string fileTypeName,

### PathStringAttribute(string, string, bool)

Initializes a new instance of the [PathStringAttribute](nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute.html) class with the specified *fileTypeName*  and *dotFileExtension*  class and specifies whether a **Save** or **Open** dialog is required.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public PathStringAttribute(string fileTypeName, string dotFileExtension, bool saveDialogRequired)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| fileTypeName | string | The file type name, such as "Text Document". |
| dotFileExtension | string | The file extension, including the preceding dot. For example: .txt |
| saveDialogRequired | bool | If true, specifies that a Save or Open dialog is required. |

Parent topic:

PathStringAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-pathstringattribute__string-string.html language=enus -->
## TOPIC 01257: PathStringAttribute(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-pathstringattribute__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-pathstringattribute__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the PathStringAttribute class with the specified fileTypeName and dotFileExtension . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic PathStringAttribute(string fileTypeName, string dotFileExtension)RemarksThis constructor sets IsSaveDi

### PathStringAttribute(string, string)

Initializes a new instance of the [PathStringAttribute](nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute.html) class with the specified *fileTypeName*  and *dotFileExtension* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public PathStringAttribute(string fileTypeName, string dotFileExtension)

#### Remarks

This constructor sets [IsSaveDialogRequested](nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute-issavedialogrequested.html) to false.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| fileTypeName | string | The file type name, such as "Text Document". |
| dotFileExtension | string | The file extension, including the preceding dot. For example: ".txt" |

Parent topic:

PathStringAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute.html language=enus -->
## TOPIC 01258: PathStringAttribute Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-pathstringattribute.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an attribute that indicates that a string is a file path. Derives fromAttributeSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class PathStringAttribute : AttributeRemarksInherits from System.Attribute. Thread SafetyAny members of this type are not guara

### PathStringAttribute Class

Represents an attribute that indicates that a string is a file path.

#### Derives from

- Attribute

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class PathStringAttribute : Attribute

#### Remarks

Inherits from System.Attribute.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| PathStringAttribute(string, string) | Initializes a new instance of the PathStringAttribute class with the specified fileTypeName and dotFileExtension . |
| PathStringAttribute(string, string, bool) | Initializes a new instance of the PathStringAttribute class with the specified fileTypeName and dotFileExtension class and specifies whether a Save or Open dialog is required. |

#### Properties

| Name | Description |
| --- | --- |
| DotFileExtension | Gets the default file extension for the path. |
| FileTypeName | Gets the file type name, such as Text Document, for the file at the file path. |
| IsSaveDialogRequested | Gets a value indicating whether the Save or Open dialog box is requested. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-dottedproperty.html language=enus -->
## TOPIC 01259: DottedProperty

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-dottedproperty.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-dottedproperty.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the dotted property. A dotted property allows you to access properties of the object returned by a calling property. For example, if a property with the attribute (Foo) returns an object with a property Bar, specifying Bar as the dotted property specifies to access Foo.Bar in place of F

### DottedProperty

Gets or sets the dotted property. A dotted property allows you to access properties of the object returned by a calling property. For example, if a property with the attribute (Foo) returns an object with a property Bar, specifying Bar as the dotted property specifies to access Foo.Bar in place of Foo.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string DottedProperty { get; set; }

#### Returns

The dotted property.

Parent topic:

PropertyUIDisplayAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-identifier.html language=enus -->
## TOPIC 01260: Identifier

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-identifier.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-identifier.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the identifier, or name, for the property. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Identifier { get; }ReturnsThe identifier for the property.

### Identifier

Gets the identifier, or name, for the property.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Identifier { get; }

#### Returns

The identifier for the property.

Parent topic:

PropertyUIDisplayAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-propertyuidisplayattribute__string.html language=enus -->
## TOPIC 01261: PropertyUIDisplayAttribute(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-propertyuidisplayattribute__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute-propertyuidisplayattribute__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the PropertyUIDisplayAttribute class with the specified identifier class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic PropertyUIDisplayAttribute(string identifier)ParametersNameTypeDescriptionidentifierstringThe identifier, or name

### PropertyUIDisplayAttribute(string)

Initializes a new instance of the [PropertyUIDisplayAttribute](nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute.html) class with the specified *identifier*  class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public PropertyUIDisplayAttribute(string identifier)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The identifier, or name, for the property in the Stimulus Profile Editor. |

Parent topic:

PropertyUIDisplayAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute.html language=enus -->
## TOPIC 01262: PropertyUIDisplayAttribute Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-propertyuidisplayattribute.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an attribute that indicates a property is displayed in the Stimulus Profile Editor Property Browser pane. Derives fromAttributeSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class PropertyUIDisplayAttribute : AttributeRemarksInherits from System.Attribu

### PropertyUIDisplayAttribute Class

Represents an attribute that indicates a property is displayed in the Stimulus Profile Editor **Property Browser** pane.

#### Derives from

- Attribute

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class PropertyUIDisplayAttribute : Attribute

#### Remarks

Inherits from System.Attribute.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| PropertyUIDisplayAttribute(string) | Initializes a new instance of the PropertyUIDisplayAttribute class with the specified identifier class. |

#### Properties

| Name | Description |
| --- | --- |
| DottedProperty | Gets or sets the dotted property. A dotted property allows you to access properties of the object returned by a calling property. For example, if a property with the attribute (Foo) returns an object with a property Bar, specifying Bar as the dotted property specifies to access Foo.Bar in place of Foo. |
| Identifier | Gets the identifier, or name, for the property. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-code.html language=enus -->
## TOPIC 01263: Code

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-code.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-code.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Code section of a sequence, which is the top-level container for all sequence code and contains the Setup, Main, and CleanUp sections. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Code Code { get; set; }ReturnsA Code object.

### Code

Gets or sets the **Code** section of a sequence, which is the top-level container for all sequence code and contains the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) sections.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html) Code { get; set; }

#### Returns

A [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html) object.

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-equals__object.html language=enus -->
## TOPIC 01264: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a RealTimeSequence, is equal to the current RealTimeSequence. Equivalency is determined using the Code, References, and Variables that make up the sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic overrid

### Equals(object)

Determines whether the specified *obj* , which must be a [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html), is equal to the current [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html). Equivalency is determined using the [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html), [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html), and [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) that make up the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current real-time sequence. |

#### Returns

true if the specified *obj*  is equal to the current [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html). Otherwise, false.

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-equals__realtimesequence.html language=enus -->
## TOPIC 01265: Equals(RealTimeSequence)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-equals__realtimesequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-equals__realtimesequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other real-time sequence is equal to the current RealTimeSequence. Equivalency is determined using the Code, References, and Variables that make up the sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(RealTimeSe

### Equals(RealTimeSequence)

Determines whether the specified *other*  real-time sequence is equal to the current [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html). Equivalency is determined using the [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html), [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html), and [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) that make up the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(RealTimeSequence other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | RealTimeSequence | The RealTimeSequence to compare with the current sequence. |

#### Returns

true if the specified *other*  sequence is equal to the current [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html). Otherwise, false.

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-findallcalledsubsequencepaths.html language=enus -->
## TOPIC 01266: FindAllCalledSubsequencePaths()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-findallcalledsubsequencepaths.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-findallcalledsubsequencepaths.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finds all of the sub-sequences that the current real-time sequence calls and returns an array of file paths to the sub-sequences. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string[] FindAllCalledSubsequencePaths()ReturnsAn array of string objects containing th

### FindAllCalledSubsequencePaths()

Finds all of the sub-sequences that the current real-time sequence calls and returns an array of file paths to the sub-sequences.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string[] FindAllCalledSubsequencePaths()

#### Returns

An array of string objects containing the file paths for each sub-sequence called by this real-time sequence. Every sub-sequence call has an entry in the array, even if the same sequence is called multiple times by the current sequence.

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-gethashcode.html language=enus -->
## TOPIC 01267: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a RealTimeSequence. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.Ge

### GetHashCode()

Serves as a hash function for a [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html). The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html).

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence.html language=enus -->
## TOPIC 01268: RealTimeSequence()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the RealTimeSequence class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic RealTimeSequence()

### RealTimeSequence()

Initializes a new instance of the [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public RealTimeSequence()

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__realtimesequence.html language=enus -->
## TOPIC 01269: RealTimeSequence(RealTimeSequence)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__realtimesequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__realtimesequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the RealTimeSequence class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic RealTimeSequence(RealTimeSequence node)RemarksThis constructor also copies the FileFormatVersion and Version values of the sequ

### RealTimeSequence(RealTimeSequence)

Initializes a new instance of the [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public RealTimeSequence(RealTimeSequence node)

#### Remarks

This constructor also copies the [FileFormatVersion](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-fileformatversion.html) and [Version](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-version.html) values of the sequence specified by *node* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | RealTimeSequence | The instance of RealTimeSequence to copy. |

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__string-datavalue.html language=enus -->
## TOPIC 01270: RealTimeSequence(string, DataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__string-datavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__string-datavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the RealTimeSequence class and creates a new, empty sequence with the specified return, or output, value. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic RealTimeSequence(string returnVariableIdentifier, DataValue returnValue)Parameter

### RealTimeSequence(string, DataValue)

Initializes a new instance of the [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html) class and creates a new, empty sequence with the specified return, or output, value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public RealTimeSequence(string returnVariableIdentifier, DataValue returnValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| returnVariableIdentifier | string | The identifier, or name, of the return variable. |
| returnValue | DataValue | The type and default value of the return variable. |

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__string.html language=enus -->
## TOPIC 01271: RealTimeSequence(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-realtimesequence__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the RealTimeSequence class for the file at the specified file path. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic RealTimeSequence(string file)ParametersNameTypeDescriptionfilestringThe location of the sequence file on disk.Exception

### RealTimeSequence(string)

Initializes a new instance of the [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html) class for the file at the specified *file*  path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public RealTimeSequence(string file)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file | string | The location of the sequence file on disk. |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentNullException | file is null. |
| ArgumentException | file is an empty string. |
| FileNotFoundException | file does not exist. |
| DirectoryNotFoundException | Any of the directories in the file path do not exist. |
| InvalidOperationException | file does not match the defined schema for a real-time sequence file. |

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-references.html language=enus -->
## TOPIC 01272: References

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-references.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-references.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the References section of the real-time sequence, which is represented by the References pane in the Stimulus Profile Editor. You can use this section to add references to other real-time sequences, which allows you to call those sequences from expressions within the current sequence. S

### References

Gets or sets the [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) section of the real-time sequence, which is represented by the **References** pane in the Stimulus Profile Editor. You can use this section to add references to other real-time sequences, which allows you to call those sequences from expressions within the current sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) References { get; set; }

#### Returns

A [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) object.

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-savesequence__string.html language=enus -->
## TOPIC 01273: SaveSequence(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-savesequence__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-savesequence__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the real-time sequence to the specified file name and location. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void SaveSequence(string file)ParametersNameTypeDescriptionfilestringThe location, including file name, on disk to which to save the sequence.

### SaveSequence(string)

Saves the real-time sequence to the specified *file*  name and location.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void SaveSequence(string file)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file | string | The location, including file name, on disk to which to save the sequence. |

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-sequencename.html language=enus -->
## TOPIC 01274: SequenceName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-sequencename.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-sequencename.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the real-time sequence. This name is derived from the name of the saved sequence file, and is the file name without the file extension. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string SequenceName { get; }ReturnsThe name of the real-time seq

### SequenceName

Gets the name of the real-time sequence. This name is derived from the name of the saved sequence file, and is the file name without the file extension.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string SequenceName { get; }

#### Returns

The name of the real-time sequence.

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-variables.html language=enus -->
## TOPIC 01275: Variables

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-variables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Variables section of the real-time sequence, which is represented by the Variables pane in the Stimulus Profile Editor. This section contains all the variables the sequence has access to at run time and can us in expressions. It includes Parameters, LocalVariables, ChannelReferences

### Variables

Gets or sets the [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) section of the real-time sequence, which is represented by the **Variables** pane in the Stimulus Profile Editor. This section contains all the variables the sequence has access to at run time and can us in expressions. It includes [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html), [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html), [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html), and the [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html), or output value, of the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) Variables { get; set; }

#### Returns

A [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) object.

Parent topic:

RealTimeSequence Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html language=enus -->
## TOPIC 01276: RealTimeSequence Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a real-time sequence, which is a program that can deploy to a target with a system definition file and read/write channels defined in the system definition file. Derives fromRootNodeIEquatable< RealTimeSequence >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApip

### RealTimeSequence Class

Represents a real-time sequence, which is a program that can deploy to a target with a system definition file and read/write channels defined in the system definition file.

#### Derives from

- RootNode
- IEquatable< RealTimeSequence >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class RealTimeSequence : RootNode, IEquatable< RealTimeSequence >

#### Remarks

A sequence can have zero or more [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) (defined by [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html)), zero or more [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) (defined by [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html)), zero or more [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) (defined by [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html)), and one output variable (defined by [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html)). The sequence executes a set of statements contained in its [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) sections. Each statement can operate on its own set of [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html).

Use the members of this class to access the various sections of a sequence, find any subsequences that it calls, and to save the sequence file.

**Accessing this Class:**

- [RefreshSequenceCall()](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-refreshsequencecall.html)
- RealTimeSequence Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| RealTimeSequence(RealTimeSequence) | Initializes a new instance of the RealTimeSequence class by copying an existing instance. |
| RealTimeSequence() | Initializes a new instance of the RealTimeSequence class. |
| RealTimeSequence(string, DataValue) | Initializes a new instance of the RealTimeSequence class and creates a new, empty sequence with the specified return, or output, value. |
| RealTimeSequence(string) | Initializes a new instance of the RealTimeSequence class for the file at the specified file path. |

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets or sets the Code section of a sequence, which is the top-level container for all sequence code and contains the Setup, Main, and CleanUp sections. |
| References | Gets or sets the References section of the real-time sequence, which is represented by the References pane in the Stimulus Profile Editor. You can use this section to add references to other real-time sequences, which allows you to call those sequences from expressions within the current sequence. |
| SequenceName | Gets the name of the real-time sequence. This name is derived from the name of the saved sequence file, and is the file name without the file extension. |
| Variables | Gets or sets the Variables section of the real-time sequence, which is represented by the Variables pane in the Stimulus Profile Editor. This section contains all the variables the sequence has access to at run time and can us in expressions. It includes Parameters, LocalVariables, ChannelReferences, and the ReturnDeclaration, or output value, of the sequence. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Determines whether the specified obj , which must be a RealTimeSequence, is equal to the current RealTimeSequence. Equivalency is determined using the Code, References, and Variables that make up the sequence. |
| Equals(RealTimeSequence) | Determines whether the specified other real-time sequence is equal to the current RealTimeSequence. Equivalency is determined using the Code, References, and Variables that make up the sequence. |
| FindAllCalledSubsequencePaths() | Finds all of the sub-sequences that the current real-time sequence calls and returns an array of file paths to the sub-sequences. |
| GetHashCode() | Serves as a hash function for a RealTimeSequence. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |
| SaveSequence(string) | Saves the real-time sequence to the specified file name and location. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-alias.html language=enus -->
## TOPIC 01277: Alias

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-alias.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-alias.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the alias for the reference. You use this alias to call the sequence from an Expression. This alias must be a valid identifier. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Alias { get; set; }ReturnsThe alias for the reference.

### Alias

Gets or sets the alias for the reference. You use this alias to call the sequence from an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html). This alias must be a valid identifier.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Alias { get; set; }

#### Returns

The alias for the reference.

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-equals__object.html language=enus -->
## TOPIC 01278: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a Reference, is equal to the current Reference. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj)RemarksOverrides object.Equals(object). ParametersNameTypeDescriptionobjobjectThe ob

### Equals(object)

Determines whether the specified *obj* , which must be a [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html), is equal to the current [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current reference. |

#### Returns

true if the specified *obj*  is equal to the current [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html). Otherwise, false.

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-equals__reference.html language=enus -->
## TOPIC 01279: Equals(Reference)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-equals__reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-equals__reference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current Reference. Equivalency is determined using the Path and Alias for the reference. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Reference other)ParametersNameTypeDescriptionotherRefe

### Equals(Reference)

Determines whether the specified *other*  object is equal to the current [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html). Equivalency is determined using the [Path](nationalinstruments-veristand-realtimesequencedefinitionapi-reference-path.html) and [Alias](nationalinstruments-veristand-realtimesequencedefinitionapi-reference-alias.html) for the reference.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Reference other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Reference | The Reference to compare with the current reference. |

#### Returns

true if the specified *other*  object is equal to the current [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html). Otherwise, false.

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-gethashcode.html language=enus -->
## TOPIC 01280: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Reference. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.GetHashCo

### GetHashCode()

Serves as a hash function for a [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html). The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html).

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-path.html language=enus -->
## TOPIC 01281: Path

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-path.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-path.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the path to the referenced sequence on disk. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Path { get; set; }ReturnsThe path to the sequence.

### Path

Gets or sets the path to the referenced sequence on disk.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Path { get; set; }

#### Returns

The path to the sequence.

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference.html language=enus -->
## TOPIC 01282: Reference()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Reference. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Reference()RemarksThis constructor sets Alias to "Alias" and sets Path to "C:\path.nivsseq".

### Reference()

Initializes a new instance of [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Reference()

#### Remarks

This constructor sets [Alias](nationalinstruments-veristand-realtimesequencedefinitionapi-reference-alias.html) to "Alias" and sets [Path](nationalinstruments-veristand-realtimesequencedefinitionapi-reference-path.html) to "C:\path.nivsseq".

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference__reference.html language=enus -->
## TOPIC 01283: Reference(Reference)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference__reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference__reference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Reference by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Reference(Reference node)ParametersNameTypeDescriptionnodeReferenceThe instance of Reference to copy.

### Reference(Reference)

Initializes a new instance of [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Reference(Reference node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Reference | The instance of Reference to copy. |

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference__string-string.html language=enus -->
## TOPIC 01284: Reference(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference-reference__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Reference for the sequence with the specified alias and path . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Reference(string alias, string path)ParametersNameTypeDescriptionaliasstringThe alias used to call the sequence from an expr

### Reference(string, string)

Initializes a new instance of [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html) for the sequence with the specified *alias*  and *path* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Reference(string alias, string path)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alias | string | The alias used to call the sequence from an expression. This alias must be a valid identifier. |
| path | string | The path to the referenced sequence on disk. |

Parent topic:

Reference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html language=enus -->
## TOPIC 01285: Reference Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a reference to a real-time sequence. This reference contains an alias that the current sequence can use to call the referenced sequence from an Expression. Derives fromBaseNodeIEquatable< Reference >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class R

### Reference Class

Represents a reference to a real-time sequence. This reference contains an alias that the current sequence can use to call the referenced sequence from an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

#### Derives from

- BaseNode
- IEquatable< Reference >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Reference : BaseNode, IEquatable< Reference >

#### Remarks

Use the members of this class to configure a reference to a real-time sequence.

**Accessing this Class:**

- [ReferenceList](nationalinstruments-veristand-realtimesequencedefinitionapi-references-referencelist.html)
- Reference Constructor

Foo.nivsseq

Foo.nivsseq

- Alias: Foo
- Parameters: Numeric1, Numeric2
- Output: NumericOut

f(x)

Foo

Numeric1

Numeric2

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Reference() | Initializes a new instance of Reference. |
| Reference(Reference) | Initializes a new instance of Reference by copying an existing instance. |
| Reference(string, string) | Initializes a new instance of Reference for the sequence with the specified alias and path . |

#### Properties

| Name | Description |
| --- | --- |
| Alias | Gets or sets the alias for the reference. You use this alias to call the sequence from an Expression. This alias must be a valid identifier. |
| Path | Gets or sets the path to the referenced sequence on disk. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Reference) | Determines whether the specified other object is equal to the current Reference. Equivalency is determined using the Path and Alias for the reference. |
| Equals(object) | Determines whether the specified obj , which must be a Reference, is equal to the current Reference. |
| GetHashCode() | Serves as a hash function for a Reference. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references-addreference__reference.html language=enus -->
## TOPIC 01286: AddReference(Reference)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references-addreference__reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references-addreference__reference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified reference to the references list for the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddReference(Reference reference)ParametersNameTypeDescriptionreferenceReferenceThe real-time sequence reference to add.

### AddReference(Reference)

Adds the specified *reference*  to the references list for the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddReference(Reference reference)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| reference | Reference | The real-time sequence reference to add. |

Parent topic:

References Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references-equals__object.html language=enus -->
## TOPIC 01287: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a References object, is equal to the current References instance. Equivalency is determined using the Setup, Main, and CleanUp sections of sequence code. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override b

### Equals(object)

Determines whether the specified *obj* , which must be a [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) object, is equal to the current [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) instance. Equivalency is determined using the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) sections of sequence code.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current References object. |

#### Returns

true if the specified *obj*  is equal to the current [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) object. Otherwise, false.

Parent topic:

References Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references-equals__references.html language=enus -->
## TOPIC 01288: Equals(References)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references-equals__references.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references-equals__references.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current References instance. Equivalency is determined using the ReferenceList. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(References other)ParametersNameTypeDescriptionotherReferencesTh

### Equals(References)

Determines whether the specified *other*  object is equal to the current [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) instance. Equivalency is determined using the [ReferenceList](nationalinstruments-veristand-realtimesequencedefinitionapi-references-referencelist.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(References other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | References | The References object to compare with the current object. |

#### Returns

true if the specified *other*  object is equal to the current [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) object. Otherwise, false.

Parent topic:

References Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references-gethashcode.html language=enus -->
## TOPIC 01289: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a References object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.G

### GetHashCode()

Serves as a hash function for a [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) object.

Parent topic:

References Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references-referencelist.html language=enus -->
## TOPIC 01290: ReferenceList

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references-referencelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references-referencelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets an array of all the defined references for the current real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Reference[] ReferenceList { get; set; }ReturnsAn array of Reference objects.

### ReferenceList

Gets or sets an array of all the defined references for the current real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html)[] ReferenceList { get; set; }

#### Returns

An array of [Reference](nationalinstruments-veristand-realtimesequencedefinitionapi-reference.html) objects.

Parent topic:

References Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references-references.html language=enus -->
## TOPIC 01291: References()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references-references.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references-references.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of References. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic References()

### References()

Initializes a new instance of [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public References()

Parent topic:

References Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references-references__references.html language=enus -->
## TOPIC 01292: References(References)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references-references__references.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references-references__references.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of References by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic References(References node)ParametersNameTypeDescriptionnodeReferencesThe instance of References to copy.

### References(References)

Initializes a new instance of [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public References(References node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | References | The instance of References to copy. |

Parent topic:

References Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-references.html language=enus -->
## TOPIC 01293: References Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-references.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-references.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the References section of the real-time sequence, which is represented by the References pane in the Stimulus Profile Editor. This section contains references to other real-time sequences, which you can call from expressions within the current sequence. Derives fromBaseNodeIEquatable< Ref

### References Class

Represents the References section of the real-time sequence, which is represented by the **References** pane in the Stimulus Profile Editor. This section contains references to other real-time sequences, which you can call from expressions within the current sequence.

#### Derives from

- BaseNode
- IEquatable< References >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class References : BaseNode, IEquatable< References >

#### Remarks

Use the members of this class to get or set the sub-sequences that you can call by reference from the current sequence. Calling real-time sequences by reference is useful if you want to run multiple sequences in parallel.

**Accessing this Class:**

- [References](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-references.html)
- References Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| References() | Initializes a new instance of References. |
| References(References) | Initializes a new instance of References by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| ReferenceList | Gets or sets an array of all the defined references for the current real-time sequence. |

#### Methods

| Name | Description |
| --- | --- |
| AddReference(Reference) | Adds the specified reference to the references list for the real-time sequence. |
| Equals(References) | Determines whether the specified other object is equal to the current References instance. Equivalency is determined using the ReferenceList. |
| Equals(object) | Determines whether the specified obj , which must be a References object, is equal to the current References instance. Equivalency is determined using the Setup, Main, and CleanUp sections of sequence code. |
| GetHashCode() | Serves as a hash function for a References object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-defaultvalue.html language=enus -->
## TOPIC 01294: DefaultValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-defaultvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default value of the return variable. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override DataValue DefaultValue { get; set; }ReturnsA DataValue object.

### DefaultValue

Gets or sets the default value of the return variable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override [DataValue](nationalinstruments-veristand-data-datavalue.html) DefaultValue { get; set; }

#### Returns

A DataValue object.

Parent topic:

ReturnDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration.html language=enus -->
## TOPIC 01295: ReturnDeclaration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ReturnDeclaration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ReturnDeclaration()RemarksThis constructor sets Identifier to "Output" and sets DefaultValue to a VoidValue.

### ReturnDeclaration()

Initializes a new instance of [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ReturnDeclaration()

#### Remarks

This constructor sets [Identifier](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-identifier.html) to "Output" and sets [DefaultValue](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-defaultvalue.html) to a [VoidValue](nationalinstruments-veristand-data-voidvalue.html).

Parent topic:

ReturnDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration__returndeclaration.html language=enus -->
## TOPIC 01296: ReturnDeclaration(ReturnDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration__returndeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration__returndeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ReturnDeclaration by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ReturnDeclaration(ReturnDeclaration node)ParametersNameTypeDescriptionnodeReturnDeclarationThe instance of ReturnDeclaration to copy.

### ReturnDeclaration(ReturnDeclaration)

Initializes a new instance of [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ReturnDeclaration(ReturnDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ReturnDeclaration | The instance of ReturnDeclaration to copy. |

Parent topic:

ReturnDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration__string-datavalue.html language=enus -->
## TOPIC 01297: ReturnDeclaration(string, DataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration__string-datavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration-returndeclaration__string-datavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ReturnDeclaration and creates a return variable declaration with the specified identifier and defaultValue . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ReturnDeclaration(string identifier, DataValue defaultValue)ParametersNameType

### ReturnDeclaration(string, DataValue)

Initializes a new instance of [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html) and creates a return variable declaration with the specified *identifier*  and *defaultValue* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ReturnDeclaration(string identifier, DataValue defaultValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The name of the return variable. This name must be a unique, valid identifier. |
| defaultValue | DataValue | The default value and data type of the return variable. If the sequence does not require a return variable, this can be a void value. |

Parent topic:

ReturnDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html language=enus -->
## TOPIC 01298: ReturnDeclaration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a declaration of the return variable of a real-time sequence. Derives fromAbstractDeclarationSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class ReturnDeclaration : AbstractDeclarationRemarksYou can access the return variable of a sequence when you cal

### ReturnDeclaration Class

Represents a declaration of the return variable of a real-time sequence.

#### Derives from

- AbstractDeclaration

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class ReturnDeclaration : AbstractDeclaration

#### Remarks

You can access the return variable of a sequence when you call it from another sequence as a sub-sequence (*y* = Foo(*x*)), or you can use it to get a pass/fail status when the sequence completes execution.

Use the members of this class to get or set the default value of the return variable.

**Accessing this Class:**

- [ReturnType](nationalinstruments-veristand-realtimesequencedefinitionapi-variables-returntype.html)
- ReturnDeclaration Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ReturnDeclaration(string, DataValue) | Initializes a new instance of ReturnDeclaration and creates a return variable declaration with the specified identifier and defaultValue . |
| ReturnDeclaration(ReturnDeclaration) | Initializes a new instance of ReturnDeclaration by copying an existing instance. |
| ReturnDeclaration() | Initializes a new instance of ReturnDeclaration. |

#### Properties

| Name | Description |
| --- | --- |
| DefaultValue | Gets or sets the default value of the return variable. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-fileformatversion.html language=enus -->
## TOPIC 01299: FileFormatVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-fileformatversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-fileformatversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the file format version of the real-time sequence definition file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic XMLVersionInfo FileFormatVersion { get; set; }RemarksThis property reads or writes the attributes of the < FileFormatVersion > tag. Retur

### FileFormatVersion

Gets or sets the file format version of the real-time sequence definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public XMLVersionInfo FileFormatVersion { get; set; }

#### Remarks

This property reads or writes the attributes of the < FileFormatVersion > tag.

#### Returns

An XMLVersionInfo object.

Parent topic:

RootNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-filename.html language=enus -->
## TOPIC 01300: FileName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-filename.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-filename.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the real-time sequence definition file on disk. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string FileName { get; }ReturnsThe name of the file.

### FileName

Gets the name of the real-time sequence definition file on disk.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string FileName { get; }

#### Returns

The name of the file.

Parent topic:

RootNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-filepath.html language=enus -->
## TOPIC 01301: FilePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-filepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-filepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the full path on disk to the real-time system definition file. Setting this property updates the value of FileName. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string FilePath { get; }ReturnsThe full path to the file.

### FilePath

Gets the full path on disk to the real-time system definition file. Setting this property updates the value of [FileName](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-filename.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string FilePath { get; }

#### Returns

The full path to the file.

Parent topic:

RootNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-rootnode.html language=enus -->
## TOPIC 01302: RootNode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-rootnode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-rootnode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RootNode and constructs a new root node with 0.0.0.0 for the FileFormatVersion and Version properties. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected RootNode()RemarksThis constructor is protected.

### RootNode()

Initializes a new instance of [RootNode](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html) and constructs a new root node with 0.0.0.0 for the [FileFormatVersion](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-fileformatversion.html) and [Version](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-version.html) properties.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected RootNode()

#### Remarks

This constructor is protected.

Parent topic:

RootNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-rootnode__rootnode.html language=enus -->
## TOPIC 01303: RootNode(RootNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-rootnode__rootnode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-rootnode__rootnode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RootNode by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected RootNode(RootNode node)RemarksThis constructor is protected. ParametersNameTypeDescriptionnodeRootNodeThe instance of RootNode to copy.

### RootNode(RootNode)

Initializes a new instance of [RootNode](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected RootNode(RootNode node)

#### Remarks

This constructor is protected.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | RootNode | The instance of RootNode to copy. |

Parent topic:

RootNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-version.html language=enus -->
## TOPIC 01304: Version

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-version.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode-version.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the version of the real-time sequence definition file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic XMLVersionInfo Version { get; set; }RemarksThis property reads or writes the attributes of the < Version > tag. ReturnsAn XMLVersionInfo object.

### Version

Gets or sets the version of the real-time sequence definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public XMLVersionInfo Version { get; set; }

#### Remarks

This property reads or writes the attributes of the < Version > tag.

#### Returns

An XMLVersionInfo object.

Parent topic:

RootNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html language=enus -->
## TOPIC 01305: RootNode Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the abstract base class from which real-time sequence and stimulus profile files inherit. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class RootNode : BaseNodeRemarksRootNode provides an abstract base class for RealTimeSequence an

### RootNode Class

Represents the abstract base class from which real-time sequence and stimulus profile files inherit.

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class RootNode : BaseNode

#### Remarks

**RootNode** provides an abstract base class for [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html) and [StimulusProfile](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile.html) objects.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| RootNode() | Initializes a new instance of RootNode and constructs a new root node with 0.0.0.0 for the FileFormatVersion and Version properties. |
| RootNode(RootNode) | Initializes a new instance of RootNode by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| FileFormatVersion | Gets or sets the file format version of the real-time sequence definition file. |
| FileName | Gets the name of the real-time sequence definition file on disk. |
| FilePath | Gets the full path on disk to the real-time system definition file. Setting this property updates the value of FileName. |
| Version | Gets or sets the version of the real-time sequence definition file. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-setup-setup.html language=enus -->
## TOPIC 01306: Setup()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-setup-setup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-setup-setup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Setup. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Setup()

### Setup()

Initializes a new instance of [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Setup()

Parent topic:

Setup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-setup-setup__setup.html language=enus -->
## TOPIC 01307: Setup(Setup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-setup-setup__setup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-setup-setup__setup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Setup by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Setup(Setup node)ParametersNameTypeDescriptionnodeSetupThe instance of Setup to copy.

### Setup(Setup)

Initializes a new instance of [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Setup(Setup node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Setup | The instance of Setup to copy. |

Parent topic:

Setup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html language=enus -->
## TOPIC 01308: Setup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Setup section of sequence code, which executes before the Main and CleanUp code sections. This section contains statements that initialize the sequence. Derives fromCodeSectionSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class Setup : CodeSectionR

### Setup Class

Represents the **Setup** section of sequence code, which executes before the [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) code sections. This section contains statements that initialize the sequence.

#### Derives from

- CodeSection

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Setup : CodeSection

#### Remarks

Use this section at the beginning of sequence execution to initialize variables as needed.

**Accessing this Class:**

- [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-code-setup.html)
- Setup Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Setup(Setup) | Initializes a new instance of Setup by copying an existing instance. |
| Setup() | Initializes a new instance of Setup. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__object.html language=enus -->
## TOPIC 01309: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a Statement object, is equal to the current instance of Statement. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj)RemarksOverrides object.Equals(object). ParametersNameTypeDescrip

### Equals(object)

Determines whether the specified *obj* , which must be a [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html) object, is equal to the current instance of [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current Statement object. |

#### Returns

true if the specified *obj*  is equal to the current [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html) object. Otherwise, false.

Parent topic:

Statement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__statement.html language=enus -->
## TOPIC 01310: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Statement. This is an abstract declaration only. Derived classes must implement the correct Equals comparison for that class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equa

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html). This is an abstract declaration only. Derived classes must implement the correct Equals comparison for that class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Statement other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html). Otherwise, false.

Parent topic:

Statement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html language=enus -->
## TOPIC 01311: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Statement object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. This is an abstract declaration only. Derived classes must implement the correct GetHashCode comparison for that class. SyntaxNamespace

### GetHashCode()

Serves as a hash function for a [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. This is an abstract declaration only. Derived classes must implement the correct GetHashCode comparison for that class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) object.

Parent topic:

Statement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-statement-statement.html language=enus -->
## TOPIC 01312: Statement()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-statement-statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-statement-statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Statement. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected Statement()RemarksThis constructor is protected.

### Statement()

Initializes a new instance of [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected Statement()

#### Remarks

This constructor is protected.

Parent topic:

Statement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-statement-statement__statement.html language=enus -->
## TOPIC 01313: Statement(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-statement-statement__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-statement-statement__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Statement by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected Statement(Statement node)RemarksThis constructor is protected. ParametersNameTypeDescriptionnodeStatementThe instance of Statement to copy.

### Statement(Statement)

Initializes a new instance of [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected Statement(Statement node)

#### Remarks

This constructor is protected.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Statement | The instance of Statement to copy. |

Parent topic:

Statement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html language=enus -->
## TOPIC 01314: Statement Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a functional statement that you can add to a real-time sequence. A statement can be any unique component that performs an action within the sequence, and statements can include sub-statements. Block, Expression, IfElse, and AbstractLoop are all common types of statements that you can add

### Statement Class

Represents a functional statement that you can add to a real-time sequence. A statement can be any unique component that performs an action within the sequence, and statements can include sub-statements. [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html), [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html), [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html), and [AbstractLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop.html) are all common types of statements that you can add to a real-time sequence.

#### Derives from

- BaseNode
- IEquatable< Statement >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Statement : BaseNode, IEquatable< Statement >

#### Remarks

This is a base class from which more specific statement types inherit.

**Accessing this Class:**

- [Statements](nationalinstruments-veristand-realtimesequencedefinitionapi-block-statements.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Statement(Statement) | Initializes a new instance of Statement by copying an existing instance. |
| Statement() | Initializes a new instance of Statement. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Determines whether the specified obj , which must be a Statement object, is equal to the current instance of Statement. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of Statement. This is an abstract declaration only. Derived classes must implement the correct Equals comparison for that class. |
| GetHashCode() | Serves as a hash function for a Statement object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. This is an abstract declaration only. Derived classes must implement the correct GetHashCode comparison for that class. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-events.html language=enus -->
## TOPIC 01315: Events

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-events.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-events.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the compilations events, or errors, warnings, and messages, that occur during compilation of a stimulus profile or real-time sequence definition file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CompilationEvent[] Events { get; set; }ReturnsAn arra

### Events

Gets or sets the compilations events, or errors, warnings, and messages, that occur during compilation of a stimulus profile or real-time sequence definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] Events { get; set; }

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects.

Parent topic:

StimulusProfileCompilationException Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-stimulusprofilecompilationexception.html language=enus -->
## TOPIC 01316: StimulusProfileCompilationException()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-stimulusprofilecompilationexception.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-stimulusprofilecompilationexception.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StimulusProfileCompilationException. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic StimulusProfileCompilationException()

### StimulusProfileCompilationException()

Initializes a new instance of [StimulusProfileCompilationException](nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public StimulusProfileCompilationException()

Parent topic:

StimulusProfileCompilationException Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-stimulusprofilecompilationexception__compilationevent_arr1.html language=enus -->
## TOPIC 01317: StimulusProfileCompilationException(CompilationEvent[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-stimulusprofilecompilationexception__compilationevent_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-stimulusprofilecompilationexception__compilationevent_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StimulusProfileCompilationException that recognizes the specified events as compilation errors. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic StimulusProfileCompilationException(CompilationEvent[] events)ParametersNameTypeDescription

### StimulusProfileCompilationException(CompilationEvent[])

Initializes a new instance of [StimulusProfileCompilationException](nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception.html) that recognizes the specified *events*  as compilation errors.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public StimulusProfileCompilationException(CompilationEvent[] events)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| events | CompilationEvent[] | The events to recognize as compilation errors. |

Parent topic:

StimulusProfileCompilationException Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception.html language=enus -->
## TOPIC 01318: StimulusProfileCompilationException Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents errors, warnings, or messages that occur during the compilation of a stimulus profile or real-time sequence definition file. Derives fromVeriStandExceptionSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class StimulusProfileCompilationException : VeriSta

### StimulusProfileCompilationException Class

Represents errors, warnings, or messages that occur during the compilation of a stimulus profile or real-time sequence definition file.

#### Derives from

- VeriStandException

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class StimulusProfileCompilationException : VeriStandException

#### Remarks

Use the members of this class to get or set the compilations events, or errors, warnings, and messages, that occur during compilation of a stimulus profile file.

**Accessing this Class:**

- StimulusProfileCompilationException Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| StimulusProfileCompilationException(CompilationEvent[]) | Initializes a new instance of StimulusProfileCompilationException that recognizes the specified events as compilation errors. |
| StimulusProfileCompilationException() | Initializes a new instance of StimulusProfileCompilationException. |

#### Properties

| Name | Description |
| --- | --- |
| Events | Gets or sets the compilations events, or errors, warnings, and messages, that occur during compilation of a stimulus profile or real-time sequence definition file. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-equals__statement.html language=enus -->
## TOPIC 01319: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StopTask. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksOverrides Equals(Statement). ParametersNameTypeDescriptionotherStatementThe State

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

Overrides [Equals(Statement)](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html). Otherwise, false.

Parent topic:

StopTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-equals__stoptask.html language=enus -->
## TOPIC 01320: Equals(StopTask)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-equals__stoptask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-equals__stoptask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of StopTask. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(StopTask other)ParametersNameTypeDescriptionotherStopTaskThe StopTask object to compare with the current instance

### Equals(StopTask)

Determines whether the specified *other*  object is equal to the current instance of [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(StopTask other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | StopTask | The StopTask object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

StopTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-gethashcode.html language=enus -->
## TOPIC 01321: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a StopTask object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCod

### GetHashCode()

Serves as a hash function for a [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html) object.

Parent topic:

StopTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask.html language=enus -->
## TOPIC 01322: StopTask()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StopTask. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic StopTask()RemarksThis constructor sets TaskName to "TaskName". You must update this string to valid task identifier to stop a task.

### StopTask()

Initializes a new instance of [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public StopTask()

#### Remarks

This constructor sets [TaskName](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-taskname.html) to "TaskName". You must update this string to valid task identifier to stop a task.

Parent topic:

StopTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask__stoptask.html language=enus -->
## TOPIC 01323: StopTask(StopTask)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask__stoptask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask__stoptask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StopTask by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic StopTask(StopTask node)ParametersNameTypeDescriptionnodeStopTaskThe instance of StopTask to copy.

### StopTask(StopTask)

Initializes a new instance of [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public StopTask(StopTask node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | StopTask | The instance of StopTask to copy. |

Parent topic:

StopTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask__string.html language=enus -->
## TOPIC 01324: StopTask(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-stoptask__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of StopTask that stops the specified taskName . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic StopTask(string taskName)ParametersNameTypeDescriptiontaskNamestringThe name of the task to stop. This name must be a valid identifier.

### StopTask(string)

Initializes a new instance of [StopTask](nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html) that stops the specified *taskName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public StopTask(string taskName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| taskName | string | The name of the task to stop. This name must be a valid identifier. |

Parent topic:

StopTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-taskname.html language=enus -->
## TOPIC 01325: TaskName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-taskname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask-taskname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the Task in the Multitask structure to stop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string TaskName { get; set; }RemarksYou can use the IsValidIdentifier method to determine if a string is a valid identifier. ReturnsThe name of the

### TaskName

Gets or sets the name of the [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html) in the [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) structure to stop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string TaskName { get; set; }

#### Remarks

Note

You can use the [IsValidIdentifier](nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html) method to determine if a string is a valid identifier.

#### Returns

The name of the task to stop. This name must be a valid identifier.

Parent topic:

StopTask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html language=enus -->
## TOPIC 01326: StopTask Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-stoptask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Stop Task statement, which stops a task in a Multitask structure. When a task is stopped, any sub-sequences executing in that task immediately execute their CleanUp section. Any sub-tasks are also stopped. Derives fromStatementIEquatable< StopTask >SyntaxNamespace: NationalInstruments.V

### StopTask Class

Represents a **Stop Task** statement, which stops a task in a [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) structure. When a task is stopped, any sub-sequences executing in that task immediately execute their [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) section. Any sub-tasks are also stopped.

#### Derives from

- Statement
- IEquatable< StopTask >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class StopTask : Statement, IEquatable< StopTask >

#### Remarks

Use the members of this class to specify the task to stop.

**Accessing this Class:**

- StopTask Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| StopTask() | Initializes a new instance of StopTask. |
| StopTask(StopTask) | Initializes a new instance of StopTask by copying an existing instance. |
| StopTask(string) | Initializes a new instance of StopTask that stops the specified taskName . |

#### Properties

| Name | Description |
| --- | --- |
| TaskName | Gets or sets the name of the Task in the Multitask structure to stop. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(StopTask) | Determines whether the specified other object is equal to the current instance of StopTask. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of StopTask. |
| GetHashCode() | Serves as a hash function for a StopTask object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-cases.html language=enus -->
## TOPIC 01327: Cases

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-cases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-cases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the list of case statements that the Switch statement contains and evaluates against the TestExpression. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Cases Cases { get; set; }ReturnsA Cases object.

### Cases

Gets or sets the list of case statements that the [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement contains and evaluates against the [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) Cases { get; set; }

#### Returns

A [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-default.html language=enus -->
## TOPIC 01328: Default

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-default.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-default.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default case statement to execute if the TestExpression does not match the CaseValue of any of the Cases. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DefaultCase Default { get; set; }ReturnsA DefaultCase object.

### Default

Gets or sets the default case statement to execute if the [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html) does not match the [CaseValue](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casevalue.html) of any of the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [DefaultCase](nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html) Default { get; set; }

#### Returns

A [DefaultCase](nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html) object.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-equals__statement.html language=enus -->
## TOPIC 01329: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Switch. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksOverrides Equals(Statement). ParametersNameTypeDescriptionotherStatementThe Stateme

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

Overrides [Equals(Statement)](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-equals__statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html). Otherwise, false.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-equals__switch.html language=enus -->
## TOPIC 01330: Equals(Switch)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-equals__switch.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-equals__switch.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Switch. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Switch other)ParametersNameTypeDescriptionotherSwitchThe Switch object to compare with the current instance.Returns

### Equals(Switch)

Determines whether the specified *other*  object is equal to the current instance of [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Switch other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Switch | The Switch object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-gethashcode.html language=enus -->
## TOPIC 01331: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Switch object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCode.

### GetHashCode()

Serves as a hash function for a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) object.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch.html language=enus -->
## TOPIC 01332: Switch()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Switch. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Switch()RemarksThis constructor sets TestExpression to "0".

### Switch()

Initializes a new instance of [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Switch()

#### Remarks

This constructor sets [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html) to "0".

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__expression-cases-defaultcase.html language=enus -->
## TOPIC 01333: Switch(Expression, Cases, DefaultCase)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__expression-cases-defaultcase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__expression-cases-defaultcase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Switch and creates a switch statement with the specified testExpression , list of cases to evaluate, and defaultCase . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Switch(Expression testExpression, Cases cases, DefaultCase defaultCa

### Switch(Expression, Cases, DefaultCase)

Initializes a new instance of [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) and creates a switch statement with the specified *testExpression* , list of *cases*  to evaluate, and *defaultCase* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Switch(Expression testExpression, Cases cases, DefaultCase defaultCase)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| testExpression | Expression | The expression to evaluate each CaseValue in the Cases list against to determine which case to execute. If this value matches the value of a case, the Switch statement executes that case. If no case matches this value, the statement executes the Default case. |
| cases | Cases | the list of case statements that the Switch statement contains and evaluates against the testExpression . |
| defaultCase | DefaultCase | The default case statement to execute if the testExpression does not match the CaseValue of any of the cases . |

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__expression.html language=enus -->
## TOPIC 01334: Switch(Expression)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Switch and creates a switch statement with the specified testExpression . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Switch(Expression testExpression)ParametersNameTypeDescriptiontestExpressionExpressionThe expression to evaluate

### Switch(Expression)

Initializes a new instance of [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) and creates a switch statement with the specified *testExpression* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Switch(Expression testExpression)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| testExpression | Expression | The expression to evaluate each CaseValue in the Cases list against to determine which case to execute. If this value matches the value of a case, the Switch statement executes that case. If no case matches this value, the statement executes the Default case. |

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__switch.html language=enus -->
## TOPIC 01335: Switch(Switch)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__switch.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-switch__switch.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Switch by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Switch(Switch node)ParametersNameTypeDescriptionnodeSwitchThe instance of Switch to copy.

### Switch(Switch)

Initializes a new instance of [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Switch(Switch node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Switch | The instance of Switch to copy. |

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html language=enus -->
## TOPIC 01336: TestExpression

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The expression to evaluate each CaseValue in the Cases list against to determine which case to execute. If this value matches the value of a case, the Switch statement executes that case. If no case matches this value, the statement executes the Default case. SyntaxNamespace: NationalInstruments.Ver

### TestExpression

The expression to evaluate each [CaseValue](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casevalue.html) in the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-cases.html) list against to determine which case to execute. If this value matches the value of a case, the [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement executes that case. If no case matches this value, the statement executes the [Default](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-default.html) case.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) TestExpression { get; set; }

#### Returns

An [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) object.

Parent topic:

Switch Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html language=enus -->
## TOPIC 01337: Switch Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Switch statement, which evaluates a TestExpression to determine which of multiple Cases to execute. Derives fromStatementIEquatable< Switch >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class Switch : Statement, IEquatable< Switch >RemarksUse the me

### Switch Class

Represents a **Switch** statement, which evaluates a [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html) to determine which of multiple [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) to execute.

#### Derives from

- Statement
- IEquatable< Switch >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Switch : Statement, IEquatable< Switch >

#### Remarks

Use the members of this class to get or set the cases that the **Switch** statement contains and the expression it evaluates to determine which case to execute.

**Accessing this Class:**

- Switch Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Switch() | Initializes a new instance of Switch. |
| Switch(Switch) | Initializes a new instance of Switch by copying an existing instance. |
| Switch(Expression) | Initializes a new instance of Switch and creates a switch statement with the specified testExpression . |
| Switch(Expression, Cases, DefaultCase) | Initializes a new instance of Switch and creates a switch statement with the specified testExpression , list of cases to evaluate, and defaultCase . |

#### Properties

| Name | Description |
| --- | --- |
| Cases | Gets or sets the list of case statements that the Switch statement contains and evaluates against the TestExpression. |
| Default | Gets or sets the default case statement to execute if the TestExpression does not match the CaseValue of any of the Cases. |
| TestExpression | The expression to evaluate each CaseValue in the Cases list against to determine which case to execute. If this value matches the value of a case, the Switch statement executes that case. If no case matches this value, the statement executes the Default case. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Switch) | Determines whether the specified other object is equal to the current instance of Switch. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of Switch. |
| GetHashCode() | Serves as a hash function for a Switch object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-task-task.html language=enus -->
## TOPIC 01338: Task()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-task-task.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-task-task.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Task. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Task()RemarksThis constructor sets TaskName to "TaskName".

### Task()

Initializes a new instance of [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Task()

#### Remarks

This constructor sets [TaskName](nationalinstruments-veristand-realtimesequencedefinitionapi-task-taskname.html) to "TaskName".

Parent topic:

Task Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__string-block.html language=enus -->
## TOPIC 01339: Task(string, Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__string-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__string-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Task and creates a task with the specified taskName and body of statements. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Task(string taskName, Block body)RemarksYou can use the IsValidIdentifier method to determine if a string is a

### Task(string, Block)

Initializes a new instance of [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html) and creates a task with the specified *taskName*  and *body*  of statements.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Task(string taskName, Block body)

#### Remarks

Note

You can use the [IsValidIdentifier](nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html) method to determine if a string is a valid identifier.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| taskName | string | The name of the task. This name must be a valid identifier. |
| body | Block | The body of functional statements that the task executes. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__string.html language=enus -->
## TOPIC 01340: Task(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Task and creates a task with the specified taskName . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Task(string taskName)RemarksYou can use the IsValidIdentifier method to determine if a string is a valid identifier. ParametersNameTy

### Task(string)

Initializes a new instance of [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html) and creates a task with the specified *taskName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Task(string taskName)

#### Remarks

Note

You can use the [IsValidIdentifier](nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html) method to determine if a string is a valid identifier.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| taskName | string | The name of the task. This name must be a valid identifier. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__task.html language=enus -->
## TOPIC 01341: Task(Task)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__task.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-task-task__task.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Task by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Task(Task node)ParametersNameTypeDescriptionnodeTaskThe instance of Task to copy.

### Task(Task)

Initializes a new instance of [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Task(Task node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Task | The instance of Task to copy. |

Parent topic:

Task Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-task-taskname.html language=enus -->
## TOPIC 01342: TaskName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-task-taskname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-task-taskname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of a Task. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string TaskName { get; set; }RemarksYou can use the IsValidIdentifier method to determine if a string is a valid identifier. ReturnsThe task name. This name must be a valid identifier.

### TaskName

Gets or sets the name of a [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string TaskName { get; set; }

#### Remarks

Note

You can use the [IsValidIdentifier](nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html) method to determine if a string is a valid identifier.

#### Returns

The task name. This name must be a valid identifier.

Parent topic:

Task Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-task.html language=enus -->
## TOPIC 01343: Task Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-task.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-task.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Task, or block of code, in a Multitask structure. On each time step, the MultiTask structure iteratively executes code from each child Task that it contains. A Task cannot exist outside of a MultiTask structure. Derives fromCodeSectionSyntaxNamespace: NationalInstruments.VeriStand.RealT

### Task Class

Represents a **Task**, or block of code, in a [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) structure. On each time step, the **MultiTask** structure iteratively executes code from each child **Task** that it contains. A **Task** cannot exist outside of a **MultiTask** structure.

#### Derives from

- CodeSection

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Task : CodeSection

#### Remarks

Use the members of this class to set the name and contents of a **Task**.

**Accessing this Class:**

- [Tasks](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-tasks.html)
- Task Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Task(string) | Initializes a new instance of Task and creates a task with the specified taskName . |
| Task(string, Block) | Initializes a new instance of Task and creates a task with the specified taskName and body of statements. |
| Task() | Initializes a new instance of Task. |
| Task(Task) | Initializes a new instance of Task by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| TaskName | Gets or sets the name of a Task. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-converttovalididentifier__string.html language=enus -->
## TOPIC 01344: ConvertToValidIdentifier(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-converttovalididentifier__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-converttovalididentifier__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified identifier to a string that is a valid identifier in a real-time sequence definition. Valid identifiers cannot contain spaces or special characters (except underscores), and cannot start with a number. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionAp

### ConvertToValidIdentifier(string)

Converts the specified *identifier*  to a string that is a valid identifier in a real-time sequence definition. Valid identifiers cannot contain spaces or special characters (except underscores), and cannot start with a number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static string ConvertToValidIdentifier(string identifier)

#### Remarks

This method performs the following conversions:

| Invalid Character | Conversion |
| --- | --- |
|  | "Plus" |
|  | "Minus" |
| Other Non-alphanumeric | "_" |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The identifier to convert. |

#### Returns

A valid identifier.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html language=enus -->
## TOPIC 01345: IsValidIdentifier(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified identifier is a valid identifier in a real-time sequence definition. Valid identifiers cannot contain spaces or special characters (except underscores), and cannot start with a number. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic

### IsValidIdentifier(string)

Determines whether the specified *identifier*  is a valid identifier in a real-time sequence definition. Valid identifiers cannot contain spaces or special characters (except underscores), and cannot start with a number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static bool IsValidIdentifier(string identifier)

#### Remarks

Note

You can use the [ConvertToValidIdentifier](nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-converttovalididentifier__string.html) method to convert an invalid identifier string to a valid one.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The identifier to validate. |

#### Returns

true if the *identifier*  is valid. Otherwise, false.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalidsequencefile__string-out.html language=enus -->
## TOPIC 01346: IsValidSequenceFile(string, out Exception)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalidsequencefile__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalidsequencefile__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the file at the specified path can be converted to a RealTimeSequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic static bool IsValidSequenceFile(string path, out Exception parseException)ParametersNameTypeDescriptionpathstringThe path to th

### IsValidSequenceFile(string, out Exception)

Determines whether the file at the specified *path*  can be converted to a [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static bool IsValidSequenceFile(string path, out Exception parseException)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The path to the file to test. |
| parseException | out Exception | Upon return, an exception that contains the first error encountered while parsing the file. If the file is a valid sequence file, this parameter returns null. |

#### Returns

true if the method can successfully parse the file into a sequence. false if the method encounters an exception while parsing the file.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-keywordlist.html language=enus -->
## TOPIC 01347: KeywordList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-keywordlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-keywordlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of all the keywords that are reserved by the expression language such that they have a specific, pre-defined meaning when used in an Expression. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic static string[] KeywordList()ReturnsAn array containing

### KeywordList()

Returns an array of all the keywords that are reserved by the expression language such that they have a specific, pre-defined meaning when used in an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static string[] KeywordList()

#### Returns

An array containing all the keywords that are reserved by the expression language.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-parseexpression__string.html language=enus -->
## TOPIC 01348: ParseExpression(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-parseexpression__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-parseexpression__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parses the specified expression into a list of key/value pairs. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic static List< KeyValuePair< string, string > > ParseExpression(string expression)ParametersNameTypeDescriptionexpressionstringThe expression to parse. Ret

### ParseExpression(string)

Parses the specified *expression*  into a list of key/value pairs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static List< KeyValuePair< string, string > > ParseExpression(string expression)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expression | string | The expression to parse. |

#### Returns

A List<T> of key/value pairs.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-utilities.html language=enus -->
## TOPIC 01349: Utilities Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-utilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-utilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides a set of static methods for locating and resolving common issues in real-time sequence development, such as invalid sequence files, invalid identifiers, and so on. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class UtilitiesRemarksUse th

### Utilities Class

Provides a set of static methods for locating and resolving common issues in real-time sequence development, such as invalid sequence files, invalid identifiers, and so on.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Utilities

#### Remarks

Use the members of this class to locate and resolve common issues in real-time sequence development.

**Accessing this Class:**

All members of this class are static.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Methods

| Name | Description |
| --- | --- |
| ConvertToValidIdentifier(string) | Converts the specified identifier to a string that is a valid identifier in a real-time sequence definition. Valid identifiers cannot contain spaces or special characters (except underscores), and cannot start with a number. |
| IsValidIdentifier(string) | Determines whether the specified identifier is a valid identifier in a real-time sequence definition. Valid identifiers cannot contain spaces or special characters (except underscores), and cannot start with a number. |
| IsValidSequenceFile(string, out Exception) | Determines whether the file at the specified path can be converted to a RealTimeSequence. |
| KeywordList() | Returns an array of all the keywords that are reserved by the expression language such that they have a specific, pre-defined meaning when used in an Expression. |
| ParseExpression(string) | Parses the specified expression into a list of key/value pairs. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-channelreferences.html language=enus -->
## TOPIC 01350: ChannelReferences

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-channelreferences.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-channelreferences.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the ChannelReferences section, which contains the set of channel references used by a real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferences ChannelReferences { get; set; }ReturnsA ChannelReferences object.

### ChannelReferences

Gets or sets the [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) section, which contains the set of channel references used by a real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) ChannelReferences { get; set; }

#### Returns

A [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) object.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-equals__object.html language=enus -->
## TOPIC 01351: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a Variables object, is equal to the current Variables instance. Equivalency is determined using the LocalVariables, Parameters, and ReturnType. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals

### Equals(object)

Determines whether the specified *obj* , which must be a [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) object, is equal to the current [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) instance. Equivalency is determined using the [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html), [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-variables-parameters.html), and [ReturnType](nationalinstruments-veristand-realtimesequencedefinitionapi-variables-returntype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current Variables object. |

#### Returns

true if the specified *obj*  is equal to the current [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) object. Otherwise, false.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-equals__variables.html language=enus -->
## TOPIC 01352: Equals(Variables)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-equals__variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-equals__variables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current Variables instance. Equivalency is determined using the LocalVariables, Parameters, and ReturnType. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Variables other)ParametersNameTypeD

### Equals(Variables)

Determines whether the specified *other*  object is equal to the current [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) instance. Equivalency is determined using the [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html), [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-variables-parameters.html), and [ReturnType](nationalinstruments-veristand-realtimesequencedefinitionapi-variables-returntype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Variables other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Variables | The Variables object to compare with the current object. |

#### Returns

true if the specified *other*  object is equal to the current [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) object. Otherwise, false.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-findvariable__string-out.html language=enus -->
## TOPIC 01353: FindVariable(string, out AbstractDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-findvariable__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-findvariable__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the Variables section for a variable with the specified identifier . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool FindVariable(string identifier, out AbstractDeclaration variable)ParametersNameTypeDescriptionidentifierstringThe name of the variable

### FindVariable(string, out AbstractDeclaration)

Searches the [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) section for a variable with the specified *identifier* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool FindVariable(string identifier, out AbstractDeclaration variable)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The name of the variable to search for. |
| variable | out AbstractDeclaration | Upon return, contains an AbstractDeclaration reference to the variable. |

#### Returns

true if the variable is found. Otherwise, false.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-findvariable_t___string-out.html language=enus -->
## TOPIC 01354: FindVariable< T >(string, out T)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-findvariable_t___string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-findvariable_t___string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the Variables section for a variable of type T with the specified identifier . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool FindVariable< T >(string identifier, out T variable)ParametersNameTypeDescriptionidentifierstringThe name of the variable to

### FindVariable< T >(string, out T)

Searches the [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) section for a variable of type *T*  with the specified *identifier* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool FindVariable< T >(string identifier, out T variable)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The name of the variable to search for. |
| variable | out T | Upon return, contains the reference to the variable. |

#### Returns

true if the variable is found. Otherwise, false.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-gethashcode.html language=enus -->
## TOPIC 01355: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Variables object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.Ge

### GetHashCode()

Serves as a hash function for a [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) instance.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-localvariables.html language=enus -->
## TOPIC 01356: LocalVariables

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-localvariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-localvariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the LocalVariables section, which contains the set of local variables that a real-time sequence uses to hold values that a Statement, such as an Expression, can access. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic LocalVariables LocalVariables { get

### LocalVariables

Gets or sets the [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) section, which contains the set of local variables that a real-time sequence uses to hold values that a [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html), such as an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html), can access.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) LocalVariables { get; set; }

#### Returns

A [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) object.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-parameters.html language=enus -->
## TOPIC 01357: Parameters

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-parameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Parameters section, which contains the parameters that the real-time sequence accepts when called. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Parameters Parameters { get; set; }ReturnsA Parameters object.

### Parameters

Gets or sets the [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) section, which contains the parameters that the real-time sequence accepts when called.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) Parameters { get; set; }

#### Returns

A [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) object.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-returntype.html language=enus -->
## TOPIC 01358: ReturnType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-returntype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-returntype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the ReturnDeclaration of the real-time sequence, which is the variable that the sequence returns after it executes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ReturnDeclaration ReturnType { get; set; }ReturnsA ReturnDeclaration object.

### ReturnType

Gets or sets the [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html) of the real-time sequence, which is the variable that the sequence returns after it executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html) ReturnType { get; set; }

#### Returns

A [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html) object.

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-variables.html language=enus -->
## TOPIC 01359: Variables()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-variables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Variables. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Variables()

### Variables()

Initializes a new instance of [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Variables()

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables-variables__variables.html language=enus -->
## TOPIC 01360: Variables(Variables)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables-variables__variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables-variables__variables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Variables by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Variables(Variables node)ParametersNameTypeDescriptionnodeVariablesThe instance of Variables to copy.

### Variables(Variables)

Initializes a new instance of [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Variables(Variables node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Variables | The instance of Variables to copy. |

Parent topic:

Variables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html language=enus -->
## TOPIC 01361: Variables Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-variables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Variables section of a real-time sequence definition, which contains the Parameters, LocalVariables, ReturnDeclaration, and ChannelReferences for the sequence. Derives fromBaseNodeIEquatable< Variables >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic

### Variables Class

Represents the **Variables** section of a real-time sequence definition, which contains the [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html), [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html), [ReturnDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-returndeclaration.html), and [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) for the sequence.

#### Derives from

- BaseNode
- IEquatable< Variables >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Variables : BaseNode, IEquatable< Variables >

#### Remarks

Use the members of this class to access variables and parameters in a real-time sequence definition.

**Accessing this Class:**

- [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-variables.html)
- Variables Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Variables() | Initializes a new instance of Variables. |
| Variables(Variables) | Initializes a new instance of Variables by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| ChannelReferences | Gets or sets the ChannelReferences section, which contains the set of channel references used by a real-time sequence. |
| LocalVariables | Gets or sets the LocalVariables section, which contains the set of local variables that a real-time sequence uses to hold values that a Statement, such as an Expression, can access. |
| Parameters | Gets or sets the Parameters section, which contains the parameters that the real-time sequence accepts when called. |
| ReturnType | Gets or sets the ReturnDeclaration of the real-time sequence, which is the variable that the sequence returns after it executes. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Variables) | Determines whether the specified other object is equal to the current Variables instance. Equivalency is determined using the LocalVariables, Parameters, and ReturnType. |
| Equals(object) | Determines whether the specified obj , which must be a Variables object, is equal to the current Variables instance. Equivalency is determined using the LocalVariables, Parameters, and ReturnType. |
| FindVariable(string, out AbstractDeclaration) | Searches the Variables section for a variable with the specified identifier . |
| FindVariable< T >(string, out T) | Searches the Variables section for a variable of type T with the specified identifier . |
| GetHashCode() | Serves as a hash function for a Variables object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-equals__statement.html language=enus -->
## TOPIC 01362: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of WhileLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe WhileLoop type inherits from Statement. ParametersNameTypeDescriptionotherSt

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html). Otherwise, false.

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-equals__whileloop.html language=enus -->
## TOPIC 01363: Equals(WhileLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-equals__whileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-equals__whileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of WhileLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(WhileLoop other)ParametersNameTypeDescriptionotherWhileLoopThe WhileLoop object to compare with the current inst

### Equals(WhileLoop)

Determines whether the specified *other*  object is equal to the current instance of [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(WhileLoop other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | WhileLoop | The WhileLoop object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-gethashcode.html language=enus -->
## TOPIC 01364: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a WhileLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCo

### GetHashCode()

Serves as a hash function for a [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html) object.

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-looptest.html language=enus -->
## TOPIC 01365: LoopTest

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-looptest.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-looptest.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Boolean expression that is evaluated to determine whether to execute the WhileLoop. The loop executes as long as this expression evaluates to true. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression LoopTest { get; set; }ReturnsAn Expressio

### LoopTest

Gets or sets the Boolean expression that is evaluated to determine whether to execute the [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html). The loop executes as long as this expression evaluates to true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) LoopTest { get; set; }

#### Returns

An [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) object. This expression must evaluate to a Boolean value.

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop.html language=enus -->
## TOPIC 01366: WhileLoop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of WhileLoop with a LoopTest that evaluates to false, meaning the loop does not execute. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic WhileLoop()

### WhileLoop()

Initializes a new instance of [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html) with a [LoopTest](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-looptest.html) that evaluates to false, meaning the loop does not execute.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public WhileLoop()

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__expression-bool-block.html language=enus -->
## TOPIC 01367: WhileLoop(Expression, bool, Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__expression-bool-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__expression-bool-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of WhileLoop with the specified loopTest expression and body of statements. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic WhileLoop(Expression loopTest, bool autoYield, Block body)ParametersNameTypeDescriptionloopTestExpressionThe Boole

### WhileLoop(Expression, bool, Block)

Initializes a new instance of [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html) with the specified *loopTest*  expression and *body*  of statements.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public WhileLoop(Expression loopTest, bool autoYield, Block body)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopTest | Expression | The Boolean expression that is evaluated to determine whether to execute the loop. The loop executes as long as this expression evaluates to true. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| body | Block | The body of statements to execute on each iteration of the loop. |

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__expression-bool.html language=enus -->
## TOPIC 01368: WhileLoop(Expression, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__expression-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__expression-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of WhileLoop with the specified loopTest expression. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic WhileLoop(Expression loopTest, bool autoYield)ParametersNameTypeDescriptionloopTestExpressionThe Boolean expression that is evaluated to

### WhileLoop(Expression, bool)

Initializes a new instance of [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html) with the specified *loopTest*  expression.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public WhileLoop(Expression loopTest, bool autoYield)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopTest | Expression | The Boolean expression that is evaluated to determine whether to execute the loop. The loop executes as long as this expression evaluates to true. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__whileloop.html language=enus -->
## TOPIC 01369: WhileLoop(WhileLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__whileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop-whileloop__whileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of WhileLoop by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic WhileLoop(WhileLoop node)ParametersNameTypeDescriptionnodeWhileLoopThe instance of WhileLoop to copy.

### WhileLoop(WhileLoop)

Initializes a new instance of [WhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public WhileLoop(WhileLoop node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | WhileLoop | The instance of WhileLoop to copy. |

Parent topic:

WhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html language=enus -->
## TOPIC 01370: WhileLoop Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-whileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a While Loop, which executes its body of statements repeatedly as long as a specified condition is true. Derives fromAbstractLoopIEquatable< WhileLoop >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class WhileLoop : AbstractLoop, IEquatable< WhileLoop

### WhileLoop Class

Represents a **While Loop**, which executes its body of statements repeatedly as long as a specified condition is true.

#### Derives from

- AbstractLoop
- IEquatable< WhileLoop >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class WhileLoop : AbstractLoop, IEquatable< WhileLoop >

#### Remarks

Use the members of this class to configure the loop, including the statements it executes and the condition it checks to determine execution.

**Accessing this Class:**

- WhileLoop Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| WhileLoop() | Initializes a new instance of WhileLoop with a LoopTest that evaluates to false, meaning the loop does not execute. |
| WhileLoop(WhileLoop) | Initializes a new instance of WhileLoop by copying an existing instance. |
| WhileLoop(Expression, bool) | Initializes a new instance of WhileLoop with the specified loopTest expression. |
| WhileLoop(Expression, bool, Block) | Initializes a new instance of WhileLoop with the specified loopTest expression and body of statements. |

#### Properties

| Name | Description |
| --- | --- |
| LoopTest | Gets or sets the Boolean expression that is evaluated to determine whether to execute the WhileLoop. The loop executes as long as this expression evaluates to true. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(WhileLoop) | Determines whether the specified other object is equal to the current instance of WhileLoop. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of WhileLoop. |
| GetHashCode() | Serves as a hash function for a WhileLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-yield-equals__statement.html language=enus -->
## TOPIC 01371: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-yield-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-yield-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Yield. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe Yield type inherits from Statement. ParametersNameTypeDescriptionotherStatementT

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html). Otherwise, false.

Parent topic:

Yield Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-yield-equals__yield.html language=enus -->
## TOPIC 01372: Equals(Yield)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-yield-equals__yield.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-yield-equals__yield.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Yield. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Yield other)ParametersNameTypeDescriptionotherYieldThe Yield object to compare with the current instance.Returnstrue

### Equals(Yield)

Determines whether the specified *other*  object is equal to the current instance of [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Yield other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Yield | The Yield object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Yield Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-yield-gethashcode.html language=enus -->
## TOPIC 01373: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-yield-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-yield-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Yield object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCode.

### GetHashCode()

Serves as a hash function for a [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html) object.

Parent topic:

Yield Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-yield-yield.html language=enus -->
## TOPIC 01374: Yield()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-yield-yield.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-yield-yield.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Yield. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Yield()

### Yield()

Initializes a new instance of [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Yield()

Parent topic:

Yield Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-yield-yield__yield.html language=enus -->
## TOPIC 01375: Yield(Yield)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-yield-yield__yield.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-yield-yield__yield.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Yield by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Yield(Yield node)ParametersNameTypeDescriptionnodeYieldThe instance of Yield to copy.

### Yield(Yield)

Initializes a new instance of [Yield](nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Yield(Yield node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Yield | The instance of Yield to copy. |

Parent topic:

Yield Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html language=enus -->
## TOPIC 01376: Yield Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-yield.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Yield statement, which causes a real-time sequence to pause while the Primary Control Loop iterates, and then resume executing. In a multi-tasking sequence, this statement causes the current task to yield control of the CPU to the next task, if one exists. Derives fromStatementIEquatabl

### Yield Class

Represents a **Yield** statement, which causes a real-time sequence to pause while the Primary Control Loop iterates, and then resume executing. In a multi-tasking sequence, this statement causes the current task to yield control of the CPU to the next task, if one exists.

#### Derives from

- Statement
- IEquatable< Yield >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Yield : Statement, IEquatable< Yield >

#### Remarks

**Accessing this Class:**

- Yield Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Yield() | Initializes a new instance of Yield. |
| Yield(Yield) | Initializes a new instance of Yield by copying an existing instance. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of Yield. |
| Equals(Yield) | Determines whether the specified other object is equal to the current instance of Yield. |
| GetHashCode() | Serves as a hash function for a Yield object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities-zipdistributionutilities-createsequencezipdistribution__string-string.html language=enus -->
## TOPIC 01377: CreateSequenceZipDistribution(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities-zipdistributionutilities-createsequencezipdistribution__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities-zipdistributionutilities-createsequencezipdistribution__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a zip distribution for the specified top-level sequence file and returns the Uri to the file within the distribution. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ZipDistributionUtilitiespublic static Uri CreateSequenceZipDistribution(string topLevelSequencePa

### CreateSequenceZipDistribution(string, string)

Creates a zip distribution for the specified top-level sequence file and returns the Uri to the file within the distribution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ZipDistributionUtilities](nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities.html)

public static Uri CreateSequenceZipDistribution(string topLevelSequencePath, string zipDistributionPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| topLevelSequencePath | string | Specifies the top-level sequence. |
| zipDistributionPath | string | Specifies the path to the zip file. |

#### Returns

Returns the Uri for the top-level sequence in the zip distribution.

Parent topic:

ZipDistributionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities-zipdistributionutilities.html language=enus -->
## TOPIC 01378: ZipDistributionUtilities Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities-zipdistributionutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities-zipdistributionutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Utilities for creating zip file distributions for real-time sequences and their dependencies. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ZipDistributionUtilitiespublic class ZipDistributionUtilitiesMethodsNameDescriptionCreateSequenceZipDistribution(

### ZipDistributionUtilities Class

Utilities for creating zip file distributions for real-time sequences and their dependencies.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ZipDistributionUtilities](nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities.html)

public class ZipDistributionUtilities

#### Methods

| Name | Description |
| --- | --- |
| CreateSequenceZipDistribution(string, string) | Creates a zip distribution for the specified top-level sequence file and returns the Uri to the file within the distribution. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ZipDistributionUtilities

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities.html language=enus -->
## TOPIC 01379: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ZipDistributionUtilities

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-zipdistributionutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionZipDistributionUtilitiesUtilities for creating zip file distributions for real-time sequences and their dependencies. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.ZipDistributionUtilities

#### Classes

| Name | Description |
| --- | --- |
| ZipDistributionUtilities | Utilities for creating zip file distributions for real-time sequences and their dependencies. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi.html language=enus -->
## TOPIC 01380: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionAbstractDeclarationRepresents the abstract base class from which all variable, parameter, and return declarations derive. AbstractLoopRepresents the abstract base class from which all loop statements derive. BaseNodeRepresents the abstract base class from which all nodes in a r

### NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

#### Classes

| Name | Description |
| --- | --- |
| AbstractDeclaration | Represents the abstract base class from which all variable, parameter, and return declarations derive. |
| AbstractLoop | Represents the abstract base class from which all loop statements derive. |
| BaseNode | Represents the abstract base class from which all nodes in a real-time sequence definition derive. |
| Block | Represents a Block primitive, which contains a list of functional statements to execute. You can use blocks to organize sequence code. Also, because a block itself is a single statement, you can use blocks to easily duplicate or move related statements that are grouped under a block. Certain pre-defined sections of sequence code, such as Setup, Main, and CleanUp, use code blocks for the Body of their code. |
| CaseStatement | Represents an individual case under the Cases section of a Switch statement. |
| Cases | Represents the Cases section under a Switch statement, which contains all the cases the statement can execute other than the DefaultCase. |
| ChannelReferenceDeclaration | Represents a declaration of a real-time sequence channel reference. |
| ChannelReferences | Represents the Channel References section of the real-time sequence definition, which contains the channel reference declarations for the sequence. |
| CleanUp | Represents the Clean Up section of sequence code, which executes after the Setup and Main code sections. This section contains statements that are critical to execute at the end of sequence execution. If a task running a sequence is stopped, the sequence immediately begins executing the statements in the CleanUp section. |
| Code | Represents the Code section of a sequence, which is the top-level container for all sequence code and contains the Setup, Main, and CleanUp sections. |
| CodeSection | Represents a section of code in a real-time sequence. This is a base class from which more specific code section classes, such as Setup, Main, and CleanUp, inherit. |
| Comment | Represents a Comment primitive, which is a a non-functional statement you can use to document code. This primitive simply stores a string, and functions similarly to comment tags in text-based programming. It has no effect on the execution of a real-time sequence. |
| CompilationEvent | Provides information about errors, warnings, and messages that occurred during compilation of real-time sequence and stimulus profile files. |
| Compiler | Represents the compiler for real-time sequence files. All open and referenced real-time sequence files are compiled automatically when you run a stimulus profile. |
| DefaultCase | Represents the default case in a Switch statement, which executes if none of the conditions for executing a CaseStatement under the Cases section are met. |
| DirectoryPathAttribute | Represents an attribute that indicates that a string is a directory path. |
| DoWhileLoop | Represents a DoWhile Loop primitive, which executes its body of statements at least once and continues executing until a specified condition is false. |
| Expression | Represents a formula-type expression that operates on constant and/or variable values. Expressions can call built-in functions, such as sin(x) and cos(x), and real-time sequences that you add to the current sequence as References. |
| ForEachLoop | Represents a ForEach Loop, which iterates over an array of values and executes its body of statements once per array element. |
| ForLoop | Represents a For Loop, which executes its body of statements for a fixed number of iterations. |
| GenerateError | Represents a statement that generates a user-specified error. |
| IfElse | Represents an IfElse conditional statement, which executes one of two code sections depending on the value of a Boolean expression. |
| IsInternal | Represents an attribute that indicates if a property is internal or public. |
| LocalDeclaration | Represents a declaration of a local variable in a real-time sequence. |
| LocalVariables | Represents the Local Variables section of a real-time sequence definition, which contains the set of local variables that the sequence uses. |
| Main | Represents the Main section of sequence code, which executes after the Setup section and before the CleanUp sections. This section contains the core set of statements that the sequence executes. |
| MultilineStringAttribute | Represents an attribute that indicates that a string contains multiple lines. |
| Multitask | Represents a MultiTask structure, which branches sequence code execution into one or more child tasks. On each time step, the MultiTask structure iteratively executes code from each child task until the task either terminates or yields execution to the next time step. |
| ParameterDeclaration | Represents a declaration of a real-time sequence parameter. |
| Parameters | Represents the Parameters section of the real-time sequence definition, which contains the parameter declarations for the sequence. |
| PathStringAttribute | Represents an attribute that indicates that a string is a file path. |
| PropertyUIDisplayAttribute | Represents an attribute that indicates a property is displayed in the Stimulus Profile Editor Property Browser pane. |
| RealTimeSequence | Represents a real-time sequence, which is a program that can deploy to a target with a system definition file and read/write channels defined in the system definition file. |
| Reference | Represents a reference to a real-time sequence. This reference contains an alias that the current sequence can use to call the referenced sequence from an Expression. |
| References | Represents the References section of the real-time sequence, which is represented by the References pane in the Stimulus Profile Editor. This section contains references to other real-time sequences, which you can call from expressions within the current sequence. |
| ReturnDeclaration | Represents a declaration of the return variable of a real-time sequence. |
| RootNode | Represents the abstract base class from which real-time sequence and stimulus profile files inherit. |
| Setup | Represents the Setup section of sequence code, which executes before the Main and CleanUp code sections. This section contains statements that initialize the sequence. |
| Statement | Represents a functional statement that you can add to a real-time sequence. A statement can be any unique component that performs an action within the sequence, and statements can include sub-statements. Block, Expression, IfElse, and AbstractLoop are all common types of statements that you can add to a real-time sequence. |
| StimulusProfileCompilationException | Represents errors, warnings, or messages that occur during the compilation of a stimulus profile or real-time sequence definition file. |
| StopTask | Represents a Stop Task statement, which stops a task in a Multitask structure. When a task is stopped, any sub-sequences executing in that task immediately execute their CleanUp section. Any sub-tasks are also stopped. |
| Switch | Represents a Switch statement, which evaluates a TestExpression to determine which of multiple Cases to execute. |
| Task | Represents a Task, or block of code, in a Multitask structure. On each time step, the MultiTask structure iteratively executes code from each child Task that it contains. A Task cannot exist outside of a MultiTask structure. |
| Utilities | Provides a set of static methods for locating and resolving common issues in real-time sequence development, such as invalid sequence files, invalid identifiers, and so on. |
| Variables | Represents the Variables section of a real-time sequence definition, which contains the Parameters, LocalVariables, ReturnDeclaration, and ChannelReferences for the sequence. |
| WhileLoop | Represents a While Loop, which executes its body of statements repeatedly as long as a specified condition is true. |
| Yield | Represents a Yield statement, which causes a real-time sequence to pause while the Primary Control Loop iterates, and then resume executing. In a multi-tasking sequence, this statement causes the current task to yield control of the CPU to the next task, if one exists. |

#### Interfaces

| Name | Description |
| --- | --- |
| IGetChannelInfo | Interface used for obtaining information about channels mapped in real-time sequences. |

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| ChannelSizeType | Specifies the type of channel to reference. |
| CompilationEventCode | Specifies the code for an event that occurs during compilation of a real-time sequence or stimulus profile. |
| CompilationEventType | Specifies the type of a CompilationEvent. |
| ErrorAction | Specifies what action to take after generating an error. |
| EvaluationMethod | Specifies how the value of a ParameterDeclaration is passed in to the real-time sequence. |
| OverwriteExistingFileBehavior | Specifies the behavior when an existing file has the same name as the new file. |

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-getcompiledinstance__compiler.html language=enus -->
## TOPIC 01381: GetCompiledInstance(Compiler)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-getcompiledinstance__compiler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-getcompiledinstance__compiler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the compiled instance from the specified compiler. Exists to give access to an internal method via InternalsVisibleTo. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static long[] GetCompiledInstance(Compiler compiler)ParametersNameTypeDescription

### GetCompiledInstance(Compiler)

Returns the compiled instance from the specified compiler. Exists to give access to an internal method via InternalsVisibleTo.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static long[] GetCompiledInstance(Compiler compiler)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| compiler | Compiler | The compiler to get the compiled instance from. |

#### Returns

The compiled instance.

Parent topic:

CompilerUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-getcompiledmessages__compiler.html language=enus -->
## TOPIC 01382: GetCompiledMessages(Compiler)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-getcompiledmessages__compiler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-getcompiledmessages__compiler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of compiled messages for the compiler instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static string[] GetCompiledMessages(Compiler compiler)ParametersNameTypeDescriptioncompilerCompilerThe compiler instance.ReturnsReturns the compil

### GetCompiledMessages(Compiler)

Gets the list of compiled messages for the compiler instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static string[] GetCompiledMessages(Compiler compiler)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| compiler | Compiler | The compiler instance. |

#### Returns

Returns the compiled messages.

Parent topic:

CompilerUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-trygetcompiledinstance__realtimesequence-bool-out-out.html language=enus -->
## TOPIC 01383: TryGetCompiledInstance(RealTimeSequence, bool, out long[], out CompilationEvent[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-trygetcompiledinstance__realtimesequence-bool-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-trygetcompiledinstance__realtimesequence-bool-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Tries to compiles a sequence and returns the compiled instance data if successful. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static bool TryGetCompiledInstance(RealTimeSequence sequence, bool debug, out long[] compiledInstance, out CompilationEvent[]

### TryGetCompiledInstance(RealTimeSequence, bool, out long[], out CompilationEvent[])

Tries to compiles a sequence and returns the compiled instance data if successful.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static bool TryGetCompiledInstance(RealTimeSequence sequence, bool debug, out long[] compiledInstance, out CompilationEvent[] compilationEvents)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sequence | RealTimeSequence | Specifies the sequence to compile |
| debug | bool | Specifies whether to compile the sequence in debug mode |
| compiledInstance | out long[] | Indicates the compiled instance. If there is an error compiling the sequence, this array is emtpy. |
| compilationEvents | out CompilationEvent[] | Indicates any compilation events that were detected while compiling the sequence. If no events were detected, this array is empty. |

#### Returns

Returns true if compilation succeeded

Parent topic:

CompilerUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-writecompiledinstancetofile__compiler-string-out.html language=enus -->
## TOPIC 01384: WriteCompiledInstanceToFile(Compiler, string, out bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-writecompiledinstancetofile__compiler-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities-writecompiledinstancetofile__compiler-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes the compiled instance to a binary file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static void WriteCompiledInstanceToFile(Compiler compiler, string path, out bool isLittleEndian)ParametersNameTypeDescriptioncompilerCompilerThe compiler to get

### WriteCompiledInstanceToFile(Compiler, string, out bool)

Writes the compiled instance to a binary file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static void WriteCompiledInstanceToFile(Compiler compiler, string path, out bool isLittleEndian)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| compiler | Compiler | The compiler to get the compiled instance from. |
| path | string | A unique file path to write the binary compiled instance to. |
| isLittleEndian | out bool | Indicates if the data was serialized in little endian format |

Parent topic:

CompilerUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities.html language=enus -->
## TOPIC 01385: CompilerUtilities Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-compilerutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Static utilities class that contain utilities for working with the Compiler class from RealTimeSequenceDefinitionApi. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic class CompilerUtilitiesMethodsNameDescriptionGetCompiledInstance(Compiler)

### CompilerUtilities Class

Static utilities class that contain utilities for working with the Compiler class from RealTimeSequenceDefinitionApi.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public class CompilerUtilities

#### Methods

| Name | Description |
| --- | --- |
| GetCompiledInstance(Compiler) | Returns the compiled instance from the specified compiler. Exists to give access to an internal method via InternalsVisibleTo. |
| GetCompiledMessages(Compiler) | Gets the list of compiled messages for the compiler instance. |
| TryGetCompiledInstance(RealTimeSequence, bool, out long[], out CompilationEvent[]) | Tries to compiles a sequence and returns the compiled instance data if successful. |
| WriteCompiledInstanceToFile(Compiler, string, out bool) | Writes the compiled instance to a binary file. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-generatelogformulatriggersequence__string-reference_arr1-out.html language=enus -->
## TOPIC 01386: GenerateLogFormulaTriggerSequence(string, Reference[], out RealTimeSequence)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-generatelogformulatriggersequence__string-reference_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-generatelogformulatriggersequence__string-reference_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a log trigger sequence based on the specified Boolean formula. This does some special pre-processing to transform the pseudo-function calls of posedge(signal, level) and negedge(signal, level) into valid subsequence calls that maintain appropriate state data. SyntaxNamespace: NationalInstr

### GenerateLogFormulaTriggerSequence(string, Reference[], out RealTimeSequence)

Generates a log trigger sequence based on the specified Boolean formula. This does some special pre-processing to transform the pseudo-function calls of posedge(signal, level) and negedge(signal, level) into valid subsequence calls that maintain appropriate state data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) GenerateLogFormulaTriggerSequence(string formula, Reference[] references, out RealTimeSequence sequence)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| formula | string | The Boolean formula to evaluate |
| references | Reference[] | References to any external subsequences to be used in the formula |
| sequence | out RealTimeSequence | Indicates the generated sequence |

#### Returns

Returns error information.

Parent topic:

ExpressionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getsubsequencecalls__string-out-out.html language=enus -->
## TOPIC 01387: GetSubsequenceCalls(string, out bool, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getsubsequencecalls__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getsubsequencecalls__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the function aliases for any subsequence calls found in the expression string. This does not include built-in functions like sin. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static string[] GetSubsequenceCalls(string expressionString, out bool

### GetSubsequenceCalls(string, out bool, out string)

Returns the function aliases for any subsequence calls found in the expression string. This does not include built-in functions like sin.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static string[] GetSubsequenceCalls(string expressionString, out bool validExpression, out string parseErrors)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expressionString | string | The expression string to parse. |
| validExpression | out bool | Indicates whether the expression string is a valid expression |
| parseErrors | out string | Returns any parse errors encountered |

#### Returns

Returns the function aliases for any subsequence calls found in the expression string.

Parent topic:

ExpressionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getvariablenames__expression.html language=enus -->
## TOPIC 01388: GetVariableNames(Expression)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getvariablenames__expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getvariablenames__expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the variable names found in an expression string. This does not include subsequence calls or built-in functions. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static string[] GetVariableNames(Expression expression)ParametersNameTypeDescriptionexp

### GetVariableNames(Expression)

Returns the variable names found in an expression string. This does not include subsequence calls or built-in functions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static string[] GetVariableNames(Expression expression)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expression | Expression | The expression to parse. |

#### Returns

Returns the names of all variables in the expression string.

Parent topic:

ExpressionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getvariablenames__string-out-out.html language=enus -->
## TOPIC 01389: GetVariableNames(string, out bool, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getvariablenames__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-getvariablenames__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the variable names found in an expression string. This does not include subsequence calls or built-in functions. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static string[] GetVariableNames(string expressionString, out bool validExpression, out

### GetVariableNames(string, out bool, out string)

Returns the variable names found in an expression string. This does not include subsequence calls or built-in functions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static string[] GetVariableNames(string expressionString, out bool validExpression, out string parseErrors)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expressionString | string | The expression string to parse |
| validExpression | out bool | Indicates whether the expression string is a valid expression |
| parseErrors | out string | Returns any parse errors encountered |

#### Returns

Returns the names of all variables in the expression string

Parent topic:

ExpressionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-renamevariables__expression-dictionary_string-string..html language=enus -->
## TOPIC 01390: RenameVariables(Expression, Dictionary< string, string >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-renamevariables__expression-dictionary_string-string..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-renamevariables__expression-dictionary_string-string..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parse an expression and rename some identifiers (variables). SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static void RenameVariables(Expression expression, Dictionary< string, string > renames)ParametersNameTypeDescriptionexpressionExpressionThe expres

### RenameVariables(Expression, Dictionary< string, string >)

Parse an expression and rename some identifiers (variables).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static void RenameVariables(Expression expression, Dictionary< string, string > renames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expression | Expression | The expression to parse. |
| renames | Dictionary< string, string > | The variables to rename. |

Parent topic:

ExpressionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-renamevariables__string-dictionary_string-string_-out-out.html language=enus -->
## TOPIC 01391: RenameVariables(string, Dictionary< string, string >, out bool, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-renamevariables__string-dictionary_string-string_-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-renamevariables__string-dictionary_string-string_-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parse an expression and rename some identifiers (variables). SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static string RenameVariables(string expressionString, Dictionary< string, string > renames, out bool validExpression, out string parseErrors)Param

### RenameVariables(string, Dictionary< string, string >, out bool, out string)

Parse an expression and rename some identifiers (variables).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static string RenameVariables(string expressionString, Dictionary< string, string > renames, out bool validExpression, out string parseErrors)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expressionString | string | The expression to parse. |
| renames | Dictionary< string, string > | The variables to rename. |
| validExpression | out bool | Indicates whether the expression string is a valid expression. |
| parseErrors | out string | Returns any parse errors encountered. |

#### Returns

The expresion string with the variable names replaced.

Parent topic:

ExpressionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-resolvetriggerfunctions__expression-realtimesequence.html language=enus -->
## TOPIC 01392: ResolveTriggerFunctions(Expression, RealTimeSequence)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-resolvetriggerfunctions__expression-realtimesequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities-resolvetriggerfunctions__expression-realtimesequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Recursively search for specific trigger pseudo-functions and replace them with implementation sequence calls The supported function calls are: posedge(signal, threshold) negedge(signal, threshold) changed(signal, delta) These will be transformed into sequence calls that pass in generated local varia

### ResolveTriggerFunctions(Expression, RealTimeSequence)

Recursively search for specific trigger pseudo-functions and replace them with implementation sequence calls The supported function calls are: posedge(signal, threshold) negedge(signal, threshold) changed(signal, delta) These will be transformed into sequence calls that pass in generated local variable values to store the unit delay of the trigger source and the first call flag.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) ResolveTriggerFunctions(Expression expression, RealTimeSequence sequence)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expression | Expression | The expression to resolve. |
| sequence | RealTimeSequence | The sequence that contains the expression. |

#### Returns

Returns error information.

Parent topic:

ExpressionUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities.html language=enus -->
## TOPIC 01393: ExpressionUtilities Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-expressionutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Helper methods for working with expressions. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic class ExpressionUtilitiesMethodsNameDescriptionGenerateLogFormulaTriggerSequence(string, Reference[], out RealTimeSequence)Generates a log trigger

### ExpressionUtilities Class

Helper methods for working with expressions.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public class ExpressionUtilities

#### Methods

| Name | Description |
| --- | --- |
| GenerateLogFormulaTriggerSequence(string, Reference[], out RealTimeSequence) | Generates a log trigger sequence based on the specified Boolean formula. This does some special pre-processing to transform the pseudo-function calls of posedge(signal, level) and negedge(signal, level) into valid subsequence calls that maintain appropriate state data. |
| GetSubsequenceCalls(string, out bool, out string) | Returns the function aliases for any subsequence calls found in the expression string. This does not include built-in functions like sin. |
| GetVariableNames(string, out bool, out string) | Returns the variable names found in an expression string. This does not include subsequence calls or built-in functions. |
| GetVariableNames(Expression) | Returns the variable names found in an expression string. This does not include subsequence calls or built-in functions. |
| RenameVariables(string, Dictionary< string, string >, out bool, out string) | Parse an expression and rename some identifiers (variables). |
| RenameVariables(Expression, Dictionary< string, string >) | Parse an expression and rename some identifiers (variables). |
| ResolveTriggerFunctions(Expression, RealTimeSequence) | Recursively search for specific trigger pseudo-functions and replace them with implementation sequence calls The supported function calls are: posedge(signal, threshold) negedge(signal, threshold) changed(signal, delta) These will be transformed into sequence calls that pass in generated local variable values to store the unit delay of the trigger source and the first call flag. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-createmodelparameterparser__string-updatemodelparametersfromfile.delimiters.html language=enus -->
## TOPIC 01394: CreateModelParameterParser(string, UpdateModelParametersFromFile.Delimiters)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-createmodelparameterparser__string-updatemodelparametersfromfile.delimiters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-createmodelparameterparser__string-updatemodelparametersfromfile.delimiters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an instance of the ModelParameterParser class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic Error CreateModelParameterParser(string inputFileName, UpdateModelParametersFromFile.Delimiters delimiter)ParametersNameTypeDescriptioninputFileNamestrin

### CreateModelParameterParser(string, UpdateModelParametersFromFile.Delimiters)

Creates an instance of the ModelParameterParser class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) CreateModelParameterParser(string inputFileName, UpdateModelParametersFromFile.Delimiters delimiter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputFileName | string | name of file containing model parameters and values |
| delimiter | Delimiters | character used to mark difference between name and value fields |

#### Returns

An error if the the file is not formatted correctly, is empty, or is missing data, or is not of a supported file type or does not exist. The error is an excpetion of type ParameterFileParseException

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-getparameterdata__out.html language=enus -->
## TOPIC 01395: GetParameterData(out DataArray[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-getparameterdata__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-getparameterdata__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of parameter values parsed from the file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic Error GetParameterData(out DataArray[] paramData)ParametersNameTypeDescriptionparamDataout DataArray[]Array of parameter values.ReturnsAn error if the o

### GetParameterData(out DataArray[])

Gets the list of parameter values parsed from the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) GetParameterData(out DataArray[] paramData)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| paramData | out DataArray[] | Array of parameter values. |

#### Returns

An error if the object is not of type ModelParameterParser.

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-getparameternames__out.html language=enus -->
## TOPIC 01396: GetParameterNames(out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-getparameternames__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-getparameternames__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of parameter names parsed from the file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic Error GetParameterNames(out string[] paramNames)ParametersNameTypeDescriptionparamNamesout string[]Array of parameter names.ReturnsAn error if the object

### GetParameterNames(out string[])

Gets the list of parameter names parsed from the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) GetParameterNames(out string[] paramNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| paramNames | out string[] | Array of parameter names. |

#### Returns

An error if the object is not of type ModelParameterParser.

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-modelparameterparserutilities.html language=enus -->
## TOPIC 01397: ModelParameterParserUtilities()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-modelparameterparserutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-modelparameterparserutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ModelParameterParserUtilities class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic ModelParameterParserUtilities()

### ModelParameterParserUtilities()

Initializes a new instance of the ModelParameterParserUtilities class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public ModelParameterParserUtilities()

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-parsefile.html language=enus -->
## TOPIC 01398: ParseFile()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-parsefile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-parsefile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This method parses the file data, processes and evaluates it. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic Error ParseFile()ReturnsAn error which might be an exception thrown by one of the sub-methods.

### ParseFile()

This method parses the file data, processes and evaluates it.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) ParseFile()

#### Returns

An error which might be an exception thrown by one of the sub-methods.

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-setaliasfile__string.html language=enus -->
## TOPIC 01399: SetAliasFile(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-setaliasfile__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-setaliasfile__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the alias file path to be used by the parser. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic Error SetAliasFile(string inputFileName)ParametersNameTypeDescriptioninputFileNamestringPath to the alias file.ReturnsAn error if the object is not of type M

### SetAliasFile(string)

Sets the alias file path to be used by the parser.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) SetAliasFile(string inputFileName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| inputFileName | string | Path to the alias file. |

#### Returns

An error if the object is not of type ModelParameterParser.

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-setallowtemporaryvariablesproperty__bool.html language=enus -->
## TOPIC 01400: SetAllowTemporaryVariablesProperty(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-setallowtemporaryvariablesproperty__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-setallowtemporaryvariablesproperty__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the AllowTemporaryVariables property to indicate whether temporary variables will be allowed in the parameter calibration file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic Error SetAllowTemporaryVariablesProperty(bool allowTemporaryVariables)Param

### SetAllowTemporaryVariablesProperty(bool)

Sets the AllowTemporaryVariables property to indicate whether temporary variables will be allowed in the parameter calibration file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) SetAllowTemporaryVariablesProperty(bool allowTemporaryVariables)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| allowTemporaryVariables | bool | True indicates that temporary vcariables can be present in the parameter calibration file |

#### Returns

An error if the object is not of type ModelParameterParser.

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-settarget__string.html language=enus -->
## TOPIC 01401: SetTarget(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-settarget__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities-settarget__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the target on which these parameters exist. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic Error SetTarget(string target)ParametersNameTypeDescriptiontargetstringtarget nameReturnsAn error if the object is not of type ModelParameterParser.

### SetTarget(string)

Sets the target on which these parameters exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public [Error](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) SetTarget(string target)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | string | target name |

#### Returns

An error if the object is not of type ModelParameterParser.

Parent topic:

ModelParameterParserUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities.html language=enus -->
## TOPIC 01402: ModelParameterParserUtilities Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-modelparameterparserutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: helper methods for parsing parameters file Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic class ModelParameterParserUtilitiesConstructorsNameDescriptionModelParameterParserUtilities()Initializes a new instance of the ModelParameterParserUt

### ModelParameterParserUtilities Class

helper methods for parsing parameters file

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public class ModelParameterParserUtilities

#### Constructors

| Name | Description |
| --- | --- |
| ModelParameterParserUtilities() | Initializes a new instance of the ModelParameterParserUtilities class. |

#### Methods

| Name | Description |
| --- | --- |
| CreateModelParameterParser(string, UpdateModelParametersFromFile.Delimiters) | Creates an instance of the ModelParameterParser class. |
| GetParameterData(out DataArray[]) | Gets the list of parameter values parsed from the file. |
| GetParameterNames(out string[]) | Gets the list of parameter names parsed from the file. |
| ParseFile() | This method parses the file data, processes and evaluates it. |
| SetAliasFile(string) | Sets the alias file path to be used by the parser. |
| SetAllowTemporaryVariablesProperty(bool) | Sets the AllowTemporaryVariables property to indicate whether temporary variables will be allowed in the parameter calibration file. |
| SetTarget(string) | Sets the target on which these parameters exist. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-realtimesequenceutilities-createsequencezipdistribution__string-string.html language=enus -->
## TOPIC 01403: CreateSequenceZipDistribution(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-realtimesequenceutilities-createsequencezipdistribution__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-realtimesequenceutilities-createsequencezipdistribution__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a zip distribution for the specified top-level sequence file and returns the Uri to the file within the distribution. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic static Uri CreateSequenceZipDistribution(string topLevelSequencePath, string zipDi

### CreateSequenceZipDistribution(string, string)

Creates a zip distribution for the specified top-level sequence file and returns the Uri to the file within the distribution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public static Uri CreateSequenceZipDistribution(string topLevelSequencePath, string zipDistributionPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| topLevelSequencePath | string | Specifies the top-level sequence. |
| zipDistributionPath | string | Specifies the path to the zip file. |

#### Returns

Returns the Uri for the top-level sequence in the zip distribution.

Parent topic:

RealTimeSequenceUtilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities-realtimesequenceutilities.html language=enus -->
## TOPIC 01404: RealTimeSequenceUtilities Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities-realtimesequenceutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities-realtimesequenceutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Utilities for working with real-time sequences. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilitiespublic class RealTimeSequenceUtilitiesMethodsNameDescriptionCreateSequenceZipDistribution(string, string)Creates a zip distribution for the specified t

### RealTimeSequenceUtilities Class

Utilities for working with real-time sequences.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities](nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html)

public class RealTimeSequenceUtilities

#### Methods

| Name | Description |
| --- | --- |
| CreateSequenceZipDistribution(string, string) | Creates a zip distribution for the specified top-level sequence file and returns the Uri to the file within the distribution. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html language=enus -->
## TOPIC 01405: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapiutilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionCompilerUtilitiesStatic utilities class that contain utilities for working with the Compiler class from RealTimeSequenceDefinitionApi. ExpressionUtilitiesHelper methods for working with expressions. ModelParameterParserUtilitieshelper methods for parsing parameters file RealTim

### NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities

#### Classes

| Name | Description |
| --- | --- |
| CompilerUtilities | Static utilities class that contain utilities for working with the Compiler class from RealTimeSequenceDefinitionApi. |
| ExpressionUtilities | Helper methods for working with expressions. |
| ModelParameterParserUtilities | helper methods for parsing parameters file |
| RealTimeSequenceUtilities | Utilities for working with real-time sequences. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-actionstep.html language=enus -->
## TOPIC 01406: ActionStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-actionstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-actionstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ActionStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected ActionStep()RemarksThis constructor is protected.

### ActionStep()

Initializes a new instance of [ActionStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected ActionStep()

#### Remarks

This constructor is protected.

Parent topic:

ActionStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-actionstep__actionstep.html language=enus -->
## TOPIC 01407: ActionStep(ActionStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-actionstep__actionstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-actionstep__actionstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ActionStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected ActionStep(ActionStep node)RemarksThis constructor is protected. ParametersNameTypeDescriptionnodeActionStepThe instance of ActionStep to cop

### ActionStep(ActionStep)

Initializes a new instance of [ActionStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected ActionStep(ActionStep node)

#### Remarks

This constructor is protected.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ActionStep | The instance of ActionStep to copy. |

Parent topic:

ActionStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html language=enus -->
## TOPIC 01408: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CompilationEvent[] CheckForErrors()ReturnsAn array of CompilationEvent objects that represe

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

ActionStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-id.html language=enus -->
## TOPIC 01409: Id

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-id.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-id.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Id { get; }ReturnsA string containing the position of the step in the stimulus profile hierarchy. For

### Id

Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Id { get; }

#### Returns

A string containing the position of the step in the stimulus profile hierarchy. For example, a Play Macro step under the **Main** code section has the following ID: Main/Play Macro: *MacroFile*.nivsmacro.

Parent topic:

ActionStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-state.html language=enus -->
## TOPIC 01410: State

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-state.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-state.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the execution state of a step (Idle, Initializing, Running, and so on.) SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StepExecutionState State { get; }ReturnsAn enumeration of StepExecutionState.

### State

Gets the execution state of a step (Idle, Initializing, Running, and so on.)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [StepExecutionState](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepexecutionstate.html) State { get; }

#### Returns

An enumeration of [StepExecutionState](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepexecutionstate.html).

Parent topic:

ActionStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html language=enus -->
## TOPIC 01411: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of a step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string StepName { get; }ReturnsThe step name.

### StepName

Gets the name of a step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string StepName { get; }

#### Returns

The step name.

Parent topic:

ActionStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html language=enus -->
## TOPIC 01412: ActionStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a step that performs an action, such as opening or closing a project, opening or closing the Workspace, or calling a real-time sequence. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class ActionStep : BaseNodeRemarksAccessing this C

### ActionStep Class

Represents a step that performs an action, such as opening or closing a project, opening or closing the Workspace, or calling a real-time sequence.

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class ActionStep : BaseNode

#### Remarks

**Accessing this Class:**

Note

- ActionStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ActionStep(ActionStep) | Initializes a new instance of ActionStep by copying an existing instance. |
| ActionStep() | Initializes a new instance of ActionStep. |

#### Properties

| Name | Description |
| --- | --- |
| Id | Gets the unique identifier for a step, which is the full path to the step in the stimulus profile hierarchy. |
| State | Gets the execution state of a step (Idle, Initializing, Running, and so on.) |
| StepName | Gets the name of a step. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-alwayspassevaluation.html language=enus -->
## TOPIC 01413: AlwaysPassEvaluation()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-alwayspassevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-alwayspassevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of AlwaysPassEvaluation. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic AlwaysPassEvaluation()

### AlwaysPassEvaluation()

Initializes a new instance of [AlwaysPassEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public AlwaysPassEvaluation()

Parent topic:

AlwaysPassEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-alwayspassevaluation__alwayspassevaluation.html language=enus -->
## TOPIC 01414: AlwaysPassEvaluation(AlwaysPassEvaluation)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-alwayspassevaluation__alwayspassevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-alwayspassevaluation__alwayspassevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of AlwaysPassEvaluation by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic AlwaysPassEvaluation(AlwaysPassEvaluation node)ParametersNameTypeDescriptionnodeAlwaysPassEvaluationThe instance of AlwaysPassEvaluati

### AlwaysPassEvaluation(AlwaysPassEvaluation)

Initializes a new instance of [AlwaysPassEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public AlwaysPassEvaluation(AlwaysPassEvaluation node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | AlwaysPassEvaluation | The instance of AlwaysPassEvaluation to copy. |

Parent topic:

AlwaysPassEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-evaluate__datavalue.html language=enus -->
## TOPIC 01415: Evaluate(DataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-evaluate__datavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation-evaluate__datavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs an AlwaysPass evaluation, which always returns true. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override bool Evaluate(DataValue value)RemarksOverrides Evaluate. ParametersNameTypeDescriptionvalueDataValueThe value to evaluate. This is typically the re

### Evaluate(DataValue)

Performs an **AlwaysPass** evaluation, which always returns true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override bool Evaluate(DataValue value)

#### Remarks

Overrides [Evaluate](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluate__datavalue.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | DataValue | The value to evaluate. This is typically the return value of a real-time sequence. This method ignores this value and always returns true. |

#### Returns

true

Parent topic:

AlwaysPassEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation.html language=enus -->
## TOPIC 01416: AlwaysPassEvaluation Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-alwayspassevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a pass/fail evaluation that always passes, regardless of the value being evaluated. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. Derives fromEvaluationSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileD

### AlwaysPassEvaluation Class

Represents a pass/fail evaluation that always passes, regardless of the value being evaluated. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails.

#### Derives from

- Evaluation

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class AlwaysPassEvaluation : Evaluation

#### Remarks

Use the members of this class to perform an **AlwaysPass** evaluation.

**Accessing this Class:**

- AlwaysPassEvaluation Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| AlwaysPassEvaluation(AlwaysPassEvaluation) | Initializes a new instance of AlwaysPassEvaluation by copying an existing instance. |
| AlwaysPassEvaluation() | Initializes a new instance of AlwaysPassEvaluation. |

#### Methods

| Name | Description |
| --- | --- |
| Evaluate(DataValue) | Performs an AlwaysPass evaluation, which always returns true. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation.html language=enus -->
## TOPIC 01417: BooleanEvaluation()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanEvaluation. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic BooleanEvaluation()RemarksThis constructor sets Invert to false.

### BooleanEvaluation()

Initializes a new instance of [BooleanEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public BooleanEvaluation()

#### Remarks

This constructor sets [Invert](nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-invert.html) to false.

Parent topic:

BooleanEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation__bool.html language=enus -->
## TOPIC 01418: BooleanEvaluation(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanEvaluation and specifies whether the evaluation is inverted such that a false value indicates passing and a true value indicates failing. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic BooleanEvaluation(bool invert)ParametersNam

### BooleanEvaluation(bool)

Initializes a new instance of [BooleanEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation.html) and specifies whether the evaluation is inverted such that a false value indicates passing and a true value indicates failing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public BooleanEvaluation(bool invert)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| invert | bool | true to invert the evaluation. |

Parent topic:

BooleanEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation__booleanevaluation.html language=enus -->
## TOPIC 01419: BooleanEvaluation(BooleanEvaluation)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation__booleanevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-booleanevaluation__booleanevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BooleanEvaluation by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic BooleanEvaluation(BooleanEvaluation node)ParametersNameTypeDescriptionnodeBooleanEvaluationThe instance of BooleanEvaluation to copy.

### BooleanEvaluation(BooleanEvaluation)

Initializes a new instance of [BooleanEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public BooleanEvaluation(BooleanEvaluation node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BooleanEvaluation | The instance of BooleanEvaluation to copy. |

Parent topic:

BooleanEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-evaluate__datavalue.html language=enus -->
## TOPIC 01420: Evaluate(DataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-evaluate__datavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-evaluate__datavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a Boolean evaluation on the specified value . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override bool Evaluate(DataValue value)RemarksYou can use the Invert property to invert a Boolean evaluation.Overrides Evaluate. ParametersNameTypeDescriptionvalue

### Evaluate(DataValue)

Performs a **Boolean** evaluation on the specified *value* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override bool Evaluate(DataValue value)

#### Remarks

Note

You can use the [Invert](nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-invert.html) property to invert a **Boolean** evaluation.

Evaluate

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | DataValue | The value to evaluate. This is typically the return value of a real-time sequence. |

#### Returns

By default, true if the value passes. If you invert the evaluation, false indicates a pass.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentNullException | value is null. |

Parent topic:

BooleanEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-invert.html language=enus -->
## TOPIC 01421: Invert

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-invert.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation-invert.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the Boolean evaluation is inverted. In an inverted evaluation, a false value indicates passing and a true value indicates failing. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool Invert { get; set; }Returnstrue if the evaluation is inverted

### Invert

Gets or sets whether the **Boolean** evaluation is inverted. In an inverted evaluation, a false value indicates passing and a true value indicates failing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool Invert { get; set; }

#### Returns

true if the evaluation is inverted.

Parent topic:

BooleanEvaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation.html language=enus -->
## TOPIC 01422: BooleanEvaluation Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-booleanevaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Boolean pass/fail evaluation, where one value (usually true) indicates a pass and the other a fail. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. Derives fromEvaluationSyntaxNamespace: NationalInstruments.VeriStan

### BooleanEvaluation Class

Represents a **Boolean** pass/fail evaluation, where one value (usually true) indicates a pass and the other a fail. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails.

#### Derives from

- Evaluation

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class BooleanEvaluation : Evaluation

#### Remarks

Use the members of this class to perform a **Boolean** evaluation. You also can invert the evaluation, so that a false value indicates a pass.

**Accessing this Class:**

- BooleanEvaluation Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| BooleanEvaluation() | Initializes a new instance of BooleanEvaluation. |
| BooleanEvaluation(BooleanEvaluation) | Initializes a new instance of BooleanEvaluation by copying an existing instance. |
| BooleanEvaluation(bool) | Initializes a new instance of BooleanEvaluation and specifies whether the evaluation is inverted such that a false value indicates passing and a true value indicates failing. |

#### Properties

| Name | Description |
| --- | --- |
| Invert | Gets or sets whether the Boolean evaluation is inverted. In an inverted evaluation, a false value indicates passing and a true value indicates failing. |

#### Methods

| Name | Description |
| --- | --- |
| Evaluate(DataValue) | Performs a Boolean evaluation on the specified value . |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-boundschecktype.html language=enus -->
## TOPIC 01423: BoundsCheckType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-boundschecktype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-boundschecktype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of bounds check used for a NumericBoundsEvaluation. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic enum BoundsCheckTypeMembersNameValueDescriptionInboundsThe evaluation passes if the value is within the specified bounds. OutOfBoundsThe evaluation

### BoundsCheckType Enumeration

Specifies the type of bounds check used for a [NumericBoundsEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-numericboundsevaluation.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public enum BoundsCheckType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Inbounds |  | The evaluation passes if the value is within the specified bounds. |
| OutOfBounds |  | The evaluation passes if the value is outside the specified bounds. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup.html language=enus -->
## TOPIC 01424: CleanupStepGroup()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CleanupStepGroup. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CleanupStepGroup()RemarksThis constructor sets GroupName to "Group".

### CleanupStepGroup()

Initializes a new instance of [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CleanupStepGroup()

#### Remarks

This constructor sets [GroupName](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-groupname.html) to "Group".

Parent topic:

CleanupStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup__cleanupstepgroup.html language=enus -->
## TOPIC 01425: CleanupStepGroup(CleanupStepGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup__cleanupstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup__cleanupstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CleanupStepGroup by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CleanupStepGroup(CleanupStepGroup node)ParametersNameTypeDescriptionnodeCleanupStepGroupThe instance of CleanupStepGroup to copy.

### CleanupStepGroup(CleanupStepGroup)

Initializes a new instance of [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CleanupStepGroup(CleanupStepGroup node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | CleanupStepGroup | The instance of CleanupStepGroup to copy. |

Parent topic:

CleanupStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup__string.html language=enus -->
## TOPIC 01426: CleanupStepGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup-cleanupstepgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CleanupStepGroup and assigns the group the specified groupName . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CleanupStepGroup(string groupName)ParametersNameTypeDescriptiongroupNamestringThe name of the step group.

### CleanupStepGroup(string)

Initializes a new instance of [CleanupStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html) and assigns the group the specified *groupName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CleanupStepGroup(string groupName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| groupName | string | The name of the step group. |

Parent topic:

CleanupStepGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html language=enus -->
## TOPIC 01427: CleanupStepGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-cleanupstepgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Clean Up, or finalization, section of stimulus profile code. This section is a StepGroup that contains all the steps you want to execute after the MainStepGroup finishes. Derives fromStepGroupSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class Clean

### CleanupStepGroup Class

Represents the **Clean Up**, or finalization, section of stimulus profile code. This section is a [StepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup.html) that contains all the steps you want to execute after the [MainStepGroup](nationalinstruments-veristand-stimulusprofiledefinitionapi-mainstepgroup.html) finishes.

#### Derives from

- StepGroup

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class CleanupStepGroup : StepGroup

#### Remarks

Use the members of this class to get and set information about the step group.

**Accessing this Class:**

- CleanupStepGroup Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CleanupStepGroup(string) | Initializes a new instance of CleanupStepGroup and assigns the group the specified groupName . |
| CleanupStepGroup(CleanupStepGroup) | Initializes a new instance of CleanupStepGroup by copying an existing instance. |
| CleanupStepGroup() | Initializes a new instance of CleanupStepGroup. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-closeprojectstep.html language=enus -->
## TOPIC 01428: CloseProjectStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-closeprojectstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-closeprojectstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CloseProjectStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CloseProjectStep()

### CloseProjectStep()

Initializes a new instance of [CloseProjectStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CloseProjectStep()

Parent topic:

CloseProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-closeprojectstep__closeprojectstep.html language=enus -->
## TOPIC 01429: CloseProjectStep(CloseProjectStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-closeprojectstep__closeprojectstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-closeprojectstep__closeprojectstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CloseProjectStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CloseProjectStep(CloseProjectStep node)ParametersNameTypeDescriptionnodeCloseProjectStepThe instance of CloseProjectStep to copy.

### CloseProjectStep(CloseProjectStep)

Initializes a new instance of [CloseProjectStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CloseProjectStep(CloseProjectStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | CloseProjectStep | The instance of CloseProjectStep to copy. |

Parent topic:

CloseProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-stepname.html language=enus -->
## TOPIC 01430: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of a step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of a step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

CloseProjectStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep.html language=enus -->
## TOPIC 01431: CloseProjectStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeprojectstep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Close VeriStand Project step, which closes an open NI VeriStand project. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class CloseProjectStep : ActionStepRemarksUse the members of this class to get and set information about the s

### CloseProjectStep Class

Represents a Close VeriStand Project step, which closes an open NI VeriStand project.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class CloseProjectStep : ActionStep

#### Remarks

Use the members of this class to get and set information about the step.

**Accessing this Class:**

- CloseProjectStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CloseProjectStep(CloseProjectStep) | Initializes a new instance of CloseProjectStep by copying an existing instance. |
| CloseProjectStep() | Initializes a new instance of CloseProjectStep. |

#### Properties

| Name | Description |
| --- | --- |
| StepName | Gets the name of a step. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-closeworkspacestep.html language=enus -->
## TOPIC 01432: CloseWorkspaceStep()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-closeworkspacestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-closeworkspacestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CloseWorkspaceStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CloseWorkspaceStep()

### CloseWorkspaceStep()

Initializes a new instance of [CloseWorkspaceStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CloseWorkspaceStep()

Parent topic:

CloseWorkspaceStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-closeworkspacestep__closeworkspacestep.html language=enus -->
## TOPIC 01433: CloseWorkspaceStep(CloseWorkspaceStep)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-closeworkspacestep__closeworkspacestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-closeworkspacestep__closeworkspacestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CloseWorkspaceStep by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CloseWorkspaceStep(CloseWorkspaceStep node)ParametersNameTypeDescriptionnodeCloseWorkspaceStepThe instance of CloseWorkspaceStep to copy

### CloseWorkspaceStep(CloseWorkspaceStep)

Initializes a new instance of [CloseWorkspaceStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CloseWorkspaceStep(CloseWorkspaceStep node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | CloseWorkspaceStep | The instance of CloseWorkspaceStep to copy. |

Parent topic:

CloseWorkspaceStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-stepname.html language=enus -->
## TOPIC 01434: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of a step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of a step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

CloseWorkspaceStep Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep.html language=enus -->
## TOPIC 01435: CloseWorkspaceStep Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-closeworkspacestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Close Workspace step, which closes the Workspace for the active and open NI VeriStand project. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class CloseWorkspaceStep : ActionStepRemarksUse the members of this class to get and set

### CloseWorkspaceStep Class

Represents a Close Workspace step, which closes the Workspace for the active and open NI VeriStand project.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class CloseWorkspaceStep : ActionStep

#### Remarks

Use the members of this class to get and set information about the step.

**Accessing this Class:**

- CloseWorkspaceStep Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CloseWorkspaceStep(CloseWorkspaceStep) | Initializes a new instance of CloseWorkspaceStep by copying an existing instance. |
| CloseWorkspaceStep() | Initializes a new instance of CloseWorkspaceStep. |

#### Properties

| Name | Description |
| --- | --- |
| StepName | Gets the name of a step. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-arguments.html language=enus -->
## TOPIC 01436: Arguments

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-arguments.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-arguments.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the command line arguments to pass to the application. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Arguments { get; set; }ReturnsThe command line arguments to pass to the application.

### Arguments

Gets or sets the command line arguments to pass to the application.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Arguments { get; set; }

#### Returns

The command line arguments to pass to the application.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-checkforerrors.html language=enus -->
## TOPIC 01437: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell.html language=enus -->
## TOPIC 01438: CommandShell()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CommandShell class. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CommandShell()RemarksThis constructor sets FileName to string.Empty, Arguments to string.Empty, WaitToComplete to false, WaitToCompleteTimeout to -1, HideCommandShe

### CommandShell()

Initializes a new instance of the [CommandShell](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CommandShell()

#### Remarks

This constructor sets [FileName](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-filename.html) to string.Empty, [Arguments](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-arguments.html) to string.Empty, [WaitToComplete](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocomplete.html) to false, [WaitToCompleteTimeout](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocompletetimeout.html) to -1, [HideCommandShellWindow](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-hidecommandshellwindow.html) to false, [RedirectStandardOutput](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandardoutput.html) to false, and [RedirectStandardError](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandarderror.html) to false.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell__commandshell.html language=enus -->
## TOPIC 01439: CommandShell(CommandShell)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell__commandshell.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell__commandshell.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CommandShell class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CommandShell(CommandShell node)ParametersNameTypeDescriptionnodeCommandShellThe instance of CommandShell to copy.

### CommandShell(CommandShell)

Initializes a new instance of the [CommandShell](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CommandShell(CommandShell node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | CommandShell | The instance of CommandShell to copy. |

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell__string-string-bool-int-bool-bool-bool.html language=enus -->
## TOPIC 01440: CommandShell(string, string, bool, int, bool, bool, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell__string-string-bool-int-bool-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-commandshell__string-string-bool-int-bool-bool-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CommandShell class with the specified fileName , arguments , and Command Prompt settings. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic CommandShell(string fileName, string arguments, bool waitToComplete, int waitToCompleteTimeout

### CommandShell(string, string, bool, int, bool, bool, bool)

Initializes a new instance of the [CommandShell](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell.html) class with the specified *fileName* , *arguments* , and Command Prompt settings.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public CommandShell(string fileName, string arguments, bool waitToComplete, int waitToCompleteTimeout, bool runMinimized, bool redirectOutput, bool redirectError)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| fileName | string | The name of the application to call from the Command Prompt. You can use a system command (for example, cmd notepad), a system variable, or the fully-qualified path to the executable. |
| arguments | string | The command line arguments to pass to fileName . |
| waitToComplete | bool | true to make the stimulus profile wait for the Command Prompt to return before completing execution. The Command Prompt does not return until all applications it calls are properly closed. |
| waitToCompleteTimeout | int | The amount of time to wait in milliseconds for the Command Prompt to return before returning a timeout error. The default value is -1, which specifies an infinite timeout. Valid values include -1 and positive numbers. Invalid values are set to -1 by default. |
| runMinimized | bool | true to run the application in an inaccessible Command Prompt window. |
| redirectOutput | bool | true to write the standard output of the Command Prompt to the ATML test results filefor the stimulus profile. |
| redirectError | bool | true to write standard error output of the Command Prompt to the ATML test results file for the stimulus profile. |

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-filename.html language=enus -->
## TOPIC 01441: FileName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-filename.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-filename.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the application to call from the Command Prompt. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string FileName { get; set; }ReturnsThe name of the application to call. You can use a system command (for example, cmd notepad), a system varia

### FileName

Gets or sets the name of the application to call from the Command Prompt.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string FileName { get; set; }

#### Returns

The name of the application to call. You can use a system command (for example, cmd notepad), a system variable, or the fully-qualified path to the executable.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-hidecommandshellwindow.html language=enus -->
## TOPIC 01442: HideCommandShellWindow

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-hidecommandshellwindow.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-hidecommandshellwindow.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the application runs in an inaccessible Command Prompt window. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool HideCommandShellWindow { get; set; }RemarksIf both RedirectStandardError and RedirectStandardOutput are false

### HideCommandShellWindow

Gets or sets a value indicating whether the application runs in an inaccessible Command Prompt window.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool HideCommandShellWindow { get; set; }

#### Remarks

If both [RedirectStandardError](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandarderror.html) and [RedirectStandardOutput](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandardoutput.html) are false and you set this property to true, that value is ignored.

#### Returns

true if the application runs in an inaccessible Command Prompt window.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandarderror.html language=enus -->
## TOPIC 01443: RedirectStandardError

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandarderror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandarderror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the standard error output of the Command Prompt is written to the ATML test results filefor the stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool RedirectStandardError { get; set; }Returnstrue if the stand

### RedirectStandardError

Gets or sets a value indicating whether the standard error output of the Command Prompt is written to the ATML test results file

for the stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool RedirectStandardError { get; set; }

#### Returns

true if the standard error output is written to the ATML test results file.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandardoutput.html language=enus -->
## TOPIC 01444: RedirectStandardOutput

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandardoutput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-redirectstandardoutput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the standard output of the Command Prompt is written to the ATML test results filefor the stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool RedirectStandardOutput { get; set; }Returnstrue if the standard o

### RedirectStandardOutput

Gets or sets a value indicating whether the standard output of the Command Prompt is written to the ATML test results file

for the stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool RedirectStandardOutput { get; set; }

#### Returns

true if the standard output is written to the ATML test results file.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-stepname.html language=enus -->
## TOPIC 01445: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of a step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }RemarksOverrides StepName. ReturnsThe step name.

### StepName

Gets the name of a step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

#### Remarks

Overrides [StepName](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-stepname.html).

#### Returns

The step name.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocomplete.html language=enus -->
## TOPIC 01446: WaitToComplete

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocomplete.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocomplete.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the CommandShell step waits for the Command Prompt to return before completing the step. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool WaitToComplete { get; set; }RemarksThe Command Prompt does not return until all appl

### WaitToComplete

Gets or sets a value indicating whether the [CommandShell](nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell.html) step waits for the Command Prompt to return before completing the step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool WaitToComplete { get; set; }

#### Remarks

The Command Prompt does not return until all applications it calls are properly closed.

#### Returns

true if the stimulus profile waits for the Command Prompt to return.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocompletetimeout.html language=enus -->
## TOPIC 01447: WaitToCompleteTimeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocompletetimeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell-waittocompletetimeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time in milliseconds to wait for the Command Prompt to return before returning a timeout error. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic int WaitToCompleteTimeout { get; set; }ReturnsThe time in milliseconds to wait for the Command Prompt to

### WaitToCompleteTimeout

Gets or sets the time in milliseconds to wait for the Command Prompt to return before returning a timeout error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public int WaitToCompleteTimeout { get; set; }

#### Returns

The time in milliseconds to wait for the Command Prompt to return. The default value is -1, which specifies an infinite timeout.

Parent topic:

CommandShell Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell.html language=enus -->
## TOPIC 01448: CommandShell Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-commandshell.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Command Shell step, which invokes the Windows Command Prompt and calls the specified application with the specified arguments. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class CommandShell : ActionStepRemarksUse the members of

### CommandShell Class

Represents a Command Shell step, which invokes the Windows Command Prompt and calls the specified application with the specified arguments.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class CommandShell : ActionStep

#### Remarks

Use the members of this class to specify which application to call, specify any arguments to pass to the application, and configure whether the rest of the stimulus profile waits for the Command Prompt to return before completing execution.

**Accessing this Class:**

- CommandShell Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CommandShell(CommandShell) | Initializes a new instance of the CommandShell class by copying an existing instance. |
| CommandShell(string, string, bool, int, bool, bool, bool) | Initializes a new instance of the CommandShell class with the specified fileName , arguments , and Command Prompt settings. |
| CommandShell() | Initializes a new instance of the CommandShell class. |

#### Properties

| Name | Description |
| --- | --- |
| Arguments | Gets or sets the command line arguments to pass to the application. |
| FileName | Gets or sets the name of the application to call from the Command Prompt. |
| HideCommandShellWindow | Gets or sets a value indicating whether the application runs in an inaccessible Command Prompt window. |
| RedirectStandardError | Gets or sets a value indicating whether the standard error output of the Command Prompt is written to the ATML test results filefor the stimulus profile. |
| RedirectStandardOutput | Gets or sets a value indicating whether the standard output of the Command Prompt is written to the ATML test results filefor the stimulus profile. |
| StepName | Gets the name of a step. |
| WaitToComplete | Gets or sets a value indicating whether the CommandShell step waits for the Command Prompt to return before completing the step. |
| WaitToCompleteTimeout | Gets or sets the time in milliseconds to wait for the Command Prompt to return before returning a timeout error. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-clone.html language=enus -->
## TOPIC 01449: Clone()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-clone.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-clone.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a clone object of the current instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic object Clone()ReturnsA object clone of the current instance.

### Clone()

Creates a clone object of the current instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public object Clone()

#### Returns

A object clone of the current instance.

Parent topic:

Evaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluate__datavalue.html language=enus -->
## TOPIC 01450: Evaluate(DataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluate__datavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluate__datavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Evaluates the specified value for a pass/fail condition. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool Evaluate(DataValue value)ParametersNameTypeDescriptionvalueDataValueThe value to evaluate. This is typically the return value of a real-time sequence.Return

### Evaluate(DataValue)

Evaluates the specified *value*  for a pass/fail condition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool Evaluate(DataValue value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| value | DataValue | The value to evaluate. This is typically the return value of a real-time sequence. |

#### Returns

true if *value*  passes, or if [EvaluationType](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluationtype.html) is [AlwaysPass](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluationtype.html).

Parent topic:

Evaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluation.html language=enus -->
## TOPIC 01451: Evaluation()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Evaluation. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected Evaluation()

### Evaluation()

Initializes a new instance of [Evaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected Evaluation()

Parent topic:

Evaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluation__evaluation.html language=enus -->
## TOPIC 01452: Evaluation(Evaluation)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluation__evaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-evaluation__evaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Evaluation by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected Evaluation(Evaluation node)ParametersNameTypeDescriptionnodeEvaluationThe instance of Evaluation to copy.

### Evaluation(Evaluation)

Initializes a new instance of [Evaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected Evaluation(Evaluation node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Evaluation | The instance of Evaluation to copy. |

Parent topic:

Evaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-getevaluationoftype__evaluationtype.html language=enus -->
## TOPIC 01453: GetEvaluationOfType(EvaluationType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-getevaluationoftype__evaluationtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-getevaluationoftype__evaluationtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a pass/fail evaluation of the type you specify. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic static Evaluation GetEvaluationOfType(EvaluationType type)ParametersNameTypeDescriptiontypeEvaluationTypeThe evaluation type. Valid values are AlwaysPassEvaluation,

### GetEvaluationOfType(EvaluationType)

Gets a pass/fail evaluation of the *type*  you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public static [Evaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html) GetEvaluationOfType(EvaluationType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| type | EvaluationType | The evaluation type. Valid values are AlwaysPassEvaluation, BooleanEvaluation, and NumericBoundsEvaluation. |

#### Returns

An object of the specified evaluation type.

Parent topic:

Evaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-propertychanged.html language=enus -->
## TOPIC 01454: PropertyChanged

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-propertychanged.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation-propertychanged.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when a property value changes. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic PropertyChangedEventHandler PropertyChanged

### PropertyChanged

Occurs when a property value changes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public PropertyChangedEventHandler PropertyChanged

Parent topic:

Evaluation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html language=enus -->
## TOPIC 01455: Evaluation Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a pass/fail evaluation performed on a value. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails. Derives fromINotifyPropertyChangedICloneableSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipubli

### Evaluation Class

Represents a pass/fail evaluation performed on a value. You typically use evaluations on the return value of a real-time sequence to determine if the sequence passes or fails.

#### Derives from

- INotifyPropertyChanged
- ICloneable

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class Evaluation : INotifyPropertyChanged, ICloneable

#### Remarks

This is a base class from which all evaluation classes inherit. Use the members of this class to specify the value to evaluate for pass/fail conditions and the type of evaluation to perform.

**Accessing this Class:**

- [OutputEvaluation](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep-outputevaluation.html)

Note

- Evaluation Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Evaluation(Evaluation) | Initializes a new instance of Evaluation by copying an existing instance. |
| Evaluation() | Initializes a new instance of Evaluation. |

#### Methods

| Name | Description |
| --- | --- |
| GetEvaluationOfType(EvaluationType) | Gets a pass/fail evaluation of the type you specify. |
| Clone() | Creates a clone object of the current instance. |
| Evaluate(DataValue) | Evaluates the specified value for a pass/fail condition. |

#### Events

| Name | Description |
| --- | --- |
| PropertyChanged | Occurs when a property value changes. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluationtype.html language=enus -->
## TOPIC 01456: EvaluationType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluationtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-evaluationtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of pass/fail evaluation performed on a given value. This value is typically the return value of a real-time sequence called by a RealTimeSequenceCallStep. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic enum EvaluationTypeMembersNameValueDescripti

### EvaluationType Enumeration

Specifies the type of pass/fail evaluation performed on a given value. This value is typically the return value of a real-time sequence called by a [RealTimeSequenceCallStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencecallstep.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public enum EvaluationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AlwaysPass |  | The evaluation always passes, regardless of the value being evaluated. |
| Boolean |  | Evaluates a bool value for pass/fail status. true is pass, unless you invert the evaluation. |
| NumericBoundsCheck |  | Evaluates an integer value relative to specified high and low boundaries. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs-resultfile.html language=enus -->
## TOPIC 01457: ResultFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs-resultfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs-resultfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the test results file, which is an XML file that adheres to the Automatic Test Markup Language (ATML) standard. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ResultFile { get; }ReturnsThe path to the results file.

### ResultFile

Gets the path to the test results file, which is an XML file that adheres to the Automatic Test Markup Language (ATML) standard.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ResultFile { get; }

#### Returns

The path to the results file.

Parent topic:

ExecuteCompletedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs-resultsdirectory.html language=enus -->
## TOPIC 01458: ResultsDirectory

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs-resultsdirectory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs-resultsdirectory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the folder on disk where test result data is stored. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ResultsDirectory { get; }ReturnsThe path to the results directory.

### ResultsDirectory

Gets the path to the folder on disk where test result data is stored.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ResultsDirectory { get; }

#### Returns

The path to the results directory.

Parent topic:

ExecuteCompletedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs.html language=enus -->
## TOPIC 01459: ExecuteCompletedEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-executecompletedeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the ExecuteCompleted event. Derives fromAsyncCompletedEventArgsSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class ExecuteCompletedEventArgs : AsyncCompletedEventArgsRemarksAccessing this Class:ExecuteCompleted Thread SafetyAny members of this ty

### ExecuteCompletedEventArgs Class

Provides data for the [ExecuteCompleted](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executecompleted.html) event.

#### Derives from

- AsyncCompletedEventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class ExecuteCompletedEventArgs : AsyncCompletedEventArgs

#### Remarks

**Accessing this Class:**

- [ExecuteCompleted](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-executecompleted.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| ResultFile | Gets the path to the test results file, which is an XML file that adheres to the Automatic Test Markup Language (ATML) standard. |
| ResultsDirectory | Gets the path to the folder on disk where test result data is stored. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststep.html language=enus -->
## TOPIC 01460: LastStep

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the most recent step executed by the stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic ActionStep LastStep { get; }ReturnsAn ActionStep reference to the step.

### LastStep

Gets the most recent step executed by the stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [ActionStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html) LastStep { get; }

#### Returns

An [ActionStep](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep.html) reference to the step.

Parent topic:

ExecuteProgressChangedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststepresult.html language=enus -->
## TOPIC 01461: LastStepResult

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststepresult.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststepresult.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the execution results (passed, failed, and so on) of the last step executed by the stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic StepResult LastStepResult { get; }ReturnsAn enumeration of StepResult.

### LastStepResult

Gets the execution results (passed, failed, and so on) of the last step executed by the stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [StepResult](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepresult.html) LastStepResult { get; }

#### Returns

An enumeration of [StepResult](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepresult.html).

Parent topic:

ExecuteProgressChangedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststepresultqualifier.html language=enus -->
## TOPIC 01462: LastStepResultQualifier

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststepresultqualifier.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs-laststepresultqualifier.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets additional information about the results of the last step, such as extended error information for a step that fails. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string LastStepResultQualifier { get; }ReturnsA string containing the additional information.

### LastStepResultQualifier

Gets additional information about the results of the last step, such as extended error information for a step that fails.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string LastStepResultQualifier { get; }

#### Returns

A string containing the additional information.

Parent topic:

ExecuteProgressChangedEventArgs Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs.html language=enus -->
## TOPIC 01463: ExecuteProgressChangedEventArgs Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-executeprogresschangedeventargs.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the ProgressChanged event. Derives fromProgressChangedEventArgsSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class ExecuteProgressChangedEventArgs : ProgressChangedEventArgsRemarksThe members of this class return progress data for the executing s

### ExecuteProgressChangedEventArgs Class

Provides data for the [ProgressChanged](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-progresschanged.html) event.

#### Derives from

- ProgressChangedEventArgs

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class ExecuteProgressChangedEventArgs : ProgressChangedEventArgs

#### Remarks

The members of this class return progress data for the executing stimulus profile, including the result of the most recent step executed.

**Accessing this Class:**

- [ProgressChanged](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-progresschanged.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| LastStep | Gets the most recent step executed by the stimulus profile. |
| LastStepResult | Gets the execution results (passed, failed, and so on) of the last step executed by the stimulus profile. |
| LastStepResultQualifier | Gets additional information about the results of the last step, such as extended error information for a step that fails. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-bufferlength.html language=enus -->
## TOPIC 01464: BufferLength

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-bufferlength.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-bufferlength.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the size of the buffer, in bytes, to use for streaming data. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic uint BufferLength { get; set; }ReturnsThe size of the buffer in bytes. The minimum value is 2. ExceptionsTypeDescriptionSystem.ArgumentOutOfRang

### BufferLength

Gets or sets the size of the buffer, in bytes, to use for streaming data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public uint BufferLength { get; set; }

#### Returns

The size of the buffer in bytes. The minimum value is 2.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentOutOfRangeException | The value of BufferLength is less than 2. |

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-checkforerrors.html language=enus -->
## TOPIC 01465: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. ReturnsAn arra

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-createuniquefilename__string.html language=enus -->
## TOPIC 01466: CreateUniqueFileName(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-createuniquefilename__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-createuniquefilename__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a unique filename by appending a number to proposedFileName . SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected string CreateUniqueFileName(string proposedFileName)ParametersNameTypeDescriptionproposedFileNamestringThe filename to use to create a unique fil

### CreateUniqueFileName(string)

Creates a unique filename by appending a number to *proposedFileName* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected string CreateUniqueFileName(string proposedFileName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| proposedFileName | string | The filename to use to create a unique filename. |

#### Returns

A unique filename.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-doesfileexistonftpserver__string.html language=enus -->
## TOPIC 01467: DoesFileExistOnFTPServer(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-doesfileexistonftpserver__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-doesfileexistonftpserver__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks if the specified file already exists on the FTP server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected bool DoesFileExistOnFTPServer(string sourceFileName)ParametersNameTypeDescriptionsourceFileNamestringThe filename.Returnstrue if the file exists.

### DoesFileExistOnFTPServer(string)

Checks if the specified file already exists on the FTP server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected bool DoesFileExistOnFTPServer(string sourceFileName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceFileName | string | The filename. |

#### Returns

true if the file exists.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-downloadfile__string-filestream.html language=enus -->
## TOPIC 01468: DownloadFile(string, FileStream)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-downloadfile__string-filestream.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-downloadfile__string-filestream.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Downloads the specified file from the FTP server and copies it to the Destination directory. This method uses a buffer of a size specified by BufferLength. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected string DownloadFile(string sourceFilePath, FileStream strea

### DownloadFile(string, FileStream)

Downloads the specified file from the FTP server and copies it to the [Destination](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-destination.html) directory. This method uses a buffer of a size specified by [BufferLength](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-bufferlength.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected string DownloadFile(string sourceFilePath, FileStream stream)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceFilePath | string | The fully qualified path to the file. |
| stream | FileStream | The stream to which to write data from the buffer. This method does not close the stream. |

#### Returns

A status message sent from the FTP server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-enableproxy.html language=enus -->
## TOPIC 01469: EnableProxy

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-enableproxy.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-enableproxy.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to transmit data through a proxy server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool EnableProxy { get; set; }Returnstrue to transmit data through a proxy server.

### EnableProxy

Gets or sets a value indicating whether to transmit data through a proxy server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool EnableProxy { get; set; }

#### Returns

true to transmit data through a proxy server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-filter.html language=enus -->
## TOPIC 01470: Filter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-filter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-filter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a regular expression to use to filter files by filename when ServerURL is a folder. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Filter { get; set; }RemarksThis step only acts on the files that match the regular expression. The match is not ca

### Filter

Gets or sets a regular expression to use to filter files by filename when [ServerURL](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-serverurl.html) is a folder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Filter { get; set; }

#### Remarks

This step only acts on the files that match the regular expression. The match is not case-sensitive.

#### Returns

The regular expression to use to filter files.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ftpbase.html language=enus -->
## TOPIC 01471: FTPBase()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ftpbase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ftpbase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FTPBase class. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic FTPBase()RemarksThis constructor sets Timeout to 180 seconds and BufferLength to 1024.

### FTPBase()

Initializes a new instance of the [FTPBase](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public FTPBase()

#### Remarks

This constructor sets [Timeout](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-timeout.html) to 180 seconds and [BufferLength](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-bufferlength.html) to 1024.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ftpbase__ftpbase.html language=enus -->
## TOPIC 01472: FTPBase(FTPBase)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ftpbase__ftpbase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ftpbase__ftpbase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FTPBase class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic FTPBase(FTPBase node)ParametersNameTypeDescriptionnodeFTPBaseThe instance of FTPBase to copy.

### FTPBase(FTPBase)

Initializes a new instance of the [FTPBase](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public FTPBase(FTPBase node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | FTPBase | The instance of FTPBase to copy. |

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-getfilelistfromdirectory.html language=enus -->
## TOPIC 01473: GetFileListFromDirectory()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-getfilelistfromdirectory.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-getfilelistfromdirectory.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of all files from a directory on the FTP server. This method uses the proxy server settings, including ProxyUserName and ProxyPassword. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected string[] GetFileListFromDirectory()ReturnsAn array of filename

### GetFileListFromDirectory()

Returns the name of all files from a directory on the FTP server. This method uses the proxy server settings, including [ProxyUserName](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyusername.html) and [ProxyPassword](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxypassword.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected string[] GetFileListFromDirectory()

#### Returns

An array of filenames.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-overwriteexistingfilebehavior.html language=enus -->
## TOPIC 01474: OverwriteExistingFileBehavior

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-overwriteexistingfilebehavior.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-overwriteexistingfilebehavior.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the action to take if a file of the same name already exists in the destination directory. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic OverwriteExistingFileBehavior OverwriteExistingFileBehavior { get; set; }ReturnsAn enumeration of OverwriteExistin

### OverwriteExistingFileBehavior

Gets or sets the action to take if a file of the same name already exists in the destination directory.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public [OverwriteExistingFileBehavior](nationalinstruments-veristand-realtimesequencedefinitionapi-overwriteexistingfilebehavior.html) OverwriteExistingFileBehavior { get; set; }

#### Returns

An enumeration of [OverwriteExistingFileBehavior](nationalinstruments-veristand-realtimesequencedefinitionapi-overwriteexistingfilebehavior.html).

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-password.html language=enus -->
## TOPIC 01475: Password

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-password.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-password.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the password for UserName to use to access the FTP server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Password { get; set; }ReturnsThe password to use to access the FTP server.

### Password

Gets or sets the password for [UserName](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-username.html) to use to access the FTP server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Password { get; set; }

#### Returns

The password to use to access the FTP server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxypassword.html language=enus -->
## TOPIC 01476: ProxyPassword

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxypassword.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxypassword.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the password for ProxyUserName to use to access the proxy server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ProxyPassword { get; set; }ReturnsThe password to use to access the proxy server.

### ProxyPassword

Gets or sets the password for [ProxyUserName](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyusername.html) to use to access the proxy server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ProxyPassword { get; set; }

#### Returns

The password to use to access the proxy server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyport.html language=enus -->
## TOPIC 01477: ProxyPort

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the port the FTP proxy uses. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic int ProxyPort { get; set; }ReturnsThe port the FTP proxy uses. If EnableProxy is false, this value is ignored.

### ProxyPort

Gets or sets the port the FTP proxy uses.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public int ProxyPort { get; set; }

#### Returns

The port the FTP proxy uses. If [EnableProxy](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-enableproxy.html) is false, this value is ignored.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyurl.html language=enus -->
## TOPIC 01478: ProxyURL

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyurl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyurl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the URL of the proxy server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ProxyURL { get; set; }ReturnsThe URL of the proxy server.

### ProxyURL

Gets or sets the URL of the proxy server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ProxyURL { get; set; }

#### Returns

The URL of the proxy server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyusername.html language=enus -->
## TOPIC 01479: ProxyUserName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyusername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-proxyusername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the username for the proxy server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ProxyUserName { get; set; }RemarksIf ProxyUserName is an empty string or null, the proxy server authenticates requests using the credentials of the currently logge

### ProxyUserName

Gets or sets the username for the proxy server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ProxyUserName { get; set; }

#### Remarks

If ProxyUserName is an empty string or null, the proxy server authenticates requests using the credentials of the currently logged in user.

#### Returns

The username for the proxy server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-serverurl.html language=enus -->
## TOPIC 01480: ServerURL

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-serverurl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-serverurl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the address of a file or directory on the FTP server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string ServerURL { get; set; }ReturnsThe address of the file or directory on the FTP server. The address cannot contain any characters that define the

### ServerURL

Gets or sets the address of a file or directory on the FTP server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string ServerURL { get; set; }

#### Returns

The address of the file or directory on the FTP server. The address cannot contain any characters that define the protocol. For example, 10.0.72.66/samplefile.txt is a valid address, but [ftp://10.0.72.66/samplefile.txt](ftp://10.0.72.66/samplefile.txt) is not.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ssl.html language=enus -->
## TOPIC 01481: SSL

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ssl.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-ssl.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether data transmission is encrypted using an SSL protocol. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool SSL { get; set; }Returnstrue if the data transmission is encrypted.

### SSL

Gets or sets a value indicating whether data transmission is encrypted using an SSL protocol.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool SSL { get; set; }

#### Returns

true if the data transmission is encrypted.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-timeout.html language=enus -->
## TOPIC 01482: Timeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-timeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-timeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time in seconds to wait for a response from the FTP server before returning a timeout error. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic uint Timeout { get; set; }ReturnsThe time in seconds to wait for a response from the FTP server.ExceptionsTy

### Timeout

Gets or sets the time in seconds to wait for a response from the FTP server before returning a timeout error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public uint Timeout { get; set; }

#### Returns

The time in seconds to wait for a response from the FTP server.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentOutOfRangeException | The value of Timeout is 0. |

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-uploadfile__string-string.html language=enus -->
## TOPIC 01483: UploadFile(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-uploadfile__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-uploadfile__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uploads a file to the FTP server with a new filename. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected string UploadFile(string filePath, string fileNameOnServer)ParametersNameTypeDescriptionfilePathstringThe fully qualified path of the file to upload.fileNameOnSe

### UploadFile(string, string)

Uploads a file to the FTP server with a new filename.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected string UploadFile(string filePath, string fileNameOnServer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The fully qualified path of the file to upload. |
| fileNameOnServer | string | The filename to create on the FTP server. |

#### Returns

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-uploadfile__string.html language=enus -->
## TOPIC 01484: UploadFile(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-uploadfile__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-uploadfile__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uploads a file to the FTP server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApiprotected string UploadFile(string filePath)ParametersNameTypeDescriptionfilePathstringThe fully qualified path of the file to upload.Returns

### UploadFile(string)

Uploads a file to the FTP server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

protected string UploadFile(string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The fully qualified path of the file to upload. |

#### Returns

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-usebinary.html language=enus -->
## TOPIC 01485: UseBinary

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-usebinary.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-usebinary.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether data is transmitted in binary form. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool UseBinary { get; set; }Returnstrue to transmit data in binary form. false to transmit data as text.

### UseBinary

Gets or sets a value indicating whether data is transmitted in binary form.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool UseBinary { get; set; }

#### Returns

true to transmit data in binary form. false to transmit data as text.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-usepassive.html language=enus -->
## TOPIC 01486: UsePassive

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-usepassive.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-usepassive.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to use a passive or active connection on the FTP server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool UsePassive { get; set; }Returnstrue if this step initiates a connection on the FTP data port. false if this step lis

### UsePassive

Gets or sets a value indicating whether to use a passive or active connection on the FTP server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool UsePassive { get; set; }

#### Returns

true if this step initiates a connection on the FTP data port. false if this step listens for a connection on the FTP server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-username.html language=enus -->
## TOPIC 01487: UserName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-username.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-username.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the username to use to access the FTP server. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string UserName { get; set; }ReturnsThe username to use to access the FTP server.

### UserName

Gets or sets the username to use to access the FTP server.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string UserName { get; set; }

#### Returns

The username to use to access the FTP server.

Parent topic:

FTPBase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase.html language=enus -->
## TOPIC 01488: FTPBase Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides an abstract base class for interacting with files on an FTP server. Derives fromActionStepSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class FTPBase : ActionStepRemarksFTPBase is the base class for all FTP steps. Thread SafetyAny members of this type are

### FTPBase Class

Provides an abstract base class for interacting with files on an FTP server.

#### Derives from

- ActionStep

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class FTPBase : ActionStep

#### Remarks

FTPBase is the base class for all FTP steps.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| FTPBase() | Initializes a new instance of the FTPBase class. |
| FTPBase(FTPBase) | Initializes a new instance of the FTPBase class by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| BufferLength | Gets or sets the size of the buffer, in bytes, to use for streaming data. |
| EnableProxy | Gets or sets a value indicating whether to transmit data through a proxy server. |
| Filter | Gets or sets a regular expression to use to filter files by filename when ServerURL is a folder. |
| OverwriteExistingFileBehavior | Gets or sets the action to take if a file of the same name already exists in the destination directory. |
| Password | Gets or sets the password for UserName to use to access the FTP server. |
| ProxyPassword | Gets or sets the password for ProxyUserName to use to access the proxy server. |
| ProxyPort | Gets or sets the port the FTP proxy uses. |
| ProxyURL | Gets or sets the URL of the proxy server. |
| ProxyUserName | Gets or sets the username for the proxy server. |
| ServerURL | Gets or sets the address of a file or directory on the FTP server. |
| SSL | Gets or sets a value indicating whether data transmission is encrypted using an SSL protocol. |
| Timeout | Gets or sets the time in seconds to wait for a response from the FTP server before returning a timeout error. |
| UseBinary | Gets or sets a value indicating whether data is transmitted in binary form. |
| UsePassive | Gets or sets a value indicating whether to use a passive or active connection on the FTP server. |
| UserName | Gets or sets the username to use to access the FTP server. |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |
| CreateUniqueFileName(string) | Creates a unique filename by appending a number to proposedFileName . |
| DoesFileExistOnFTPServer(string) | Checks if the specified file already exists on the FTP server. |
| DownloadFile(string, FileStream) | Downloads the specified file from the FTP server and copies it to the Destination directory. This method uses a buffer of a size specified by BufferLength. |
| GetFileListFromDirectory() | Returns the name of all files from a directory on the FTP server. This method uses the proxy server settings, including ProxyUserName and ProxyPassword. |
| UploadFile(string) | Uploads a file to the FTP server. |
| UploadFile(string, string) | Uploads a file to the FTP server with a new filename. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-checkforerrors.html language=enus -->
## TOPIC 01489: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. Overrides Chec

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

FTPDownload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-destination.html language=enus -->
## TOPIC 01490: Destination

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-destination.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-destination.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination directory for downloaded files. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic string Destination { get; set; }ReturnsThe destination directory. If you do not specify a destination, this step downloads files to the directory that contai

### Destination

Gets or sets the destination directory for downloaded files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public string Destination { get; set; }

#### Returns

The destination directory. If you do not specify a destination, this step downloads files to the directory that contains the stimulus profile.

Parent topic:

FTPDownload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-filter.html language=enus -->
## TOPIC 01491: Filter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-filter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-filter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string Filter { get; set; }RemarksThis step only acts on the files that match the regular expression. The match is not case-sensitive. Overrides Filter.

### Filter

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string Filter { get; set; }

#### Remarks

This step only acts on the files that match the regular expression. The match is not case-sensitive.

Overrides [Filter](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-filter.html).

Parent topic:

FTPDownload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-ftpdownload.html language=enus -->
## TOPIC 01492: FTPDownload()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-ftpdownload.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-ftpdownload.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FTPDownload class. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic FTPDownload()

### FTPDownload()

Initializes a new instance of the [FTPDownload](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public FTPDownload()

Parent topic:

FTPDownload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-ftpdownload__ftpdownload.html language=enus -->
## TOPIC 01493: FTPDownload(FTPDownload)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-ftpdownload__ftpdownload.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-ftpdownload__ftpdownload.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FTPDownload class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic FTPDownload(FTPDownload node)ParametersNameTypeDescriptionnodeFTPDownloadThe instance of FTPDownload to copy.

### FTPDownload(FTPDownload)

Initializes a new instance of the [FTPDownload](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public FTPDownload(FTPDownload node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | FTPDownload | The instance of FTPDownload to copy. |

Parent topic:

FTPDownload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-serverurlisfolder.html language=enus -->
## TOPIC 01494: ServerURLIsFolder

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-serverurlisfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-serverurlisfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the path to the source files is a file or a folder. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic bool ServerURLIsFolder { get; set; }Returnstrue if ServerURL is a folder. If false, ServerURL must be a specific file.

### ServerURLIsFolder

Gets or sets a value indicating whether the path to the source files is a file or a folder.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public bool ServerURLIsFolder { get; set; }

#### Returns

true if [ServerURL](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-serverurl.html) is a folder. If false, [ServerURL](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-serverurl.html) must be a specific file.

Parent topic:

FTPDownload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-stepname.html language=enus -->
## TOPIC 01495: StepName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-stepname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload-stepname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string StepName { get; }

### StepName

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string StepName { get; }

Parent topic:

FTPDownload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload.html language=enus -->
## TOPIC 01496: FTPDownload Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpdownload.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an FTP Download step, which downloads files from an FTP server, such as an RT target. Derives fromFTPBaseSyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic class FTPDownload : FTPBaseRemarksUse the members of this class to configure FTP settings and download

### FTPDownload Class

Represents an FTP Download step, which downloads files from an FTP server, such as an RT target.

#### Derives from

- FTPBase

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public class FTPDownload : FTPBase

#### Remarks

Note

Some versions of Microsoft Windows block incoming FTP traffic by default. If prompted by the OS, allow NI VeriStand to use port 21 (FTP) to transfer data.

**Accessing this Class:**

- FTPDownload Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| FTPDownload(FTPDownload) | Initializes a new instance of the FTPDownload class by copying an existing instance. |
| FTPDownload() | Initializes a new instance of the FTPDownload class. |

#### Properties

| Name | Description |
| --- | --- |
| Destination | Gets or sets the destination directory for downloaded files. |
| Filter |  |
| ServerURLIsFolder | Gets or sets a value indicating whether the path to the source files is a file or a folder. |
| StepName |  |

#### Methods

| Name | Description |
| --- | --- |
| CheckForErrors() | Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. |

Parent topic:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-checkforerrors.html language=enus -->
## TOPIC 01497: CheckForErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-checkforerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-checkforerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override CompilationEvent[] CheckForErrors()RemarksOverrides CheckForErrors. Overrides Chec

### CheckForErrors()

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CheckForErrors()

#### Remarks

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html).

Overrides [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-checkforerrors.html).

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects that represent the errors, warnings, and messages generated by the step.

Parent topic:

FTPUpload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-filter.html language=enus -->
## TOPIC 01498: Filter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-filter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-filter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic override string Filter { get; set; }RemarksThis step only acts on the files that match the regular expression. The match is not case-sensitive. Overrides Filter.

### Filter

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public override string Filter { get; set; }

#### Remarks

This step only acts on the files that match the regular expression. The match is not case-sensitive.

Overrides [Filter](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpbase-filter.html).

Parent topic:

FTPUpload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload.html language=enus -->
## TOPIC 01499: FTPUpload()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FTPUpload class. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic FTPUpload()

### FTPUpload()

Initializes a new instance of the [FTPUpload](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public FTPUpload()

Parent topic:

FTPUpload Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload__ftpupload.html language=enus -->
## TOPIC 01500: FTPUpload(FTPUpload)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload__ftpupload.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload-ftpupload__ftpupload.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FTPUpload class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.StimulusProfileDefinitionApipublic FTPUpload(FTPUpload node)ParametersNameTypeDescriptionnodeFTPUploadThe instance of FTPUpload to copy.

### FTPUpload(FTPUpload)

Initializes a new instance of the [FTPUpload](nationalinstruments-veristand-stimulusprofiledefinitionapi-ftpupload.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.StimulusProfileDefinitionApi](nationalinstruments-veristand-stimulusprofiledefinitionapi.html)

public FTPUpload(FTPUpload node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | FTPUpload | The instance of FTPUpload to copy. |

Parent topic:

FTPUpload Class
