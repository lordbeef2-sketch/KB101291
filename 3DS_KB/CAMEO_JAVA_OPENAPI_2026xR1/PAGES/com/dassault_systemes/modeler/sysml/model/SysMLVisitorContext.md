# JAVA OPENAPI: SysMLVisitorContext (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/SysMLVisitorContext.html
- source_path: `com/dassault_systemes/modeler/sysml/model/SysMLVisitorContext.html`
- source_sha256: `3e85c6d1db48c801af959e24b9610ba7090e01f791d45406283e948ced4d84ba`
- captured_utc: `2026-07-14T16:45:03.137042+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Interface SysMLVisitorContext

All Superinterfaces:
`[KerMLVisitorContext](../../kerml/model/KerMLVisitorContext.html)`

@OpenApiAllpublic interfaceSysMLVisitorContextextends [KerMLVisitorContext](../../kerml/model/KerMLVisitorContext.html)

Interface for SysML visitor context, extending KerMLVisitorContext.
 Provides constants for various SysML elements and overrides the getClassCount method.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[ACCEPT_ACTION_USAGE](#ACCEPT_ACTION_USAGE)`

`static final int`
`[ACTION_DEFINITION](#ACTION_DEFINITION)`

`static final int`
`[ACTION_USAGE](#ACTION_USAGE)`

`static final int`
`[ACTOR_MEMBERSHIP](#ACTOR_MEMBERSHIP)`

`static final int`
`[ALLOCATION_DEFINITION](#ALLOCATION_DEFINITION)`

`static final int`
`[ALLOCATION_USAGE](#ALLOCATION_USAGE)`

`static final int`
`[ANALYSIS_CASE_DEFINITION](#ANALYSIS_CASE_DEFINITION)`

`static final int`
`[ANALYSIS_CASE_USAGE](#ANALYSIS_CASE_USAGE)`

`static final int`
`[ASSERT_CONSTRAINT_USAGE](#ASSERT_CONSTRAINT_USAGE)`

`static final int`
`[ASSIGNMENT_ACTION_USAGE](#ASSIGNMENT_ACTION_USAGE)`

`static final int`
`[ATTRIBUTE_DEFINITION](#ATTRIBUTE_DEFINITION)`

`static final int`
`[ATTRIBUTE_USAGE](#ATTRIBUTE_USAGE)`

`static final int`
`[BINDING_CONNECTOR_AS_USAGE](#BINDING_CONNECTOR_AS_USAGE)`

`static final int`
`[CALCULATION_DEFINITION](#CALCULATION_DEFINITION)`

`static final int`
`[CALCULATION_USAGE](#CALCULATION_USAGE)`

`static final int`
`[CASE_DEFINITION](#CASE_DEFINITION)`

`static final int`
`[CASE_USAGE](#CASE_USAGE)`

`static final int`
`[CONCERN_DEFINITION](#CONCERN_DEFINITION)`

`static final int`
`[CONCERN_USAGE](#CONCERN_USAGE)`

`static final int`
`[CONJUGATED_PORT_DEFINITION](#CONJUGATED_PORT_DEFINITION)`

`static final int`
`[CONJUGATED_PORT_TYPING](#CONJUGATED_PORT_TYPING)`

`static final int`
`[CONNECTION_DEFINITION](#CONNECTION_DEFINITION)`

`static final int`
`[CONNECTION_USAGE](#CONNECTION_USAGE)`

`static final int`
`[CONNECTOR_AS_USAGE](#CONNECTOR_AS_USAGE)`

`static final int`
`[CONSTRAINT_DEFINITION](#CONSTRAINT_DEFINITION)`

`static final int`
`[CONSTRAINT_USAGE](#CONSTRAINT_USAGE)`

`static final int`
`[CONTROL_NODE](#CONTROL_NODE)`

`static final int`
`[DECISION_NODE](#DECISION_NODE)`

`static final int`
`[DEFINITION](#DEFINITION)`

`static final int`
`[ENUMERATION_DEFINITION](#ENUMERATION_DEFINITION)`

`static final int`
`[ENUMERATION_USAGE](#ENUMERATION_USAGE)`

`static final int`
`[EVENT_OCCURRENCE_USAGE](#EVENT_OCCURRENCE_USAGE)`

`static final int`
`[EXHIBIT_STATE_USAGE](#EXHIBIT_STATE_USAGE)`

`static final int`
`[EXPOSE](#EXPOSE)`

`static final int`
`[FLOW_DEFINITION](#FLOW_DEFINITION)`

`static final int`
`[FLOW_USAGE](#FLOW_USAGE)`

`static final int`
`[FOR_LOOP_ACTION_USAGE](#FOR_LOOP_ACTION_USAGE)`

`static final int`
`[FORK_NODE](#FORK_NODE)`

`static final int`
`[FRAMED_CONCERN_MEMBERSHIP](#FRAMED_CONCERN_MEMBERSHIP)`

`static final int`
`[IF_ACTION_USAGE](#IF_ACTION_USAGE)`

`static final int`
`[INCLUDE_USE_CASE_USAGE](#INCLUDE_USE_CASE_USAGE)`

`static final int`
`[INTERFACE_DEFINITION](#INTERFACE_DEFINITION)`

`static final int`
`[INTERFACE_USAGE](#INTERFACE_USAGE)`

`static final int`
`[ITEM_DEFINITION](#ITEM_DEFINITION)`

`static final int`
`[ITEM_USAGE](#ITEM_USAGE)`

`static final int`
`[JOIN_NODE](#JOIN_NODE)`

`static final int`
`[LOOP_ACTION_USAGE](#LOOP_ACTION_USAGE)`

`static final int`
`[MEMBERSHIP_EXPOSE](#MEMBERSHIP_EXPOSE)`

`static final int`
`[MERGE_NODE](#MERGE_NODE)`

`static final int`
`[METADATA_DEFINITION](#METADATA_DEFINITION)`

`static final int`
`[METADATA_USAGE](#METADATA_USAGE)`

`static final int`
`[NAMESPACE_EXPOSE](#NAMESPACE_EXPOSE)`

`static final int`
`[OBJECTIVE_MEMBERSHIP](#OBJECTIVE_MEMBERSHIP)`

`static final int`
`[OCCURRENCE_DEFINITION](#OCCURRENCE_DEFINITION)`

`static final int`
`[OCCURRENCE_USAGE](#OCCURRENCE_USAGE)`

`static final int`
`[PART_DEFINITION](#PART_DEFINITION)`

`static final int`
`[PART_USAGE](#PART_USAGE)`

`static final int`
`[PERFORM_ACTION_USAGE](#PERFORM_ACTION_USAGE)`

`static final int`
`[PORT_CONJUGATION](#PORT_CONJUGATION)`

