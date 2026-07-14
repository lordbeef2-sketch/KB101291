# JAVA OPENAPI: DiagramType (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/DiagramType.html
- source_path: `com/nomagic/magicdraw/uml/DiagramType.html`
- source_sha256: `99573f692e552ec55149a403556549ae2516331882e81084b0d68be60d0b1aea`
- captured_utc: `2026-07-14T16:58:27.211170+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class DiagramType

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.uml.symbols.AbstractDiagramType](symbols/AbstractDiagramType.html)
com.nomagic.magicdraw.uml.DiagramType

All Implemented Interfaces:
`[DiagramTypeConstants](DiagramTypeConstants.html)`, `[DiagramTypes](../../uml2/diagram/DiagramTypes.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApipublic classDiagramType
extends [AbstractDiagramType](symbols/AbstractDiagramType.html)
implements [DiagramTypeConstants](DiagramTypeConstants.html)

The `DiagramType` class represents the diagram type

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.uml2.diagram.[DiagramTypes](../../uml2/diagram/DiagramTypes.html)
`[CONTENT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#CONTENT_DIAGRAM), [DEPENDENCY_MATRIX](../../uml2/diagram/DiagramTypes.html#DEPENDENCY_MATRIX), [GENERIC_TABLE](../../uml2/diagram/DiagramTypes.html#GENERIC_TABLE), [GLOSSARY_TABLE](../../uml2/diagram/DiagramTypes.html#GLOSSARY_TABLE), [INSTANCE_TABLE](../../uml2/diagram/DiagramTypes.html#INSTANCE_TABLE), [RELATION_MAP_DIAGRAM](../../uml2/diagram/DiagramTypes.html#RELATION_MAP_DIAGRAM), [UML_ACTIVITY_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM), [UML_ANY_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_ANY_DIAGRAM), [UML_BEHAVIOR_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_BEHAVIOR_DIAGRAM), [UML_CLASS_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM), [UML_COMMUNICATION_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM), [UML_COMPONENT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM), [UML_COMPOSITE_STRUCTURE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM), [UML_DEPLOYMENT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM), [UML_INTERACTION_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_DIAGRAM), [UML_INTERACTION_OVERVIEW_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_OVERVIEW_DIAGRAM), [UML_OBJECT_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM), [UML_PACKAGE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM), [UML_PROFILE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM), [UML_PROTOCOL_STATE_MACHINE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM), [UML_SEQUENCE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM), [UML_STATECHART_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM), [UML_STATIC_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_STATIC_DIAGRAM), [UML_USECASE_DIAGRAM](../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM), [USER_INTERFACE_MODELING_DIAGRAM](../../uml2/diagram/DiagramTypes.html#USER_INTERFACE_MODELING_DIAGRAM)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramType](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Constructs diagram type according given diagram type string representation.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[DiagramType](DiagramType.html)`
`[clone](#clone())()`

`static [DiagramType](DiagramType.html)`
`[createDiagramType](#createDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Creates diagram type of given type string representation.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getAllDiagramTypes](#getAllDiagramTypes())()`
Returns list of all diagram types.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getCreatableDiagramTypes](#getCreatableDiagramTypes())()`
Returns list of available to create (creatable) diagram types.
`static [DiagramType](DiagramType.html)`
`[getDiagramType](#getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram))([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)`
Return diagram type for a given diagram
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getRootType](#getRootType())()`
Returns root type of this diagram type.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getType](#getType())()`
Returns the diagram type string representation
`static boolean`
`[isCreatableDiagramType](#isCreatableDiagramType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Check, whether diagram type is creatable.
`boolean`
`[isEqualType](#isEqualType(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](DiagramType.html) type)`
Checks if diagram type is equal to given diagram type.
`boolean`
`[isEqualType](#isEqualType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Checks if diagram type is equal to given diagram type.
`boolean`
`[isTypeOf](#isTypeOf(com.nomagic.magicdraw.uml.DiagramType))([DiagramType](DiagramType.html) type)`
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
`boolean`
`[isTypeOf](#isTypeOf(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
`void`
`[setType](#setType(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)`
Sets the diagram type, according given diagram type string representation
Methods inherited from class com.nomagic.magicdraw.uml.symbols.[AbstractDiagramType](symbols/AbstractDiagramType.html)
`[isTypeOf](symbols/AbstractDiagramType.html#isTypeOf(java.util.List))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramType
@OpenApipublic DiagramType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Constructs diagram type according given diagram type string representation.
Parameters:
`type` - diagram type string representation
See Also:
[`createDiagramType(String)`](#createDiagramType(java.lang.String))
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`getCreatableDiagramTypes()`](#getCreatableDiagramTypes())
 ============ METHOD DETAIL ========== 
Method Details
getDiagramType
@OpenApipublic static [DiagramType](DiagramType.html) getDiagramType([Diagram](../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html) diagram)
Return diagram type for a given diagram
Parameters:
`diagram` - diagram
Returns:
diagram type
setType
@OpenApipublic void setType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Sets the diagram type, according given diagram type string representation
Parameters:
`type` - diagram type string representation
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`getCreatableDiagramTypes()`](#getCreatableDiagramTypes())
getType
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getType()
Returns the diagram type string representation
Specified by:
`[getType](symbols/AbstractDiagramType.html#getType())` in class `[AbstractDiagramType](symbols/AbstractDiagramType.html)`
Returns:
diagram type string representation
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
isEqualType
@OpenApipublic boolean isEqualType([DiagramType](DiagramType.html) type)
Checks if diagram type is equal to given diagram type.
Parameters:
`type` - diagram type
Returns:
`true` if this diagram type is equal to given diagram type; otherwise - `false`.
See Also:
[`isTypeOf(DiagramType)`](#isTypeOf(com.nomagic.magicdraw.uml.DiagramType))
isEqualType
@OpenApipublic boolean isEqualType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Checks if diagram type is equal to given diagram type.
Parameters:
`type` - diagram type string representation
Returns:
`true` if this diagram type is equal to given diagram type; otherwise - `false`.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`isTypeOf(String)`](#isTypeOf(java.lang.String))
isTypeOf
@OpenApipublic boolean isTypeOf([DiagramType](DiagramType.html) type)
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
Parameters:
`type` - diagram type.
Returns:
`true` if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - `false`.
See Also:
[`isTypeOf(String)`](#isTypeOf(java.lang.String))
isTypeOf
@OpenApipublic boolean isTypeOf([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Checks if diagram type is of given diagram type (analogy of `instanceof` operator)
Specified by:
`[isTypeOf](symbols/AbstractDiagramType.html#isTypeOf(java.lang.String))` in class `[AbstractDiagramType](symbols/AbstractDiagramType.html)`
Parameters:
`type` - diagram type string representation.
Returns:
`true` if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - `false`.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
[`getAllDiagramTypes()`](#getAllDiagramTypes())
[`isTypeOf(DiagramType)`](#isTypeOf(com.nomagic.magicdraw.uml.DiagramType))
getRootType
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getRootType()
Returns root type of this diagram type.
Returns:
root type.
clone
@OpenApipublic [DiagramType](DiagramType.html) clone()
Overrides:
`[clone](symbols/AbstractDiagramType.html#clone())` in class `[AbstractDiagramType](symbols/AbstractDiagramType.html)`
getAllDiagramTypes
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getAllDiagramTypes()
Returns list of all diagram types.
Returns:
list of all diagram types.
See Also:
[`getCreatableDiagramTypes()`](#getCreatableDiagramTypes())
getCreatableDiagramTypes
@OpenApipublic static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getCreatableDiagramTypes()
Returns list of available to create (creatable) diagram types.
Returns:
list of available to create (creatable) diagram types.
See Also:
[`getAllDiagramTypes()`](#getAllDiagramTypes())
createDiagramType
@OpenApipublic static [DiagramType](DiagramType.html) createDiagramType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Creates diagram type of given type string representation.
Parameters:
`type` - diagram type string representation
Returns:
created diagram type.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)
isCreatableDiagramType
@OpenApipublic static boolean isCreatableDiagramType([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) type)
Check, whether diagram type is creatable.
Parameters:
`type` - diagram type string representation
Returns:
true, if type is creatable.
See Also:
[`DiagramTypeConstants`](DiagramTypeConstants.html)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class DiagramType">Class DiagramType</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="symbols/AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml.symbols">com.nomagic.magicdraw.uml.symbols.AbstractDiagramType</a>
<div class="inheritance">com.nomagic.magicdraw.uml.DiagramType</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml">DiagramTypeConstants</a></code>, <code><a href="../../uml2/diagram/DiagramTypes.html" title="interface in com.nomagic.uml2.diagram">DiagramTypes</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramType</span>
<span class="extends-implements">extends <a href="symbols/AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramType</a>
implements <a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml">DiagramTypeConstants</a></span></div>
<div class="block">The <code>DiagramType</code> class represents the diagram type</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.uml2.diagram.DiagramTypes">Fields inherited from interface com.nomagic.uml2.diagram.<a href="../../uml2/diagram/DiagramTypes.html" title="interface in com.nomagic.uml2.diagram">DiagramTypes</a></h3>
<code><a href="../../uml2/diagram/DiagramTypes.html#CONTENT_DIAGRAM">CONTENT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#DEPENDENCY_MATRIX">DEPENDENCY_MATRIX</a>, <a href="../../uml2/diagram/DiagramTypes.html#GENERIC_TABLE">GENERIC_TABLE</a>, <a href="../../uml2/diagram/DiagramTypes.html#GLOSSARY_TABLE">GLOSSARY_TABLE</a>, <a href="../../uml2/diagram/DiagramTypes.html#INSTANCE_TABLE">INSTANCE_TABLE</a>, <a href="../../uml2/diagram/DiagramTypes.html#RELATION_MAP_DIAGRAM">RELATION_MAP_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_ACTIVITY_DIAGRAM">UML_ACTIVITY_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_ANY_DIAGRAM">UML_ANY_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_BEHAVIOR_DIAGRAM">UML_BEHAVIOR_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_CLASS_DIAGRAM">UML_CLASS_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_COMMUNICATION_DIAGRAM">UML_COMMUNICATION_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_COMPONENT_DIAGRAM">UML_COMPONENT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_COMPOSITE_STRUCTURE_DIAGRAM">UML_COMPOSITE_STRUCTURE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_DEPLOYMENT_DIAGRAM">UML_DEPLOYMENT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_DIAGRAM">UML_INTERACTION_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_INTERACTION_OVERVIEW_DIAGRAM">UML_INTERACTION_OVERVIEW_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_OBJECT_DIAGRAM">UML_OBJECT_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_PACKAGE_DIAGRAM">UML_PACKAGE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_PROFILE_DIAGRAM">UML_PROFILE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_PROTOCOL_STATE_MACHINE_DIAGRAM">UML_PROTOCOL_STATE_MACHINE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_SEQUENCE_DIAGRAM">UML_SEQUENCE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_STATECHART_DIAGRAM">UML_STATECHART_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_STATIC_DIAGRAM">UML_STATIC_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#UML_USECASE_DIAGRAM">UML_USECASE_DIAGRAM</a>, <a href="../../uml2/diagram/DiagramTypes.html#USER_INTERFACE_MODELING_DIAGRAM">USER_INTERFACE_MODELING_DIAGRAM</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">DiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs diagram type according given diagram type string representation.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDiagramType(java.lang.String)">createDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates diagram type of given type string representation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllDiagramTypes()">getAllDiagramTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns list of all diagram types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCreatableDiagramTypes()">getCreatableDiagramTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns list of available to create (creatable) diagram types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">getDiagramType</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return diagram type for a given diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRootType()">getRootType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns root type of this diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the diagram type string representation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isCreatableDiagramType(java.lang.String)">isCreatableDiagramType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check, whether diagram type is creatable.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEqualType(com.nomagic.magicdraw.uml.DiagramType)">isEqualType</a><wbr/>(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is equal to given diagram type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEqualType(java.lang.String)">isEqualType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is equal to given diagram type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(com.nomagic.magicdraw.uml.DiagramType)">isTypeOf</a><wbr/>(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeOf(java.lang.String)">isTypeOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setType(java.lang.String)">setType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the diagram type, according given diagram type string representation</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.uml.symbols.AbstractDiagramType">Methods inherited from class com.nomagic.magicdraw.uml.symbols.<a href="symbols/AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramType</a></h3>
<code><a href="symbols/AbstractDiagramType.html#isTypeOf(java.util.List)">isTypeOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>DiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">DiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Constructs diagram type according given diagram type string representation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#createDiagramType(java.lang.String)"><code>createDiagramType(String)</code></a></li>
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#getCreatableDiagramTypes()"><code>getCreatableDiagramTypes()</code></a></li>
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
<section class="detail" id="getDiagramType(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram)">
<h3>getDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">getDiagramType</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Diagram.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Diagram</a> diagram)</span></div>
<div class="block">Return diagram type for a given diagram</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - diagram</dd>
<dt>Returns:</dt>
<dd>diagram type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setType(java.lang.String)">
<h3>setType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Sets the diagram type, according given diagram type string representation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#getCreatableDiagramTypes()"><code>getCreatableDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getType</span>()</div>
<div class="block">Returns the diagram type string representation</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="symbols/AbstractDiagramType.html#getType()">getType</a></code> in class <code><a href="symbols/AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramType</a></code></dd>
<dt>Returns:</dt>
<dd>diagram type string representation</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEqualType(com.nomagic.magicdraw.uml.DiagramType)">
<h3>isEqualType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEqualType</span><wbr/><span class="parameters">(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</span></div>
<div class="block">Checks if diagram type is equal to given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isTypeOf(com.nomagic.magicdraw.uml.DiagramType)"><code>isTypeOf(DiagramType)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEqualType(java.lang.String)">
<h3>isEqualType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEqualType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Checks if diagram type is equal to given diagram type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#isTypeOf(java.lang.String)"><code>isTypeOf(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(com.nomagic.magicdraw.uml.DiagramType)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a> type)</span></div>
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isTypeOf(java.lang.String)"><code>isTypeOf(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeOf(java.lang.String)">
<h3>isTypeOf</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Checks if diagram type is of given diagram type (analogy of <code>instanceof</code> operator)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="symbols/AbstractDiagramType.html#isTypeOf(java.lang.String)">isTypeOf</a></code> in class <code><a href="symbols/AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramType</a></code></dd>
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation.</dd>
<dt>Returns:</dt>
<dd><code>true</code> if this diagram type is a 'subtype' of given diagram type or
 equal to given diagram type; otherwise - <code>false</code>.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
<li><a href="#isTypeOf(com.nomagic.magicdraw.uml.DiagramType)"><code>isTypeOf(DiagramType)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRootType()">
<h3>getRootType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRootType</span>()</div>
<div class="block">Returns root type of this diagram type.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="symbols/AbstractDiagramType.html#clone()">clone</a></code> in class <code><a href="symbols/AbstractDiagramType.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramType</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllDiagramTypes()">
<h3>getAllDiagramTypes</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllDiagramTypes</span>()</div>
<div class="block">Returns list of all diagram types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of all diagram types.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getCreatableDiagramTypes()"><code>getCreatableDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCreatableDiagramTypes()">
<h3>getCreatableDiagramTypes</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getCreatableDiagramTypes</span>()</div>
<div class="block">Returns list of available to create (creatable) diagram types.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of available to create (creatable) diagram types.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getAllDiagramTypes()"><code>getAllDiagramTypes()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDiagramType(java.lang.String)">
<h3>createDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DiagramType.html" title="class in com.nomagic.magicdraw.uml">DiagramType</a></span> <span class="element-name">createDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Creates diagram type of given type string representation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>Returns:</dt>
<dd>created diagram type.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCreatableDiagramType(java.lang.String)">
<h3>isCreatableDiagramType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isCreatableDiagramType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> type)</span></div>
<div class="block">Check, whether diagram type is creatable.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - diagram type string representation</dd>
<dt>Returns:</dt>
<dd>true, if type is creatable.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="DiagramTypeConstants.html" title="interface in com.nomagic.magicdraw.uml"><code>DiagramTypeConstants</code></a></li>
</ul>
</dd>
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
