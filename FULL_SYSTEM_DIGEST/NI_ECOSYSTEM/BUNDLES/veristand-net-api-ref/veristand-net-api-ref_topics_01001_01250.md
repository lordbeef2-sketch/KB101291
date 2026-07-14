# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=1001 end=1250 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-identifier.html language=enus -->
## TOPIC 01001: Identifier

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-identifier.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-identifier.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the declared object. This name must be unique, and it must be a valid identifier. It cannot contain spaces or invalid characters. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Identifier { get; set; }RemarksYou can use the IsValidI

### Identifier

Gets or sets the name of the declared object. This name must be unique, and it must be a valid identifier. It cannot contain spaces or invalid characters.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Identifier { get; set; }

#### Remarks

Note

You can use the [IsValidIdentifier](nationalinstruments-veristand-realtimesequencedefinitionapi-utilities-isvalididentifier__string.html) method to determine if a string is a valid identifier.

#### Returns

The name of the declared object.

Parent topic:

AbstractDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-units.html language=enus -->
## TOPIC 01002: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the units associated with the declared value. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Units { get; set; }ReturnsThe units associated with the declared value. This can be any string.

### Units

Gets or sets the units associated with the declared value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Units { get; set; }

#### Returns

The units associated with the declared value. This can be any string.

Parent topic:

AbstractDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration.html language=enus -->
## TOPIC 01003: AbstractDeclaration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the abstract base class from which all variable, parameter, and return declarations derive. Derives fromBaseNodeIEquatable< AbstractDeclaration >INotifyPropertyChangedSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class AbstractDeclaration : BaseNode, I

### AbstractDeclaration Class

Represents the abstract base class from which all variable, parameter, and return declarations derive.

#### Derives from

- BaseNode
- IEquatable< AbstractDeclaration >
- INotifyPropertyChanged

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class AbstractDeclaration : BaseNode, IEquatable< AbstractDeclaration >, INotifyPropertyChanged

#### Remarks

AbstractDeclaration provides an abstract base class for declarations within the [RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html) namespace.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| AbstractDeclaration(string, DataValue) | Initializes a new instance of AbstractDeclaration and creates a declaration with the specified identifier and defaultValue . |
| AbstractDeclaration(AbstractDeclaration) | Initializes a new instance of AbstractDeclaration by copying an existing instance. |
| AbstractDeclaration() | Initializes a new instance of AbstractDeclaration. |

#### Properties

| Name | Description |
| --- | --- |
| DataType | Gets the data type of the declared object. |
| DefaultValue | Gets or sets the default value of the declared object. |
| Identifier | Gets or sets the name of the declared object. This name must be unique, and it must be a valid identifier. It cannot contain spaces or invalid characters. |
| Units | Gets or sets the units associated with the declared value. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Determines whether the specified obj , which must be a AbstractDeclaration, is equal to the current AbstractDeclaration. |
| Equals(AbstractDeclaration) | Determines whether the specified other object is equal to the current instance of AbstractDeclaration. Equality is determined using the DefaultValue and Identifier. |
| GetHashCode() | Serves as a hash function for a AbstractDeclaration object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-abstractloop.html language=enus -->
## TOPIC 01004: AbstractLoop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-abstractloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-abstractloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of AbstractLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected AbstractLoop()RemarksThis constructor is protected.This constructor sets AutoYield to true.

### AbstractLoop()