`static final int`
`[PORT_DEFINITION](#PORT_DEFINITION)`

`static final int`
`[PORT_USAGE](#PORT_USAGE)`

`static final int`
`[REFERENCE_USAGE](#REFERENCE_USAGE)`

`static final int`
`[RENDERING_DEFINITION](#RENDERING_DEFINITION)`

`static final int`
`[RENDERING_USAGE](#RENDERING_USAGE)`

`static final int`
`[REQUIREMENT_CONSTRAINT_MEMBERSHIP](#REQUIREMENT_CONSTRAINT_MEMBERSHIP)`

`static final int`
`[REQUIREMENT_DEFINITION](#REQUIREMENT_DEFINITION)`

`static final int`
`[REQUIREMENT_USAGE](#REQUIREMENT_USAGE)`

`static final int`
`[REQUIREMENT_VERIFICATION_MEMBERSHIP](#REQUIREMENT_VERIFICATION_MEMBERSHIP)`

`static final int`
`[SATISFY_REQUIREMENT_USAGE](#SATISFY_REQUIREMENT_USAGE)`

`static final int`
`[SEND_ACTION_USAGE](#SEND_ACTION_USAGE)`

`static final int`
`[STAKEHOLDER_MEMBERSHIP](#STAKEHOLDER_MEMBERSHIP)`

`static final int`
`[STATE_DEFINITION](#STATE_DEFINITION)`

`static final int`
`[STATE_SUBACTION_MEMBERSHIP](#STATE_SUBACTION_MEMBERSHIP)`

`static final int`
`[STATE_USAGE](#STATE_USAGE)`

`static final int`
`[SUBJECT_MEMBERSHIP](#SUBJECT_MEMBERSHIP)`

`static final int`
`[SUCCESSION_AS_USAGE](#SUCCESSION_AS_USAGE)`

`static final int`
`[SUCCESSION_FLOW_USAGE](#SUCCESSION_FLOW_USAGE)`

`static final int`
`[TERMINATE_ACTION_USAGE](#TERMINATE_ACTION_USAGE)`

`static final int`
`[TRANSITION_FEATURE_MEMBERSHIP](#TRANSITION_FEATURE_MEMBERSHIP)`

`static final int`
`[TRANSITION_USAGE](#TRANSITION_USAGE)`

`static final int`
`[TRIGGER_INVOCATION_EXPRESSION](#TRIGGER_INVOCATION_EXPRESSION)`

`static final int`
`[USAGE](#USAGE)`

`static final int`
`[USE_CASE_DEFINITION](#USE_CASE_DEFINITION)`

`static final int`
`[USE_CASE_USAGE](#USE_CASE_USAGE)`

`static final int`
`[VARIANT_MEMBERSHIP](#VARIANT_MEMBERSHIP)`

`static final int`
`[VERIFICATION_CASE_DEFINITION](#VERIFICATION_CASE_DEFINITION)`

`static final int`
`[VERIFICATION_CASE_USAGE](#VERIFICATION_CASE_USAGE)`

`static final int`
`[VIEW_DEFINITION](#VIEW_DEFINITION)`

`static final int`
`[VIEW_RENDERING_MEMBERSHIP](#VIEW_RENDERING_MEMBERSHIP)`

`static final int`
`[VIEW_USAGE](#VIEW_USAGE)`

`static final int`
`[VIEWPOINT_DEFINITION](#VIEWPOINT_DEFINITION)`

`static final int`
`[VIEWPOINT_USAGE](#VIEWPOINT_USAGE)`

