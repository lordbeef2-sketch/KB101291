# JAVA OPENAPI: KerMLVisitorContext (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/KerMLVisitorContext.html
- source_path: `com/dassault_systemes/modeler/kerml/model/KerMLVisitorContext.html`
- source_sha256: `9d2ea857677e0ed8f344dd765beffa92697fbe05b72bc9513fa60b4ae6a45260`
- captured_utc: `2026-07-14T16:44:47.705838+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Interface KerMLVisitorContext

All Known Subinterfaces:
`[SysMLVisitorContext](../../sysml/model/SysMLVisitorContext.html)`

@OpenApiAllpublic interfaceKerMLVisitorContext

A context interface for KerML model visitors.
 This interface provides methods to track visited elements during the traversal of the KerML model.
 It uses integer constants to represent different types of elements in the model.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[ANNOTATING_ELEMENT](#ANNOTATING_ELEMENT)`

`static final int`
`[ANNOTATION](#ANNOTATION)`

`static final int`
`[ASSOCIATION](#ASSOCIATION)`

`static final int`
`[ASSOCIATION_STRUCTURE](#ASSOCIATION_STRUCTURE)`

`static final int`
`[BEHAVIOR](#BEHAVIOR)`

`static final int`
`[BINDING_CONNECTOR](#BINDING_CONNECTOR)`

`static final int`
`[BOOLEAN_EXPRESSION](#BOOLEAN_EXPRESSION)`

`static final int`
`[CLASS](#CLASS)`

`static final int`
`[CLASSIFIER](#CLASSIFIER)`

`static final int`
`[COLLECT_EXPRESSION](#COLLECT_EXPRESSION)`

`static final int`
`[COMMENT](#COMMENT)`

`static final int`
`[CONJUGATION](#CONJUGATION)`

`static final int`
`[CONNECTOR](#CONNECTOR)`

`static final int`
`[CONSTRUCTOR_EXPRESSION](#CONSTRUCTOR_EXPRESSION)`

`static final int`
`[CROSS_SUBSETTING](#CROSS_SUBSETTING)`

`static final int`
`[DATA_TYPE](#DATA_TYPE)`

`static final int`
`[DEPENDENCY](#DEPENDENCY)`

`static final int`
`[DIFFERENCING](#DIFFERENCING)`

`static final int`
`[DISJOINING](#DISJOINING)`

`static final int`
`[DOCUMENTATION](#DOCUMENTATION)`

`static final int`
`[ELEMENT](#ELEMENT)`

`static final int`
`[ELEMENT_FILTER_MEMBERSHIP](#ELEMENT_FILTER_MEMBERSHIP)`

`static final int`
`[END_FEATURE_MEMBERSHIP](#END_FEATURE_MEMBERSHIP)`

`static final int`
`[EXPRESSION](#EXPRESSION)`

`static final int`
`[FEATURE](#FEATURE)`

`static final int`
`[FEATURE_CHAIN_EXPRESSION](#FEATURE_CHAIN_EXPRESSION)`

`static final int`
`[FEATURE_CHAINING](#FEATURE_CHAINING)`

`static final int`
`[FEATURE_INVERTING](#FEATURE_INVERTING)`

`static final int`
`[FEATURE_MEMBERSHIP](#FEATURE_MEMBERSHIP)`

`static final int`
`[FEATURE_REFERENCE_EXPRESSION](#FEATURE_REFERENCE_EXPRESSION)`

`static final int`
`[FEATURE_TYPING](#FEATURE_TYPING)`

`static final int`
`[FEATURE_VALUE](#FEATURE_VALUE)`

`static final int`
`[FLOW](#FLOW)`

`static final int`
`[FLOW_END](#FLOW_END)`

`static final int`
`[FUNCTION](#FUNCTION)`

`static final int`
`[IMPORT](#IMPORT)`

`static final int`
`[INDEX_EXPRESSION](#INDEX_EXPRESSION)`