Initializes a new instance of [AbstractLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected AbstractLoop()

#### Remarks

Note

This constructor is protected.

AutoYield

true

Parent topic:

AbstractLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-abstractloop__abstractloop.html language=enus -->
## TOPIC 01005: AbstractLoop(AbstractLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-abstractloop__abstractloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-abstractloop__abstractloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of AbstractLoop by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected AbstractLoop(AbstractLoop node)RemarksThis constructor is protected. ParametersNameTypeDescriptionnodeAbstractLoopThe instance of Abstract

### AbstractLoop(AbstractLoop)

Initializes a new instance of [AbstractLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected AbstractLoop(AbstractLoop node)

#### Remarks

Note

This constructor is protected.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | AbstractLoop | The instance of AbstractLoop to copy. |

Parent topic:

AbstractLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-addstatement__statement.html language=enus -->
## TOPIC 01006: AddStatement(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-addstatement__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-addstatement__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified statement to the end of the loop body. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddStatement(Statement statement)ParametersNameTypeDescriptionstatementStatementThe statement to add to the loop.

### AddStatement(Statement)

Adds the specified *statement*  to the end of the loop body.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddStatement(Statement statement)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| statement | Statement | The statement to add to the loop. |

Parent topic:

AbstractLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-autoyield.html language=enus -->
## TOPIC 01007: AutoYield

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-autoyield.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-autoyield.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the loop automatically yields control of the CPU to the next task at the end of each iteration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool AutoYield { get; set; }Returnstrue if the loop automatically yields execution until the next ti

### AutoYield

Gets or sets whether the loop automatically yields control of the CPU to the next task at the end of each iteration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool AutoYield { get; set; }

#### Returns

true if the loop automatically yields execution until the next time step. Otherwise, false

Parent topic:

AbstractLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-body.html language=enus -->
## TOPIC 01008: Body

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-body.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-body.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the set of statements that execute in the loop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Block Body { get; set; }ReturnsA Block object.

### Body

Gets or sets the set of statements that execute in the loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) Body { get; set; }

#### Returns

A [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) object.

Parent topic:

AbstractLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-clearstatements.html language=enus -->
## TOPIC 01009: ClearStatements()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-clearstatements.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-clearstatements.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all statements from the loop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearStatements()

### ClearStatements()

Clears all statements from the loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearStatements()

Parent topic:

AbstractLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop.html language=enus -->
## TOPIC 01010: AbstractLoop Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the abstract base class from which all loop statements derive. Derives fromStatementSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class AbstractLoop : StatementRemarksAbstractLoop provides an abstract base class for loop statements within the RealTimeS

### AbstractLoop Class

Represents the abstract base class from which all loop statements derive.

#### Derives from

- Statement

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class AbstractLoop : Statement

#### Remarks

AbstractLoop provides an abstract base class for loop statements within the [RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html) namespace.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| AbstractLoop(AbstractLoop) | Initializes a new instance of AbstractLoop by copying an existing instance. |
| AbstractLoop() | Initializes a new instance of AbstractLoop. |

#### Properties

| Name | Description |
| --- | --- |
| AutoYield | Gets or sets whether the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| Body | Gets or sets the set of statements that execute in the loop. |

#### Methods

| Name | Description |
| --- | --- |
| AddStatement(Statement) | Adds the specified statement to the end of the loop body. |
| ClearStatements() | Clears all statements from the loop. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-basenode.html language=enus -->
## TOPIC 01011: BaseNode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BaseNode. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected BaseNode()RemarksThis constructor is protected.

### BaseNode()

Initializes a new instance of [BaseNode](nationalinstruments-veristand-realtimesequencedefinitionapi-basenode.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected BaseNode()

#### Remarks

This constructor is protected.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-basenode__basenode.html language=enus -->
## TOPIC 01012: BaseNode(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-basenode__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-basenode__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of BaseNode by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected BaseNode(BaseNode node)RemarksThis constructor is protected. ParametersNameTypeDescriptionnodeBaseNodeThe instance of BaseNode to copy.

### BaseNode(BaseNode)

Initializes a new instance of [BaseNode](nationalinstruments-veristand-realtimesequencedefinitionapi-basenode.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected BaseNode(BaseNode node)

#### Remarks

This constructor is protected.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BaseNode | The instance of BaseNode to copy. |

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-clone.html language=enus -->
## TOPIC 01013: Clone()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-clone.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-clone.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new object that is a copy of the current instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic object Clone()ReturnsA new object that is a copy of this instance.

### Clone()

Creates a new object that is a copy of the current instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public object Clone()

#### Returns

A new object that is a copy of this instance.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-description.html language=enus -->
## TOPIC 01014: Description

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-description.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-description.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Description { get; set; }ReturnsThe description of the node.

### Description

Gets or sets the description of the node that appears in the **Property Browser** when you select the node in the Stimulus Profile Editor.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Description { get; set; }

#### Returns

The description of the node.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-propertychanged.html language=enus -->
## TOPIC 01015: PropertyChanged

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-propertychanged.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-propertychanged.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when a property value changes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic PropertyChangedEventHandler PropertyChanged

### PropertyChanged

Occurs when a property value changes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public PropertyChangedEventHandler PropertyChanged

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-resxkey.html language=enus -->
## TOPIC 01016: ResXKey

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-resxkey.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-basenode-resxkey.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string ResXKey { get; set; }RemarksFor a node to receive context help from a .resx file

### ResXKey

Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string ResXKey { get; set; }

#### Remarks

Note

For a node to receive context help from a .resx file, the file must exist in the following location: < Application Data > \User Interface\ResX\en

.resx files are useful if you want to store the context help strings for a real-time sequence in a separate place from the code itself. For example, if you have a designated technical writer, you can give that person one file to work in instead of all the code for your real-time sequence.

#### Returns

The ResX key. This must be the name of the .resx file with no file extensions followed by *data name*. For example, if an object with the data name My Sequence is defined in the .resx file My_ResX.en.resx, the ResX key for that object is:

My_ResX\My Sequence

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-basenode.html language=enus -->
## TOPIC 01017: BaseNode Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the abstract base class from which all nodes in a real-time sequence definition derive. Derives fromINotifyPropertyChangedICloneableSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class BaseNode : INotifyPropertyChanged, ICloneableRemarksBaseNode provide

### BaseNode Class

Represents the abstract base class from which all nodes in a real-time sequence definition derive.

#### Derives from

- INotifyPropertyChanged
- ICloneable

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class BaseNode : INotifyPropertyChanged, ICloneable

#### Remarks

BaseNode provides an abstract base class for nodes within the [RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html) namespace.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| BaseNode(BaseNode) | Initializes a new instance of BaseNode by copying an existing instance. |
| BaseNode() | Initializes a new instance of BaseNode. |

#### Properties

| Name | Description |
| --- | --- |
| Description | Gets or sets the description of the node that appears in the Property Browser when you select the node in the Stimulus Profile Editor. |
| ResXKey | Gets or sets the ResX key for the node, which is a pointer to a .resx file that contains a context help description for the node. |

#### Methods

| Name | Description |
| --- | --- |
| Clone() | Creates a new object that is a copy of the current instance. |

#### Events

| Name | Description |
| --- | --- |
| PropertyChanged | Occurs when a property value changes. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-addstatement__statement.html language=enus -->
## TOPIC 01018: AddStatement(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-addstatement__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-addstatement__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified functional statement to the end of the current block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddStatement(Statement statement)ParametersNameTypeDescriptionstatementStatementThe statement to add.

### AddStatement(Statement)

Adds the specified functional *statement*  to the end of the current block.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddStatement(Statement statement)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| statement | Statement | The statement to add. |

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-block.html language=enus -->
## TOPIC 01019: Block()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Block()

### Block()

Initializes a new instance of [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Block()

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-block__block.html language=enus -->
## TOPIC 01020: Block(Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-block__block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-block__block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Block by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Block(Block node)ParametersNameTypeDescriptionnodeBlockThe instance of Block to copy.

### Block(Block)

Initializes a new instance of [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Block(Block node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Block | The instance of Block to copy. |

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-block__statement_arr1.html language=enus -->
## TOPIC 01021: Block(Statement[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-block__statement_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-block__statement_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Block and creates a new block that contains the specified statements . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Block(Statement[] statements)ParametersNameTypeDescriptionstatementsStatement[]The functional statements to add to t

### Block(Statement[])

Initializes a new instance of [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) and creates a new block that contains the specified *statements* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Block(Statement[] statements)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| statements | Statement[] | The functional statements to add to the block. |

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-clearstatements.html language=enus -->
## TOPIC 01022: ClearStatements()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-clearstatements.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-clearstatements.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all the functional statements from the current block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearStatements()

### ClearStatements()

Clears all the functional statements from the current block.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearStatements()

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-equals__block.html language=enus -->
## TOPIC 01023: Equals(Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-equals__block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-equals__block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Block. Equivalency is determined using the Statements in the block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Block other)ParametersNameTypeDescriptionotherBlockThe

### Equals(Block)

Determines whether the specified *other*  object is equal to the current instance of [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html). Equivalency is determined using the [Statements](nationalinstruments-veristand-realtimesequencedefinitionapi-block-statements.html) in the block.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Block other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Block | The Block object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-equals__statement.html language=enus -->
## TOPIC 01024: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe Block type inherits from Statement. ParametersNameTypeDescriptionotherStatementT

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html). Otherwise, false.

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-gethashcode.html language=enus -->
## TOPIC 01025: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Block object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.GetHas

### GetHashCode()

Serves as a hash function for a [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) object.

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-name.html language=enus -->
## TOPIC 01026: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Name { get; set; }ReturnsThe name of the block. The default value is string.Empty.

### Name

Gets or sets the name of the block.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Name { get; set; }

#### Returns

The name of the block. The default value is string.Empty.

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block-statements.html language=enus -->
## TOPIC 01027: Statements

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block-statements.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block-statements.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get or sets the set of functional statements that the block contains and that execute when the block executes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Statement[] Statements { get; set; }ReturnsAn array of Statement objects.

### Statements

Get or sets the set of functional statements that the block contains and that execute when the block executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html)[] Statements { get; set; }

#### Returns

An array of [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html) objects.

Parent topic:

Block Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-block.html language=enus -->
## TOPIC 01028: Block Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Block primitive, which contains a list of functional statements to execute. You can use blocks to organize sequence code. Also, because a block itself is a single statement, you can use blocks to easily duplicate or move related statements that are grouped under a block. Certain pre-def

### Block Class

Represents a **Block** primitive, which contains a list of functional statements to execute. You can use blocks to organize sequence code. Also, because a block itself is a single statement, you can use blocks to easily duplicate or move related statements that are grouped under a block. Certain pre-defined sections of sequence code, such as [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html), use code blocks for the [Body](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-body.html) of their code.

#### Derives from

- Statement
- IEquatable< Block >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Block : Statement, IEquatable< Block >

#### Remarks

Use the members of this class to configure a code block. For example, you can add or remove the [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html) objects that belong to the block.

**Accessing this Class:**

- [Body](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-body.html)
- [Body](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-body.html)
- Block Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Block() | Initializes a new instance of Block. |
| Block(Statement[]) | Initializes a new instance of Block and creates a new block that contains the specified statements . |
| Block(Block) | Initializes a new instance of Block by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| Name | Gets or sets the name of the block. |
| Statements | Get or sets the set of functional statements that the block contains and that execute when the block executes. |

#### Methods

| Name | Description |
| --- | --- |
| AddStatement(Statement) | Adds the specified functional statement to the end of the current block. |
| ClearStatements() | Clears all the functional statements from the current block. |
| Equals(Block) | Determines whether the specified other object is equal to the current instance of Block. Equivalency is determined using the Statements in the block. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of Block. |
| GetHashCode() | Serves as a hash function for a Block object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-addcase__casestatement.html language=enus -->
## TOPIC 01029: AddCase(CaseStatement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-addcase__casestatement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-addcase__casestatement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified caseToAdd to the Cases section. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddCase(CaseStatement caseToAdd)ParametersNameTypeDescriptioncaseToAddCaseStatementThe case to add.

### AddCase(CaseStatement)

Adds the specified *caseToAdd*  to the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddCase(CaseStatement caseToAdd)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| caseToAdd | CaseStatement | The case to add. |

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-caselist.html language=enus -->
## TOPIC 01030: CaseList

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-caselist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-caselist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the list of case statements under the Cases section of a Switch statement. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CaseStatement[] CaseList { get; set; }ReturnsAn array of CaseStatement objects.

### CaseList

Gets or sets the list of case statements under the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section of a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html)[] CaseList { get; set; }

#### Returns

An array of [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) objects.

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases.html language=enus -->
## TOPIC 01031: Cases()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Cases. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Cases()

### Cases()

Initializes a new instance of [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Cases()

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases__cases.html language=enus -->
## TOPIC 01032: Cases(Cases)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases__cases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases__cases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Cases by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Cases(Cases node)ParametersNameTypeDescriptionnodeCasesThe instance of Cases to copy.

### Cases(Cases)

Initializes a new instance of [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Cases(Cases node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Cases | The instance of Cases to copy. |

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases__casestatement_arr1.html language=enus -->
## TOPIC 01033: Cases(CaseStatement[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases__casestatement_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-cases__casestatement_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Cases that contains the statements specified by caseList . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Cases(CaseStatement[] caseList)ParametersNameTypeDescriptioncaseListCaseStatement[]The case statements that the Cases section co

### Cases(CaseStatement[])

Initializes a new instance of [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) that contains the statements specified by *caseList* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Cases(CaseStatement[] caseList)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| caseList | CaseStatement[] | The case statements that the Cases section contains. |

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-clearcases.html language=enus -->
## TOPIC 01034: ClearCases()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-clearcases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-clearcases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all the statements from the Cases section. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearCases()

### ClearCases()

Clears all the statements from the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearCases()

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-equals__cases.html language=enus -->
## TOPIC 01035: Equals(Cases)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-equals__cases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-equals__cases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Cases. Equivalency is determined using the CaseList. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Cases other)ParametersNameTypeDescriptionotherCasesThe Cases object to

### Equals(Cases)

Determines whether the specified *other*  object is equal to the current instance of [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html). Equivalency is determined using the [CaseList](nationalinstruments-veristand-realtimesequencedefinitionapi-cases-caselist.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Cases other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Cases | The Cases object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-equals__object.html language=enus -->
## TOPIC 01036: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a Cases object, is equal to the current Cases. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj)RemarksOverrides object.Equals(object). ParametersNameTypeDescriptionobjobjectThe obj

### Equals(object)

Determines whether the specified *obj* , which must be a [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object, is equal to the current [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current Cases. |

#### Returns

true if the specified *obj*  is equal to the current [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html). Otherwise, false.

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases-gethashcode.html language=enus -->
## TOPIC 01037: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Cases object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.GetHas

### GetHashCode()

Serves as a hash function for a [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode().

#### Returns

A hash code for the current [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object.

Parent topic:

Cases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html language=enus -->
## TOPIC 01038: Cases Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Cases section under a Switch statement, which contains all the cases the statement can execute other than the DefaultCase. Derives fromBaseNodeIEquatable< Cases >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class Cases : BaseNode, IEquatable< Case

### Cases Class

Represents the **Cases** section under a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement, which contains all the cases the statement can execute other than the [DefaultCase](nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html).

#### Derives from

- BaseNode
- IEquatable< Cases >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Cases : BaseNode, IEquatable< Cases >

#### Remarks

Use the members of this class to add or remove cases of a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement.

**Accessing this Class:**

- [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-cases.html)
- Cases Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Cases() | Initializes a new instance of Cases. |
| Cases(CaseStatement[]) | Initializes a new instance of Cases that contains the statements specified by caseList . |
| Cases(Cases) | Initializes a new instance of Cases by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| CaseList | Gets or sets the list of case statements under the Cases section of a Switch statement. |

#### Methods

| Name | Description |
| --- | --- |
| AddCase(CaseStatement) | Adds the specified caseToAdd to the Cases section. |
| ClearCases() | Clears all the statements from the Cases section. |
| Equals(object) | Determines whether the specified obj , which must be a Cases object, is equal to the current Cases. |
| Equals(Cases) | Determines whether the specified other object is equal to the current instance of Cases. Equivalency is determined using the CaseList. |
| GetHashCode() | Serves as a hash function for a Cases object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement.html language=enus -->
## TOPIC 01039: CaseStatement()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CaseStatement. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CaseStatement()RemarksA CaseStatement can only exist under the Cases section of a Switch statement, and cannot stand alone.

### CaseStatement()

Initializes a new instance of [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public CaseStatement()

#### Remarks

Note

A [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) can only exist under the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section of a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement, and cannot stand alone.

Parent topic:

CaseStatement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement__casestatement.html language=enus -->
## TOPIC 01040: CaseStatement(CaseStatement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement__casestatement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement__casestatement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CaseStatement by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CaseStatement(CaseStatement node)RemarksA CaseStatement can only exist under the Cases section of a Switch statement, and cannot stand alone

### CaseStatement(CaseStatement)

Initializes a new instance of [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public CaseStatement(CaseStatement node)

#### Remarks

Note

A [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) can only exist under the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section of a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement, and cannot stand alone.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | CaseStatement | The instance of CaseStatement to copy. |

Parent topic:

CaseStatement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement__expression-block.html language=enus -->
## TOPIC 01041: CaseStatement(Expression, Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement__expression-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casestatement__expression-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CaseStatement and creates a case that executes the specified body of code when the value of the TestExpression in the Switch statement that contains the case is equal to the specified caseValue . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionA

### CaseStatement(Expression, Block)

Initializes a new instance of [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) and creates a case that executes the specified *body*  of code when the value of the [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html) in the [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement that contains the case is equal to the specified *caseValue* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public CaseStatement(Expression caseValue, Block body)

#### Remarks

Note

A [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) can only exist under the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section of a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement, and cannot stand alone.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| caseValue | Expression | The value that, if equal to the TestExpression value, executes the case. |
| body | Block | The set of statements that execute in the case. |

Parent topic:

CaseStatement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casevalue.html language=enus -->
## TOPIC 01042: CaseValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casevalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casevalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the value that, if equal to the TestExpression value, executes the case. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression CaseValue { get; set; }ReturnsThe value that specifies to execute this case, as an Expression.

### CaseValue

Gets or sets the value that, if equal to the [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-testexpression.html) value, executes the case.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) CaseValue { get; set; }

#### Returns

The value that specifies to execute this case, as an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

Parent topic:

CaseStatement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-equals__casestatement.html language=enus -->
## TOPIC 01043: Equals(CaseStatement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-equals__casestatement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-equals__casestatement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of CaseStatement. Equivalency is determined using the CaseValue and the body of code that the case executes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(CaseStatement oth

### Equals(CaseStatement)

Determines whether the specified *other*  object is equal to the current instance of [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html). Equivalency is determined using the [CaseValue](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casevalue.html) and the body of code that the case executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(CaseStatement other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | CaseStatement | The CaseStatement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

CaseStatement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-equals__object.html language=enus -->
## TOPIC 01044: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a CaseStatement object, is equal to the current CaseStatement. Equivalency is determined using the CaseValue and the body of code that the case executes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override b

### Equals(object)

Determines whether the specified *obj* , which must be a [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) object, is equal to the current [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html). Equivalency is determined using the [CaseValue](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-casevalue.html) and the body of code that the case executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current Cases. |

#### Returns

true if the specified *obj*  is equal to the current [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html). Otherwise, false.

Parent topic:

CaseStatement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-gethashcode.html language=enus -->
## TOPIC 01045: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a CaseStatement object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHa

### GetHashCode()

Serves as a hash function for a [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-gethashcode.html).

#### Returns

A hash code for the current [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) object.

Parent topic:

CaseStatement Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html language=enus -->
## TOPIC 01046: CaseStatement Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an individual case under the Cases section of a Switch statement. Derives fromCodeSectionIEquatable< CaseStatement >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class CaseStatement : CodeSection, IEquatable< CaseStatement >RemarksUse the members of th

### CaseStatement Class

Represents an individual case under the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section of a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement.

#### Derives from

- CodeSection
- IEquatable< CaseStatement >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class CaseStatement : CodeSection, IEquatable< CaseStatement >

#### Remarks

Use the members of this class to configure the statements that a case executes and to get or set the value that specifies to execute the case.

**Accessing this Class:**

- [CaseList](nationalinstruments-veristand-realtimesequencedefinitionapi-cases-caselist.html)
- CaseStatement Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CaseStatement(Expression, Block) | Initializes a new instance of CaseStatement and creates a case that executes the specified body of code when the value of the TestExpression in the Switch statement that contains the case is equal to the specified caseValue . |
| CaseStatement(CaseStatement) | Initializes a new instance of CaseStatement by copying an existing instance. |
| CaseStatement() | Initializes a new instance of CaseStatement. |

#### Properties

| Name | Description |
| --- | --- |
| CaseValue | Gets or sets the value that, if equal to the TestExpression value, executes the case. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Determines whether the specified obj , which must be a CaseStatement object, is equal to the current CaseStatement. Equivalency is determined using the CaseValue and the body of code that the case executes. |
| Equals(CaseStatement) | Determines whether the specified other object is equal to the current instance of CaseStatement. Equivalency is determined using the CaseValue and the body of code that the case executes. |
| GetHashCode() | Serves as a hash function for a CaseStatement object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channel.html language=enus -->
## TOPIC 01047: Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Channel. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic SystemDefinitionChannelResource Channel { get; set; }

### Channel

Gets or sets the Channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [SystemDefinitionChannelResource](nationalinstruments-veristand-data-systemdefinitionchannelresource.html) Channel { get; set; }

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration.html language=enus -->
## TOPIC 01048: ChannelReferenceDeclaration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ChannelReferenceDeclaration class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferenceDeclaration()

### ChannelReferenceDeclaration()

Initializes a new instance of the [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ChannelReferenceDeclaration()

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__channelreferencedeclaration.html language=enus -->
## TOPIC 01049: ChannelReferenceDeclaration(ChannelReferenceDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__channelreferencedeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__channelreferencedeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ChannelReferenceDeclaration class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferenceDeclaration(ChannelReferenceDeclaration node)ParametersNameTypeDescriptionnodeChannelReferenceDeclar

### ChannelReferenceDeclaration(ChannelReferenceDeclaration)

Initializes a new instance of the [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ChannelReferenceDeclaration(ChannelReferenceDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ChannelReferenceDeclaration | The instance of ChannelReferenceDeclaration to copy. |

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__string-systemdefinitionchannelresource-channelsizetype.html language=enus -->
## TOPIC 01050: ChannelReferenceDeclaration(string, SystemDefinitionChannelResource, ChannelSizeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__string-systemdefinitionchannelresource-channelsizetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__string-systemdefinitionchannelresource-channelsizetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ChannelReferenceDeclaration class and creates a sequence channel with the specified identifier . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferenceDeclaration(string identifier, SystemDefinitionChannelResource channel

### ChannelReferenceDeclaration(string, SystemDefinitionChannelResource, ChannelSizeType)

Initializes a new instance of the [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) class and creates a sequence channel with the specified *identifier* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ChannelReferenceDeclaration(string identifier, SystemDefinitionChannelResource channel, ChannelSizeType channelType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The name of the channel. |
| channel | SystemDefinitionChannelResource | The channel to map the data resource to in the system definition file. |
| channelType | ChannelSizeType | Specifies the channel type. |

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__string-systemdefinitionchannelresource.html language=enus -->
## TOPIC 01051: ChannelReferenceDeclaration(string, SystemDefinitionChannelResource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__string-systemdefinitionchannelresource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channelreferencedeclaration__string-systemdefinitionchannelresource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ChannelReferenceDeclaration class and creates a sequence channel with the specified identifier . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferenceDeclaration(string identifier, SystemDefinitionChannelResource channel

### ChannelReferenceDeclaration(string, SystemDefinitionChannelResource)

Initializes a new instance of the [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) class and creates a sequence channel with the specified *identifier* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ChannelReferenceDeclaration(string identifier, SystemDefinitionChannelResource channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The name of the channel. |
| channel | SystemDefinitionChannelResource | The channel to map the data resource to in the system definition file. |

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channeltype.html language=enus -->
## TOPIC 01052: ChannelType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channeltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channeltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the type of channel referenced. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelSizeType ChannelType { get; set; }

### ChannelType

Gets or sets a value indicating the type of channel referenced.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [ChannelSizeType](nationalinstruments-veristand-realtimesequencedefinitionapi-channelsizetype.html) ChannelType { get; set; }

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-defaultvalue.html language=enus -->
## TOPIC 01053: DefaultValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-defaultvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default value of the declared object. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override DataValue DefaultValue { get; set; }ReturnsA DataValue object.

### DefaultValue

Gets or sets the default value of the declared object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override [DataValue](nationalinstruments-veristand-data-datavalue.html) DefaultValue { get; set; }

#### Returns

A [DataValue](nationalinstruments-veristand-data-datavalue.html) object.

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-equals__channelreferencedeclaration.html language=enus -->
## TOPIC 01054: Equals(ChannelReferenceDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-equals__channelreferencedeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-equals__channelreferencedeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of ChannelReferenceDeclaration. Equivalency is determined using the base class and Channel. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(ChannelReferenceDeclaration other)

### Equals(ChannelReferenceDeclaration)

Determines whether the specified *other*  object is equal to the current instance of [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html). Equivalency is determined using the base class and [Channel](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-channel.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(ChannelReferenceDeclaration other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ChannelReferenceDeclaration | The ChannelReferenceDeclaration object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-equals__object.html language=enus -->
## TOPIC 01055: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a ChannelReferenceDeclaration object, is equal to the current ChannelReferenceDeclaration. Equivalency is determined using the base class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(obje

### Equals(object)

Determines whether the specified *obj* , which must be a [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) object, is equal to the current [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html). Equivalency is determined using the base class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current ChannelReferenceDeclaration. |

#### Returns

true if the specified *obj*  is equal to the current [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html). Otherwise, false.

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-gethashcode.html language=enus -->
## TOPIC 01056: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Cases object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCode.

### GetHashCode()

Serves as a hash function for a [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-gethashcode.html).

#### Returns

A hash code for the current [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object.

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-operator-localdeclaration__channelreferencedeclaration.html language=enus -->
## TOPIC 01057: operator LocalDeclaration(ChannelReferenceDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-operator-localdeclaration__channelreferencedeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-operator-localdeclaration__channelreferencedeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a ChannelReferenceDeclaration to a LocalDeclaration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic static operator LocalDeclaration(ChannelReferenceDeclaration node)ParametersNameTypeDescriptionnodeChannelReferenceDeclarationThe node to cast.ReturnsA Loc

### operator LocalDeclaration(ChannelReferenceDeclaration)

Converts a [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) to a [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static operator LocalDeclaration(ChannelReferenceDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ChannelReferenceDeclaration | The node to cast. |

#### Returns

A [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html) with similar settings to the source [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html).

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-operator-parameterdeclaration__channelreferencedeclaration.html language=enus -->
## TOPIC 01058: operator ParameterDeclaration(ChannelReferenceDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-operator-parameterdeclaration__channelreferencedeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration-operator-parameterdeclaration__channelreferencedeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a ChannelReferenceDeclaration to a ParameterDeclaration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic static operator ParameterDeclaration(ChannelReferenceDeclaration node)ParametersNameTypeDescriptionnodeChannelReferenceDeclarationThe node to cast.Retu

### operator ParameterDeclaration(ChannelReferenceDeclaration)

Converts a [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) to a [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static operator ParameterDeclaration(ChannelReferenceDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ChannelReferenceDeclaration | The node to cast. |

#### Returns

A [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) with similar settings to the source [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html).

Parent topic:

ChannelReferenceDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html language=enus -->
## TOPIC 01059: ChannelReferenceDeclaration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a declaration of a real-time sequence channel reference. Derives fromAbstractDeclarationIEquatable< ChannelReferenceDeclaration >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class ChannelReferenceDeclaration : AbstractDeclaration, IEquatable< ChannelR

### ChannelReferenceDeclaration Class

Represents a declaration of a real-time sequence channel reference.

#### Derives from

- AbstractDeclaration
- IEquatable< ChannelReferenceDeclaration >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class ChannelReferenceDeclaration : AbstractDeclaration, IEquatable< ChannelReferenceDeclaration >

#### Constructors

| Name | Description |
| --- | --- |
| ChannelReferenceDeclaration(string, SystemDefinitionChannelResource, ChannelSizeType) | Initializes a new instance of the ChannelReferenceDeclaration class and creates a sequence channel with the specified identifier . |
| ChannelReferenceDeclaration(string, SystemDefinitionChannelResource) | Initializes a new instance of the ChannelReferenceDeclaration class and creates a sequence channel with the specified identifier . |
| ChannelReferenceDeclaration() | Initializes a new instance of the ChannelReferenceDeclaration class. |
| ChannelReferenceDeclaration(ChannelReferenceDeclaration) | Initializes a new instance of the ChannelReferenceDeclaration class by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| Channel | Gets or sets the Channel. |
| ChannelType | Gets or sets a value indicating the type of channel referenced. |
| DefaultValue | Gets or sets the default value of the declared object. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Determines whether the specified obj , which must be a ChannelReferenceDeclaration object, is equal to the current ChannelReferenceDeclaration. Equivalency is determined using the base class. |
| Equals(ChannelReferenceDeclaration) | Determines whether the specified other object is equal to the current instance of ChannelReferenceDeclaration. Equivalency is determined using the base class and Channel. |
| GetHashCode() | Serves as a hash function for a Cases object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

#### Operators

| Name | Description |
| --- | --- |
| operator LocalDeclaration(ChannelReferenceDeclaration) | Converts a ChannelReferenceDeclaration to a LocalDeclaration. |
| operator ParameterDeclaration(ChannelReferenceDeclaration) | Converts a ChannelReferenceDeclaration to a ParameterDeclaration. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-addchannelreference__channelreferencedeclaration.html language=enus -->
## TOPIC 01060: AddChannelReference(ChannelReferenceDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-addchannelreference__channelreferencedeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-addchannelreference__channelreferencedeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified channelRef to the end of the ChannelReferences section. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddChannelReference(ChannelReferenceDeclaration channelRef)ParametersNameTypeDescriptionchannelRefChannelReferenceDeclarationThe channel

### AddChannelReference(ChannelReferenceDeclaration)

Adds the specified *channelRef*  to the end of the [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddChannelReference(ChannelReferenceDeclaration channelRef)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelRef | ChannelReferenceDeclaration | The channel reference declaration to add. |

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channelreferences.html language=enus -->
## TOPIC 01061: ChannelReferences()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channelreferences.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channelreferences.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ChannelReferences class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferences()

### ChannelReferences()

Initializes a new instance of the [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ChannelReferences()

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channelreferences__channelreferences.html language=enus -->
## TOPIC 01062: ChannelReferences(ChannelReferences)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channelreferences__channelreferences.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channelreferences__channelreferences.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ChannelReferences class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferences(ChannelReferences node)ParametersNameTypeDescriptionnodeChannelReferencesThe instance of ChannelReferences t

### ChannelReferences(ChannelReferences)

Initializes a new instance of the [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ChannelReferences(ChannelReferences node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ChannelReferences | The instance of ChannelReferences to copy. |

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channels.html language=enus -->
## TOPIC 01063: Channels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the array of defined channel reference declarations for the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ChannelReferenceDeclaration[] Channels { get; set; }ReturnsAn array of ChannelReferenceDeclaration objects.

### Channels

Gets or sets the array of defined channel reference declarations for the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html)[] Channels { get; set; }

#### Returns

An array of [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) objects.

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-clearchannelreferences.html language=enus -->
## TOPIC 01064: ClearChannelReferences()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-clearchannelreferences.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-clearchannelreferences.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all the currently declared channel references from the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearChannelReferences()

### ClearChannelReferences()

Clears all the currently declared channel references from the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearChannelReferences()

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-equals__channelreferences.html language=enus -->
## TOPIC 01065: Equals(ChannelReferences)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-equals__channelreferences.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-equals__channelreferences.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of ChannelReferences. Equivalency is determined using Channels. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(ChannelReferences other)ParametersNameTypeDescriptionotherChan

### Equals(ChannelReferences)

Determines whether the specified *other*  object is equal to the current instance of [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html). Equivalency is determined using [Channels](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channels.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(ChannelReferences other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ChannelReferences | The ChannelReferences object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-equals__object.html language=enus -->
## TOPIC 01066: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a ChannelReferences object, is equal to the current ChannelReferences. Equivalency is determined using Channels. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj)RemarksOverrides ob

### Equals(object)

Determines whether the specified *obj* , which must be a [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) object, is equal to the current [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html). Equivalency is determined using [Channels](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-channels.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current ChannelReferences. |

#### Returns

true if the specified *obj*  is equal to the current [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html). Otherwise, false.

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-gethashcode.html language=enus -->
## TOPIC 01067: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a ChannelReferences object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides o

### GetHashCode()

Serves as a hash function for a [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [ChannelReferences](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html) object.

Parent topic:

ChannelReferences Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html language=enus -->
## TOPIC 01068: ChannelReferences Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferences.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Channel References section of the real-time sequence definition, which contains the channel reference declarations for the sequence. Derives fromBaseNodeIEquatable< ChannelReferences >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class ChannelRefer

### ChannelReferences Class

Represents the **Channel References** section of the real-time sequence definition, which contains the channel reference declarations for the sequence.

#### Derives from

- BaseNode
- IEquatable< ChannelReferences >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class ChannelReferences : BaseNode, IEquatable< ChannelReferences >

#### Constructors

| Name | Description |
| --- | --- |
| ChannelReferences() | Initializes a new instance of the ChannelReferences class. |
| ChannelReferences(ChannelReferences) | Initializes a new instance of the ChannelReferences class by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| Channels | Gets or sets the array of defined channel reference declarations for the real-time sequence. |

#### Methods

| Name | Description |
| --- | --- |
| AddChannelReference(ChannelReferenceDeclaration) | Adds the specified channelRef to the end of the ChannelReferences section. |
| ClearChannelReferences() | Clears all the currently declared channel references from the real-time sequence. |
| Equals(object) | Determines whether the specified obj , which must be a ChannelReferences object, is equal to the current ChannelReferences. Equivalency is determined using Channels. |
| Equals(ChannelReferences) | Determines whether the specified other object is equal to the current instance of ChannelReferences. Equivalency is determined using Channels. |
| GetHashCode() | Serves as a hash function for a ChannelReferences object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-channelsizetype.html language=enus -->
## TOPIC 01069: ChannelSizeType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-channelsizetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-channelsizetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of channel to reference. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic enum ChannelSizeTypeMembersNameValueDescriptionScalarSpecifies that the channel is a scalar. VectorSpecifies that the channel is a vector.

### ChannelSizeType Enumeration

Specifies the type of channel to reference.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public enum ChannelSizeType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Scalar |  | Specifies that the channel is a scalar. |
| Vector |  | Specifies that the channel is a vector. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup-cleanup.html language=enus -->
## TOPIC 01070: CleanUp()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup-cleanup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup-cleanup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CleanUp. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CleanUp()

### CleanUp()

Initializes a new instance of [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public CleanUp()

Parent topic:

CleanUp Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup-cleanup__cleanup.html language=enus -->
## TOPIC 01071: CleanUp(CleanUp)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup-cleanup__cleanup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup-cleanup__cleanup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CleanUp by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CleanUp(CleanUp node)ParametersNameTypeDescriptionnodeCleanUpThe instance of CleanUp to copy.

### CleanUp(CleanUp)

Initializes a new instance of [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public CleanUp(CleanUp node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | CleanUp | The instance of CleanUp to copy. |

Parent topic:

CleanUp Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html language=enus -->
## TOPIC 01072: CleanUp Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Clean Up section of sequence code, which executes after the Setup and Main code sections. This section contains statements that are critical to execute at the end of sequence execution. If a task running a sequence is stopped, the sequence immediately begins executing the statements i

### CleanUp Class

Represents the **Clean Up** section of sequence code, which executes after the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) and [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) code sections. This section contains statements that are critical to execute at the end of sequence execution. If a task running a sequence is stopped, the sequence immediately begins executing the statements in the CleanUp section.

#### Derives from

- CodeSection

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class CleanUp : CodeSection

#### Remarks

Use this section at the end of sequence execution to reset variables to appropriate values as needed.

**Accessing this Class:**

- [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-code-cleanup.html)
- CleanUp Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CleanUp(CleanUp) | Initializes a new instance of CleanUp by copying an existing instance. |
| CleanUp() | Initializes a new instance of CleanUp. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-cleanup.html language=enus -->
## TOPIC 01073: CleanUp

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-cleanup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-cleanup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CleanUp section of sequence code, which executes after the Setup and Main code sections. This section contains statements that are critical to execute at the end of sequence execution. If a task running a sequence is stopped, the sequence immediately begins executing the statements

### CleanUp

Gets or sets the [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) section of sequence code, which executes after the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) and [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) code sections. This section contains statements that are critical to execute at the end of sequence execution. If a task running a sequence is stopped, the sequence immediately begins executing the statements in the [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) CleanUp { get; set; }

#### Returns

A [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) object.

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-code.html language=enus -->
## TOPIC 01074: Code()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-code.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-code.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Code. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Code()

### Code()

Initializes a new instance of [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Code()

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-code__code.html language=enus -->
## TOPIC 01075: Code(Code)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-code__code.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-code__code.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Code by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Code(Code node)ParametersNameTypeDescriptionnodeCodeThe instance of Code to copy.

### Code(Code)

Initializes a new instance of [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Code(Code node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Code | The instance of Code to copy. |

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-equals__code.html language=enus -->
## TOPIC 01076: Equals(Code)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-equals__code.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-equals__code.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Code. Equivalency is determined using the Setup, Main, and CleanUp code sections. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Code other)ParametersNameTypeDescriptiono

### Equals(Code)

Determines whether the specified *other*  object is equal to the current instance of [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html). Equivalency is determined using the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) code sections.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Code other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Code | The Code object to compare with the current instance. |

#### Returns

true if the specified *other*  object equal to the current instance. Otherwise, false.

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-equals__object.html language=enus -->
## TOPIC 01077: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a Code object, is equal to the current instance of Code. Equivalency is determined using the Setup, Main, and CleanUp code sections. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj

### Equals(object)

Determines whether the specified *obj* , which must be a [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html) object, is equal to the current instance of [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html). Equivalency is determined using the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) code sections.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current Code object. |

#### Returns

true if the specified *obj*  is equal to the current [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html) object. Otherwise, false.

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-gethashcode.html language=enus -->
## TOPIC 01078: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Code object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.GetHash

### GetHashCode()

Serves as a hash function for a [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-code.html) object.

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-main.html language=enus -->
## TOPIC 01079: Main

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-main.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-main.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Main section of sequence code, which executes after the Setup section and before the CleanUp sections. This section contains the core set of statements that the sequence executes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Main Main { get; set

### Main

Gets or sets the [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) section of sequence code, which executes after the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) section and before the [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) sections. This section contains the core set of statements that the sequence executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) Main { get; set; }

#### Returns

A [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) object.

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code-setup.html language=enus -->
## TOPIC 01080: Setup

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code-setup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code-setup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Setup section of sequence code, which executes before the Main and CleanUp code sections. This section contains statements that initialize the sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Setup Setup { get; set; }ReturnsA Setup object.

### Setup

Gets or sets the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) section of sequence code, which executes before the [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) code sections. This section contains statements that initialize the sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) Setup { get; set; }

#### Returns

A [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) object.

Parent topic:

Code Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-code.html language=enus -->
## TOPIC 01081: Code Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-code.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-code.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Code section of a sequence, which is the top-level container for all sequence code and contains the Setup, Main, and CleanUp sections. Derives fromBaseNodeIEquatable< Code >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class Code : BaseNode, IEquat

### Code Class

Represents the **Code** section of a sequence, which is the top-level container for all sequence code and contains the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) sections.

#### Derives from

- BaseNode
- IEquatable< Code >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Code : BaseNode, IEquatable< Code >

#### Remarks

Use the members of this class to access the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) sections of sequence code.

**Accessing this Class:**

- [Code](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence-code.html)
- Code Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Code(Code) | Initializes a new instance of Code by copying an existing instance. |
| Code() | Initializes a new instance of Code. |

#### Properties

| Name | Description |
| --- | --- |
| CleanUp | Gets or sets the CleanUp section of sequence code, which executes after the Setup and Main code sections. This section contains statements that are critical to execute at the end of sequence execution. If a task running a sequence is stopped, the sequence immediately begins executing the statements in the CleanUp section. |
| Main | Gets or sets the Main section of sequence code, which executes after the Setup section and before the CleanUp sections. This section contains the core set of statements that the sequence executes. |
| Setup | Gets or sets the Setup section of sequence code, which executes before the Main and CleanUp code sections. This section contains statements that initialize the sequence. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Determines whether the specified obj , which must be a Code object, is equal to the current instance of Code. Equivalency is determined using the Setup, Main, and CleanUp code sections. |
| Equals(Code) | Determines whether the specified other object is equal to the current instance of Code. Equivalency is determined using the Setup, Main, and CleanUp code sections. |
| GetHashCode() | Serves as a hash function for a Code object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-addstatement__statement.html language=enus -->
## TOPIC 01082: AddStatement(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-addstatement__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-addstatement__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified functional statement to the end of the current section of code. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddStatement(Statement statement)ParametersNameTypeDescriptionstatementStatementThe statement to add.

### AddStatement(Statement)

Adds the specified functional *statement*  to the end of the current section of code.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddStatement(Statement statement)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| statement | Statement | The statement to add. |

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-body.html language=enus -->
## TOPIC 01083: Body

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-body.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-body.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the body of the code section, which contains all the blocks and statements in the section. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Block Body { get; set; }ReturnsA Block object.

### Body

Gets or sets the body of the code section, which contains all the blocks and statements in the section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) Body { get; set; }

#### Returns

A [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) object.

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-clearstatements.html language=enus -->
## TOPIC 01084: ClearStatements()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-clearstatements.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-clearstatements.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all the functional statements from the current section of code. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearStatements()

### ClearStatements()

Clears all the functional statements from the current section of code.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearStatements()

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-codesection.html language=enus -->
## TOPIC 01085: CodeSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-codesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-codesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CodeSection. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected CodeSection()

### CodeSection()

Initializes a new instance of [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected CodeSection()

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-codesection__codesection.html language=enus -->
## TOPIC 01086: CodeSection(CodeSection)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-codesection__codesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-codesection__codesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CodeSection by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiprotected CodeSection(CodeSection node)ParametersNameTypeDescriptionnodeCodeSectionThe instance of CodeSection to copy.

### CodeSection(CodeSection)

Initializes a new instance of [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

protected CodeSection(CodeSection node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | CodeSection | The instance of CodeSection to copy. |

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-equals__codesection.html language=enus -->
## TOPIC 01087: Equals(CodeSection)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-equals__codesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-equals__codesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of CodeSection. Equivalency is determined using the Body code block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(CodeSection other)ParametersNameTypeDescriptionotherCodeS

### Equals(CodeSection)

Determines whether the specified *other*  object is equal to the current instance of [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html). Equivalency is determined using the [Body](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-body.html) code block.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(CodeSection other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | CodeSection | The CodeSection object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-equals__object.html language=enus -->
## TOPIC 01088: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a CodeSection object, is equal to the current instance of CodeSection. Equivalency is determined using the Body code block. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj)RemarksO

### Equals(object)

Determines whether the specified *obj* , which must be a [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html) object, is equal to the current instance of [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html). Equivalency is determined using the [Body](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-body.html) code block.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current CodeSection object. |

#### Returns

true if the specified *obj*  is equal to the current [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html) object. Otherwise, false.

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-gethashcode.html language=enus -->
## TOPIC 01089: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a CodeSection object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.

### GetHashCode()

Serves as a hash function for a [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [CodeSection](nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html) object.

Parent topic:

CodeSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html language=enus -->
## TOPIC 01090: CodeSection Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-codesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a section of code in a real-time sequence. This is a base class from which more specific code section classes, such as Setup, Main, and CleanUp, inherit. Derives fromBaseNodeIEquatable< CodeSection >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class C

### CodeSection Class

Represents a section of code in a real-time sequence. This is a base class from which more specific code section classes, such as [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html), [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html), and [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html), inherit.

#### Derives from

- BaseNode
- IEquatable< CodeSection >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class CodeSection : BaseNode, IEquatable< CodeSection >

#### Remarks

Use the members of this class to configure the statements included in a section of real-time sequence code.

**Accessing this Class:**

- CodeSection Constructor

Note

You also can access members of this class from any class that defines a section of real-time sequence code.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CodeSection(CodeSection) | Initializes a new instance of CodeSection by copying an existing instance. |
| CodeSection() | Initializes a new instance of CodeSection. |

#### Properties

| Name | Description |
| --- | --- |
| Body | Gets or sets the body of the code section, which contains all the blocks and statements in the section. |

#### Methods

| Name | Description |
| --- | --- |
| AddStatement(Statement) | Adds the specified functional statement to the end of the current section of code. |
| ClearStatements() | Clears all the functional statements from the current section of code. |
| Equals(CodeSection) | Determines whether the specified other object is equal to the current instance of CodeSection. Equivalency is determined using the Body code block. |
| Equals(object) | Determines whether the specified obj , which must be a CodeSection object, is equal to the current instance of CodeSection. Equivalency is determined using the Body code block. |
| GetHashCode() | Serves as a hash function for a CodeSection object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment.html language=enus -->
## TOPIC 01091: Comment()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Comment. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Comment()

### Comment()

Initializes a new instance of [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Comment()

Parent topic:

Comment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment__comment.html language=enus -->
## TOPIC 01092: Comment(Comment)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment__comment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment__comment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Comment by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Comment(Comment node)ParametersNameTypeDescriptionnodeCommentThe instance of Comment to copy.

### Comment(Comment)

Initializes a new instance of [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Comment(Comment node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Comment | The instance of Comment to copy. |

Parent topic:

Comment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment__string.html language=enus -->
## TOPIC 01093: Comment(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment-comment__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Comment and creates a comment with the specified text string. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Comment(string text)ParametersNameTypeDescriptiontextstringThe string that the comment stores.

### Comment(string)

Initializes a new instance of [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html) and creates a comment with the specified *text*  string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Comment(string text)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| text | string | The string that the comment stores. |

Parent topic:

Comment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment-equals__comment.html language=enus -->
## TOPIC 01094: Equals(Comment)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment-equals__comment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment-equals__comment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Comment. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Comment other)ParametersNameTypeDescriptionotherCommentThe Comment object to compare with the current instance.Ret

### Equals(Comment)

Determines whether the specified *other*  object is equal to the current instance of [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Comment other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Comment | The Comment object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Comment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment-equals__statement.html language=enus -->
## TOPIC 01095: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Comment. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe Comment type inherits from Statement. ParametersNameTypeDescriptionotherStatem

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html). Otherwise, false.

Parent topic:

Comment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment-gethashcode.html language=enus -->
## TOPIC 01096: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Comment object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.GetH

### GetHashCode()

Serves as a hash function for a [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [Comment](nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html) object.

Parent topic:

Comment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment-text.html language=enus -->
## TOPIC 01097: Text

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment-text.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment-text.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the string that a comment contains. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Text { get; set; }ReturnsThe text of the comment.

### Text

Gets or sets the string that a comment contains.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Text { get; set; }

#### Returns

The text of the comment.

Parent topic:

Comment Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html language=enus -->
## TOPIC 01098: Comment Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-comment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Comment primitive, which is a a non-functional statement you can use to document code. This primitive simply stores a string, and functions similarly to comment tags in text-based programming. It has no effect on the execution of a real-time sequence. Derives fromStatementIEquatable< Co

### Comment Class

Represents a **Comment** primitive, which is a a non-functional statement you can use to document code. This primitive simply stores a string, and functions similarly to comment tags in text-based programming. It has no effect on the execution of a real-time sequence.

#### Derives from

- Statement
- IEquatable< Comment >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Comment : Statement, IEquatable< Comment >

#### Remarks

Use the members of this class to get or set the text that a **Comment** contains.

**Accessing this Class:**

- Comment Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Comment(Comment) | Initializes a new instance of Comment by copying an existing instance. |
| Comment() | Initializes a new instance of Comment. |
| Comment(string) | Initializes a new instance of Comment and creates a comment with the specified text string. |

#### Properties

| Name | Description |
| --- | --- |
| Text | Gets or sets the string that a comment contains. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of Comment. |
| Equals(Comment) | Determines whether the specified other object is equal to the current instance of Comment. |
| GetHashCode() | Serves as a hash function for a Comment object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-code.html language=enus -->
## TOPIC 01099: Code

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-code.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-code.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the code for an event that occurs during compilation. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CompilationEventCode Code { get; }ReturnsAn enumeration of CompilationEventCode.

### Code

Gets the code for an event that occurs during compilation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [CompilationEventCode](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventcode.html) Code { get; }

#### Returns

An enumeration of [CompilationEventCode](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventcode.html).

Parent topic:

CompilationEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-details.html language=enus -->
## TOPIC 01100: Details

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-details.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-details.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets details about the event that occurred during compilation. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Details { get; }ReturnsDetails about the event.

### Details

Gets details about the event that occurred during compilation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Details { get; }

#### Returns

Details about the event.

Parent topic:

CompilationEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-eventtype.html language=enus -->
## TOPIC 01101: EventType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-eventtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-eventtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of event that occurred during compilation. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CompilationEventType EventType { get; }ReturnsAn enumeration of CompilationEventType.

### EventType

Gets the type of event that occurred during compilation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [CompilationEventType](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html) EventType { get; }

#### Returns

An enumeration of [CompilationEventType](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html).

Parent topic:

CompilationEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-message.html language=enus -->
## TOPIC 01102: Message

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-message.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-message.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a message describing the event that occurred during compilation. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Message { get; }ReturnsA message describing the event.

### Message

Gets a message describing the event that occurred during compilation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Message { get; }

#### Returns

A message describing the event.

Parent topic:

CompilationEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-sourcefile.html language=enus -->
## TOPIC 01103: SourceFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-sourcefile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-sourcefile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the file that this event occurred in. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string SourceFile { get; }ReturnsThe path to the source file on disk.

### SourceFile

Gets the file that this event occurred in.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string SourceFile { get; }

#### Returns

The path to the source file on disk.

Parent topic:

CompilationEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-sourcenodepath.html language=enus -->
## TOPIC 01104: SourceNodePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-sourcenodepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-sourcenodepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that represents a path from the RootNode to the node that is the source of the compilation event. The path is represented through successive indices in the array, starting at the RootNode of the RealTimeSequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinition

### SourceNodePath

Gets an array that represents a path from the [RootNode](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html) to the node that is the source of the compilation event. The path is represented through successive indices in the array, starting at the [RootNode](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html) of the [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public int[] SourceNodePath { get; }

#### Returns

An array representing the path from the [RootNode](nationalinstruments-veristand-realtimesequencedefinitionapi-rootnode.html) to the node that is the source of the compilation event.

Parent topic:

CompilationEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-tostring.html language=enus -->
## TOPIC 01105: ToString()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-tostring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent-tostring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the compilation event. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override string ToString()RemarksOverrides object.ToString. ReturnsA string representation of the event that occurred.

### ToString()

Returns a string representation of the compilation event.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override string ToString()

#### Remarks

Overrides object.ToString.

#### Returns

A string representation of the event that occurred.

Parent topic:

CompilationEvent Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html language=enus -->
## TOPIC 01106: CompilationEvent Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides information about errors, warnings, and messages that occurred during compilation of real-time sequence and stimulus profile files. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class CompilationEventRemarksUse the members of this class t

### CompilationEvent Class

Provides information about errors, warnings, and messages that occurred during compilation of real-time sequence and stimulus profile files.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class CompilationEvent

#### Remarks

Use the members of this class to get information about a compilation event, such as the relevant error code, the type of event, and so on.

**Accessing this Class:**

- [CompilationEvents](nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compilationevents.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-actionstep-checkforerrors.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-macroplayerstep-checkforerrors.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-openprojectstep-checkforerrors.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-openworkspacetoolstep-checkforerrors.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-realtimesequencegroupstep-checkforerrors.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-startloggingstep-checkforerrors.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-stepgroup-checkforerrors.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-stimulusprofile-checkforerrors.html)
- [Events](nationalinstruments-veristand-realtimesequencedefinitionapi-stimulusprofilecompilationexception-events.html)
- [CheckForErrors](nationalinstruments-veristand-stimulusprofiledefinitionapi-stoploggingstep-checkforerrors.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets the code for an event that occurs during compilation. |
| Details | Gets details about the event that occurred during compilation. |
| EventType | Gets the type of event that occurred during compilation. |
| Message | Gets a message describing the event that occurred during compilation. |
| SourceFile | Gets the file that this event occurred in. |
| SourceNodePath | Gets an array that represents a path from the RootNode to the node that is the source of the compilation event. The path is represented through successive indices in the array, starting at the RootNode of the RealTimeSequence. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the compilation event. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventcode.html language=enus -->
## TOPIC 01107: CompilationEventCode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the code for an event that occurs during compilation of a real-time sequence or stimulus profile. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic enum CompilationEventCodeMembersNameValueDescriptionNone0No event occurred. Generic-1TO DO. DuplicateTaskName

### CompilationEventCode Enumeration

Specifies the code for an event that occurs during compilation of a real-time sequence or stimulus profile.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public enum CompilationEventCode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No event occurred. |
| Generic | -1 | TO DO. |
| DuplicateTaskName | -2 | A real-time sequence contains two or more tasks with the same name. Task names must be unique within a sequence. |
| TaskDoesNotExist | -3 | The Task does not exist. |
| AliasDoesNotExist | -4 | A specified subsequence name could not be found. The calling sequence might be missing a reference to the subsequence. |
| AliasMaskedByBuiltInFunction | -5 | A specified subsequence name is the same as the name of a built-in function of NI VeriStand. New subsequences must have unique names. |
| AmbiguousAlias | -6 | A specified subsequence name is ambiguous, and could refer to more than one reference. Check the References section for duplicate reference names. |
| ArrayParameterTypeMismatch | -7 | A specified expression is a type of array that does not match the type of the parameter it is being passed to. Array parameters must match exactly. |
| ArrayPassedAsScalar | -8 | An array type expression was passed to a scalar type parameter. |
| IncompatibleParameterType | -9 | A real-time sequence contains a parameter of an incompatible type. Assign the value to a variable of the desired type and use that variable in the parameter. |
| NonLValuePassedByReference | -10 | An expression cannot be used in a parameter because the parameter is passed by reference. You can only use variable names or array indexing operations in reference parameters. |
| ReferenceParameterTypeMismatch | -11 | An expression of one type is being passed by reference to a ParameterDeclaration of another type. |
| ScalarPassedAsArray | -12 | An expression with a scalar value is being passed into an array parameter. |
| SequenceFileDoesNotExist | -13 | The real-time sequence references a file that cannot be found. Check the References section for incorrect file paths. |
| WrongNumberOfArguments | -14 | A statement contains the wrong number of arguments. |
| Recursion | -15 | Recursion detected in a sequence call chain. |
| AssignmentToNonLValue | -16 | Attempted to assign to a value that cannot be modified. |
| IndexingScalar | -17 | An array was indexed using scalar indexing. |
| NonIntegerArrayIndex | -18 | An array was indexed using a non-integer value. |
| VariableUndeclared | -19 | A variable was accessed without being declared. |
| VariableRedeclared | -20 | A variable was redeclared. |
| VoidUsedAsValue | -21 | An expression has a void value and cannot be used where a value is expected. |
| AmbiguousCall | -22 | A specified function call is ambiguous. |
| ConditionalExpressionTypeMismatch | -23 | There is a type mismatch in a conditional expression. |
| IncompatibleOperandType | -24 | A statement contains an operand of an incompatible type. |
| InvalidTestExpressionType | -25 | A test expression in a Switch or IfElse statement has an invalid type. The test expression must evaluate to a Boolean value. |
| NoMatchingSignature | -26 | An operation is not defined for operands in an expression. |
| WrongNumberOfOperands | -27 | A statement contains the wrong number of operands. |
| ScalarArrayExpression | -28 | An expression with a scalar value cannot be the ArrayExpression for a ForEachLoop. |
| NonIntegralIterationsExpression | -29 | An Iterations expression does not have an integral (I32 or I64) value. |
| NonScalarCaseValue | -30 | A CaseValue has a non-scalar type. |
| NonScalarSwitchExpression | -31 | A TestExpression has a non-scalar type. |
| MismatchedCaseValueType | -32 | The type of a CaseValue does not match the type of the TestExpression. |
| VoidCaseValue | -33 | A CaseValue is void. |
| VoidSwitchExpression | -34 | A Switch statement has a void TestExpression. |
| InvalidExpression | -35 | An expression is invalid. |
| TopLevelSequenceFileDoesNotExist | -36 | The top-level real-time sequence file does not exist. |
| ReferencePathIsNotAbsolute | -37 | A referenced path is not absolute. |
| ReferencePathHasInvalidCharacters | -38 | A referenced path contains invalid characters. |
| WrongNumberOfParameterMappings | -39 | A real-time sequence contains the wrong number of parameter mappings. Refresh the Parameters list. |
| InvalidChannelMapping | -40 | The channel mapping for a parameter is invalid. Confirm that the specified mapping is a valid path to a channel in the system definition file. |
| VoidReturnUsedInEvaluation | -41 | An Evaluation has a void ReturnDeclaration value, but is being used in a pass/fail evaluation. |
| DuplicateLoggingConfigurationNames | -42 | The stimulus profile contains two or more logging configurations with the same configuration names. Logging configuration names must be unique. |
| InvalidLoggingConfigurationName | -43 | A logging configuration is invalid. |
| MacroFileNotFound | -44 | A macro (.nivsmacro) file was not found. |
| ProjectFileNotFound | -45 | An NI VeriStand project (.nivsproj) file was not found. |
| ConfigurationNotDeployedErrorMessage | -46 | TO DO. |
| DuplicateHeading | -47 | TO DO. |
| EarlyExitException | -48 | TO DO. |
| FTPFailed | -49 | TO DO. |
| InvalidExpectedValueAt | -50 | TO DO. |
| InvalidExpectedValueHeading | -51 | TO DO. |
| InvalidFaultHeading | -52 | TO DO. |
| InvalidFaultStateAt | -53 | TO DO. |
| InvalidFaultValueAt | -54 | TO DO. |
| InvalidFileType | -55 | TO DO. |
| InvalidIdentifier | -56 | TO DO. |
| InvalidStimulusValueAt | -57 | TO DO. |
| InvalidTimestampAt | -58 | TO DO. |
| InvalidURL | -59 | TO DO. |
| MismatchedTokenException | -60 | TO DO. |
| MissingData | -61 | TO DO. |
| MissingTimestamp | -62 | TO DO. |
| MissingTokenException | -63 | TO DO. |
| NoActiveVeriStandProjectErrorMessage | -64 | TO DO. |
| NoChannelData | -65 | TO DO. |
| NoChannelHeading | -66 | TO DO. |
| NoViableAltException | -67 | TO DO. |
| TOKEN_EOF | -68 | TO DO. |
| TOKEN_ID | -69 | TO DO. |
| TOKEN_LPAREN | -70 | TO DO. |
| UndefinedCommandShellCommand | -71 | TO DO. |
| UnsupportedHeadingTag | -72 | TO DO. |
| UnwantedTokenException | -73 | TO DO. |
| InvalidMFilePath | -74 | TO DO. |
| CommandShellWaitOnCompleteHasToBeTrue | -75 | TO DO. |
| CommandShellWaitOnCompleteTimedOut | -76 | TO DO. |
| InvalidCharacters | -77 | TO DO. |
| TOKEN_RPAREN | -78 | TO DO. |
| CommandShellCommandFailed | -79 | TO DO. |
| EmptyFolderOrFilePath | -80 | TO DO. |
| ModelParameterFileParseError | -81 | An error occurred when parsing the file containing model parameters. |
| NegativePreTriggerDuration | -82 | Start logging step has a negative pre-trigger duration. |
| NegativePostTriggerDuration | -83 | Start logging step has a negative post-trigger duration. |
| TimestampSegmentWarning | -84 | Warning when segmented log option is selected, but not timestamping the filename. |
| LocalDeclarationError | -85 | Local Declaration error. |
| InvalidFolderOrFilePath | -86 | Invalid Folder Or FilePath. |
| InvalidChannelReferenceMapping | -87 | Channel reference mapped to an invalid channel. |
| ChannelReferenceTypeMismatch | -88 | The channel reference type does not match the channel type. |
| SequenceFileParseError | -89 | An error occured parsing the real-time sequence file. |
| ImplicitCoercionOfArgument | 2 | An argument was implicitly coerced to another type. |
| ReferencePassedByValue | 3 | A ParameterDeclaration value was passed by reference. |
| EmptyLoggingConfiguration | 4 | A logging configuration does not contain any data to log. |
| WorkspaceToolNotFound | 5 | A Workspace tool was not found. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html language=enus -->
## TOPIC 01108: CompilationEventType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compilationeventtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of a CompilationEvent. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic enum CompilationEventTypeMembersNameValueDescriptionErrorThe event is an error. WarningThe event is a warning. MessageThe event is a message displayed to the user.

### CompilationEventType Enumeration

Specifies the type of a [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public enum CompilationEventType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Error |  | The event is an error. |
| Warning |  | The event is a warning. |
| Message |  | The event is a message displayed to the user. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compilationevents.html language=enus -->
## TOPIC 01109: CompilationEvents

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compilationevents.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compilationevents.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of events that occurred during compilation. These can be errors, warnings, or messages. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic CompilationEvent[] CompilationEvents { get; }ReturnsAn array of CompilationEvent objects.

### CompilationEvents

Gets an array of events that occurred during compilation. These can be errors, warnings, or messages.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html)[] CompilationEvents { get; }

#### Returns

An array of [CompilationEvent](nationalinstruments-veristand-realtimesequencedefinitionapi-compilationevent.html) objects.

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compiler__string-bool-dictionary_string-realtimesequence..html language=enus -->
## TOPIC 01110: Compiler(string, bool, Dictionary< string, RealTimeSequence >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compiler__string-bool-dictionary_string-realtimesequence..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compiler__string-bool-dictionary_string-realtimesequence..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Compiler and compiles the sequence at topLevelSequencePath and its dependencies into a binary form that the real-time sequence virtual machine can execute. This constructor allows you to specify a dictionary of preloaded sequence paths to prevent the compiler from loadi

### Compiler(string, bool, Dictionary< string, RealTimeSequence >)

Initializes a new instance of [Compiler](nationalinstruments-veristand-realtimesequencedefinitionapi-compiler.html) and compiles the sequence at *topLevelSequencePath*  and its dependencies into a binary form that the real-time sequence virtual machine can execute. This constructor allows you to specify a dictionary of preloaded sequence paths to prevent the compiler from loading separate copies of mapped sequences from disk during compilation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Compiler(string topLevelSequencePath, bool debug, Dictionary< string, RealTimeSequence > preloadedSequences)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| topLevelSequencePath | string | The full path to the top-level real-time sequence to compile. |
| debug | bool | true if the compiler should produce additional data for use during debugging. |
| preloadedSequences | Dictionary< string, RealTimeSequence > | A dictionary mapping full paths to in-memory RealTimeSequence objects for the compiler to use. Specifying preloaded sequences prevents the compiler from loading separate copies of the mapped sequences from disk. |

#### Exceptions

| Type | Description |
| --- | --- |
| StimulusProfileCompilationException | An error or multiple errors prevented compilation of the top-level real-time sequence. |

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compiler__string-bool.html language=enus -->
## TOPIC 01111: Compiler(string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compiler__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-compiler__string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Compiler and compiles and compiles the sequence at topLevelSequencePath and its dependencies into a binary form that the real-time sequence virtual machine can execute. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Compiler(string to

### Compiler(string, bool)

Initializes a new instance of [Compiler](nationalinstruments-veristand-realtimesequencedefinitionapi-compiler.html) and compiles and compiles the sequence at *topLevelSequencePath*  and its dependencies into a binary form that the real-time sequence virtual machine can execute.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Compiler(string topLevelSequencePath, bool debug)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| topLevelSequencePath | string | The full path to the top-level real-time sequence to compile. |
| debug | bool | true if the compiler should produce additional data for use during debugging. |

#### Exceptions

| Type | Description |
| --- | --- |
| StimulusProfileCompilationException | An error or multiple errors prevented compilation of the top-level real-time sequence. |

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-containsfaulting.html language=enus -->
## TOPIC 01112: ContainsFaulting

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-containsfaulting.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-containsfaulting.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the compiled instance contains faulting instructions. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool ContainsFaulting { get; }Returnstrue if the compiled instance contains faulting instructions.

### ContainsFaulting

Gets whether the compiled instance contains faulting instructions.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool ContainsFaulting { get; }

#### Returns

true if the compiled instance contains faulting instructions.

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-findvariable__string-string-out.html language=enus -->
## TOPIC 01113: FindVariable(string, string, out long)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-findvariable__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-findvariable__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Finds the variable ID for a variable in the real-time sequence file at filePath with the specified variableName . You can use the variable ID to look up the current value of the variable. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void FindVariable(string file

### FindVariable(string, string, out long)

Finds the variable ID for a variable in the real-time sequence file at *filePath*  with the specified *variableName* . You can use the variable ID to look up the current value of the variable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void FindVariable(string filePath, string variableName, out long variableId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path to the sequence file that contains the variable. |
| variableName | string | The name of the variable to get the ID for. |
| variableId | out long | Upon return, contains the variable ID for variableName . |

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-getrealtimesequence__string.html language=enus -->
## TOPIC 01114: GetRealTimeSequence(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-getrealtimesequence__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-getrealtimesequence__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic RealTimeSequence GetRealTimeSequence(string sequencePath)ParametersNameTypeDescriptionsequencePathstringThe name of the real-time sequence to returnReturnsThe real-time sequence whose name

### GetRealTimeSequence(string)

Gets the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html) GetRealTimeSequence(string sequencePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sequencePath | string | The name of the real-time sequence to return |

#### Returns

The real-time sequence whose name is passed as a parameter, or null if the sequence wasn't found.

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-gettoplevelrealtimesequence.html language=enus -->
## TOPIC 01115: GetTopLevelRealTimeSequence()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-gettoplevelrealtimesequence.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-gettoplevelrealtimesequence.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the top-level real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic RealTimeSequence GetTopLevelRealTimeSequence()ReturnsThe top level real-time sequence, or null if the sequence wasn't found.

### GetTopLevelRealTimeSequence()

Gets the top-level real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [RealTimeSequence](nationalinstruments-veristand-realtimesequencedefinitionapi-realtimesequence.html) GetTopLevelRealTimeSequence()

#### Returns

The top level real-time sequence, or null if the sequence wasn't found.

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-isdebuggable.html language=enus -->
## TOPIC 01116: IsDebuggable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-isdebuggable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-isdebuggable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the compiled instance was built with information necessary for debugging. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool IsDebuggable { get; }Returnstrue if the compiled instance is debuggable.

### IsDebuggable

Gets whether the compiled instance was built with information necessary for debugging.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool IsDebuggable { get; }

#### Returns

true if the compiled instance is debuggable.

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-tostring.html language=enus -->
## TOPIC 01117: ToString()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-tostring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler-tostring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the current object. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override string ToString()RemarksOverrides object.ToString. ReturnsThe string representation of the current object.

### ToString()

Returns a string representation of the current object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override string ToString()

#### Remarks

Overrides object.ToString.

#### Returns

The string representation of the current object.

Parent topic:

Compiler Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-compiler.html language=enus -->
## TOPIC 01118: Compiler Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-compiler.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-compiler.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the compiler for real-time sequence files. All open and referenced real-time sequence files are compiled automatically when you run a stimulus profile. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class CompilerRemarksUse the members o

### Compiler Class

Represents the compiler for real-time sequence files. All open and referenced real-time sequence files are compiled automatically when you run a stimulus profile.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Compiler

#### Remarks

Use the members of this class to get information about sequence compilation, such as the instance that was compiled, whether the compiled instance is debuggable, and so on.

**Accessing this Class:**

- Compiler Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Compiler(string, bool, Dictionary< string, RealTimeSequence >) | Initializes a new instance of Compiler and compiles the sequence at topLevelSequencePath and its dependencies into a binary form that the real-time sequence virtual machine can execute. This constructor allows you to specify a dictionary of preloaded sequence paths to prevent the compiler from loading separate copies of mapped sequences from disk during compilation. |
| Compiler(string, bool) | Initializes a new instance of Compiler and compiles and compiles the sequence at topLevelSequencePath and its dependencies into a binary form that the real-time sequence virtual machine can execute. |

#### Properties

| Name | Description |
| --- | --- |
| CompilationEvents | Gets an array of events that occurred during compilation. These can be errors, warnings, or messages. |
| ContainsFaulting | Gets whether the compiled instance contains faulting instructions. |
| IsDebuggable | Gets whether the compiled instance was built with information necessary for debugging. |

#### Methods

| Name | Description |
| --- | --- |
| FindVariable(string, string, out long) | Finds the variable ID for a variable in the real-time sequence file at filePath with the specified variableName . You can use the variable ID to look up the current value of the variable. |
| GetRealTimeSequence(string) | Gets the real-time sequence. |
| GetTopLevelRealTimeSequence() | Gets the top-level real-time sequence. |
| ToString() | Returns a string representation of the current object. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase-defaultcase.html language=enus -->
## TOPIC 01119: DefaultCase()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase-defaultcase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase-defaultcase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DefaultCase. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DefaultCase()

### DefaultCase()

Initializes a new instance of [DefaultCase](nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public DefaultCase()

Parent topic:

DefaultCase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase-defaultcase__defaultcase.html language=enus -->
## TOPIC 01120: DefaultCase(DefaultCase)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase-defaultcase__defaultcase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase-defaultcase__defaultcase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DefaultCase by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DefaultCase(DefaultCase node)ParametersNameTypeDescriptionnodeDefaultCaseThe instance of DefaultCase to copy.

### DefaultCase(DefaultCase)

Initializes a new instance of [DefaultCase](nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public DefaultCase(DefaultCase node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | DefaultCase | The instance of DefaultCase to copy. |

Parent topic:

DefaultCase Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html language=enus -->
## TOPIC 01121: DefaultCase Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-defaultcase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the default case in a Switch statement, which executes if none of the conditions for executing a CaseStatement under the Cases section are met. Derives fromCodeSectionSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class DefaultCase : CodeSectionRemarksU

### DefaultCase Class

Represents the default case in a [Switch](nationalinstruments-veristand-realtimesequencedefinitionapi-switch.html) statement, which executes if none of the conditions for executing a [CaseStatement](nationalinstruments-veristand-realtimesequencedefinitionapi-casestatement.html) under the [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) section are met.

#### Derives from

- CodeSection

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class DefaultCase : CodeSection

#### Remarks

Use the members of this class to configure the default case.

**Accessing this Class:**

- [Default](nationalinstruments-veristand-realtimesequencedefinitionapi-switch-default.html)
- DefaultCase Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DefaultCase(DefaultCase) | Initializes a new instance of DefaultCase by copying an existing instance. |
| DefaultCase() | Initializes a new instance of DefaultCase. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute-directorypath.html language=enus -->
## TOPIC 01122: DirectoryPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute-directorypath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute-directorypath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the directory path. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string DirectoryPath { get; }ReturnsThe directory path, as a string.

### DirectoryPath

Gets the directory path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string DirectoryPath { get; }

#### Returns

The directory path, as a string.

Parent topic:

DirectoryPathAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute-directorypathattribute__string.html language=enus -->
## TOPIC 01123: DirectoryPathAttribute(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute-directorypathattribute__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute-directorypathattribute__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DirectoryPathAttribute class for the specified directoryPath string. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DirectoryPathAttribute(string directoryPath)ParametersNameTypeDescriptiondirectoryPathstringThe path to the direct

### DirectoryPathAttribute(string)

Initializes a new instance of the [DirectoryPathAttribute](nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute.html) class for the specified *directoryPath*  string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public DirectoryPathAttribute(string directoryPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| directoryPath | string | The path to the directory. |

Parent topic:

DirectoryPathAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute.html language=enus -->
## TOPIC 01124: DirectoryPathAttribute Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-directorypathattribute.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an attribute that indicates that a string is a directory path. Derives fromAttributeSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class DirectoryPathAttribute : AttributeRemarksInherits from System.Attribute. Thread SafetyAny members of this type are n

### DirectoryPathAttribute Class

Represents an attribute that indicates that a string is a directory path.

#### Derives from

- Attribute

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class DirectoryPathAttribute : Attribute

#### Remarks

Inherits from System.Attribute.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DirectoryPathAttribute(string) | Initializes a new instance of the DirectoryPathAttribute class for the specified directoryPath string. |

#### Properties

| Name | Description |
| --- | --- |
| DirectoryPath | Gets the directory path. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop.html language=enus -->
## TOPIC 01125: DoWhileLoop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DoWhileLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DoWhileLoop()RemarksThis constructor sets LoopTest to an expression that evaluates to false.

### DoWhileLoop()

Initializes a new instance of [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public DoWhileLoop()

#### Remarks

This constructor sets [LoopTest](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-looptest.html) to an expression that evaluates to false.

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__dowhileloop.html language=enus -->
## TOPIC 01126: DoWhileLoop(DoWhileLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__dowhileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__dowhileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DoWhileLoop by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DoWhileLoop(DoWhileLoop node)ParametersNameTypeDescriptionnodeDoWhileLoopThe instance of DoWhileLoop to copy.

### DoWhileLoop(DoWhileLoop)

Initializes a new instance of [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public DoWhileLoop(DoWhileLoop node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | DoWhileLoop | The instance of DoWhileLoop to copy. |

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__expression-bool-block.html language=enus -->
## TOPIC 01127: DoWhileLoop(Expression, bool, Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__expression-bool-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__expression-bool-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DoWhileLoop that contains the set of statements specified by body and that evaluates the specified loopTest expression to determine when to stop execution. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DoWhileLoop(Expression loopTest

### DoWhileLoop(Expression, bool, Block)

Initializes a new instance of [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html) that contains the set of statements specified by *body*  and that evaluates the specified *loopTest*  expression to determine when to stop execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public DoWhileLoop(Expression loopTest, bool autoYield, Block body)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopTest | Expression | The Expression to evaluate to determine whether the loop should stop executing. The loop terminates when this expression is false. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| body | Block | The set of statements that execute in the loop. |

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__expression-bool.html language=enus -->
## TOPIC 01128: DoWhileLoop(Expression, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__expression-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-dowhileloop__expression-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of DoWhileLoop that evaluates the specified loopTest expression to determine when to stop execution. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic DoWhileLoop(Expression loopTest, bool autoYield)ParametersNameTypeDescriptionloopTestExpr

### DoWhileLoop(Expression, bool)

Initializes a new instance of [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html) that evaluates the specified *loopTest*  expression to determine when to stop execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public DoWhileLoop(Expression loopTest, bool autoYield)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopTest | Expression | The Expression to evaluate to determine whether the loop should stop executing. The loop terminates when this expression is false. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-equals__dowhileloop.html language=enus -->
## TOPIC 01129: Equals(DoWhileLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-equals__dowhileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-equals__dowhileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of DoWhileLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(DoWhileLoop other)ParametersNameTypeDescriptionotherDoWhileLoopThe DoWhileLoop object to compare with the curr

### Equals(DoWhileLoop)

Determines whether the specified *other*  object is equal to the current instance of [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(DoWhileLoop other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | DoWhileLoop | The DoWhileLoop object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-equals__statement.html language=enus -->
## TOPIC 01130: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of DoWhileLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe DoWhileLoop type inherits from Statement. ParametersNameTypeDescriptionoth

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html). Otherwise, false.

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-gethashcode.html language=enus -->
## TOPIC 01131: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a DoWhileLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHash

### GetHashCode()

Serves as a hash function for a [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [DoWhileLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html) object.

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-looptest.html language=enus -->
## TOPIC 01132: LoopTest

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-looptest.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop-looptest.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Expression that is evaluated to determine whether the loop should stop executing. The loop terminates when this expression is false. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression LoopTest { get; set; }ReturnsAn Expression object.

### LoopTest

Gets or sets the [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) that is evaluated to determine whether the loop should stop executing. The loop terminates when this expression is false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) LoopTest { get; set; }

#### Returns

An [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) object.

Parent topic:

DoWhileLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html language=enus -->
## TOPIC 01133: DoWhileLoop Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-dowhileloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DoWhile Loop primitive, which executes its body of statements at least once and continues executing until a specified condition is false. Derives fromAbstractLoopIEquatable< DoWhileLoop >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class DoWhileLoop

### DoWhileLoop Class

Represents a **DoWhile Loop** primitive, which executes its body of statements at least once and continues executing until a specified condition is false.

#### Derives from

- AbstractLoop
- IEquatable< DoWhileLoop >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class DoWhileLoop : AbstractLoop, IEquatable< DoWhileLoop >

#### Remarks

Use the members of this class to configure the loop, including the condition to use to stop execution.

**Accessing this Class:**

- DoWhileLoop Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| DoWhileLoop(Expression, bool) | Initializes a new instance of DoWhileLoop that evaluates the specified loopTest expression to determine when to stop execution. |
| DoWhileLoop(Expression, bool, Block) | Initializes a new instance of DoWhileLoop that contains the set of statements specified by body and that evaluates the specified loopTest expression to determine when to stop execution. |
| DoWhileLoop() | Initializes a new instance of DoWhileLoop. |
| DoWhileLoop(DoWhileLoop) | Initializes a new instance of DoWhileLoop by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| LoopTest | Gets or sets the Expression that is evaluated to determine whether the loop should stop executing. The loop terminates when this expression is false. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of DoWhileLoop. |
| Equals(DoWhileLoop) | Determines whether the specified other object is equal to the current instance of DoWhileLoop. |
| GetHashCode() | Serves as a hash function for a DoWhileLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-erroraction.html language=enus -->
## TOPIC 01134: ErrorAction Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-erroraction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-erroraction.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies what action to take after generating an error. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic enum ErrorActionMembersNameValueDescriptionContinueSequenceExecutionSpecifies to continue executing the sequence. StopSequenceSpecifies to stop the sequence. Ab

### ErrorAction Enumeration

Specifies what action to take after generating an error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public enum ErrorAction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ContinueSequenceExecution |  | Specifies to continue executing the sequence. |
| StopSequence |  | Specifies to stop the sequence. |
| AbortSequence |  | Specifies to abort the sequence. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-evaluationmethod.html language=enus -->
## TOPIC 01135: EvaluationMethod Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-evaluationmethod.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-evaluationmethod.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the value of a ParameterDeclaration is passed in to the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic enum EvaluationMethodMembersNameValueDescriptionByValueThe parameter value is passed in by value from the calling sequence, mea

### EvaluationMethod Enumeration

Specifies how the value of a [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) is passed in to the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public enum EvaluationMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ByValue |  | The parameter value is passed in by value from the calling sequence, meaning a copy of the parameter value is read. |
| ByReference |  | The parameter value is passed in by reference from the calling sequence, meaning it is read directly. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-equals__expression.html language=enus -->
## TOPIC 01136: Equals(Expression)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-equals__expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-equals__expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Expression. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Expression other)ParametersNameTypeDescriptionotherExpressionThe Expression object to compare with the current

### Equals(Expression)

Determines whether the specified *other*  object is equal to the current instance of [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Expression other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Expression | The Expression object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-equals__statement.html language=enus -->
## TOPIC 01137: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Expression. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe Expression type inherits from Statement. ParametersNameTypeDescriptionother

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Expression object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html). Otherwise, false.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression.html language=enus -->
## TOPIC 01138: Expression()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Expression. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression()RemarksThis constructor sets ExpressionString to string.Empty.

### Expression()

Initializes a new instance of [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Expression()

#### Remarks

This constructor sets [ExpressionString](nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expressionstring.html) to string.Empty.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__expression.html language=enus -->
## TOPIC 01139: Expression(Expression)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Expression by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression(Expression node)ParametersNameTypeDescriptionnodeExpressionThe instance of Expression to copy.

### Expression(Expression)

Initializes a new instance of [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Expression(Expression node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Expression | The instance of Expression to copy. |

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__string-out-out.html language=enus -->
## TOPIC 01140: Expression(string, out bool, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__string-out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Expression that executes the specified expressionString . This constructor also indicates whether the expression uses valid syntax and, if not, returns any formatted parse errors. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Express

### Expression(string, out bool, out string)

Initializes a new instance of [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) that executes the specified *expressionString* . This constructor also indicates whether the expression uses valid syntax and, if not, returns any formatted parse errors.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Expression(string expressionString, out bool validExpression, out string parseErrors)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expressionString | string | The functional expression to execute. |
| validExpression | out bool | true if the expression uses valid syntax. |
| parseErrors | out string | Upon return, contains any formatted parse errors from the expressionString . |

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__string.html language=enus -->
## TOPIC 01141: Expression(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expression__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Expression that executes the specified expressionString . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression(string expressionString)ParametersNameTypeDescriptionexpressionStringstringThe functional expression to execute.

### Expression(string)

Initializes a new instance of [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) that executes the specified *expressionString* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Expression(string expressionString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expressionString | string | The functional expression to execute. |

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expressionstring.html language=enus -->
## TOPIC 01142: ExpressionString

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expressionstring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-expressionstring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the functional expression that the expression executes, as a string. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string ExpressionString { get; set; }ReturnsThe functional expression, as a string.

### ExpressionString

Gets or sets the functional expression that the expression executes, as a string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string ExpressionString { get; set; }

#### Returns

The functional expression, as a string.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-gethashcode.html language=enus -->
## TOPIC 01143: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Expression object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashC

### GetHashCode()

Serves as a hash function for a [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) object.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-identifier.html language=enus -->
## TOPIC 01144: Identifier

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-identifier.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-identifier.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the identifier, if the expression evaluates to an identifier value. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Identifier { get; }ReturnsThe identifier value.

### Identifier

Gets the identifier, if the expression evaluates to an identifier value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Identifier { get; }

#### Returns

The identifier value.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-isvalid.html language=enus -->
## TOPIC 01145: IsValid

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-isvalid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-isvalid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the expression uses valid syntax. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool IsValid { get; }RemarksThis property only performs a syntax check. It does not perform more advanced checks such as whether variables are mapped to channels correctl

### IsValid

Gets whether the expression uses valid syntax.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool IsValid { get; }

#### Remarks

This property only performs a syntax check. It does not perform more advanced checks such as whether variables are mapped to channels correctly.

#### Returns

true if the expression is valid.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-operands.html language=enus -->
## TOPIC 01146: Operands

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-operands.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-operands.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sub-expressions in the parse tree of the top-level expression. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression[] Operands { get; }ReturnsThe array of sub-expressions.

### Operands

Gets the sub-expressions in the parse tree of the top-level expression.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html)[] Operands { get; }

#### Returns

The array of sub-expressions.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-parseerrors.html language=enus -->
## TOPIC 01147: ParseErrors

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-parseerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-parseerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets any formatted parse errors for the expression if IsValid is false. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string ParseErrors { get; }ReturnsThe error information.

### ParseErrors

Gets any formatted parse errors for the expression if [IsValid](nationalinstruments-veristand-realtimesequencedefinitionapi-expression-isvalid.html) is false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string ParseErrors { get; }

#### Returns

The error information.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-setstring__string.html language=enus -->
## TOPIC 01148: SetString(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-setstring__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-setstring__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the functional expression string that the current expression evaluates. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void SetString(string expression)ParametersNameTypeDescriptionexpressionstringThe functional expression to evaluate. For example, y = x + 10

### SetString(string)

Sets the functional expression string that the current expression evaluates.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void SetString(string expression)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| expression | string | The functional expression to evaluate. For example, y = x + 100. |

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression-tostring.html language=enus -->
## TOPIC 01149: ToString()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression-tostring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression-tostring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the current object. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override string ToString()RemarksOverrides object.ToString. ReturnsThe string representation of the current object.

### ToString()

Returns a string representation of the current object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override string ToString()

#### Remarks

Overrides object.ToString.

#### Returns

The string representation of the current object.

Parent topic:

Expression Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html language=enus -->
## TOPIC 01150: Expression Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a formula-type expression that operates on constant and/or variable values. Expressions can call built-in functions, such as sin(x) and cos(x), and real-time sequences that you add to the current sequence as References. Derives fromStatementIEquatable< Expression >SyntaxNamespace: Nationa

### Expression Class

Represents a formula-type expression that operates on constant and/or variable values. Expressions can call built-in functions, such as sin(*x*) and cos(*x*), and real-time sequences that you add to the current sequence as [References](nationalinstruments-veristand-realtimesequencedefinitionapi-references.html).

#### Derives from

- Statement
- IEquatable< Expression >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Expression : Statement, IEquatable< Expression >

#### Remarks

Note

Refer to the *Editing Expressions* section of the *NI VeriStand Help* for detailed information about expression syntax, functions, and allowed operators.

**Accessing this Class:**

- Expression Constructor

CaseValue

LoopTest

ArrayExpression

Iterations

TestExpression

TestExpression

LoopTest

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Expression() | Initializes a new instance of Expression. |
| Expression(string) | Initializes a new instance of Expression that executes the specified expressionString . |
| Expression(Expression) | Initializes a new instance of Expression by copying an existing instance. |
| Expression(string, out bool, out string) | Initializes a new instance of Expression that executes the specified expressionString . This constructor also indicates whether the expression uses valid syntax and, if not, returns any formatted parse errors. |

#### Properties

| Name | Description |
| --- | --- |
| ExpressionString | Gets or sets the functional expression that the expression executes, as a string. |
| Identifier | Gets the identifier, if the expression evaluates to an identifier value. |
| IsValid | Gets whether the expression uses valid syntax. |
| Operands | Gets the sub-expressions in the parse tree of the top-level expression. |
| ParseErrors | Gets any formatted parse errors for the expression if IsValid is false. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Expression) | Determines whether the specified other object is equal to the current instance of Expression. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of Expression. |
| GetHashCode() | Serves as a hash function for a Expression object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |
| SetString(string) | Sets the functional expression string that the current expression evaluates. |
| ToString() | Returns a string representation of the current object. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-arrayexpression.html language=enus -->
## TOPIC 01151: ArrayExpression

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-arrayexpression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-arrayexpression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the array of values that the loop iterates over. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression ArrayExpression { get; set; }ReturnsThe array of values, as an Expression.

### ArrayExpression

Gets or sets the array of values that the loop iterates over.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) ArrayExpression { get; set; }

#### Returns

The array of values, as an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-equals__foreachloop.html language=enus -->
## TOPIC 01152: Equals(ForEachLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-equals__foreachloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-equals__foreachloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of ForEachLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(ForEachLoop other)ParametersNameTypeDescriptionotherForEachLoopThe ForEachLoop object to compare with the curr

### Equals(ForEachLoop)

Determines whether the specified *other*  object is equal to the current instance of [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(ForEachLoop other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ForEachLoop | The ForEachLoop object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-equals__statement.html language=enus -->
## TOPIC 01153: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of ForEachLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe ForEachLoop type inherits from Statement. ParametersNameTypeDescriptionoth

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html). Otherwise, false.

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop.html language=enus -->
## TOPIC 01154: ForEachLoop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForEachLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForEachLoop()RemarksThis constructor sets LoopVariable to "i", AutoYield to true, and ArrayExpression to an Expression with a value of "ArrayName".

### ForEachLoop()

Initializes a new instance of [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForEachLoop()

#### Remarks

This constructor sets [LoopVariable](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-loopvariable.html) to "i", [AutoYield](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-autoyield.html) to true, and [ArrayExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-arrayexpression.html) to an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) with a value of "ArrayName".

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__foreachloop.html language=enus -->
## TOPIC 01155: ForEachLoop(ForEachLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__foreachloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__foreachloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForEachLoop by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForEachLoop(ForEachLoop node)ParametersNameTypeDescriptionnodeForEachLoopThe instance of ForEachLoop to copy.

### ForEachLoop(ForEachLoop)

Initializes a new instance of [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForEachLoop(ForEachLoop node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ForEachLoop | The instance of ForEachLoop to copy. |

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__string-expression-bool-block.html language=enus -->
## TOPIC 01156: ForEachLoop(string, Expression, bool, Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__string-expression-bool-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__string-expression-bool-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForEachLoop that iterates over the array specified by arrayExpression and executes the specified body of code on each iteration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForEachLoop(string loopVariable, Expression arrayExpressio

### ForEachLoop(string, Expression, bool, Block)

Initializes a new instance of [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html) that iterates over the array specified by *arrayExpression*  and executes the specified *body*  of code on each iteration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForEachLoop(string loopVariable, Expression arrayExpression, bool autoYield, Block body)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopVariable | string | The identifier for the variable that holds the current value of the array element. For example, i. |
| arrayExpression | Expression | The array of values that the loop iterates over. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| body | Block | The sequence code to execute on each iteration of the loop. |

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__string-expression-bool.html language=enus -->
## TOPIC 01157: ForEachLoop(string, Expression, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__string-expression-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-foreachloop__string-expression-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForEachLoop that iterates over the array specified by arrayExpression . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForEachLoop(string loopVariable, Expression arrayExpression, bool autoYield)ParametersNameTypeDescriptionloopVariab

### ForEachLoop(string, Expression, bool)

Initializes a new instance of [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html) that iterates over the array specified by *arrayExpression* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForEachLoop(string loopVariable, Expression arrayExpression, bool autoYield)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopVariable | string | The identifier for the variable that holds the current value of the array element. For example, i. |
| arrayExpression | Expression | The array of values that the loop iterates over. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-gethashcode.html language=enus -->
## TOPIC 01158: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a ForEachLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHash

### GetHashCode()

Serves as a hash function for a [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [ForEachLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html) object.

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-loopvariable.html language=enus -->
## TOPIC 01159: LoopVariable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-loopvariable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop-loopvariable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the identifier for the variable that holds the current value of the array element. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string LoopVariable { get; set; }ReturnsThe identifier for the variable. For example, i.

### LoopVariable

Gets or sets the identifier for the variable that holds the current value of the array element.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string LoopVariable { get; set; }

#### Returns

The identifier for the variable. For example, *i*.

Parent topic:

ForEachLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html language=enus -->
## TOPIC 01160: ForEachLoop Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-foreachloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a ForEach Loop, which iterates over an array of values and executes its body of statements once per array element. Derives fromAbstractLoopIEquatable< ForEachLoop >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class ForEachLoop : AbstractLoop, IEquatab

### ForEachLoop Class

Represents a **ForEach Loop**, which iterates over an array of values and executes its body of statements once per array element.

#### Derives from

- AbstractLoop
- IEquatable< ForEachLoop >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class ForEachLoop : AbstractLoop, IEquatable< ForEachLoop >

#### Remarks

Use the members of this class to configure the loop and the array of values it iterates over.

**Accessing this Class:**

- ForEachLoop Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ForEachLoop() | Initializes a new instance of ForEachLoop. |
| ForEachLoop(string, Expression, bool, Block) | Initializes a new instance of ForEachLoop that iterates over the array specified by arrayExpression and executes the specified body of code on each iteration. |
| ForEachLoop(ForEachLoop) | Initializes a new instance of ForEachLoop by copying an existing instance. |
| ForEachLoop(string, Expression, bool) | Initializes a new instance of ForEachLoop that iterates over the array specified by arrayExpression . |

#### Properties

| Name | Description |
| --- | --- |
| ArrayExpression | Gets or sets the array of values that the loop iterates over. |
| LoopVariable | Gets or sets the identifier for the variable that holds the current value of the array element. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(ForEachLoop) | Determines whether the specified other object is equal to the current instance of ForEachLoop. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of ForEachLoop. |
| GetHashCode() | Serves as a hash function for a ForEachLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-equals__forloop.html language=enus -->
## TOPIC 01161: Equals(ForLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-equals__forloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-equals__forloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of ForLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(ForLoop other)ParametersNameTypeDescriptionotherForLoopThe ForLoop object to compare with the current instance.Ret

### Equals(ForLoop)

Determines whether the specified *other*  object is equal to the current instance of [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(ForLoop other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ForLoop | The ForLoop object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-equals__statement.html language=enus -->
## TOPIC 01162: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of ForLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe ForLoop type inherits from Statement. ParametersNameTypeDescriptionotherStatem

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html). Otherwise, false.

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop.html language=enus -->
## TOPIC 01163: ForLoop()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForLoop()RemarksThis constructor sets LoopVariable to "i", Iterations to 10, and AutoYield to true.

### ForLoop()

Initializes a new instance of [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForLoop()

#### Remarks

This constructor sets [LoopVariable](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-loopvariable.html) to "i", [Iterations](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-iterations.html) to 10, and [AutoYield](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractloop-autoyield.html) to true.

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__forloop.html language=enus -->
## TOPIC 01164: ForLoop(ForLoop)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__forloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__forloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForLoop by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForLoop(ForLoop node)ParametersNameTypeDescriptionnodeForLoopThe instance of ForLoop to copy.

### ForLoop(ForLoop)

Initializes a new instance of [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForLoop(ForLoop node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ForLoop | The instance of ForLoop to copy. |

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__string-expression-bool-block.html language=enus -->
## TOPIC 01165: ForLoop(string, Expression, bool, Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__string-expression-bool-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__string-expression-bool-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForLoop that runs for the specified number of iterations and executes the specified body of code on each iteration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForLoop(string loopVariable, Expression iterations, bool autoYield, Blo

### ForLoop(string, Expression, bool, Block)

Initializes a new instance of [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html) that runs for the specified number of *iterations*  and executes the specified *body*  of code on each iteration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForLoop(string loopVariable, Expression iterations, bool autoYield, Block body)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopVariable | string | The identifier for the variable that holds the current iteration count for the ForLoop. |
| iterations | Expression | The number of iterations to execute. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |
| body | Block | The sequence code to execute on each iteration of the loop. |

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__string-expression-bool.html language=enus -->
## TOPIC 01166: ForLoop(string, Expression, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__string-expression-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-forloop__string-expression-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ForLoop that runs for the specified number of iterations . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ForLoop(string loopVariable, Expression iterations, bool autoYield)ParametersNameTypeDescriptionloopVariablestringThe identifier

### ForLoop(string, Expression, bool)

Initializes a new instance of [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html) that runs for the specified number of *iterations* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ForLoop(string loopVariable, Expression iterations, bool autoYield)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| loopVariable | string | The identifier for the variable that holds the current iteration count for the ForLoop. |
| iterations | Expression | The number of iterations to execute. |
| autoYield | bool | If true, specifies that the loop automatically yields control of the CPU to the next task at the end of each iteration. |

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-gethashcode.html language=enus -->
## TOPIC 01167: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a ForLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCode

### GetHashCode()

Serves as a hash function for a [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html) object.

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-iterations.html language=enus -->
## TOPIC 01168: Iterations

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-iterations.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-iterations.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the expression that represents the number of iterations the loop executes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression Iterations { get; set; }ReturnsThe total number of iterations, as an Expression.

### Iterations

Gets or sets the expression that represents the number of iterations the loop executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) Iterations { get; set; }

#### Returns

The total number of iterations, as an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-loopvariable.html language=enus -->
## TOPIC 01169: LoopVariable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-loopvariable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop-loopvariable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the identifier for the variable that holds the current iteration count for the ForLoop. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string LoopVariable { get; set; }ReturnsThe identifier for the variable. For example, i.

### LoopVariable

Gets or sets the identifier for the variable that holds the current iteration count for the [ForLoop](nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string LoopVariable { get; set; }

#### Returns

The identifier for the variable. For example, *i*.

Parent topic:

ForLoop Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html language=enus -->
## TOPIC 01170: ForLoop Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-forloop.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a For Loop, which executes its body of statements for a fixed number of iterations. Derives fromAbstractLoopIEquatable< ForLoop >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class ForLoop : AbstractLoop, IEquatable< ForLoop >RemarksUse the members of

### ForLoop Class

Represents a **For Loop**, which executes its body of statements for a fixed number of iterations.

#### Derives from

- AbstractLoop
- IEquatable< ForLoop >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class ForLoop : AbstractLoop, IEquatable< ForLoop >

#### Remarks

Use the members of this class to configure the loop, including the number of iterations it executes.

**Accessing this Class:**

- ForLoop Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ForLoop() | Initializes a new instance of ForLoop. |
| ForLoop(string, Expression, bool, Block) | Initializes a new instance of ForLoop that runs for the specified number of iterations and executes the specified body of code on each iteration. |
| ForLoop(ForLoop) | Initializes a new instance of ForLoop by copying an existing instance. |
| ForLoop(string, Expression, bool) | Initializes a new instance of ForLoop that runs for the specified number of iterations . |

#### Properties

| Name | Description |
| --- | --- |
| Iterations | Gets or sets the expression that represents the number of iterations the loop executes. |
| LoopVariable | Gets or sets the identifier for the variable that holds the current iteration count for the ForLoop. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(ForLoop) | Determines whether the specified other object is equal to the current instance of ForLoop. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of ForLoop. |
| GetHashCode() | Serves as a hash function for a ForLoop object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-action.html language=enus -->
## TOPIC 01171: Action

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-action.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-action.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the action to take after generating the error. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ErrorAction Action { get; set; }

### Action

Gets or sets a value indicating the action to take after generating the error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [ErrorAction](nationalinstruments-veristand-realtimesequencedefinitionapi-erroraction.html) Action { get; set; }

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-code.html language=enus -->
## TOPIC 01172: Code

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-code.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-code.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the error code for the error to generate. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic int Code { get; set; }

### Code

Gets or sets a value indicating the error code for the error to generate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public int Code { get; set; }

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-equals__object.html language=enus -->
## TOPIC 01173: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines equality. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectThe object to compare.ReturnsReturns whether the two objects are equal.

### Equals(object)

Determines equality.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare. |

#### Returns

Returns whether the two objects are equal.

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-equals__statement.html language=enus -->
## TOPIC 01174: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines equality. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)ParametersNameTypeDescriptionotherStatementThe statement to compare.ReturnsReturns whether the two objects are equal.

### Equals(Statement)

Determines equality.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The statement to compare. |

#### Returns

Returns whether the two objects are equal.

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror.html language=enus -->
## TOPIC 01175: GenerateError()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the GenerateError class using default data. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic GenerateError()

### GenerateError()

Initializes a new instance of the GenerateError class using default data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public GenerateError()

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror__generateerror.html language=enus -->
## TOPIC 01176: GenerateError(GenerateError)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror__generateerror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror__generateerror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the GenerateError class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic GenerateError(GenerateError node)ParametersNameTypeDescriptionnodeGenerateErrorThe existing instance to copy.

### GenerateError(GenerateError)

Initializes a new instance of the GenerateError class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public GenerateError(GenerateError node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | GenerateError | The existing instance to copy. |

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror__int-string-erroraction.html language=enus -->
## TOPIC 01177: GenerateError(int, string, ErrorAction)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror__int-string-erroraction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-generateerror__int-string-erroraction.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the GenerateError class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic GenerateError(int code, string message, ErrorAction action)ParametersNameTypeDescriptioncodeintSpecifies the error code for the error to generate.messagestringSpe

### GenerateError(int, string, ErrorAction)

Initializes a new instance of the GenerateError class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public GenerateError(int code, string message, ErrorAction action)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| code | int | Specifies the error code for the error to generate. |
| message | string | Specifies the message for the error to generate. |
| action | ErrorAction | Specifies the action to take after generating the error. |

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-gethashcode.html language=enus -->
## TOPIC 01178: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a hash code. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()ReturnsReturns a hash code.

### GetHashCode()

Gets a hash code.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Returns

Returns a hash code.

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-message.html language=enus -->
## TOPIC 01179: Message

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-message.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror-message.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating the error message for the error to generate. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic string Message { get; set; }

### Message

Gets or sets a value indicating the error message for the error to generate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public string Message { get; set; }

Parent topic:

GenerateError Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror.html language=enus -->
## TOPIC 01180: GenerateError Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-generateerror.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a statement that generates a user-specified error. Derives fromStatementSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class GenerateError : StatementConstructorsNameDescriptionGenerateError(GenerateError)Initializes a new instance of the GenerateError

### GenerateError Class

Represents a statement that generates a user-specified error.

#### Derives from

- Statement

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class GenerateError : Statement

#### Constructors

| Name | Description |
| --- | --- |
| GenerateError(GenerateError) | Initializes a new instance of the GenerateError class by copying an existing instance. |
| GenerateError(int, string, ErrorAction) | Initializes a new instance of the GenerateError class. |
| GenerateError() | Initializes a new instance of the GenerateError class using default data. |

#### Properties

| Name | Description |
| --- | --- |
| Action | Gets or sets a value indicating the action to take after generating the error. |
| Code | Gets or sets a value indicating the error code for the error to generate. |
| Message | Gets or sets a value indicating the error message for the error to generate. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(Statement) | Determines equality. |
| Equals(object) | Determines equality. |
| GetHashCode() | Gets a hash code. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-equals__ifelse.html language=enus -->
## TOPIC 01181: Equals(IfElse)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-equals__ifelse.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-equals__ifelse.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of IfElse. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(IfElse other)ParametersNameTypeDescriptionotherIfElseThe IfElse object to compare with the current instance.Returns

### Equals(IfElse)

Determines whether the specified *other*  object is equal to the current instance of [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(IfElse other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | IfElse | The IfElse object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-equals__statement.html language=enus -->
## TOPIC 01182: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of IfElse. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe IfElse type inherits from Statement. ParametersNameTypeDescriptionotherStatemen

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Statement object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html). Otherwise, false.

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-gethashcode.html language=enus -->
## TOPIC 01183: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a IfElse object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCode.

### GetHashCode()

Serves as a hash function for a [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html) object.

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse.html language=enus -->
## TOPIC 01184: IfElse()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of IfElse. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic IfElse()RemarksThis constructor sets TestExpression to an Expression with a value of true.

### IfElse()

Initializes a new instance of [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public IfElse()

#### Remarks

This constructor sets [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-testexpression.html) to an [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) with a value of true.

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__expression-block-block.html language=enus -->
## TOPIC 01185: IfElse(Expression, Block, Block)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__expression-block-block.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__expression-block-block.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of IfElse that evaluates the specified testExpression and executes the ifTrue or ifFalse code section, depending on the result of the evaluation. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic IfElse(Expression testExpression, Block ifTr

### IfElse(Expression, Block, Block)

Initializes a new instance of [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html) that evaluates the specified *testExpression*  and executes the *ifTrue*  or *ifFalse*  code section, depending on the result of the evaluation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public IfElse(Expression testExpression, Block ifTrue, Block ifFalse)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| testExpression | Expression | The expression to evaluate to determine whether to execute the IfTrue or IfFalse code section. This expression must evaluate to a Boolean value. |
| ifTrue | Block | The block of code to execute if testExpression is true. |
| ifFalse | Block | The block of code to execute if testExpression is false. |

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__expression.html language=enus -->
## TOPIC 01186: IfElse(Expression)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of IfElse that evaluates the specified testExpression . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic IfElse(Expression testExpression)ParametersNameTypeDescriptiontestExpressionExpressionThe expression to evaluate to determine whether

### IfElse(Expression)

Initializes a new instance of [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html) that evaluates the specified *testExpression* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public IfElse(Expression testExpression)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| testExpression | Expression | The expression to evaluate to determine whether to execute the IfTrue or IfFalse code section. This expression must evaluate to a Boolean value. |

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__ifelse.html language=enus -->
## TOPIC 01187: IfElse(IfElse)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__ifelse.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-ifelse__ifelse.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of IfElse by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic IfElse(IfElse node)ParametersNameTypeDescriptionnodeIfElseThe instance of IfElse to copy.

### IfElse(IfElse)

Initializes a new instance of [IfElse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public IfElse(IfElse node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | IfElse | The instance of IfElse to copy. |

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iffalse.html language=enus -->
## TOPIC 01188: IfFalse

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iffalse.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iffalse.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the block of code to execute if TestExpression is false. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Block IfFalse { get; set; }ReturnsThe code Block to execute.

### IfFalse

Gets or sets the block of code to execute if [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-testexpression.html) is false.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) IfFalse { get; set; }

#### Returns

The code [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) to execute.

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iftrue.html language=enus -->
## TOPIC 01189: IfTrue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iftrue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iftrue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the block of code to execute if TestExpression is true. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Block IfTrue { get; set; }ReturnsThe code Block to execute.

### IfTrue

Gets or sets the block of code to execute if [TestExpression](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-testexpression.html) is true.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) IfTrue { get; set; }

#### Returns

The code [Block](nationalinstruments-veristand-realtimesequencedefinitionapi-block.html) to execute.

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-testexpression.html language=enus -->
## TOPIC 01190: TestExpression

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-testexpression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-testexpression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the expression that is evaluated to determine whether to execute the IfTrue or IfFalse code section. The expression must evaluate to a Boolean value. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Expression TestExpression { get; set; }ReturnsThe Bool

### TestExpression

Gets or sets the expression that is evaluated to determine whether to execute the [IfTrue](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iftrue.html) or [IfFalse](nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse-iffalse.html) code section. The expression must evaluate to a Boolean value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html) TestExpression { get; set; }

#### Returns

The Boolean [Expression](nationalinstruments-veristand-realtimesequencedefinitionapi-expression.html).

Parent topic:

IfElse Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html language=enus -->
## TOPIC 01191: IfElse Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-ifelse.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an IfElse conditional statement, which executes one of two code sections depending on the value of a Boolean expression. Derives fromStatementIEquatable< IfElse >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class IfElse : Statement, IEquatable< IfElse

### IfElse Class

Represents an **IfElse** conditional statement, which executes one of two code sections depending on the value of a Boolean expression.

#### Derives from

- Statement
- IEquatable< IfElse >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class IfElse : Statement, IEquatable< IfElse >

#### Remarks

Use the members of this class to configure the conditional statement, including the Boolean expression to evaluate and the code to execute based on that value.

**Accessing this Class:**

- IfElse Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| IfElse() | Initializes a new instance of IfElse. |
| IfElse(IfElse) | Initializes a new instance of IfElse by copying an existing instance. |
| IfElse(Expression) | Initializes a new instance of IfElse that evaluates the specified testExpression . |
| IfElse(Expression, Block, Block) | Initializes a new instance of IfElse that evaluates the specified testExpression and executes the ifTrue or ifFalse code section, depending on the result of the evaluation. |

#### Properties

| Name | Description |
| --- | --- |
| IfFalse | Gets or sets the block of code to execute if TestExpression is false. |
| IfTrue | Gets or sets the block of code to execute if TestExpression is true. |
| TestExpression | Gets or sets the expression that is evaluated to determine whether to execute the IfTrue or IfFalse code section. The expression must evaluate to a Boolean value. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(IfElse) | Determines whether the specified other object is equal to the current instance of IfElse. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of IfElse. |
| GetHashCode() | Serves as a hash function for a IfElse object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-doeschannelexist__string.html language=enus -->
## TOPIC 01192: DoesChannelExist(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-doeschannelexist__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-doeschannelexist__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the channel exists. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool DoesChannelExist(string channelPath)ParametersNameTypeDescriptionchannelPathstringChannel or alias pathReturnsReturns true if the channel exists

### DoesChannelExist(string)

Indicates if the channel exists.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool DoesChannelExist(string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | Channel or alias path |

#### Returns

Returns true if the channel exists

Parent topic:

IGetChannelInfo Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getchanneldataindex__string.html language=enus -->
## TOPIC 01193: GetChannelDataIndex(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getchanneldataindex__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getchanneldataindex__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel's data index. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic int GetChannelDataIndex(string channelPath)ParametersNameTypeDescriptionchannelPathstringChannel or alias pathReturnsReturns the channel's data index

### GetChannelDataIndex(string)

Gets the channel's data index.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public int GetChannelDataIndex(string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | Channel or alias path |

#### Returns

Returns the channel's data index

Parent topic:

IGetChannelInfo Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getchannelfaultindex__string.html language=enus -->
## TOPIC 01194: GetChannelFaultIndex(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getchannelfaultindex__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getchannelfaultindex__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel's fault index or -1 if the channel is not faultable. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic int GetChannelFaultIndex(string channelPath)ParametersNameTypeDescriptionchannelPathstringChannel or alias pathReturnsReturns the channel's fault i

### GetChannelFaultIndex(string)

Gets the channel's fault index or -1 if the channel is not faultable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public int GetChannelFaultIndex(string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | Channel or alias path |

#### Returns

Returns the channel's fault index

Parent topic:

IGetChannelInfo Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getvectorchannelsize__string.html language=enus -->
## TOPIC 01195: GetVectorChannelSize(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getvectorchannelsize__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-getvectorchannelsize__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the size of a vector channel in bytes. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic int GetVectorChannelSize(string channelPath)ParametersNameTypeDescriptionchannelPathstringChannel or alias pathReturnsReturns the size of a vector channel in bytes.

### GetVectorChannelSize(string)

Gets the size of a vector channel in bytes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public int GetVectorChannelSize(string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | Channel or alias path |

#### Returns

Returns the size of a vector channel in bytes.

Parent topic:

IGetChannelInfo Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischannelfaultable__string.html language=enus -->
## TOPIC 01196: IsChannelFaultable(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischannelfaultable__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischannelfaultable__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the channel is faultable. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool IsChannelFaultable(string channelPath)ParametersNameTypeDescriptionchannelPathstringChannel or alias pathReturnsReturns true if the channel is faultable

### IsChannelFaultable(string)

Indicates if the channel is faultable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool IsChannelFaultable(string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | Channel or alias path |

#### Returns

Returns true if the channel is faultable

Parent topic:

IGetChannelInfo Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischanneloftype__string-channelsizetype.html language=enus -->
## TOPIC 01197: IsChannelOfType(string, ChannelSizeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischanneloftype__string-channelsizetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischanneloftype__string-channelsizetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the channel is of the specified type. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool IsChannelOfType(string channelPath, ChannelSizeType type)ParametersNameTypeDescriptionchannelPathstringChannel or alias pathtypeChannelSizeTypeThe type of channe

### IsChannelOfType(string, ChannelSizeType)

Indicates if the channel is of the specified type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool IsChannelOfType(string channelPath, ChannelSizeType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | Channel or alias path |
| type | ChannelSizeType | The type of channel to verify |

#### Returns

Returns true if the channel is of the specified type

Parent topic:

IGetChannelInfo Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischannelwritable__string.html language=enus -->
## TOPIC 01198: IsChannelWritable(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischannelwritable__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo-ischannelwritable__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the channel is writable. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool IsChannelWritable(string channelPath)ParametersNameTypeDescriptionchannelPathstringChannel or alias pathReturnsReturns true if the channel is writable

### IsChannelWritable(string)

Indicates if the channel is writable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool IsChannelWritable(string channelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelPath | string | Channel or alias path |

#### Returns

Returns true if the channel is writable

Parent topic:

IGetChannelInfo Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo.html language=enus -->
## TOPIC 01199: IGetChannelInfo Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-igetchannelinfo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interface used for obtaining information about channels mapped in real-time sequences. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic interface IGetChannelInfoMethodsNameDescriptionDoesChannelExist(string)Indicates if the channel exists. GetChannel

### IGetChannelInfo Interface

Interface used for obtaining information about channels mapped in real-time sequences.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public interface IGetChannelInfo

#### Methods

| Name | Description |
| --- | --- |
| DoesChannelExist(string) | Indicates if the channel exists. |
| GetChannelDataIndex(string) | Gets the channel's data index. |
| GetChannelFaultIndex(string) | Gets the channel's fault index or -1 if the channel is not faultable. |
| GetVectorChannelSize(string) | Gets the size of a vector channel in bytes. |
| IsChannelFaultable(string) | Indicates if the channel is faultable. |
| IsChannelOfType(string, ChannelSizeType) | Indicates if the channel is of the specified type. |
| IsChannelWritable(string) | Indicates if the channel is writable. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-isinternal-value.html language=enus -->
## TOPIC 01200: Value

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-isinternal-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-isinternal-value.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the property is internal or public. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Value { get; }Returnstrue if the property is internal. false if it is public.

### Value

Gets a value indicating whether the property is internal or public.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Value { get; }

#### Returns

true if the property is internal. false if it is public.

Parent topic:

IsInternal Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-isinternal.html language=enus -->
## TOPIC 01201: IsInternal Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-isinternal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-isinternal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an attribute that indicates if a property is internal or public. Derives fromAttributeSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class IsInternal : AttributeRemarksInherits from System.Attribute. Thread SafetyAny members of this type are not guarant

### IsInternal Class

Represents an attribute that indicates if a property is internal or public.

#### Derives from

- Attribute

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class IsInternal : Attribute

#### Remarks

Inherits from System.Attribute.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Value | Gets a value indicating whether the property is internal or public. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-defaultvalue.html language=enus -->
## TOPIC 01202: DefaultValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-defaultvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default value of the local variable. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override DataValue DefaultValue { get; set; }ReturnsA DataValue object.

### DefaultValue

Gets or sets the default value of the local variable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override [DataValue](nationalinstruments-veristand-data-datavalue.html) DefaultValue { get; set; }

#### Returns

A [DataValue](nationalinstruments-veristand-data-datavalue.html) object.

Parent topic:

LocalDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration.html language=enus -->
## TOPIC 01203: LocalDeclaration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LocalDeclaration class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic LocalDeclaration()RemarksThis constructor sets Identifier to "LocalVariable" and sets DefaultValue to a DoubleValue.

### LocalDeclaration()

Initializes a new instance of the [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public LocalDeclaration()

#### Remarks

This constructor sets [Identifier](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-identifier.html) to "LocalVariable" and sets [DefaultValue](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-defaultvalue.html) to a [DoubleValue](nationalinstruments-veristand-data-doublevalue.html).

Parent topic:

LocalDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration__localdeclaration.html language=enus -->
## TOPIC 01204: LocalDeclaration(LocalDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration__localdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration__localdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the LocalDeclaration class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic LocalDeclaration(LocalDeclaration node)ParametersNameTypeDescriptionnodeLocalDeclarationThe instance of LocalDeclaration to cop

### LocalDeclaration(LocalDeclaration)

Initializes a new instance of the [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public LocalDeclaration(LocalDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | LocalDeclaration | The instance of LocalDeclaration to copy. |

Parent topic:

LocalDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration__string-datavalue.html language=enus -->
## TOPIC 01205: LocalDeclaration(string, DataValue)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration__string-datavalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-localdeclaration__string-datavalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of theLocalDeclaration class and creates a local variable with the specified variable name, default value, and data type. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic LocalDeclaration(string identifier, DataValue defaultValue)Parameter

### LocalDeclaration(string, DataValue)

Initializes a new instance of the[LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html) class and creates a local variable with the specified variable name, default value, and data type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public LocalDeclaration(string identifier, DataValue defaultValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The name of the local variable. |
| defaultValue | DataValue | The default value and data type of the local variable. |

Parent topic:

LocalDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-operator-channelreferencedeclaration__localdeclaration.html language=enus -->
## TOPIC 01206: operator ChannelReferenceDeclaration(LocalDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-operator-channelreferencedeclaration__localdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration-operator-channelreferencedeclaration__localdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new ChannelReferenceDeclaration object using the properties of a LocalDeclaration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic static operator ChannelReferenceDeclaration(LocalDeclaration node)ParametersNameTypeDescriptionnodeLocalDeclarationThe node

### operator ChannelReferenceDeclaration(LocalDeclaration)

Creates a new [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) object using the properties of a [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static operator ChannelReferenceDeclaration(LocalDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | LocalDeclaration | The node to cast. |

#### Returns

a [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) with similar settings to the source [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html).

Parent topic:

LocalDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html language=enus -->
## TOPIC 01207: LocalDeclaration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a declaration of a local variable in a real-time sequence. Derives fromAbstractDeclarationSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class LocalDeclaration : AbstractDeclarationRemarksUse the members of this class to configure the properties of the

### LocalDeclaration Class

Represents a declaration of a local variable in a real-time sequence.

#### Derives from

- AbstractDeclaration

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class LocalDeclaration : AbstractDeclaration

#### Remarks

Use the members of this class to configure the properties of the local variable, including its default value.

**Accessing this Class:**

- [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-variables.html)
- LocalDeclaration Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| LocalDeclaration(string, DataValue) | Initializes a new instance of theLocalDeclaration class and creates a local variable with the specified variable name, default value, and data type. |
| LocalDeclaration(LocalDeclaration) | Initializes a new instance of the LocalDeclaration class by copying an existing instance. |
| LocalDeclaration() | Initializes a new instance of the LocalDeclaration class. |

#### Properties

| Name | Description |
| --- | --- |
| DefaultValue | Gets or sets the default value of the local variable. |

#### Operators

| Name | Description |
| --- | --- |
| operator ChannelReferenceDeclaration(LocalDeclaration) | Creates a new ChannelReferenceDeclaration object using the properties of a LocalDeclaration. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-addlocalvariable__localdeclaration.html language=enus -->
## TOPIC 01208: AddLocalVariable(LocalDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-addlocalvariable__localdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-addlocalvariable__localdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified localVariable to the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddLocalVariable(LocalDeclaration localVariable)ParametersNameTypeDescriptionlocalVariableLocalDeclarationThe variable to add.

### AddLocalVariable(LocalDeclaration)

Adds the specified *localVariable*  to the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddLocalVariable(LocalDeclaration localVariable)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| localVariable | LocalDeclaration | The variable to add. |

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-clearlocalvariables.html language=enus -->
## TOPIC 01209: ClearLocalVariables()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-clearlocalvariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-clearlocalvariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all the defined local variables from the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearLocalVariables()

### ClearLocalVariables()

Clears all the defined local variables from the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearLocalVariables()

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-equals__localvariables.html language=enus -->
## TOPIC 01210: Equals(LocalVariables)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-equals__localvariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-equals__localvariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of LocalVariables. Equivalency is determined using M:NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.LocalVariables.Variables. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic

### Equals(LocalVariables)

Determines whether the specified *other*  object is equal to the current instance of [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html). Equivalency is determined using M:NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.LocalVariables.Variables.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(LocalVariables other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | LocalVariables | The LocalVariables object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-equals__object.html language=enus -->
## TOPIC 01211: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a LocalVariables object, is equal to the current instance of LocalVariables. Equivalency is determined using M:NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.LocalVariables.Variables. SyntaxNamespace: NationalInstruments.VeriStand.Rea

### Equals(object)

Determines whether the specified *obj* , which must be a [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) object, is equal to the current instance of [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html). Equivalency is determined using M:NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.LocalVariables.Variables.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current LocalVariables object. |

#### Returns

true if the specified *obj*  is equal to the current [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) object. Otherwise, false.

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-gethashcode.html language=enus -->
## TOPIC 01212: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a LocalVariables object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides obje

### GetHashCode()

Serves as a hash function for a [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) object.

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-localvariables.html language=enus -->
## TOPIC 01213: LocalVariables()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-localvariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-localvariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of LocalVariables. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic LocalVariables()

### LocalVariables()

Initializes a new instance of [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public LocalVariables()

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-localvariables__localvariables.html language=enus -->
## TOPIC 01214: LocalVariables(LocalVariables)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-localvariables__localvariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-localvariables__localvariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of LocalVariables by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic LocalVariables(LocalVariables node)ParametersNameTypeDescriptionnodeLocalVariablesThe instance of LocalVariables to copy.

### LocalVariables(LocalVariables)

Initializes a new instance of [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public LocalVariables(LocalVariables node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | LocalVariables | The instance of LocalVariables to copy. |

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-variables.html language=enus -->
## TOPIC 01215: Variables

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-variables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables-variables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the defined local variables for a real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic LocalDeclaration[] Variables { get; set; }ReturnsAn array of LocalDeclaration objects.

### Variables

Gets or sets the defined local variables for a real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html)[] Variables { get; set; }

#### Returns

An array of [LocalDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-localdeclaration.html) objects.

Parent topic:

LocalVariables Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html language=enus -->
## TOPIC 01216: LocalVariables Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-localvariables.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Local Variables section of a real-time sequence definition, which contains the set of local variables that the sequence uses. Derives fromBaseNodeIEquatable< LocalVariables >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class LocalVariables : BaseN

### LocalVariables Class

Represents the **Local Variables** section of a real-time sequence definition, which contains the set of local variables that the sequence uses.

#### Derives from

- BaseNode
- IEquatable< LocalVariables >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class LocalVariables : BaseNode, IEquatable< LocalVariables >

#### Remarks

Use the members of this class to add, access, or clear the local variables of a real-time sequence.

**Accessing this Class:**

- [LocalVariables](nationalinstruments-veristand-realtimesequencedefinitionapi-variables-localvariables.html)
- LocalVariables Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| LocalVariables() | Initializes a new instance of LocalVariables. |
| LocalVariables(LocalVariables) | Initializes a new instance of LocalVariables by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| Variables | Gets or sets the defined local variables for a real-time sequence. |

#### Methods

| Name | Description |
| --- | --- |
| AddLocalVariable(LocalDeclaration) | Adds the specified localVariable to the real-time sequence. |
| ClearLocalVariables() | Clears all the defined local variables from the real-time sequence. |
| Equals(LocalVariables) | Determines whether the specified other object is equal to the current instance of LocalVariables. Equivalency is determined using M:NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.LocalVariables.Variables. |
| Equals(object) | Determines whether the specified obj , which must be a LocalVariables object, is equal to the current instance of LocalVariables. Equivalency is determined using M:NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.LocalVariables.Variables. |
| GetHashCode() | Serves as a hash function for a LocalVariables object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-main-main.html language=enus -->
## TOPIC 01217: Main()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-main-main.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-main-main.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Main. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Main()

### Main()

Initializes a new instance of [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Main()

Parent topic:

Main Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-main-main__main.html language=enus -->
## TOPIC 01218: Main(Main)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-main-main__main.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-main-main__main.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Main by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Main(Main node)ParametersNameTypeDescriptionnodeMainThe instance of Main to copy.

### Main(Main)

Initializes a new instance of [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-main.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Main(Main node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Main | The instance of Main to copy. |

Parent topic:

Main Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-main.html language=enus -->
## TOPIC 01219: Main Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-main.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-main.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Main section of sequence code, which executes after the Setup section and before the CleanUp sections. This section contains the core set of statements that the sequence executes. Derives fromCodeSectionSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic

### Main Class

Represents the **Main** section of sequence code, which executes after the [Setup](nationalinstruments-veristand-realtimesequencedefinitionapi-setup.html) section and before the [CleanUp](nationalinstruments-veristand-realtimesequencedefinitionapi-cleanup.html) sections. This section contains the core set of statements that the sequence executes.

#### Derives from

- CodeSection

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Main : CodeSection

#### Remarks

Use this section to configure the main execution steps of the real-time sequence.

**Accessing this Class:**

- [Main](nationalinstruments-veristand-realtimesequencedefinitionapi-code-main.html)
- Main Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Main(Main) | Initializes a new instance of Main by copying an existing instance. |
| Main() | Initializes a new instance of Main. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multilinestringattribute-multilinestringattribute.html language=enus -->
## TOPIC 01220: MultilineStringAttribute()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multilinestringattribute-multilinestringattribute.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multilinestringattribute-multilinestringattribute.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the MultilineStringAttribute class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic MultilineStringAttribute()

### MultilineStringAttribute()

Initializes a new instance of the [MultilineStringAttribute](nationalinstruments-veristand-realtimesequencedefinitionapi-multilinestringattribute.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public MultilineStringAttribute()

Parent topic:

MultilineStringAttribute Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multilinestringattribute.html language=enus -->
## TOPIC 01221: MultilineStringAttribute Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multilinestringattribute.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multilinestringattribute.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an attribute that indicates that a string contains multiple lines. Derives fromAttributeSyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class MultilineStringAttribute : AttributeRemarksInherits from System.Attribute. Thread SafetyAny members of this type

### MultilineStringAttribute Class

Represents an attribute that indicates that a string contains multiple lines.

#### Derives from

- Attribute

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class MultilineStringAttribute : Attribute

#### Remarks

Inherits from System.Attribute.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| MultilineStringAttribute() | Initializes a new instance of the MultilineStringAttribute class. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-addtask__task.html language=enus -->
## TOPIC 01222: AddTask(Task)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-addtask__task.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-addtask__task.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified task as a child of the Multitask structure. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddTask(Task task)ParametersNameTypeDescriptiontaskTaskThe task to add.

### AddTask(Task)

Adds the specified *task*  as a child of the [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) structure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddTask(Task task)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| task | Task | The task to add. |

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-cleartasks.html language=enus -->
## TOPIC 01223: ClearTasks()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-cleartasks.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-cleartasks.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all the child tasks from the Multitask structure. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearTasks()

### ClearTasks()

Clears all the child tasks from the [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) structure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearTasks()

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-equals__multitask.html language=enus -->
## TOPIC 01224: Equals(Multitask)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-equals__multitask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-equals__multitask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Multitask. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Multitask other)ParametersNameTypeDescriptionotherMultitaskThe Multitask object to compare with the current inst

### Equals(Multitask)

Determines whether the specified *other*  object is equal to the current instance of [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Multitask other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Multitask | The Multitask object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-equals__statement.html language=enus -->
## TOPIC 01225: Equals(Statement)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-equals__statement.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-equals__statement.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Multitask. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(Statement other)RemarksThe Multitask type inherits from Statement. ParametersNameTypeDescriptionotherSt

### Equals(Statement)

Determines whether the specified *other*  object is equal to the current instance of [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(Statement other)

#### Remarks

The [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) type inherits from [Statement](nationalinstruments-veristand-realtimesequencedefinitionapi-statement.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Statement | The Multitask object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance of [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html). Otherwise, false.

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-gethashcode.html language=enus -->
## TOPIC 01226: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Multitask object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCo

### GetHashCode()

Serves as a hash function for a [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-statement-gethashcode.html).

#### Returns

A hash code for the current [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) object.

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask.html language=enus -->
## TOPIC 01227: Multitask()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Multitask. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Multitask()

### Multitask()

Initializes a new instance of [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Multitask()

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask__multitask.html language=enus -->
## TOPIC 01228: Multitask(Multitask)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask__multitask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask__multitask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Multitask by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Multitask(Multitask node)ParametersNameTypeDescriptionnodeMultitaskThe instance of Multitask to copy.

### Multitask(Multitask)

Initializes a new instance of [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Multitask(Multitask node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Multitask | The instance of Multitask to copy. |

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask__task_arr1.html language=enus -->
## TOPIC 01229: Multitask(Task[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask__task_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-multitask__task_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Multitask that executes the specified child tasks . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Multitask(Task[] tasks)ParametersNameTypeDescriptiontasksTask[]The set of child tasks to iteratively execute in the same time step.

### Multitask(Task[])

Initializes a new instance of [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) that executes the specified child *tasks* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Multitask(Task[] tasks)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tasks | Task[] | The set of child tasks to iteratively execute in the same time step. |

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-tasks.html language=enus -->
## TOPIC 01230: Tasks

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-tasks.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask-tasks.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the set of child tasks of the Multitask structure. These tasks iteratively execute in the same time step. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Task[] Tasks { get; set; }ReturnsAn array of Task objects.

### Tasks

Gets or sets the set of child tasks of the [Multitask](nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html) structure. These tasks iteratively execute in the same time step.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html)[] Tasks { get; set; }

#### Returns

An array of [Task](nationalinstruments-veristand-realtimesequencedefinitionapi-task.html) objects.

Parent topic:

Multitask Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html language=enus -->
## TOPIC 01231: Multitask Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-multitask.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a MultiTask structure, which branches sequence code execution into one or more child tasks. On each time step, the MultiTask structure iteratively executes code from each child task until the task either terminates or yields execution to the next time step. Derives fromStatementIEquatable

### Multitask Class

Represents a **MultiTask** structure, which branches sequence code execution into one or more child tasks. On each time step, the **MultiTask** structure iteratively executes code from each child task until the task either terminates or yields execution to the next time step.

#### Derives from

- Statement
- IEquatable< Multitask >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class Multitask : Statement, IEquatable< Multitask >

#### Remarks

Use the members of this class to add or access tasks in a **MultiTask** structure.

**Accessing this Class:**

- Multitask Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Multitask() | Initializes a new instance of Multitask. |
| Multitask(Task[]) | Initializes a new instance of Multitask that executes the specified child tasks . |
| Multitask(Multitask) | Initializes a new instance of Multitask by copying an existing instance. |

#### Properties

| Name | Description |
| --- | --- |
| Tasks | Gets or sets the set of child tasks of the Multitask structure. These tasks iteratively execute in the same time step. |

#### Methods

| Name | Description |
| --- | --- |
| AddTask(Task) | Adds the specified task as a child of the Multitask structure. |
| ClearTasks() | Clears all the child tasks from the Multitask structure. |
| Equals(Multitask) | Determines whether the specified other object is equal to the current instance of Multitask. |
| Equals(Statement) | Determines whether the specified other object is equal to the current instance of Multitask. |
| GetHashCode() | Serves as a hash function for a Multitask object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-overwriteexistingfilebehavior.html language=enus -->
## TOPIC 01232: OverwriteExistingFileBehavior Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-overwriteexistingfilebehavior.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-overwriteexistingfilebehavior.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior when an existing file has the same name as the new file. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic enum OverwriteExistingFileBehaviorMembersNameValueDescriptionOverwrite0Overwrites the existing file with the new file. Skip1Ignores the n

### OverwriteExistingFileBehavior Enumeration

Specifies the behavior when an existing file has the same name as the new file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public enum OverwriteExistingFileBehavior

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Overwrite | 0 | Overwrites the existing file with the new file. |
| Skip | 1 | Ignores the new file. |
| Unique | 2 | Creates a new file with a unique name. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultassignment.html language=enus -->
## TOPIC 01233: DefaultAssignment

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultassignment.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultassignment.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default system definition channel mapping for a parameter, which is the fully qualified path to the channel node within the system definition. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic SystemDefinitionChannelResource DefaultAssignment { get;

### DefaultAssignment

Gets or sets the default system definition channel mapping for a parameter, which is the fully qualified path to the channel node within the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [SystemDefinitionChannelResource](nationalinstruments-veristand-data-systemdefinitionchannelresource.html) DefaultAssignment { get; set; }

#### Returns

A [SystemDefinitionChannelResource](nationalinstruments-veristand-data-systemdefinitionchannelresource.html) object. The default is an empty path.

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultvalue.html language=enus -->
## TOPIC 01234: DefaultValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default value of a real-time sequence parameter. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override DataValue DefaultValue { get; set; }ReturnsA DataValue object.

### DefaultValue

Gets or sets the default value of a real-time sequence parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override [DataValue](nationalinstruments-veristand-data-datavalue.html) DefaultValue { get; set; }

#### Returns

A [DataValue](nationalinstruments-veristand-data-datavalue.html) object.

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-equals__object.html language=enus -->
## TOPIC 01235: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a ParameterDeclaration object, is equal to the current ParameterDeclaration. Equivalency is determined using the base class, EvaluationMethod and DefaultAssignment. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic

### Equals(object)

Determines whether the specified *obj* , which must be a [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) object, is equal to the current [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html). Equivalency is determined using the base class, [EvaluationMethod](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-evaluationmethod.html) and [DefaultAssignment](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultassignment.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current ParameterDeclaration. |

#### Returns

true if the specified *obj*  is equal to the current [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html). Otherwise, false.

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-equals__parameterdeclaration.html language=enus -->
## TOPIC 01236: Equals(ParameterDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-equals__parameterdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-equals__parameterdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of ParameterDeclaration. Equivalency is determined using the base class, EvaluationMethod and DefaultAssignment. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(ParameterDecl

### Equals(ParameterDeclaration)

Determines whether the specified *other*  object is equal to the current instance of [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html). Equivalency is determined using the base class, [EvaluationMethod](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-evaluationmethod.html) and [DefaultAssignment](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-defaultassignment.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(ParameterDeclaration other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ParameterDeclaration | The ParameterDeclaration object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-evaluationmethod.html language=enus -->
## TOPIC 01237: EvaluationMethod

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-evaluationmethod.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-evaluationmethod.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the evaluation method (ByReference or ByValue) used to get the parameter value. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic EvaluationMethod EvaluationMethod { get; set; }ReturnsAn enumeration of EvaluationMethod.

### EvaluationMethod

Gets or sets the evaluation method (**ByReference** or **ByValue**) used to get the parameter value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public [EvaluationMethod](nationalinstruments-veristand-realtimesequencedefinitionapi-evaluationmethod.html) EvaluationMethod { get; set; }

#### Returns

An enumeration of [EvaluationMethod](nationalinstruments-veristand-realtimesequencedefinitionapi-evaluationmethod.html).

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-gethashcode.html language=enus -->
## TOPIC 01238: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Cases object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides GetHashCode.

### GetHashCode()

Serves as a hash function for a [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides [GetHashCode](nationalinstruments-veristand-realtimesequencedefinitionapi-abstractdeclaration-gethashcode.html).

#### Returns

A hash code for the current [Cases](nationalinstruments-veristand-realtimesequencedefinitionapi-cases.html) object.

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-operator-channelreferencedeclaration__parameterdeclaration.html language=enus -->
## TOPIC 01239: operator ChannelReferenceDeclaration(ParameterDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-operator-channelreferencedeclaration__parameterdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-operator-channelreferencedeclaration__parameterdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a ParameterDeclaration to a ChannelReferenceDeclaration. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic static operator ChannelReferenceDeclaration(ParameterDeclaration node)ParametersNameTypeDescriptionnodeParameterDeclarationThe node to cast.ReturnsA Ch

### operator ChannelReferenceDeclaration(ParameterDeclaration)

Converts a [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) to a [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public static operator ChannelReferenceDeclaration(ParameterDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ParameterDeclaration | The node to cast. |

#### Returns

A [ChannelReferenceDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-channelreferencedeclaration.html) with similar settings to the source [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html).

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration.html language=enus -->
## TOPIC 01240: ParameterDeclaration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ParameterDeclaration class. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ParameterDeclaration()

### ParameterDeclaration()

Initializes a new instance of the [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ParameterDeclaration()

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration__parameterdeclaration.html language=enus -->
## TOPIC 01241: ParameterDeclaration(ParameterDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration__parameterdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration__parameterdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ParameterDeclaration class by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ParameterDeclaration(ParameterDeclaration node)ParametersNameTypeDescriptionnodeParameterDeclarationThe instance of Paramet

### ParameterDeclaration(ParameterDeclaration)

Initializes a new instance of the [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) class by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ParameterDeclaration(ParameterDeclaration node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ParameterDeclaration | The instance of ParameterDeclaration to copy. |

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration__string-datavalue-evaluationmethod.html language=enus -->
## TOPIC 01242: ParameterDeclaration(string, DataValue, EvaluationMethod)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration__string-datavalue-evaluationmethod.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration-parameterdeclaration__string-datavalue-evaluationmethod.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ParameterDeclaration class and creates a sequence parameter with the specified identifier , defaultValue , and evaluationMethod . SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic ParameterDeclaration(string identifier, DataValue def

### ParameterDeclaration(string, DataValue, EvaluationMethod)

Initializes a new instance of the [ParameterDeclaration](nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html) class and creates a sequence parameter with the specified *identifier* , *defaultValue* , and *evaluationMethod* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public ParameterDeclaration(string identifier, DataValue defaultValue, EvaluationMethod evaluationMethod)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| identifier | string | The name of the parameter. |
| defaultValue | DataValue | The default value and data type of the parameter. |
| evaluationMethod | EvaluationMethod | The evaluation method for the parameter value. If the parameter value is passed in by reference, the sequence directly reads or writes the value of the calling sequence, rather than a copy of that value. |

Parent topic:

ParameterDeclaration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html language=enus -->
## TOPIC 01243: ParameterDeclaration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameterdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a declaration of a real-time sequence parameter. Derives fromAbstractDeclarationIEquatable< ParameterDeclaration >SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic class ParameterDeclaration : AbstractDeclaration, IEquatable< ParameterDeclaration >RemarksA

### ParameterDeclaration Class

Represents a declaration of a real-time sequence parameter.

#### Derives from

- AbstractDeclaration
- IEquatable< ParameterDeclaration >

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public class ParameterDeclaration : AbstractDeclaration, IEquatable< ParameterDeclaration >

#### Remarks

A parameter has a unique name, a data type, and a value associated with it. You can evaluate a parameter by value or by reference. If a parameter is passed into a sequence by reference, the sequence reads or writes the value of the caller's variable directly, rather than reading a copy of that value.

Use the members of this class to get or set the default assignment and evaluation method for a real-time sequence parameter.

**Accessing this Class:**

- [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-variables.html)
- ParameterDeclaration Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ParameterDeclaration() | Initializes a new instance of the ParameterDeclaration class. |
| ParameterDeclaration(ParameterDeclaration) | Initializes a new instance of the ParameterDeclaration class by copying an existing instance. |
| ParameterDeclaration(string, DataValue, EvaluationMethod) | Initializes a new instance of the ParameterDeclaration class and creates a sequence parameter with the specified identifier , defaultValue , and evaluationMethod . |

#### Properties

| Name | Description |
| --- | --- |
| DefaultAssignment | Gets or sets the default system definition channel mapping for a parameter, which is the fully qualified path to the channel node within the system definition. |
| DefaultValue | Gets or sets the default value of a real-time sequence parameter. |
| EvaluationMethod | Gets or sets the evaluation method (ByReference or ByValue) used to get the parameter value. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(ParameterDeclaration) | Determines whether the specified other object is equal to the current instance of ParameterDeclaration. Equivalency is determined using the base class, EvaluationMethod and DefaultAssignment. |
| Equals(object) | Determines whether the specified obj , which must be a ParameterDeclaration object, is equal to the current ParameterDeclaration. Equivalency is determined using the base class, EvaluationMethod and DefaultAssignment. |
| GetHashCode() | Serves as a hash function for a Cases object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. |

#### Operators

| Name | Description |
| --- | --- |
| operator ChannelReferenceDeclaration(ParameterDeclaration) | Converts a ParameterDeclaration to a ChannelReferenceDeclaration. |

Parent topic:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-addparameter__parameterdeclaration.html language=enus -->
## TOPIC 01244: AddParameter(ParameterDeclaration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-addparameter__parameterdeclaration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-addparameter__parameterdeclaration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified parameter to the end of the Parameters section. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void AddParameter(ParameterDeclaration parameter)ParametersNameTypeDescriptionparameterParameterDeclarationThe parameter to add.

### AddParameter(ParameterDeclaration)

Adds the specified *parameter*  to the end of the [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void AddParameter(ParameterDeclaration parameter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameter | ParameterDeclaration | The parameter to add. |

Parent topic:

Parameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-clearparameters.html language=enus -->
## TOPIC 01245: ClearParameters()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-clearparameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-clearparameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all the currently declared parameters from the real-time sequence. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic void ClearParameters()

### ClearParameters()

Clears all the currently declared parameters from the real-time sequence.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public void ClearParameters()

Parent topic:

Parameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-equals__object.html language=enus -->
## TOPIC 01246: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified obj , which must be a Parameters object, is equal to the current Parameters. Equivalency is determined using Variables. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override bool Equals(object obj)RemarksOverrides object.Equals(o

### Equals(object)

Determines whether the specified *obj* , which must be a [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) object, is equal to the current [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html). Equivalency is determined using [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-variables.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override bool Equals(object obj)

#### Remarks

Overrides object.Equals(object).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The object to compare with the current Parameters. |

#### Returns

true if the specified *obj*  is equal to the current [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html). Otherwise, false.

Parent topic:

Parameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-equals__parameters.html language=enus -->
## TOPIC 01247: Equals(Parameters)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-equals__parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-equals__parameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified other object is equal to the current instance of Parameters. Equivalency is determined using Variables. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic bool Equals(Parameters other)ParametersNameTypeDescriptionotherParametersThe Par

### Equals(Parameters)

Determines whether the specified *other*  object is equal to the current instance of [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html). Equivalency is determined using [Variables](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-variables.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public bool Equals(Parameters other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | Parameters | The Parameters object to compare with the current instance. |

#### Returns

true if the specified *other*  object is equal to the current instance. Otherwise, false.

Parent topic:

Parameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-gethashcode.html language=enus -->
## TOPIC 01248: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serves as a hash function for a Parameters object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic override int GetHashCode()RemarksOverrides object.G

### GetHashCode()

Serves as a hash function for a [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) object. The hash code this method returns is suitable for use in hashing algorithms and data structures like a hash table.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public override int GetHashCode()

#### Remarks

Overrides object.GetHashCode.

#### Returns

A hash code for the current [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) object.

Parent topic:

Parameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-parameters.html language=enus -->
## TOPIC 01249: Parameters()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-parameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Parameters. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Parameters()

### Parameters()

Initializes a new instance of [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Parameters()

Parent topic:

Parameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-parameters__parameters.html language=enus -->
## TOPIC 01250: Parameters(Parameters)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-parameters__parameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-realtimesequencedefinitionapi-parameters-parameters__parameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Parameters by copying an existing instance. SyntaxNamespace: NationalInstruments.VeriStand.RealTimeSequenceDefinitionApipublic Parameters(Parameters node)ParametersNameTypeDescriptionnodeParametersThe instance of Parameters to copy.

### Parameters(Parameters)

Initializes a new instance of [Parameters](nationalinstruments-veristand-realtimesequencedefinitionapi-parameters.html) by copying an existing instance.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi](nationalinstruments-veristand-realtimesequencedefinitionapi.html)

public Parameters(Parameters node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | Parameters | The instance of Parameters to copy. |

Parent topic:

Parameters Class
