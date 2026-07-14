# JAVA OPENAPI: Objectives (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Objectives.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Objectives.html`
- source_sha256: `e6efa54a7eca564b3305215b44639c9fa1fdf8d4cebccdb93f946431963a624e`
- captured_utc: `2026-07-14T16:45:02.452034+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Objectives

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Objectives

@OpenApiAllpublic classObjectives
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for identifying, creating, and
 retrieving objective requirements. An objective requirement is a
 [`RequirementUsage`](sysml/RequirementUsage.html) owned through an [`ObjectiveMembership`](sysml/ObjectiveMembership.html),
 typically associated with a [`CaseUsage`](sysml/CaseUsage.html) or [`CaseDefinition`](sysml/CaseDefinition.html).

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Objectives](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [RequirementUsage](sysml/RequirementUsage.html)`
`[createObjectiveRequirement](#createObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Namespace))([Namespace](../../kerml/model/kerml/Namespace.html) owner)`
Creates a new objective requirement under the given namespace.
`static [RequirementUsage](sysml/RequirementUsage.html)`
`[getObjectiveRequirement](#getObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the objective requirement associated with the given type.
`static [RequirementUsage](sysml/RequirementUsage.html)`
`[getOwnedObjectiveRequirement](#getOwnedObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the objective requirement owned directly by the given type,
 if one exists.
`static boolean`
`[isObjective](#isObjective(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the given feature represents an objective requirement.
`static boolean`
`[isObjective](#isObjective(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the given membership is an [`ObjectiveMembership`](sysml/ObjectiveMembership.html).
`static boolean`
`[isObjectiveRequirementOwner](#isObjectiveRequirementOwner(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Determines whether the given type is allowed to own an objective requirement.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Objectives
public Objectives()
 ============ METHOD DETAIL ========== 
Method Details
isObjective
public static boolean isObjective([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the given feature represents an objective requirement.
 A feature is considered an objective if it is a [`RequirementUsage`](sysml/RequirementUsage.html)
 owned through an [`ObjectiveMembership`](sysml/ObjectiveMembership.html).
Parameters:
`feature` - the feature to check
Returns:
true if the feature is an objective requirement
isObjective
public static boolean isObjective(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the given membership is an [`ObjectiveMembership`](sysml/ObjectiveMembership.html).
Parameters:
`membership` - the membership to check
Returns:
true if the membership is an objective membership
isObjectiveRequirementOwner
public static boolean isObjectiveRequirementOwner([Type](../../kerml/model/kerml/Type.html) type)
Determines whether the given type is allowed to own an objective requirement.
 Objective requirements may only be owned by case usages or definitions.
Parameters:
`type` - the type to check
Returns:
true if the type is a case usage or definition
createObjectiveRequirement
public static [RequirementUsage](sysml/RequirementUsage.html) createObjectiveRequirement([Namespace](../../kerml/model/kerml/Namespace.html) owner)
Creates a new objective requirement under the given namespace.
 The requirement is owned through an [`ObjectiveMembership`](sysml/ObjectiveMembership.html).
Parameters:
`owner` - the namespace that will own the objective requirement
Returns:
the newly created requirement usage
getOwnedObjectiveRequirement
@CheckForNullpublic static [RequirementUsage](sysml/RequirementUsage.html) getOwnedObjectiveRequirement([Type](../../kerml/model/kerml/Type.html) type)
Returns the objective requirement owned directly by the given type,
 if one exists.
Parameters:
`type` - the type to inspect
Returns:
the owned objective requirement, or null if none exists
getObjectiveRequirement
@CheckForNullpublic static [RequirementUsage](sysml/RequirementUsage.html) getObjectiveRequirement([Type](../../kerml/model/kerml/Type.html) type)
Returns the objective requirement associated with the given type.
 Case usages and case definitions may define an objective requirement.
Parameters:
`type` - the type to inspect
Returns:
the objective requirement, or null if none exists

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Objectives">Class Objectives</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Objectives</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Objectives</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for identifying, creating, and
 retrieving objective requirements. An objective requirement is a
 <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementUsage</code></a> owned through an <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ObjectiveMembership</code></a>,
 typically associated with a <a href="sysml/CaseUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseUsage</code></a> or <a href="sysml/CaseDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>CaseDefinition</code></a>.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Objectives</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">createObjectiveRequirement</a><wbr/>(<a href="../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a new objective requirement under the given namespace.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getObjectiveRequirement</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the objective requirement associated with the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getOwnedObjectiveRequirement</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the objective requirement owned directly by the given type,
 if one exists.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isObjective(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isObjective</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature represents an objective requirement.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isObjective(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isObjective</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given membership is an <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ObjectiveMembership</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isObjectiveRequirementOwner(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isObjectiveRequirementOwner</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Determines whether the given type is allowed to own an objective requirement.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>Objectives</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Objectives</span>()</div>
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
<section class="detail" id="isObjective(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isObjective</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isObjective</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature represents an objective requirement.
 A feature is considered an objective if it is a <a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementUsage</code></a>
 owned through an <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ObjectiveMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature to check</dd>
<dt>Returns:</dt>
<dd>true if the feature is an objective requirement</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isObjective(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isObjective</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isObjective</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the given membership is an <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ObjectiveMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership to check</dd>
<dt>Returns:</dt>
<dd>true if the membership is an objective membership</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isObjectiveRequirementOwner(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isObjectiveRequirementOwner</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isObjectiveRequirementOwner</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Determines whether the given type is allowed to own an objective requirement.
 Objective requirements may only be owned by case usages or definitions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to check</dd>
<dt>Returns:</dt>
<dd>true if the type is a case usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Namespace)">
<h3>createObjectiveRequirement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></span> <span class="element-name">createObjectiveRequirement</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Namespace.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Namespace</a> owner)</span></div>
<div class="block">Creates a new objective requirement under the given namespace.
 The requirement is owned through an <a href="sysml/ObjectiveMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ObjectiveMembership</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - the namespace that will own the objective requirement</dd>
<dt>Returns:</dt>
<dd>the newly created requirement usage</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getOwnedObjectiveRequirement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></span> <span class="element-name">getOwnedObjectiveRequirement</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the objective requirement owned directly by the given type,
 if one exists.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>the owned objective requirement, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getObjectiveRequirement(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getObjectiveRequirement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/RequirementUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RequirementUsage</a></span> <span class="element-name">getObjectiveRequirement</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the objective requirement associated with the given type.
 Case usages and case definitions may define an objective requirement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to inspect</dd>
<dt>Returns:</dt>
<dd>the objective requirement, or null if none exists</dd>
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