`static final int`
`[WHILE_LOOP_ACTION_USAGE](#WHILE_LOOP_ACTION_USAGE)`
Fields inherited from interface com.dassault_systemes.modeler.kerml.model.[KerMLVisitorContext](../../kerml/model/KerMLVisitorContext.html)
`[ANNOTATING_ELEMENT](../../kerml/model/KerMLVisitorContext.html#ANNOTATING_ELEMENT), [ANNOTATION](../../kerml/model/KerMLVisitorContext.html#ANNOTATION), [ASSOCIATION](../../kerml/model/KerMLVisitorContext.html#ASSOCIATION), [ASSOCIATION_STRUCTURE](../../kerml/model/KerMLVisitorContext.html#ASSOCIATION_STRUCTURE), [BEHAVIOR](../../kerml/model/KerMLVisitorContext.html#BEHAVIOR), [BINDING_CONNECTOR](../../kerml/model/KerMLVisitorContext.html#BINDING_CONNECTOR), [BOOLEAN_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#BOOLEAN_EXPRESSION), [CLASS](../../kerml/model/KerMLVisitorContext.html#CLASS), [CLASSIFIER](../../kerml/model/KerMLVisitorContext.html#CLASSIFIER), [COLLECT_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#COLLECT_EXPRESSION), [COMMENT](../../kerml/model/KerMLVisitorContext.html#COMMENT), [CONJUGATION](../../kerml/model/KerMLVisitorContext.html#CONJUGATION), [CONNECTOR](../../kerml/model/KerMLVisitorContext.html#CONNECTOR), [CONSTRUCTOR_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#CONSTRUCTOR_EXPRESSION), [CROSS_SUBSETTING](../../kerml/model/KerMLVisitorContext.html#CROSS_SUBSETTING), [DATA_TYPE](../../kerml/model/KerMLVisitorContext.html#DATA_TYPE), [DEPENDENCY](../../kerml/model/KerMLVisitorContext.html#DEPENDENCY), [DIFFERENCING](../../kerml/model/KerMLVisitorContext.html#DIFFERENCING), [DISJOINING](../../kerml/model/KerMLVisitorContext.html#DISJOINING), [DOCUMENTATION](../../kerml/model/KerMLVisitorContext.html#DOCUMENTATION), [ELEMENT](../../kerml/model/KerMLVisitorContext.html#ELEMENT), [ELEMENT_FILTER_MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#ELEMENT_FILTER_MEMBERSHIP), [END_FEATURE_MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#END_FEATURE_MEMBERSHIP), [EXPRESSION](../../kerml/model/KerMLVisitorContext.html#EXPRESSION), [FEATURE](../../kerml/model/KerMLVisitorContext.html#FEATURE), [FEATURE_CHAIN_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#FEATURE_CHAIN_EXPRESSION), [FEATURE_CHAINING](../../kerml/model/KerMLVisitorContext.html#FEATURE_CHAINING), [FEATURE_INVERTING](../../kerml/model/KerMLVisitorContext.html#FEATURE_INVERTING), [FEATURE_MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#FEATURE_MEMBERSHIP), [FEATURE_REFERENCE_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#FEATURE_REFERENCE_EXPRESSION), [FEATURE_TYPING](../../kerml/model/KerMLVisitorContext.html#FEATURE_TYPING), [FEATURE_VALUE](../../kerml/model/KerMLVisitorContext.html#FEATURE_VALUE), [FLOW](../../kerml/model/KerMLVisitorContext.html#FLOW), [FLOW_END](../../kerml/model/KerMLVisitorContext.html#FLOW_END), [FUNCTION](../../kerml/model/KerMLVisitorContext.html#FUNCTION), [IMPORT](../../kerml/model/KerMLVisitorContext.html#IMPORT), [INDEX_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#INDEX_EXPRESSION), [INSTANTIATION_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#INSTANTIATION_EXPRESSION), [INTERACTION](../../kerml/model/KerMLVisitorContext.html#INTERACTION), [INTERSECTING](../../kerml/model/KerMLVisitorContext.html#INTERSECTING), [INVARIANT](../../kerml/model/KerMLVisitorContext.html#INVARIANT), [INVOCATION_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#INVOCATION_EXPRESSION), [LIBRARY_PACKAGE](../../kerml/model/KerMLVisitorContext.html#LIBRARY_PACKAGE), [LITERAL_BOOLEAN](../../kerml/model/KerMLVisitorContext.html#LITERAL_BOOLEAN), [LITERAL_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#LITERAL_EXPRESSION), [LITERAL_INFINITY](../../kerml/model/KerMLVisitorContext.html#LITERAL_INFINITY), [LITERAL_INTEGER](../../kerml/model/KerMLVisitorContext.html#LITERAL_INTEGER), [LITERAL_RATIONAL](../../kerml/model/KerMLVisitorContext.html#LITERAL_RATIONAL), [LITERAL_STRING](../../kerml/model/KerMLVisitorContext.html#LITERAL_STRING), [MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#MEMBERSHIP), [MEMBERSHIP_IMPORT](../../kerml/model/KerMLVisitorContext.html#MEMBERSHIP_IMPORT), [METACLASS](../../kerml/model/KerMLVisitorContext.html#METACLASS), [METADATA_ACCESS_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#METADATA_ACCESS_EXPRESSION), [METADATA_FEATURE](../../kerml/model/KerMLVisitorContext.html#METADATA_FEATURE), [MULTIPLICITY](../../kerml/model/KerMLVisitorContext.html#MULTIPLICITY), [MULTIPLICITY_RANGE](../../kerml/model/KerMLVisitorContext.html#MULTIPLICITY_RANGE), [NAMESPACE](../../kerml/model/KerMLVisitorContext.html#NAMESPACE), [NAMESPACE_IMPORT](../../kerml/model/KerMLVisitorContext.html#NAMESPACE_IMPORT), [NULL_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#NULL_EXPRESSION), [OPERATOR_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#OPERATOR_EXPRESSION), [OWNING_MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#OWNING_MEMBERSHIP), [PACKAGE](../../kerml/model/KerMLVisitorContext.html#PACKAGE), [PARAMETER_MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#PARAMETER_MEMBERSHIP), [PAYLOAD_FEATURE](../../kerml/model/KerMLVisitorContext.html#PAYLOAD_FEATURE), [PREDICATE](../../kerml/model/KerMLVisitorContext.html#PREDICATE), [REDEFINITION](../../kerml/model/KerMLVisitorContext.html#REDEFINITION), [REFERENCE_SUBSETTING](../../kerml/model/KerMLVisitorContext.html#REFERENCE_SUBSETTING), [RELATIONSHIP](../../kerml/model/KerMLVisitorContext.html#RELATIONSHIP), [RESULT_EXPRESSION_MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#RESULT_EXPRESSION_MEMBERSHIP), [RETURN_PARAMETER_MEMBERSHIP](../../kerml/model/KerMLVisitorContext.html#RETURN_PARAMETER_MEMBERSHIP), [SELECT_EXPRESSION](../../kerml/model/KerMLVisitorContext.html#SELECT_EXPRESSION), [SPECIALIZATION](../../kerml/model/KerMLVisitorContext.html#SPECIALIZATION), [STEP](../../kerml/model/KerMLVisitorContext.html#STEP), [STRUCTURE](../../kerml/model/KerMLVisitorContext.html#STRUCTURE), [SUBCLASSIFICATION](../../kerml/model/KerMLVisitorContext.html#SUBCLASSIFICATION), [SUBSETTING](../../kerml/model/KerMLVisitorContext.html#SUBSETTING), [SUCCESSION](../../kerml/model/KerMLVisitorContext.html#SUCCESSION), [SUCCESSION_FLOW](../../kerml/model/KerMLVisitorContext.html#SUCCESSION_FLOW), [TEXTUAL_REPRESENTATION](../../kerml/model/KerMLVisitorContext.html#TEXTUAL_REPRESENTATION), [TYPE](../../kerml/model/KerMLVisitorContext.html#TYPE), [TYPE_FEATURING](../../kerml/model/KerMLVisitorContext.html#TYPE_FEATURING), [UNIONING](../../kerml/model/KerMLVisitorContext.html#UNIONING)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsDefault Methods
Modifier and Type
Method
Description
`default int`
`[getClassCount](#getClassCount())()`
Returns the count of classes in the SysML visitor context.
Methods inherited from interface com.dassault_systemes.modeler.kerml.model.[KerMLVisitorContext](../../kerml/model/KerMLVisitorContext.html)
`[addToVisited](../../kerml/model/KerMLVisitorContext.html#addToVisited(int)), [isAlreadyVisited](../../kerml/model/KerMLVisitorContext.html#isAlreadyVisited(int))`

============ FIELD DETAIL =========== 
Field Details
ACCEPT_ACTION_USAGE
static final int ACCEPT_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACCEPT_ACTION_USAGE)
ACTION_DEFINITION
static final int ACTION_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACTION_DEFINITION)
ACTION_USAGE
static final int ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACTION_USAGE)
ACTOR_MEMBERSHIP
static final int ACTOR_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACTOR_MEMBERSHIP)
ALLOCATION_DEFINITION
static final int ALLOCATION_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ALLOCATION_DEFINITION)
ALLOCATION_USAGE
static final int ALLOCATION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ALLOCATION_USAGE)
ANALYSIS_CASE_DEFINITION
static final int ANALYSIS_CASE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ANALYSIS_CASE_DEFINITION)
ANALYSIS_CASE_USAGE
static final int ANALYSIS_CASE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ANALYSIS_CASE_USAGE)
ASSERT_CONSTRAINT_USAGE
static final int ASSERT_CONSTRAINT_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ASSERT_CONSTRAINT_USAGE)
ASSIGNMENT_ACTION_USAGE
static final int ASSIGNMENT_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ASSIGNMENT_ACTION_USAGE)
ATTRIBUTE_DEFINITION
static final int ATTRIBUTE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ATTRIBUTE_DEFINITION)
ATTRIBUTE_USAGE
static final int ATTRIBUTE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ATTRIBUTE_USAGE)
BINDING_CONNECTOR_AS_USAGE
static final int BINDING_CONNECTOR_AS_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.BINDING_CONNECTOR_AS_USAGE)
CALCULATION_DEFINITION
static final int CALCULATION_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CALCULATION_DEFINITION)
CALCULATION_USAGE
static final int CALCULATION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CALCULATION_USAGE)
CASE_DEFINITION
static final int CASE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CASE_DEFINITION)
CASE_USAGE
static final int CASE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CASE_USAGE)
CONCERN_DEFINITION
static final int CONCERN_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONCERN_DEFINITION)
CONCERN_USAGE
static final int CONCERN_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONCERN_USAGE)
CONJUGATED_PORT_DEFINITION
static final int CONJUGATED_PORT_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONJUGATED_PORT_DEFINITION)
CONJUGATED_PORT_TYPING
static final int CONJUGATED_PORT_TYPING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONJUGATED_PORT_TYPING)
CONNECTION_DEFINITION
static final int CONNECTION_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONNECTION_DEFINITION)
CONNECTION_USAGE
static final int CONNECTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONNECTION_USAGE)
CONNECTOR_AS_USAGE
static final int CONNECTOR_AS_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONNECTOR_AS_USAGE)
CONSTRAINT_DEFINITION
static final int CONSTRAINT_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONSTRAINT_DEFINITION)
CONSTRAINT_USAGE
static final int CONSTRAINT_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONSTRAINT_USAGE)
CONTROL_NODE
static final int CONTROL_NODE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONTROL_NODE)
DECISION_NODE
static final int DECISION_NODE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.DECISION_NODE)
DEFINITION
static final int DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.DEFINITION)
ENUMERATION_DEFINITION
static final int ENUMERATION_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ENUMERATION_DEFINITION)
ENUMERATION_USAGE
static final int ENUMERATION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ENUMERATION_USAGE)
EVENT_OCCURRENCE_USAGE
static final int EVENT_OCCURRENCE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.EVENT_OCCURRENCE_USAGE)
EXHIBIT_STATE_USAGE
static final int EXHIBIT_STATE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.EXHIBIT_STATE_USAGE)
EXPOSE
static final int EXPOSE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.EXPOSE)
FLOW_DEFINITION
static final int FLOW_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FLOW_DEFINITION)
FLOW_USAGE
static final int FLOW_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FLOW_USAGE)
FOR_LOOP_ACTION_USAGE
static final int FOR_LOOP_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FOR_LOOP_ACTION_USAGE)
FORK_NODE
static final int FORK_NODE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FORK_NODE)
FRAMED_CONCERN_MEMBERSHIP
static final int FRAMED_CONCERN_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FRAMED_CONCERN_MEMBERSHIP)
IF_ACTION_USAGE
static final int IF_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.IF_ACTION_USAGE)
INCLUDE_USE_CASE_USAGE
static final int INCLUDE_USE_CASE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.INCLUDE_USE_CASE_USAGE)
INTERFACE_DEFINITION
static final int INTERFACE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.INTERFACE_DEFINITION)
INTERFACE_USAGE
static final int INTERFACE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.INTERFACE_USAGE)
ITEM_DEFINITION
static final int ITEM_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ITEM_DEFINITION)
ITEM_USAGE
static final int ITEM_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ITEM_USAGE)
JOIN_NODE
static final int JOIN_NODE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.JOIN_NODE)
LOOP_ACTION_USAGE
static final int LOOP_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.LOOP_ACTION_USAGE)
MEMBERSHIP_EXPOSE
static final int MEMBERSHIP_EXPOSE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.MEMBERSHIP_EXPOSE)
MERGE_NODE
static final int MERGE_NODE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.MERGE_NODE)
METADATA_DEFINITION
static final int METADATA_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.METADATA_DEFINITION)
METADATA_USAGE
static final int METADATA_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.METADATA_USAGE)
NAMESPACE_EXPOSE
static final int NAMESPACE_EXPOSE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.NAMESPACE_EXPOSE)
OBJECTIVE_MEMBERSHIP
static final int OBJECTIVE_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.OBJECTIVE_MEMBERSHIP)
OCCURRENCE_DEFINITION
static final int OCCURRENCE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.OCCURRENCE_DEFINITION)
OCCURRENCE_USAGE
static final int OCCURRENCE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.OCCURRENCE_USAGE)
PART_DEFINITION
static final int PART_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PART_DEFINITION)
PART_USAGE
static final int PART_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PART_USAGE)
PERFORM_ACTION_USAGE
static final int PERFORM_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PERFORM_ACTION_USAGE)
PORT_CONJUGATION
static final int PORT_CONJUGATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PORT_CONJUGATION)
PORT_DEFINITION
static final int PORT_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PORT_DEFINITION)
PORT_USAGE
static final int PORT_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PORT_USAGE)
REFERENCE_USAGE
static final int REFERENCE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REFERENCE_USAGE)
RENDERING_DEFINITION
static final int RENDERING_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.RENDERING_DEFINITION)
RENDERING_USAGE
static final int RENDERING_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.RENDERING_USAGE)
REQUIREMENT_CONSTRAINT_MEMBERSHIP
static final int REQUIREMENT_CONSTRAINT_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_CONSTRAINT_MEMBERSHIP)
REQUIREMENT_DEFINITION
static final int REQUIREMENT_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_DEFINITION)
REQUIREMENT_USAGE
static final int REQUIREMENT_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_USAGE)
REQUIREMENT_VERIFICATION_MEMBERSHIP
static final int REQUIREMENT_VERIFICATION_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_VERIFICATION_MEMBERSHIP)
SATISFY_REQUIREMENT_USAGE
static final int SATISFY_REQUIREMENT_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SATISFY_REQUIREMENT_USAGE)
SEND_ACTION_USAGE
static final int SEND_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SEND_ACTION_USAGE)
STAKEHOLDER_MEMBERSHIP
static final int STAKEHOLDER_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STAKEHOLDER_MEMBERSHIP)
STATE_DEFINITION
static final int STATE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STATE_DEFINITION)
STATE_SUBACTION_MEMBERSHIP
static final int STATE_SUBACTION_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STATE_SUBACTION_MEMBERSHIP)
STATE_USAGE
static final int STATE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STATE_USAGE)
SUBJECT_MEMBERSHIP
static final int SUBJECT_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SUBJECT_MEMBERSHIP)
SUCCESSION_AS_USAGE
static final int SUCCESSION_AS_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SUCCESSION_AS_USAGE)
SUCCESSION_FLOW_USAGE
static final int SUCCESSION_FLOW_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SUCCESSION_FLOW_USAGE)
TERMINATE_ACTION_USAGE
static final int TERMINATE_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TERMINATE_ACTION_USAGE)
TRANSITION_FEATURE_MEMBERSHIP
static final int TRANSITION_FEATURE_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TRANSITION_FEATURE_MEMBERSHIP)
TRANSITION_USAGE
static final int TRANSITION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TRANSITION_USAGE)
TRIGGER_INVOCATION_EXPRESSION
static final int TRIGGER_INVOCATION_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TRIGGER_INVOCATION_EXPRESSION)
USAGE
static final int USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.USAGE)
USE_CASE_DEFINITION
static final int USE_CASE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.USE_CASE_DEFINITION)
USE_CASE_USAGE
static final int USE_CASE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.USE_CASE_USAGE)
VARIANT_MEMBERSHIP
static final int VARIANT_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VARIANT_MEMBERSHIP)
VERIFICATION_CASE_DEFINITION
static final int VERIFICATION_CASE_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VERIFICATION_CASE_DEFINITION)
VERIFICATION_CASE_USAGE
static final int VERIFICATION_CASE_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VERIFICATION_CASE_USAGE)
VIEW_DEFINITION
static final int VIEW_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEW_DEFINITION)
VIEW_RENDERING_MEMBERSHIP
static final int VIEW_RENDERING_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEW_RENDERING_MEMBERSHIP)
VIEW_USAGE
static final int VIEW_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEW_USAGE)
VIEWPOINT_DEFINITION
static final int VIEWPOINT_DEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEWPOINT_DEFINITION)
VIEWPOINT_USAGE
static final int VIEWPOINT_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEWPOINT_USAGE)
WHILE_LOOP_ACTION_USAGE
static final int WHILE_LOOP_ACTION_USAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.WHILE_LOOP_ACTION_USAGE)
 ============ METHOD DETAIL ========== 