`static final int`
`[INSTANTIATION_EXPRESSION](#INSTANTIATION_EXPRESSION)`

`static final int`
`[INTERACTION](#INTERACTION)`

`static final int`
`[INTERSECTING](#INTERSECTING)`

`static final int`
`[INVARIANT](#INVARIANT)`

`static final int`
`[INVOCATION_EXPRESSION](#INVOCATION_EXPRESSION)`

`static final int`
`[LIBRARY_PACKAGE](#LIBRARY_PACKAGE)`

`static final int`
`[LITERAL_BOOLEAN](#LITERAL_BOOLEAN)`

`static final int`
`[LITERAL_EXPRESSION](#LITERAL_EXPRESSION)`

`static final int`
`[LITERAL_INFINITY](#LITERAL_INFINITY)`

`static final int`
`[LITERAL_INTEGER](#LITERAL_INTEGER)`

`static final int`
`[LITERAL_RATIONAL](#LITERAL_RATIONAL)`

`static final int`
`[LITERAL_STRING](#LITERAL_STRING)`

`static final int`
`[MEMBERSHIP](#MEMBERSHIP)`

`static final int`
`[MEMBERSHIP_IMPORT](#MEMBERSHIP_IMPORT)`

`static final int`
`[METACLASS](#METACLASS)`

`static final int`
`[METADATA_ACCESS_EXPRESSION](#METADATA_ACCESS_EXPRESSION)`

`static final int`
`[METADATA_FEATURE](#METADATA_FEATURE)`

`static final int`
`[MULTIPLICITY](#MULTIPLICITY)`

`static final int`
`[MULTIPLICITY_RANGE](#MULTIPLICITY_RANGE)`

`static final int`
`[NAMESPACE](#NAMESPACE)`

`static final int`
`[NAMESPACE_IMPORT](#NAMESPACE_IMPORT)`

`static final int`
`[NULL_EXPRESSION](#NULL_EXPRESSION)`

`static final int`
`[OPERATOR_EXPRESSION](#OPERATOR_EXPRESSION)`

`static final int`
`[OWNING_MEMBERSHIP](#OWNING_MEMBERSHIP)`

`static final int`
`[PACKAGE](#PACKAGE)`

`static final int`
`[PARAMETER_MEMBERSHIP](#PARAMETER_MEMBERSHIP)`

`static final int`
`[PAYLOAD_FEATURE](#PAYLOAD_FEATURE)`

`static final int`
`[PREDICATE](#PREDICATE)`

`static final int`
`[REDEFINITION](#REDEFINITION)`

`static final int`
`[REFERENCE_SUBSETTING](#REFERENCE_SUBSETTING)`

`static final int`
`[RELATIONSHIP](#RELATIONSHIP)`

`static final int`
`[RESULT_EXPRESSION_MEMBERSHIP](#RESULT_EXPRESSION_MEMBERSHIP)`

`static final int`
`[RETURN_PARAMETER_MEMBERSHIP](#RETURN_PARAMETER_MEMBERSHIP)`

`static final int`
`[SELECT_EXPRESSION](#SELECT_EXPRESSION)`

`static final int`
`[SPECIALIZATION](#SPECIALIZATION)`

`static final int`
`[STEP](#STEP)`

`static final int`
`[STRUCTURE](#STRUCTURE)`

`static final int`
`[SUBCLASSIFICATION](#SUBCLASSIFICATION)`

`static final int`
`[SUBSETTING](#SUBSETTING)`

`static final int`
`[SUCCESSION](#SUCCESSION)`

`static final int`
`[SUCCESSION_FLOW](#SUCCESSION_FLOW)`

`static final int`
`[TEXTUAL_REPRESENTATION](#TEXTUAL_REPRESENTATION)`

`static final int`
`[TYPE](#TYPE)`

`static final int`
`[TYPE_FEATURING](#TYPE_FEATURING)`

