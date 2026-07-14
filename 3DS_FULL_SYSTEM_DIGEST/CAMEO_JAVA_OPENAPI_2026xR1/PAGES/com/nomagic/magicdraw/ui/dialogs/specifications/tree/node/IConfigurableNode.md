# JAVA OPENAPI: IConfigurableNode (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/ui/dialogs/specifications/tree/node/IConfigurableNode.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/specifications/tree/node/IConfigurableNode.html`
- source_sha256: `3fe34d0698fac7feb8a1a0db0f3bbb6e006c2e53d8bb2cabd1873f2aebaea57a`
- captured_utc: `2026-07-14T16:46:02.761836+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.specifications.tree.node](package-summary.html)

## Interface IConfigurableNode

@OpenApiAllpublic interfaceIConfigurableNode

The interface of configurable specification tree node - is used for tree configuration.
 Also defines standard specification tree nodes IDs.
 *Create this node with [`ConfigurableNodeFactory`](ConfigurableNodeFactory.html)*

See Also:
[`ConfigurableNodeFactory`](ConfigurableNodeFactory.html)
[`ISpecificationNode`](ISpecificationNode.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static interface`
`[IConfigurableNode.Position](IConfigurableNode.Position.html)`
Position to insert child node
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ACTORS](#ACTORS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ACTUAL_GATES](#ACTUAL_GATES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ARGUMENTS](#ARGUMENTS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ASSOCIATION_ENDS](#ASSOCIATION_ENDS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ATTRIBUTES](#ATTRIBUTES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[BEHAVIORS](#BEHAVIORS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CLAUSES](#CLAUSES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[COMMENT](#COMMENT)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONFIGURATIONS](#CONFIGURATIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONNECTORS](#CONNECTORS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONSTRAINTS](#CONSTRAINTS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONVEYED_INFORMATION](#CONVEYED_INFORMATION)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DEPLOYED_ARTIFACTS](#DEPLOYED_ARTIFACTS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[DOCUMENTATION_HYPERLINKS](#DOCUMENTATION_HYPERLINKS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ENUMERATION_LITERALS](#ENUMERATION_LITERALS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[EXTENSION_POINTS](#EXTENSION_POINTS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[FORMAL_GATES](#FORMAL_GATES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INFORMATION_FLOWS](#INFORMATION_FLOWS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INNER_ELEMENTS](#INNER_ELEMENTS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INNER_STATES](#INNER_STATES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INSTANCES](#INSTANCES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[INTERNAL_TRANSITIONS](#INTERNAL_TRANSITIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[LANGUAGE_PROPERTIES](#LANGUAGE_PROPERTIES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[MANAGE_NAVIGATION](#MANAGE_NAVIGATION)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[MANIFESTATIONS](#MANIFESTATIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[MESSAGES](#MESSAGES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[NESTED_NODES](#NESTED_NODES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPERANDS](#OPERANDS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPERATIONS](#OPERATIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PARAMETERS](#PARAMETERS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PINS](#PINS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PORTS](#PORTS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[PROVIDED_REQUIRED_INTERFACES](#PROVIDED_REQUIRED_INTERFACES)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[QUALIFIERS](#QUALIFIERS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[REALIZING_CLASSIFIERS](#REALIZING_CLASSIFIERS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[RECEPTIONS](#RECEPTIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[RELATIONS](#RELATIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ROLE_BINDINGS](#ROLE_BINDINGS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[SLOTS](#SLOTS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TAGS](#TAGS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_PARAMETER_SUBSTITUTIONS](#TEMPLATE_PARAMETER_SUBSTITUTIONS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[TEMPLATE_PARAMETERS](#TEMPLATE_PARAMETERS)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[USAGE](#USAGE)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[USE_CASE_SCENARIO](#USE_CASE_SCENARIO)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[USED_IN](#USED_IN)`

`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[VARIABLES](#VARIABLES)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addNode](#addNode(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode))([IConfigurableNode](IConfigurableNode.html) node)`
Adds given node as child node.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getAllChildrenNodeIDS](#getAllChildrenNodeIDS())()`
Returns all children node IDs.
`[IConfigurableNode](IConfigurableNode.html)`
`[getChild](#getChild(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Returns child node according given child id.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns ID of the node.
`void`
`[insertNode](#insertNode(java.lang.String,com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.Position,com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [IConfigurableNode.Position](IConfigurableNode.Position.html) position,
 [IConfigurableNode](IConfigurableNode.html) node)`
Inserts given node as child node near given child node id.
`void`
`[removeNode](#removeNode(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Removes child node with given id.

============ FIELD DETAIL =========== 
Field Details
DOCUMENTATION_HYPERLINKS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DOCUMENTATION_HYPERLINKS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.DOCUMENTATION_HYPERLINKS)
MANAGE_NAVIGATION
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) MANAGE_NAVIGATION
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.MANAGE_NAVIGATION)
USAGE
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) USAGE
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.USAGE)
ATTRIBUTES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ATTRIBUTES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ATTRIBUTES)
OPERATIONS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPERATIONS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.OPERATIONS)
RECEPTIONS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) RECEPTIONS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.RECEPTIONS)
PARAMETERS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PARAMETERS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PARAMETERS)
INNER_ELEMENTS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INNER_ELEMENTS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INNER_ELEMENTS)
RELATIONS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) RELATIONS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.RELATIONS)
CONNECTORS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONNECTORS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONNECTORS)
COMMENT
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) COMMENT
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.COMMENT)
ENUMERATION_LITERALS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ENUMERATION_LITERALS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ENUMERATION_LITERALS)
CONSTRAINTS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONSTRAINTS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONSTRAINTS)
TAGS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TAGS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.TAGS)
PORTS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PORTS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PORTS)
ASSOCIATION_ENDS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ASSOCIATION_ENDS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ASSOCIATION_ENDS)
PROVIDED_REQUIRED_INTERFACES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PROVIDED_REQUIRED_INTERFACES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PROVIDED_REQUIRED_INTERFACES)
TEMPLATE_PARAMETERS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_PARAMETERS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.TEMPLATE_PARAMETERS)
QUALIFIERS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) QUALIFIERS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.QUALIFIERS)
EXTENSION_POINTS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) EXTENSION_POINTS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.EXTENSION_POINTS)
CONVEYED_INFORMATION
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONVEYED_INFORMATION
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONVEYED_INFORMATION)
INFORMATION_FLOWS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INFORMATION_FLOWS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INFORMATION_FLOWS)
SLOTS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) SLOTS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.SLOTS)
TEMPLATE_PARAMETER_SUBSTITUTIONS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) TEMPLATE_PARAMETER_SUBSTITUTIONS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.TEMPLATE_PARAMETER_SUBSTITUTIONS)
VARIABLES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) VARIABLES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.VARIABLES)
CLAUSES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CLAUSES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CLAUSES)
BEHAVIORS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) BEHAVIORS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.BEHAVIORS)
ACTORS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ACTORS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ACTORS)
PINS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) PINS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PINS)
CONFIGURATIONS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONFIGURATIONS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONFIGURATIONS)
DEPLOYED_ARTIFACTS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) DEPLOYED_ARTIFACTS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.DEPLOYED_ARTIFACTS)
REALIZING_CLASSIFIERS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) REALIZING_CLASSIFIERS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.REALIZING_CLASSIFIERS)
MANIFESTATIONS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) MANIFESTATIONS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.MANIFESTATIONS)
NESTED_NODES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) NESTED_NODES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.NESTED_NODES)
LANGUAGE_PROPERTIES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) LANGUAGE_PROPERTIES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.LANGUAGE_PROPERTIES)
MESSAGES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) MESSAGES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.MESSAGES)
ARGUMENTS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ARGUMENTS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ARGUMENTS)
USE_CASE_SCENARIO
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) USE_CASE_SCENARIO
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.USE_CASE_SCENARIO)
FORMAL_GATES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) FORMAL_GATES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.FORMAL_GATES)
ACTUAL_GATES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ACTUAL_GATES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ACTUAL_GATES)
OPERANDS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPERANDS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.OPERANDS)
INNER_STATES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INNER_STATES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INNER_STATES)
INTERNAL_TRANSITIONS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INTERNAL_TRANSITIONS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INTERNAL_TRANSITIONS)
ROLE_BINDINGS
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ROLE_BINDINGS
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ROLE_BINDINGS)
USED_IN
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) USED_IN
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.USED_IN)
INSTANCES
static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) INSTANCES
See Also:
[Constant Field Values](../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INSTANCES)
 ============ METHOD DETAIL ========== 