Method Details
getClassCount
default int getClassCount()
Returns the count of classes in the SysML visitor context.
Specified by:
`[getClassCount](../../kerml/model/KerMLVisitorContext.html#getClassCount())` in interface `[KerMLVisitorContext](../../kerml/model/KerMLVisitorContext.html)`
Returns:
the count of classes, which is the sum of the super class count and 93.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Interface SysMLVisitorContext">Interface SysMLVisitorContext</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../kerml/model/KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SysMLVisitorContext</span><span class="extends-implements">
extends <a href="../../kerml/model/KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a></span></div>
<div class="block">Interface for SysML visitor context, extending KerMLVisitorContext.
 Provides constants for various SysML elements and overrides the getClassCount method.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACCEPT_ACTION_USAGE">ACCEPT_ACTION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ACTION_DEFINITION">ACTION_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTION_USAGE">ACTION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ACTOR_MEMBERSHIP">ACTOR_MEMBERSHIP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ALLOCATION_DEFINITION">ALLOCATION_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ALLOCATION_USAGE">ALLOCATION_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANALYSIS_CASE_DEFINITION">ANALYSIS_CASE_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANALYSIS_CASE_USAGE">ANALYSIS_CASE_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ASSERT_CONSTRAINT_USAGE">ASSERT_CONSTRAINT_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASSIGNMENT_ACTION_USAGE">ASSIGNMENT_ACTION_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ATTRIBUTE_DEFINITION">ATTRIBUTE_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ATTRIBUTE_USAGE">ATTRIBUTE_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BINDING_CONNECTOR_AS_USAGE">BINDING_CONNECTOR_AS_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CALCULATION_DEFINITION">CALCULATION_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CALCULATION_USAGE">CALCULATION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CASE_DEFINITION">CASE_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CASE_USAGE">CASE_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONCERN_DEFINITION">CONCERN_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONCERN_USAGE">CONCERN_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONJUGATED_PORT_DEFINITION">CONJUGATED_PORT_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONJUGATED_PORT_TYPING">CONJUGATED_PORT_TYPING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONNECTION_DEFINITION">CONNECTION_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONNECTION_USAGE">CONNECTION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONNECTOR_AS_USAGE">CONNECTOR_AS_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONSTRAINT_DEFINITION">CONSTRAINT_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONSTRAINT_USAGE">CONSTRAINT_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTROL_NODE">CONTROL_NODE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DECISION_NODE">DECISION_NODE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFINITION">DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENUMERATION_DEFINITION">ENUMERATION_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENUMERATION_USAGE">ENUMERATION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EVENT_OCCURRENCE_USAGE">EVENT_OCCURRENCE_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXHIBIT_STATE_USAGE">EXHIBIT_STATE_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXPOSE">EXPOSE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FLOW_DEFINITION">FLOW_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FLOW_USAGE">FLOW_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FOR_LOOP_ACTION_USAGE">FOR_LOOP_ACTION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FORK_NODE">FORK_NODE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FRAMED_CONCERN_MEMBERSHIP">FRAMED_CONCERN_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IF_ACTION_USAGE">IF_ACTION_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INCLUDE_USE_CASE_USAGE">INCLUDE_USE_CASE_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INTERFACE_DEFINITION">INTERFACE_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INTERFACE_USAGE">INTERFACE_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ITEM_DEFINITION">ITEM_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ITEM_USAGE">ITEM_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#JOIN_NODE">JOIN_NODE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOOP_ACTION_USAGE">LOOP_ACTION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MEMBERSHIP_EXPOSE">MEMBERSHIP_EXPOSE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MERGE_NODE">MERGE_NODE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METADATA_DEFINITION">METADATA_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#METADATA_USAGE">METADATA_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NAMESPACE_EXPOSE">NAMESPACE_EXPOSE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OBJECTIVE_MEMBERSHIP">OBJECTIVE_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OCCURRENCE_DEFINITION">OCCURRENCE_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OCCURRENCE_USAGE">OCCURRENCE_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PART_DEFINITION">PART_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PART_USAGE">PART_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PERFORM_ACTION_USAGE">PERFORM_ACTION_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PORT_CONJUGATION">PORT_CONJUGATION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PORT_DEFINITION">PORT_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PORT_USAGE">PORT_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REFERENCE_USAGE">REFERENCE_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RENDERING_DEFINITION">RENDERING_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RENDERING_USAGE">RENDERING_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REQUIREMENT_CONSTRAINT_MEMBERSHIP">REQUIREMENT_CONSTRAINT_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQUIREMENT_DEFINITION">REQUIREMENT_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REQUIREMENT_USAGE">REQUIREMENT_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQUIREMENT_VERIFICATION_MEMBERSHIP">REQUIREMENT_VERIFICATION_MEMBERSHIP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SATISFY_REQUIREMENT_USAGE">SATISFY_REQUIREMENT_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SEND_ACTION_USAGE">SEND_ACTION_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STAKEHOLDER_MEMBERSHIP">STAKEHOLDER_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STATE_DEFINITION">STATE_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STATE_SUBACTION_MEMBERSHIP">STATE_SUBACTION_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STATE_USAGE">STATE_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUBJECT_MEMBERSHIP">SUBJECT_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SUCCESSION_AS_USAGE">SUCCESSION_AS_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUCCESSION_FLOW_USAGE">SUCCESSION_FLOW_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TERMINATE_ACTION_USAGE">TERMINATE_ACTION_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRANSITION_FEATURE_MEMBERSHIP">TRANSITION_FEATURE_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TRANSITION_USAGE">TRANSITION_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRIGGER_INVOCATION_EXPRESSION">TRIGGER_INVOCATION_EXPRESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USAGE">USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#USE_CASE_DEFINITION">USE_CASE_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#USE_CASE_USAGE">USE_CASE_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VARIANT_MEMBERSHIP">VARIANT_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VERIFICATION_CASE_DEFINITION">VERIFICATION_CASE_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VERIFICATION_CASE_USAGE">VERIFICATION_CASE_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VIEW_DEFINITION">VIEW_DEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VIEW_RENDERING_MEMBERSHIP">VIEW_RENDERING_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VIEW_USAGE">VIEW_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VIEWPOINT_DEFINITION">VIEWPOINT_DEFINITION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VIEWPOINT_USAGE">VIEWPOINT_USAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#WHILE_LOOP_ACTION_USAGE">WHILE_LOOP_ACTION_USAGE</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext">Fields inherited from interface com.dassault_systemes.modeler.kerml.model.<a href="../../kerml/model/KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a></h3>