`static final int`
`[UNIONING](#UNIONING)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`void`
`[addToVisited](#addToVisited(int))(int classID)`
Adds an element class ID to the set of visited elements.
`default int`
`[getClassCount](#getClassCount())()`
Gets the total number of element classes in the KerML model.
`boolean`
`[isAlreadyVisited](#isAlreadyVisited(int))(int classID)`
Checks if an element class ID has already been visited.

============ FIELD DETAIL =========== 
Field Details
ANNOTATING_ELEMENT
static final int ANNOTATING_ELEMENT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ANNOTATING_ELEMENT)
ANNOTATION
static final int ANNOTATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ANNOTATION)
ASSOCIATION
static final int ASSOCIATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ASSOCIATION)
ASSOCIATION_STRUCTURE
static final int ASSOCIATION_STRUCTURE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ASSOCIATION_STRUCTURE)
BEHAVIOR
static final int BEHAVIOR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.BEHAVIOR)
BINDING_CONNECTOR
static final int BINDING_CONNECTOR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.BINDING_CONNECTOR)
BOOLEAN_EXPRESSION
static final int BOOLEAN_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.BOOLEAN_EXPRESSION)
CLASS
static final int CLASS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CLASS)
CLASSIFIER
static final int CLASSIFIER
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CLASSIFIER)
COLLECT_EXPRESSION
static final int COLLECT_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.COLLECT_EXPRESSION)
COMMENT
static final int COMMENT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.COMMENT)
CONJUGATION
static final int CONJUGATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CONJUGATION)
CONNECTOR
static final int CONNECTOR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CONNECTOR)
CONSTRUCTOR_EXPRESSION
static final int CONSTRUCTOR_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CONSTRUCTOR_EXPRESSION)
CROSS_SUBSETTING
static final int CROSS_SUBSETTING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CROSS_SUBSETTING)
DATA_TYPE
static final int DATA_TYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DATA_TYPE)
DEPENDENCY
static final int DEPENDENCY
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DEPENDENCY)
DIFFERENCING
static final int DIFFERENCING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DIFFERENCING)
DISJOINING
static final int DISJOINING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DISJOINING)
DOCUMENTATION
static final int DOCUMENTATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DOCUMENTATION)
ELEMENT
static final int ELEMENT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ELEMENT)
ELEMENT_FILTER_MEMBERSHIP
static final int ELEMENT_FILTER_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ELEMENT_FILTER_MEMBERSHIP)
END_FEATURE_MEMBERSHIP
static final int END_FEATURE_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.END_FEATURE_MEMBERSHIP)
EXPRESSION
static final int EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.EXPRESSION)
FEATURE
static final int FEATURE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE)
FEATURE_CHAIN_EXPRESSION
static final int FEATURE_CHAIN_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_CHAIN_EXPRESSION)
FEATURE_CHAINING
static final int FEATURE_CHAINING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_CHAINING)
FEATURE_INVERTING
static final int FEATURE_INVERTING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_INVERTING)
FEATURE_MEMBERSHIP
static final int FEATURE_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_MEMBERSHIP)
FEATURE_REFERENCE_EXPRESSION
static final int FEATURE_REFERENCE_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_REFERENCE_EXPRESSION)
FEATURE_TYPING
static final int FEATURE_TYPING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_TYPING)
FEATURE_VALUE
static final int FEATURE_VALUE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_VALUE)
FLOW
static final int FLOW
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FLOW)
FLOW_END
static final int FLOW_END
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FLOW_END)
FUNCTION
static final int FUNCTION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FUNCTION)
IMPORT
static final int IMPORT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.IMPORT)
INDEX_EXPRESSION
static final int INDEX_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INDEX_EXPRESSION)
INSTANTIATION_EXPRESSION
static final int INSTANTIATION_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INSTANTIATION_EXPRESSION)
INTERACTION
static final int INTERACTION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INTERACTION)
INTERSECTING
static final int INTERSECTING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INTERSECTING)
INVARIANT
static final int INVARIANT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INVARIANT)
INVOCATION_EXPRESSION
static final int INVOCATION_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INVOCATION_EXPRESSION)
LIBRARY_PACKAGE
static final int LIBRARY_PACKAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LIBRARY_PACKAGE)
LITERAL_BOOLEAN
static final int LITERAL_BOOLEAN
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_BOOLEAN)
LITERAL_EXPRESSION
static final int LITERAL_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_EXPRESSION)
LITERAL_INFINITY
static final int LITERAL_INFINITY
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_INFINITY)
LITERAL_INTEGER
static final int LITERAL_INTEGER
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_INTEGER)
LITERAL_RATIONAL
static final int LITERAL_RATIONAL
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_RATIONAL)
LITERAL_STRING
static final int LITERAL_STRING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_STRING)
MEMBERSHIP
static final int MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MEMBERSHIP)
MEMBERSHIP_IMPORT
static final int MEMBERSHIP_IMPORT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MEMBERSHIP_IMPORT)
METACLASS
static final int METACLASS
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.METACLASS)
METADATA_ACCESS_EXPRESSION
static final int METADATA_ACCESS_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.METADATA_ACCESS_EXPRESSION)
METADATA_FEATURE
static final int METADATA_FEATURE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.METADATA_FEATURE)
MULTIPLICITY
static final int MULTIPLICITY
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MULTIPLICITY)
MULTIPLICITY_RANGE
static final int MULTIPLICITY_RANGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MULTIPLICITY_RANGE)
NAMESPACE
static final int NAMESPACE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.NAMESPACE)
NAMESPACE_IMPORT
static final int NAMESPACE_IMPORT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.NAMESPACE_IMPORT)
NULL_EXPRESSION
static final int NULL_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.NULL_EXPRESSION)
OPERATOR_EXPRESSION
static final int OPERATOR_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.OPERATOR_EXPRESSION)
OWNING_MEMBERSHIP
static final int OWNING_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.OWNING_MEMBERSHIP)
PACKAGE
static final int PACKAGE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PACKAGE)
PARAMETER_MEMBERSHIP
static final int PARAMETER_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PARAMETER_MEMBERSHIP)
PAYLOAD_FEATURE
static final int PAYLOAD_FEATURE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PAYLOAD_FEATURE)
PREDICATE
static final int PREDICATE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PREDICATE)
REDEFINITION
static final int REDEFINITION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.REDEFINITION)
REFERENCE_SUBSETTING
static final int REFERENCE_SUBSETTING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.REFERENCE_SUBSETTING)
RELATIONSHIP
static final int RELATIONSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.RELATIONSHIP)
RESULT_EXPRESSION_MEMBERSHIP
static final int RESULT_EXPRESSION_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.RESULT_EXPRESSION_MEMBERSHIP)
RETURN_PARAMETER_MEMBERSHIP
static final int RETURN_PARAMETER_MEMBERSHIP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.RETURN_PARAMETER_MEMBERSHIP)
SELECT_EXPRESSION
static final int SELECT_EXPRESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SELECT_EXPRESSION)
SPECIALIZATION
static final int SPECIALIZATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SPECIALIZATION)
STEP
static final int STEP
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.STEP)
STRUCTURE
static final int STRUCTURE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.STRUCTURE)
SUBCLASSIFICATION
static final int SUBCLASSIFICATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUBCLASSIFICATION)
SUBSETTING
static final int SUBSETTING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUBSETTING)
SUCCESSION
static final int SUCCESSION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUCCESSION)
SUCCESSION_FLOW
static final int SUCCESSION_FLOW
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUCCESSION_FLOW)
TEXTUAL_REPRESENTATION
static final int TEXTUAL_REPRESENTATION
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.TEXTUAL_REPRESENTATION)
TYPE
static final int TYPE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.TYPE)
TYPE_FEATURING
static final int TYPE_FEATURING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.TYPE_FEATURING)
UNIONING
static final int UNIONING
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.UNIONING)
 ============ METHOD DETAIL ========== 