Method Details
getID
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getID()
Returns ID of the node.
Returns:
node id.
getChild
@CheckForNull[IConfigurableNode](IConfigurableNode.html) getChild([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Returns child node according given child id.
Parameters:
`id` - child node id.
Returns:
child node.
addNode
void addNode([IConfigurableNode](IConfigurableNode.html) node)
Adds given node as child node.
Parameters:
`node` - child node.
insertNode
void insertNode([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [IConfigurableNode.Position](IConfigurableNode.Position.html) position,
 [IConfigurableNode](IConfigurableNode.html) node)
Inserts given node as child node near given child node id.
Parameters:
`id` - id of the child node to add near.
`position` - position to add ([`IConfigurableNode.Position.BEFORE`](IConfigurableNode.Position.html#BEFORE), [`IConfigurableNode.Position.AFTER`](IConfigurableNode.Position.html#AFTER)).
`node` - child node.
removeNode
void removeNode([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Removes child node with given id.
Parameters:
`id` - child node id.
getAllChildrenNodeIDS
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getAllChildrenNodeIDS()
Returns all children node IDs.
Returns:
children nodes ids

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.specifications.tree.node</a></div>
<h1 class="title" title="Interface IConfigurableNode">Interface IConfigurableNode</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IConfigurableNode</span></div>
<div class="block">The interface of configurable specification tree node - is used for tree configuration.
 <p>Also defines standard specification tree nodes IDs.
 <p><em>Create this node with <a href="ConfigurableNodeFactory.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node"><code>ConfigurableNodeFactory</code></a></em></p></p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="ConfigurableNodeFactory.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node"><code>ConfigurableNodeFactory</code></a></li>
<li><a href="ISpecificationNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node"><code>ISpecificationNode</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="IConfigurableNode.Position.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode.Position</a></code></div>
<div class="col-last even-row-color">
<div class="block">Position to insert child node</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTORS">ACTORS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ACTUAL_GATES">ACTUAL_GATES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ARGUMENTS">ARGUMENTS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASSOCIATION_ENDS">ASSOCIATION_ENDS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ATTRIBUTES">ATTRIBUTES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BEHAVIORS">BEHAVIORS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CLAUSES">CLAUSES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMMENT">COMMENT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONFIGURATIONS">CONFIGURATIONS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONNECTORS">CONNECTORS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONSTRAINTS">CONSTRAINTS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONVEYED_INFORMATION">CONVEYED_INFORMATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPLOYED_ARTIFACTS">DEPLOYED_ARTIFACTS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOCUMENTATION_HYPERLINKS">DOCUMENTATION_HYPERLINKS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENUMERATION_LITERALS">ENUMERATION_LITERALS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXTENSION_POINTS">EXTENSION_POINTS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FORMAL_GATES">FORMAL_GATES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INFORMATION_FLOWS">INFORMATION_FLOWS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INNER_ELEMENTS">INNER_ELEMENTS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INNER_STATES">INNER_STATES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INSTANCES">INSTANCES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INTERNAL_TRANSITIONS">INTERNAL_TRANSITIONS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LANGUAGE_PROPERTIES">LANGUAGE_PROPERTIES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MANAGE_NAVIGATION">MANAGE_NAVIGATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MANIFESTATIONS">MANIFESTATIONS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MESSAGES">MESSAGES</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NESTED_NODES">NESTED_NODES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OPERANDS">OPERANDS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPERATIONS">OPERATIONS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PARAMETERS">PARAMETERS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PINS">PINS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PORTS">PORTS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROVIDED_REQUIRED_INTERFACES">PROVIDED_REQUIRED_INTERFACES</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#QUALIFIERS">QUALIFIERS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REALIZING_CLASSIFIERS">REALIZING_CLASSIFIERS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RECEPTIONS">RECEPTIONS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RELATIONS">RELATIONS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ROLE_BINDINGS">ROLE_BINDINGS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SLOTS">SLOTS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TAGS">TAGS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEMPLATE_PARAMETER_SUBSTITUTIONS">TEMPLATE_PARAMETER_SUBSTITUTIONS</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TEMPLATE_PARAMETERS">TEMPLATE_PARAMETERS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USAGE">USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USE_CASE_SCENARIO">USE_CASE_SCENARIO</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USED_IN">USED_IN</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VARIABLES">VARIABLES</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addNode(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode)">addNode</a><wbr/>(<a href="IConfigurableNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode</a> node)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds given node as child node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAllChildrenNodeIDS()">getAllChildrenNodeIDS</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns all children node IDs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="IConfigurableNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChild(java.lang.String)">getChild</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns child node according given child id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns ID of the node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#insertNode(java.lang.String,com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.Position,com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode)">insertNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="IConfigurableNode.Position.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode.Position</a> position,
 <a href="IConfigurableNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode</a> node)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Inserts given node as child node near given child node id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeNode(java.lang.String)">removeNode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes child node with given id.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="DOCUMENTATION_HYPERLINKS">
<h3>DOCUMENTATION_HYPERLINKS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DOCUMENTATION_HYPERLINKS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.DOCUMENTATION_HYPERLINKS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MANAGE_NAVIGATION">
<h3>MANAGE_NAVIGATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MANAGE_NAVIGATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.MANAGE_NAVIGATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USAGE">
<h3>USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ATTRIBUTES">
<h3>ATTRIBUTES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ATTRIBUTES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ATTRIBUTES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPERATIONS">
<h3>OPERATIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPERATIONS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.OPERATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RECEPTIONS">
<h3>RECEPTIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RECEPTIONS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.RECEPTIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PARAMETERS">
<h3>PARAMETERS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PARAMETERS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PARAMETERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INNER_ELEMENTS">
<h3>INNER_ELEMENTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INNER_ELEMENTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INNER_ELEMENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONS">
<h3>RELATIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">RELATIONS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.RELATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONNECTORS">
<h3>CONNECTORS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONNECTORS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONNECTORS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMMENT">
<h3>COMMENT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMMENT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.COMMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENUMERATION_LITERALS">
<h3>ENUMERATION_LITERALS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENUMERATION_LITERALS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ENUMERATION_LITERALS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONSTRAINTS">
<h3>CONSTRAINTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONSTRAINTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONSTRAINTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TAGS">
<h3>TAGS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TAGS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.TAGS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PORTS">
<h3>PORTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PORTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PORTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSOCIATION_ENDS">
<h3>ASSOCIATION_ENDS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ASSOCIATION_ENDS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ASSOCIATION_ENDS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROVIDED_REQUIRED_INTERFACES">
<h3>PROVIDED_REQUIRED_INTERFACES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROVIDED_REQUIRED_INTERFACES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PROVIDED_REQUIRED_INTERFACES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_PARAMETERS">
<h3>TEMPLATE_PARAMETERS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_PARAMETERS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.TEMPLATE_PARAMETERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="QUALIFIERS">
<h3>QUALIFIERS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">QUALIFIERS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.QUALIFIERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTENSION_POINTS">
<h3>EXTENSION_POINTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTENSION_POINTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.EXTENSION_POINTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONVEYED_INFORMATION">
<h3>CONVEYED_INFORMATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONVEYED_INFORMATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONVEYED_INFORMATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INFORMATION_FLOWS">
<h3>INFORMATION_FLOWS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INFORMATION_FLOWS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INFORMATION_FLOWS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SLOTS">
<h3>SLOTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SLOTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.SLOTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEMPLATE_PARAMETER_SUBSTITUTIONS">
<h3>TEMPLATE_PARAMETER_SUBSTITUTIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TEMPLATE_PARAMETER_SUBSTITUTIONS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.TEMPLATE_PARAMETER_SUBSTITUTIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VARIABLES">
<h3>VARIABLES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VARIABLES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.VARIABLES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLAUSES">
<h3>CLAUSES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CLAUSES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CLAUSES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BEHAVIORS">
<h3>BEHAVIORS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BEHAVIORS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.BEHAVIORS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTORS">
<h3>ACTORS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTORS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ACTORS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PINS">
<h3>PINS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PINS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.PINS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONFIGURATIONS">
<h3>CONFIGURATIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONFIGURATIONS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.CONFIGURATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPLOYED_ARTIFACTS">
<h3>DEPLOYED_ARTIFACTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEPLOYED_ARTIFACTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.DEPLOYED_ARTIFACTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REALIZING_CLASSIFIERS">
<h3>REALIZING_CLASSIFIERS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REALIZING_CLASSIFIERS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.REALIZING_CLASSIFIERS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MANIFESTATIONS">
<h3>MANIFESTATIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MANIFESTATIONS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.MANIFESTATIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NESTED_NODES">
<h3>NESTED_NODES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NESTED_NODES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.NESTED_NODES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LANGUAGE_PROPERTIES">
<h3>LANGUAGE_PROPERTIES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LANGUAGE_PROPERTIES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.LANGUAGE_PROPERTIES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MESSAGES">
<h3>MESSAGES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MESSAGES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.MESSAGES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ARGUMENTS">
<h3>ARGUMENTS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ARGUMENTS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ARGUMENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USE_CASE_SCENARIO">
<h3>USE_CASE_SCENARIO</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">USE_CASE_SCENARIO</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.USE_CASE_SCENARIO">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FORMAL_GATES">
<h3>FORMAL_GATES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FORMAL_GATES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.FORMAL_GATES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTUAL_GATES">
<h3>ACTUAL_GATES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTUAL_GATES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ACTUAL_GATES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPERANDS">
<h3>OPERANDS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPERANDS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.OPERANDS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INNER_STATES">
<h3>INNER_STATES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INNER_STATES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INNER_STATES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INTERNAL_TRANSITIONS">
<h3>INTERNAL_TRANSITIONS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INTERNAL_TRANSITIONS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INTERNAL_TRANSITIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROLE_BINDINGS">
<h3>ROLE_BINDINGS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROLE_BINDINGS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.ROLE_BINDINGS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USED_IN">
<h3>USED_IN</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">USED_IN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.USED_IN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INSTANCES">
<h3>INSTANCES</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INSTANCES</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../../../../constant-values.html#com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.INSTANCES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns ID of the node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>node id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChild(java.lang.String)">
<h3>getChild</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="IConfigurableNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode</a></span> <span class="element-name">getChild</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Returns child node according given child id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - child node id.</dd>
<dt>Returns:</dt>
<dd>child node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addNode(com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode)">
<h3>addNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addNode</span><wbr/><span class="parameters">(<a href="IConfigurableNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode</a> node)</span></div>
<div class="block">Adds given node as child node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>node</code> - child node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertNode(java.lang.String,com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode.Position,com.nomagic.magicdraw.ui.dialogs.specifications.tree.node.IConfigurableNode)">
<h3>insertNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">insertNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="IConfigurableNode.Position.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode.Position</a> position,
 <a href="IConfigurableNode.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.tree.node">IConfigurableNode</a> node)</span></div>
<div class="block">Inserts given node as child node near given child node id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - id of the child node to add near.</dd>
<dd><code>position</code> - position to add (<a href="IConfigurableNode.Position.html#BEFORE"><code>IConfigurableNode.Position.BEFORE</code></a>, <a href="IConfigurableNode.Position.html#AFTER"><code>IConfigurableNode.Position.AFTER</code></a>).</dd>
<dd><code>node</code> - child node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeNode(java.lang.String)">
<h3>removeNode</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeNode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Removes child node with given id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - child node id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllChildrenNodeIDS()">
<h3>getAllChildrenNodeIDS</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllChildrenNodeIDS</span>()</div>
<div class="block">Returns all children node IDs.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>children nodes ids</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