<code><a href="../../kerml/model/KerMLVisitorContext.html#ANNOTATING_ELEMENT">ANNOTATING_ELEMENT</a>, <a href="../../kerml/model/KerMLVisitorContext.html#ANNOTATION">ANNOTATION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#ASSOCIATION">ASSOCIATION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#ASSOCIATION_STRUCTURE">ASSOCIATION_STRUCTURE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#BEHAVIOR">BEHAVIOR</a>, <a href="../../kerml/model/KerMLVisitorContext.html#BINDING_CONNECTOR">BINDING_CONNECTOR</a>, <a href="../../kerml/model/KerMLVisitorContext.html#BOOLEAN_EXPRESSION">BOOLEAN_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#CLASS">CLASS</a>, <a href="../../kerml/model/KerMLVisitorContext.html#CLASSIFIER">CLASSIFIER</a>, <a href="../../kerml/model/KerMLVisitorContext.html#COLLECT_EXPRESSION">COLLECT_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#COMMENT">COMMENT</a>, <a href="../../kerml/model/KerMLVisitorContext.html#CONJUGATION">CONJUGATION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#CONNECTOR">CONNECTOR</a>, <a href="../../kerml/model/KerMLVisitorContext.html#CONSTRUCTOR_EXPRESSION">CONSTRUCTOR_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#CROSS_SUBSETTING">CROSS_SUBSETTING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#DATA_TYPE">DATA_TYPE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#DEPENDENCY">DEPENDENCY</a>, <a href="../../kerml/model/KerMLVisitorContext.html#DIFFERENCING">DIFFERENCING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#DISJOINING">DISJOINING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#DOCUMENTATION">DOCUMENTATION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#ELEMENT">ELEMENT</a>, <a href="../../kerml/model/KerMLVisitorContext.html#ELEMENT_FILTER_MEMBERSHIP">ELEMENT_FILTER_MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#END_FEATURE_MEMBERSHIP">END_FEATURE_MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#EXPRESSION">EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE">FEATURE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE_CHAIN_EXPRESSION">FEATURE_CHAIN_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE_CHAINING">FEATURE_CHAINING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE_INVERTING">FEATURE_INVERTING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE_MEMBERSHIP">FEATURE_MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE_REFERENCE_EXPRESSION">FEATURE_REFERENCE_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE_TYPING">FEATURE_TYPING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FEATURE_VALUE">FEATURE_VALUE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FLOW">FLOW</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FLOW_END">FLOW_END</a>, <a href="../../kerml/model/KerMLVisitorContext.html#FUNCTION">FUNCTION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#IMPORT">IMPORT</a>, <a href="../../kerml/model/KerMLVisitorContext.html#INDEX_EXPRESSION">INDEX_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#INSTANTIATION_EXPRESSION">INSTANTIATION_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#INTERACTION">INTERACTION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#INTERSECTING">INTERSECTING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#INVARIANT">INVARIANT</a>, <a href="../../kerml/model/KerMLVisitorContext.html#INVOCATION_EXPRESSION">INVOCATION_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#LIBRARY_PACKAGE">LIBRARY_PACKAGE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#LITERAL_BOOLEAN">LITERAL_BOOLEAN</a>, <a href="../../kerml/model/KerMLVisitorContext.html#LITERAL_EXPRESSION">LITERAL_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#LITERAL_INFINITY">LITERAL_INFINITY</a>, <a href="../../kerml/model/KerMLVisitorContext.html#LITERAL_INTEGER">LITERAL_INTEGER</a>, <a href="../../kerml/model/KerMLVisitorContext.html#LITERAL_RATIONAL">LITERAL_RATIONAL</a>, <a href="../../kerml/model/KerMLVisitorContext.html#LITERAL_STRING">LITERAL_STRING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#MEMBERSHIP">MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#MEMBERSHIP_IMPORT">MEMBERSHIP_IMPORT</a>, <a href="../../kerml/model/KerMLVisitorContext.html#METACLASS">METACLASS</a>, <a href="../../kerml/model/KerMLVisitorContext.html#METADATA_ACCESS_EXPRESSION">METADATA_ACCESS_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#METADATA_FEATURE">METADATA_FEATURE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#MULTIPLICITY">MULTIPLICITY</a>, <a href="../../kerml/model/KerMLVisitorContext.html#MULTIPLICITY_RANGE">MULTIPLICITY_RANGE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#NAMESPACE">NAMESPACE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#NAMESPACE_IMPORT">NAMESPACE_IMPORT</a>, <a href="../../kerml/model/KerMLVisitorContext.html#NULL_EXPRESSION">NULL_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#OPERATOR_EXPRESSION">OPERATOR_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#OWNING_MEMBERSHIP">OWNING_MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#PACKAGE">PACKAGE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#PARAMETER_MEMBERSHIP">PARAMETER_MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#PAYLOAD_FEATURE">PAYLOAD_FEATURE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#PREDICATE">PREDICATE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#REDEFINITION">REDEFINITION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#REFERENCE_SUBSETTING">REFERENCE_SUBSETTING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#RELATIONSHIP">RELATIONSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#RESULT_EXPRESSION_MEMBERSHIP">RESULT_EXPRESSION_MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#RETURN_PARAMETER_MEMBERSHIP">RETURN_PARAMETER_MEMBERSHIP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#SELECT_EXPRESSION">SELECT_EXPRESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#SPECIALIZATION">SPECIALIZATION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#STEP">STEP</a>, <a href="../../kerml/model/KerMLVisitorContext.html#STRUCTURE">STRUCTURE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#SUBCLASSIFICATION">SUBCLASSIFICATION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#SUBSETTING">SUBSETTING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#SUCCESSION">SUCCESSION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#SUCCESSION_FLOW">SUCCESSION_FLOW</a>, <a href="../../kerml/model/KerMLVisitorContext.html#TEXTUAL_REPRESENTATION">TEXTUAL_REPRESENTATION</a>, <a href="../../kerml/model/KerMLVisitorContext.html#TYPE">TYPE</a>, <a href="../../kerml/model/KerMLVisitorContext.html#TYPE_FEATURING">TYPE_FEATURING</a>, <a href="../../kerml/model/KerMLVisitorContext.html#UNIONING">UNIONING</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getClassCount()">getClassCount</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Returns the count of classes in the SysML visitor context.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext">Methods inherited from interface com.dassault_systemes.modeler.kerml.model.<a href="../../kerml/model/KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a></h3>
<code><a href="../../kerml/model/KerMLVisitorContext.html#addToVisited(int)">addToVisited</a>, <a href="../../kerml/model/KerMLVisitorContext.html#isAlreadyVisited(int)">isAlreadyVisited</a></code></div>
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
<section class="detail" id="ACCEPT_ACTION_USAGE">
<h3>ACCEPT_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ACCEPT_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACCEPT_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTION_DEFINITION">
<h3>ACTION_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ACTION_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACTION_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTION_USAGE">
<h3>ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTOR_MEMBERSHIP">
<h3>ACTOR_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ACTOR_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ACTOR_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ALLOCATION_DEFINITION">
<h3>ALLOCATION_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ALLOCATION_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ALLOCATION_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ALLOCATION_USAGE">
<h3>ALLOCATION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ALLOCATION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ALLOCATION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANALYSIS_CASE_DEFINITION">
<h3>ANALYSIS_CASE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ANALYSIS_CASE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ANALYSIS_CASE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANALYSIS_CASE_USAGE">
<h3>ANALYSIS_CASE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ANALYSIS_CASE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ANALYSIS_CASE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSERT_CONSTRAINT_USAGE">
<h3>ASSERT_CONSTRAINT_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ASSERT_CONSTRAINT_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ASSERT_CONSTRAINT_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSIGNMENT_ACTION_USAGE">
<h3>ASSIGNMENT_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ASSIGNMENT_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ASSIGNMENT_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ATTRIBUTE_DEFINITION">
<h3>ATTRIBUTE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ATTRIBUTE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ATTRIBUTE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ATTRIBUTE_USAGE">
<h3>ATTRIBUTE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ATTRIBUTE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ATTRIBUTE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BINDING_CONNECTOR_AS_USAGE">
<h3>BINDING_CONNECTOR_AS_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">BINDING_CONNECTOR_AS_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.BINDING_CONNECTOR_AS_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CALCULATION_DEFINITION">
<h3>CALCULATION_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CALCULATION_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CALCULATION_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CALCULATION_USAGE">
<h3>CALCULATION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CALCULATION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CALCULATION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CASE_DEFINITION">
<h3>CASE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CASE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CASE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CASE_USAGE">
<h3>CASE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CASE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CASE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONCERN_DEFINITION">
<h3>CONCERN_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONCERN_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONCERN_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONCERN_USAGE">
<h3>CONCERN_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONCERN_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONCERN_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONJUGATED_PORT_DEFINITION">
<h3>CONJUGATED_PORT_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONJUGATED_PORT_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONJUGATED_PORT_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONJUGATED_PORT_TYPING">
<h3>CONJUGATED_PORT_TYPING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONJUGATED_PORT_TYPING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONJUGATED_PORT_TYPING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONNECTION_DEFINITION">
<h3>CONNECTION_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONNECTION_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONNECTION_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONNECTION_USAGE">
<h3>CONNECTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONNECTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONNECTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONNECTOR_AS_USAGE">
<h3>CONNECTOR_AS_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONNECTOR_AS_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONNECTOR_AS_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONSTRAINT_DEFINITION">
<h3>CONSTRAINT_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONSTRAINT_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONSTRAINT_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONSTRAINT_USAGE">
<h3>CONSTRAINT_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONSTRAINT_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONSTRAINT_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONTROL_NODE">
<h3>CONTROL_NODE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONTROL_NODE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.CONTROL_NODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DECISION_NODE">
<h3>DECISION_NODE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DECISION_NODE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.DECISION_NODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFINITION">
<h3>DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENUMERATION_DEFINITION">
<h3>ENUMERATION_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENUMERATION_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ENUMERATION_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENUMERATION_USAGE">
<h3>ENUMERATION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENUMERATION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ENUMERATION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EVENT_OCCURRENCE_USAGE">
<h3>EVENT_OCCURRENCE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EVENT_OCCURRENCE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.EVENT_OCCURRENCE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXHIBIT_STATE_USAGE">
<h3>EXHIBIT_STATE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EXHIBIT_STATE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.EXHIBIT_STATE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXPOSE">
<h3>EXPOSE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EXPOSE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.EXPOSE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FLOW_DEFINITION">
<h3>FLOW_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FLOW_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FLOW_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FLOW_USAGE">
<h3>FLOW_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FLOW_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FLOW_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FOR_LOOP_ACTION_USAGE">
<h3>FOR_LOOP_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FOR_LOOP_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FOR_LOOP_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FORK_NODE">
<h3>FORK_NODE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FORK_NODE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FORK_NODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FRAMED_CONCERN_MEMBERSHIP">
<h3>FRAMED_CONCERN_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FRAMED_CONCERN_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.FRAMED_CONCERN_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IF_ACTION_USAGE">
<h3>IF_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">IF_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.IF_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INCLUDE_USE_CASE_USAGE">
<h3>INCLUDE_USE_CASE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INCLUDE_USE_CASE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.INCLUDE_USE_CASE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INTERFACE_DEFINITION">
<h3>INTERFACE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INTERFACE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.INTERFACE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INTERFACE_USAGE">
<h3>INTERFACE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INTERFACE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.INTERFACE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ITEM_DEFINITION">
<h3>ITEM_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ITEM_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ITEM_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ITEM_USAGE">
<h3>ITEM_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ITEM_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.ITEM_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="JOIN_NODE">
<h3>JOIN_NODE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">JOIN_NODE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.JOIN_NODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOOP_ACTION_USAGE">
<h3>LOOP_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOOP_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.LOOP_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MEMBERSHIP_EXPOSE">
<h3>MEMBERSHIP_EXPOSE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MEMBERSHIP_EXPOSE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.MEMBERSHIP_EXPOSE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MERGE_NODE">
<h3>MERGE_NODE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MERGE_NODE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.MERGE_NODE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METADATA_DEFINITION">
<h3>METADATA_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">METADATA_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.METADATA_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METADATA_USAGE">
<h3>METADATA_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">METADATA_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.METADATA_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NAMESPACE_EXPOSE">
<h3>NAMESPACE_EXPOSE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">NAMESPACE_EXPOSE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.NAMESPACE_EXPOSE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OBJECTIVE_MEMBERSHIP">
<h3>OBJECTIVE_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">OBJECTIVE_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.OBJECTIVE_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OCCURRENCE_DEFINITION">
<h3>OCCURRENCE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">OCCURRENCE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.OCCURRENCE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OCCURRENCE_USAGE">
<h3>OCCURRENCE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">OCCURRENCE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.OCCURRENCE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PART_DEFINITION">
<h3>PART_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PART_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PART_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PART_USAGE">
<h3>PART_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PART_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PART_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PERFORM_ACTION_USAGE">
<h3>PERFORM_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PERFORM_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PERFORM_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PORT_CONJUGATION">
<h3>PORT_CONJUGATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PORT_CONJUGATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PORT_CONJUGATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PORT_DEFINITION">
<h3>PORT_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PORT_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PORT_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PORT_USAGE">
<h3>PORT_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PORT_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.PORT_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REFERENCE_USAGE">
<h3>REFERENCE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">REFERENCE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REFERENCE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RENDERING_DEFINITION">
<h3>RENDERING_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">RENDERING_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.RENDERING_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RENDERING_USAGE">
<h3>RENDERING_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">RENDERING_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.RENDERING_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENT_CONSTRAINT_MEMBERSHIP">
<h3>REQUIREMENT_CONSTRAINT_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">REQUIREMENT_CONSTRAINT_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_CONSTRAINT_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENT_DEFINITION">
<h3>REQUIREMENT_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">REQUIREMENT_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENT_USAGE">
<h3>REQUIREMENT_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">REQUIREMENT_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENT_VERIFICATION_MEMBERSHIP">
<h3>REQUIREMENT_VERIFICATION_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">REQUIREMENT_VERIFICATION_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.REQUIREMENT_VERIFICATION_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SATISFY_REQUIREMENT_USAGE">
<h3>SATISFY_REQUIREMENT_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SATISFY_REQUIREMENT_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SATISFY_REQUIREMENT_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEND_ACTION_USAGE">
<h3>SEND_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SEND_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SEND_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STAKEHOLDER_MEMBERSHIP">
<h3>STAKEHOLDER_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STAKEHOLDER_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STAKEHOLDER_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_DEFINITION">
<h3>STATE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STATE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STATE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_SUBACTION_MEMBERSHIP">
<h3>STATE_SUBACTION_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STATE_SUBACTION_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STATE_SUBACTION_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_USAGE">
<h3>STATE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STATE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.STATE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUBJECT_MEMBERSHIP">
<h3>SUBJECT_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SUBJECT_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SUBJECT_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUCCESSION_AS_USAGE">
<h3>SUCCESSION_AS_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SUCCESSION_AS_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SUCCESSION_AS_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUCCESSION_FLOW_USAGE">
<h3>SUCCESSION_FLOW_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SUCCESSION_FLOW_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.SUCCESSION_FLOW_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TERMINATE_ACTION_USAGE">
<h3>TERMINATE_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TERMINATE_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TERMINATE_ACTION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRANSITION_FEATURE_MEMBERSHIP">
<h3>TRANSITION_FEATURE_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TRANSITION_FEATURE_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TRANSITION_FEATURE_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRANSITION_USAGE">
<h3>TRANSITION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TRANSITION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TRANSITION_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRIGGER_INVOCATION_EXPRESSION">
<h3>TRIGGER_INVOCATION_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TRIGGER_INVOCATION_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.TRIGGER_INVOCATION_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USAGE">
<h3>USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USE_CASE_DEFINITION">
<h3>USE_CASE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USE_CASE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.USE_CASE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="USE_CASE_USAGE">
<h3>USE_CASE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">USE_CASE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.USE_CASE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VARIANT_MEMBERSHIP">
<h3>VARIANT_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VARIANT_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VARIANT_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATION_CASE_DEFINITION">
<h3>VERIFICATION_CASE_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VERIFICATION_CASE_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VERIFICATION_CASE_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATION_CASE_USAGE">
<h3>VERIFICATION_CASE_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VERIFICATION_CASE_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VERIFICATION_CASE_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VIEW_DEFINITION">
<h3>VIEW_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VIEW_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEW_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VIEW_RENDERING_MEMBERSHIP">
<h3>VIEW_RENDERING_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VIEW_RENDERING_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEW_RENDERING_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VIEW_USAGE">
<h3>VIEW_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VIEW_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEW_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VIEWPOINT_DEFINITION">
<h3>VIEWPOINT_DEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VIEWPOINT_DEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEWPOINT_DEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VIEWPOINT_USAGE">
<h3>VIEWPOINT_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">VIEWPOINT_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.VIEWPOINT_USAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WHILE_LOOP_ACTION_USAGE">
<h3>WHILE_LOOP_ACTION_USAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">WHILE_LOOP_ACTION_USAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.SysMLVisitorContext.WHILE_LOOP_ACTION_USAGE">Constant Field Values</a></li>
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
<section class="detail" id="getClassCount()">
<h3>getClassCount</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">int</span> <span class="element-name">getClassCount</span>()</div>
<div class="block">Returns the count of classes in the SysML visitor context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../kerml/model/KerMLVisitorContext.html#getClassCount()">getClassCount</a></code> in interface <code><a href="../../kerml/model/KerMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.kerml.model">KerMLVisitorContext</a></code></dd>
<dt>Returns:</dt>
<dd>the count of classes, which is the sum of the super class count and 93.</dd>
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