Method Details
addToVisited
void addToVisited(int classID)
Adds an element class ID to the set of visited elements.
Parameters:
`classID` - The ID of the element class to add to the visited set.
isAlreadyVisited
boolean isAlreadyVisited(int classID)
Checks if an element class ID has already been visited.
Parameters:
`classID` - The ID of the element class to check.
Returns:
true if the element class ID has been visited, false otherwise.
getClassCount
default int getClassCount()
Gets the total number of element classes in the KerML model.
Returns:
The total number of element classes.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Interface KerMLVisitorContext">Interface KerMLVisitorContext</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../sysml/model/SysMLVisitorContext.html" title="interface in com.dassault_systemes.modeler.sysml.model">SysMLVisitorContext</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">KerMLVisitorContext</span></div>
<div class="block">A context interface for KerML model visitors.
 <p>
 This interface provides methods to track visited elements during the traversal of the KerML model.
 It uses integer constants to represent different types of elements in the model.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ANNOTATING_ELEMENT">ANNOTATING_ELEMENT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ANNOTATION">ANNOTATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ASSOCIATION">ASSOCIATION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ASSOCIATION_STRUCTURE">ASSOCIATION_STRUCTURE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BEHAVIOR">BEHAVIOR</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BINDING_CONNECTOR">BINDING_CONNECTOR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BOOLEAN_EXPRESSION">BOOLEAN_EXPRESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CLASS">CLASS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CLASSIFIER">CLASSIFIER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COLLECT_EXPRESSION">COLLECT_EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMMENT">COMMENT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONJUGATION">CONJUGATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONNECTOR">CONNECTOR</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONSTRUCTOR_EXPRESSION">CONSTRUCTOR_EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CROSS_SUBSETTING">CROSS_SUBSETTING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DATA_TYPE">DATA_TYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEPENDENCY">DEPENDENCY</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIFFERENCING">DIFFERENCING</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DISJOINING">DISJOINING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DOCUMENTATION">DOCUMENTATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ELEMENT">ELEMENT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ELEMENT_FILTER_MEMBERSHIP">ELEMENT_FILTER_MEMBERSHIP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#END_FEATURE_MEMBERSHIP">END_FEATURE_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXPRESSION">EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FEATURE">FEATURE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FEATURE_CHAIN_EXPRESSION">FEATURE_CHAIN_EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FEATURE_CHAINING">FEATURE_CHAINING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FEATURE_INVERTING">FEATURE_INVERTING</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FEATURE_MEMBERSHIP">FEATURE_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FEATURE_REFERENCE_EXPRESSION">FEATURE_REFERENCE_EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FEATURE_TYPING">FEATURE_TYPING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FEATURE_VALUE">FEATURE_VALUE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FLOW">FLOW</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#FLOW_END">FLOW_END</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FUNCTION">FUNCTION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IMPORT">IMPORT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INDEX_EXPRESSION">INDEX_EXPRESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INSTANTIATION_EXPRESSION">INSTANTIATION_EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INTERACTION">INTERACTION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INTERSECTING">INTERSECTING</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INVARIANT">INVARIANT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INVOCATION_EXPRESSION">INVOCATION_EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LIBRARY_PACKAGE">LIBRARY_PACKAGE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LITERAL_BOOLEAN">LITERAL_BOOLEAN</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LITERAL_EXPRESSION">LITERAL_EXPRESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LITERAL_INFINITY">LITERAL_INFINITY</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LITERAL_INTEGER">LITERAL_INTEGER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LITERAL_RATIONAL">LITERAL_RATIONAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LITERAL_STRING">LITERAL_STRING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MEMBERSHIP">MEMBERSHIP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MEMBERSHIP_IMPORT">MEMBERSHIP_IMPORT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METACLASS">METACLASS</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#METADATA_ACCESS_EXPRESSION">METADATA_ACCESS_EXPRESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#METADATA_FEATURE">METADATA_FEATURE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MULTIPLICITY">MULTIPLICITY</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MULTIPLICITY_RANGE">MULTIPLICITY_RANGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NAMESPACE">NAMESPACE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NAMESPACE_IMPORT">NAMESPACE_IMPORT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NULL_EXPRESSION">NULL_EXPRESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OPERATOR_EXPRESSION">OPERATOR_EXPRESSION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OWNING_MEMBERSHIP">OWNING_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PACKAGE">PACKAGE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PARAMETER_MEMBERSHIP">PARAMETER_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PAYLOAD_FEATURE">PAYLOAD_FEATURE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PREDICATE">PREDICATE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REDEFINITION">REDEFINITION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REFERENCE_SUBSETTING">REFERENCE_SUBSETTING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RELATIONSHIP">RELATIONSHIP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#RESULT_EXPRESSION_MEMBERSHIP">RESULT_EXPRESSION_MEMBERSHIP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#RETURN_PARAMETER_MEMBERSHIP">RETURN_PARAMETER_MEMBERSHIP</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SELECT_EXPRESSION">SELECT_EXPRESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SPECIALIZATION">SPECIALIZATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STEP">STEP</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STRUCTURE">STRUCTURE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUBCLASSIFICATION">SUBCLASSIFICATION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SUBSETTING">SUBSETTING</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SUCCESSION">SUCCESSION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SUCCESSION_FLOW">SUCCESSION_FLOW</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TEXTUAL_REPRESENTATION">TEXTUAL_REPRESENTATION</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE">TYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TYPE_FEATURING">TYPE_FEATURING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNIONING">UNIONING</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addToVisited(int)">addToVisited</a><wbr/>(int classID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds an element class ID to the set of visited elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getClassCount()">getClassCount</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Gets the total number of element classes in the KerML model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isAlreadyVisited(int)">isAlreadyVisited</a><wbr/>(int classID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if an element class ID has already been visited.</div>
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
<section class="detail" id="ANNOTATING_ELEMENT">
<h3>ANNOTATING_ELEMENT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ANNOTATING_ELEMENT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ANNOTATING_ELEMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ANNOTATION">
<h3>ANNOTATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ANNOTATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ANNOTATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSOCIATION">
<h3>ASSOCIATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ASSOCIATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ASSOCIATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ASSOCIATION_STRUCTURE">
<h3>ASSOCIATION_STRUCTURE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ASSOCIATION_STRUCTURE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ASSOCIATION_STRUCTURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BEHAVIOR">
<h3>BEHAVIOR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">BEHAVIOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.BEHAVIOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BINDING_CONNECTOR">
<h3>BINDING_CONNECTOR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">BINDING_CONNECTOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.BINDING_CONNECTOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BOOLEAN_EXPRESSION">
<h3>BOOLEAN_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">BOOLEAN_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.BOOLEAN_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLASS">
<h3>CLASS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CLASS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CLASS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLASSIFIER">
<h3>CLASSIFIER</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CLASSIFIER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CLASSIFIER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COLLECT_EXPRESSION">
<h3>COLLECT_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">COLLECT_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.COLLECT_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMMENT">
<h3>COMMENT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">COMMENT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.COMMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONJUGATION">
<h3>CONJUGATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONJUGATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CONJUGATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONNECTOR">
<h3>CONNECTOR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONNECTOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CONNECTOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONSTRUCTOR_EXPRESSION">
<h3>CONSTRUCTOR_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CONSTRUCTOR_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CONSTRUCTOR_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CROSS_SUBSETTING">
<h3>CROSS_SUBSETTING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CROSS_SUBSETTING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.CROSS_SUBSETTING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DATA_TYPE">
<h3>DATA_TYPE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DATA_TYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DATA_TYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEPENDENCY">
<h3>DEPENDENCY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DEPENDENCY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DEPENDENCY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DIFFERENCING">
<h3>DIFFERENCING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DIFFERENCING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DIFFERENCING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DISJOINING">
<h3>DISJOINING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DISJOINING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DISJOINING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DOCUMENTATION">
<h3>DOCUMENTATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">DOCUMENTATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.DOCUMENTATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ELEMENT">
<h3>ELEMENT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ELEMENT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ELEMENT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ELEMENT_FILTER_MEMBERSHIP">
<h3>ELEMENT_FILTER_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ELEMENT_FILTER_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.ELEMENT_FILTER_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="END_FEATURE_MEMBERSHIP">
<h3>END_FEATURE_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">END_FEATURE_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.END_FEATURE_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXPRESSION">
<h3>EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE">
<h3>FEATURE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_CHAIN_EXPRESSION">
<h3>FEATURE_CHAIN_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE_CHAIN_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_CHAIN_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_CHAINING">
<h3>FEATURE_CHAINING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE_CHAINING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_CHAINING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_INVERTING">
<h3>FEATURE_INVERTING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE_INVERTING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_INVERTING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_MEMBERSHIP">
<h3>FEATURE_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_REFERENCE_EXPRESSION">
<h3>FEATURE_REFERENCE_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE_REFERENCE_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_REFERENCE_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_TYPING">
<h3>FEATURE_TYPING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE_TYPING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_TYPING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FEATURE_VALUE">
<h3>FEATURE_VALUE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FEATURE_VALUE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FEATURE_VALUE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FLOW">
<h3>FLOW</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FLOW</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FLOW_END">
<h3>FLOW_END</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FLOW_END</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FLOW_END">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FUNCTION">
<h3>FUNCTION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">FUNCTION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.FUNCTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMPORT">
<h3>IMPORT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">IMPORT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.IMPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INDEX_EXPRESSION">
<h3>INDEX_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INDEX_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INDEX_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INSTANTIATION_EXPRESSION">
<h3>INSTANTIATION_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INSTANTIATION_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INSTANTIATION_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INTERACTION">
<h3>INTERACTION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INTERACTION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INTERACTION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INTERSECTING">
<h3>INTERSECTING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INTERSECTING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INTERSECTING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INVARIANT">
<h3>INVARIANT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INVARIANT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INVARIANT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INVOCATION_EXPRESSION">
<h3>INVOCATION_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">INVOCATION_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.INVOCATION_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LIBRARY_PACKAGE">
<h3>LIBRARY_PACKAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LIBRARY_PACKAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LIBRARY_PACKAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LITERAL_BOOLEAN">
<h3>LITERAL_BOOLEAN</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LITERAL_BOOLEAN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_BOOLEAN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LITERAL_EXPRESSION">
<h3>LITERAL_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LITERAL_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LITERAL_INFINITY">
<h3>LITERAL_INFINITY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LITERAL_INFINITY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_INFINITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LITERAL_INTEGER">
<h3>LITERAL_INTEGER</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LITERAL_INTEGER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_INTEGER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LITERAL_RATIONAL">
<h3>LITERAL_RATIONAL</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LITERAL_RATIONAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_RATIONAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LITERAL_STRING">
<h3>LITERAL_STRING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LITERAL_STRING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.LITERAL_STRING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MEMBERSHIP">
<h3>MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MEMBERSHIP_IMPORT">
<h3>MEMBERSHIP_IMPORT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MEMBERSHIP_IMPORT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MEMBERSHIP_IMPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METACLASS">
<h3>METACLASS</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">METACLASS</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.METACLASS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METADATA_ACCESS_EXPRESSION">
<h3>METADATA_ACCESS_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">METADATA_ACCESS_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.METADATA_ACCESS_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="METADATA_FEATURE">
<h3>METADATA_FEATURE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">METADATA_FEATURE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.METADATA_FEATURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MULTIPLICITY">
<h3>MULTIPLICITY</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MULTIPLICITY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MULTIPLICITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MULTIPLICITY_RANGE">
<h3>MULTIPLICITY_RANGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">MULTIPLICITY_RANGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.MULTIPLICITY_RANGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NAMESPACE">
<h3>NAMESPACE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">NAMESPACE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.NAMESPACE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NAMESPACE_IMPORT">
<h3>NAMESPACE_IMPORT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">NAMESPACE_IMPORT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.NAMESPACE_IMPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NULL_EXPRESSION">
<h3>NULL_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">NULL_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.NULL_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPERATOR_EXPRESSION">
<h3>OPERATOR_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">OPERATOR_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.OPERATOR_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OWNING_MEMBERSHIP">
<h3>OWNING_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">OWNING_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.OWNING_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PACKAGE">
<h3>PACKAGE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PACKAGE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PACKAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PARAMETER_MEMBERSHIP">
<h3>PARAMETER_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PARAMETER_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PARAMETER_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PAYLOAD_FEATURE">
<h3>PAYLOAD_FEATURE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PAYLOAD_FEATURE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PAYLOAD_FEATURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PREDICATE">
<h3>PREDICATE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">PREDICATE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.PREDICATE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REDEFINITION">
<h3>REDEFINITION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">REDEFINITION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.REDEFINITION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REFERENCE_SUBSETTING">
<h3>REFERENCE_SUBSETTING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">REFERENCE_SUBSETTING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.REFERENCE_SUBSETTING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RELATIONSHIP">
<h3>RELATIONSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">RELATIONSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.RELATIONSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RESULT_EXPRESSION_MEMBERSHIP">
<h3>RESULT_EXPRESSION_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">RESULT_EXPRESSION_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.RESULT_EXPRESSION_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="RETURN_PARAMETER_MEMBERSHIP">
<h3>RETURN_PARAMETER_MEMBERSHIP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">RETURN_PARAMETER_MEMBERSHIP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.RETURN_PARAMETER_MEMBERSHIP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SELECT_EXPRESSION">
<h3>SELECT_EXPRESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SELECT_EXPRESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SELECT_EXPRESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SPECIALIZATION">
<h3>SPECIALIZATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SPECIALIZATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SPECIALIZATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STEP">
<h3>STEP</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STEP</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.STEP">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STRUCTURE">
<h3>STRUCTURE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STRUCTURE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.STRUCTURE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUBCLASSIFICATION">
<h3>SUBCLASSIFICATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SUBCLASSIFICATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUBCLASSIFICATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUBSETTING">
<h3>SUBSETTING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SUBSETTING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUBSETTING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUCCESSION">
<h3>SUCCESSION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SUCCESSION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUCCESSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SUCCESSION_FLOW">
<h3>SUCCESSION_FLOW</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SUCCESSION_FLOW</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.SUCCESSION_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TEXTUAL_REPRESENTATION">
<h3>TEXTUAL_REPRESENTATION</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TEXTUAL_REPRESENTATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.TEXTUAL_REPRESENTATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE">
<h3>TYPE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.TYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TYPE_FEATURING">
<h3>TYPE_FEATURING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">TYPE_FEATURING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.TYPE_FEATURING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNIONING">
<h3>UNIONING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">UNIONING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.KerMLVisitorContext.UNIONING">Constant Field Values</a></li>
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
<section class="detail" id="addToVisited(int)">
<h3>addToVisited</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addToVisited</span><wbr/><span class="parameters">(int classID)</span></div>
<div class="block">Adds an element class ID to the set of visited elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classID</code> - The ID of the element class to add to the visited set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAlreadyVisited(int)">
<h3>isAlreadyVisited</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isAlreadyVisited</span><wbr/><span class="parameters">(int classID)</span></div>
<div class="block">Checks if an element class ID has already been visited.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>classID</code> - The ID of the element class to check.</dd>
<dt>Returns:</dt>
<dd>true if the element class ID has been visited, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassCount()">
<h3>getClassCount</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">int</span> <span class="element-name">getClassCount</span>()</div>
<div class="block">Gets the total number of element classes in the KerML model.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The total number of element classes.</dd>
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
