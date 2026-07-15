# JAVA OPENAPI: AssignmentActions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/AssignmentActions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/AssignmentActions.html`
- source_sha256: `a012da31e35f02acc76bac730aae81988399ef93d1318c928e60dfb45cc14d0a`
- captured_utc: `2026-07-14T16:45:02.242033+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class AssignmentActions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.AssignmentActions

@OpenApiAllpublic classAssignmentActions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[REPLACEMENT_VALUES_PARAMETER_INDEX](#REPLACEMENT_VALUES_PARAMETER_INDEX)`
Index of the replacement-values input parameter.
`static final int`
`[TARGET_PARAMETER_INDEX](#TARGET_PARAMETER_INDEX)`
Index of the target input parameter.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AssignmentActions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[createTargetParameterStartingAt](#createTargetParameterStartingAt(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) targetParameter)`
Initializes a newly created target parameter with a nested reference structure:
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreateReplacementValuesParameter](#getOrCreateReplacementValuesParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)`
Returns the replacement-values parameter of the assignment action,
 creating it if necessary.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreateTargetParameter](#getOrCreateTargetParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)`
Returns the target parameter of the assignment action, creating it if necessary.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOwnedReplacementValuesParameter](#getOwnedReplacementValuesParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)`
Returns the owned replacement-values parameter of the assignment action,
 or `null` if it has not been created.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOwnedTargetParameter](#getOwnedTargetParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)`
Returns the owned target parameter of the assignment action, or `null`
 if it has not been created.
`static [Membership](../../kerml/model/kerml/Membership.html)`
`[getReferentMembership](#getReferentMembership(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)`
Returns the referent membership of the assignment action, excluding
 feature memberships.
`static void`
`[setReferent](#setReferent(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage,
 [Feature](../../kerml/model/kerml/Feature.html) referent)`
Sets the referent of the assignment action.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TARGET_PARAMETER_INDEX
public static final int TARGET_PARAMETER_INDEX
Index of the target input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AssignmentActions.TARGET_PARAMETER_INDEX)
REPLACEMENT_VALUES_PARAMETER_INDEX
public static final int REPLACEMENT_VALUES_PARAMETER_INDEX
Index of the replacement-values input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AssignmentActions.REPLACEMENT_VALUES_PARAMETER_INDEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AssignmentActions
public AssignmentActions()
 ============ METHOD DETAIL ========== 
Method Details
getOwnedTargetParameter
@CheckForNullpublic static [Feature](../../kerml/model/kerml/Feature.html) getOwnedTargetParameter([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)
Returns the owned target parameter of the assignment action, or `null`
 if it has not been created.
Parameters:
`actionUsage` - the assignment action usage
Returns:
the owned target parameter, or `null`
getOrCreateTargetParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreateTargetParameter([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)
Returns the target parameter of the assignment action, creating it if necessary.
 When created, the parameter is initialized with a nested reference structure
 representing the “startingAt → accessedFeature” pattern.
Parameters:
`actionUsage` - the assignment action usage
Returns:
the existing or newly created target parameter
createTargetParameterStartingAt
public static void createTargetParameterStartingAt([Feature](../../kerml/model/kerml/Feature.html) targetParameter)
Initializes a newly created target parameter with a nested reference structure:
 targetParameter
 └─ startingAt : ReferenceUsage
 └─ accessedFeature : ReferenceUsage
 This mirrors the typical structure of assignment target expressions.
Parameters:
`targetParameter` - the target parameter to initialize
getOwnedReplacementValuesParameter
@CheckForNullpublic static [Feature](../../kerml/model/kerml/Feature.html) getOwnedReplacementValuesParameter([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)
Returns the owned replacement-values parameter of the assignment action,
 or `null` if it has not been created.
Parameters:
`actionUsage` - the assignment action usage
Returns:
the owned replacement-values parameter, or `null`
getOrCreateReplacementValuesParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreateReplacementValuesParameter([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)
Returns the replacement-values parameter of the assignment action,
 creating it if necessary.
Parameters:
`actionUsage` - the assignment action usage
Returns:
the existing or newly created replacement-values parameter
setReferent
public static void setReferent([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage,
 [Feature](../../kerml/model/kerml/Feature.html) referent)
Sets the referent of the assignment action. The referent membership is
 inserted immediately after the target parameter.
Parameters:
`actionUsage` - the assignment action usage
`referent` - the feature to set as the referent
getReferentMembership
@CheckForNullpublic static [Membership](../../kerml/model/kerml/Membership.html) getReferentMembership([AssignmentActionUsage](sysml/AssignmentActionUsage.html) actionUsage)
Returns the referent membership of the assignment action, excluding
 feature memberships. This identifies the membership that holds the
 referent feature for the assignment.
Parameters:
`actionUsage` - the assignment action usage
Returns:
the referent membership, or `null`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class AssignmentActions">Class AssignmentActions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.AssignmentActions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AssignmentActions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REPLACEMENT_VALUES_PARAMETER_INDEX">REPLACEMENT_VALUES_PARAMETER_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the replacement-values input parameter.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_PARAMETER_INDEX">TARGET_PARAMETER_INDEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Index of the target input parameter.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AssignmentActions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTargetParameterStartingAt(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">createTargetParameterStartingAt</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> targetParameter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes a newly created target parameter with a nested reference structure:</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateReplacementValuesParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">getOrCreateReplacementValuesParameter</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the replacement-values parameter of the assignment action,
 creating it if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateTargetParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">getOrCreateTargetParameter</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target parameter of the assignment action, creating it if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedReplacementValuesParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">getOwnedReplacementValuesParameter</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned replacement-values parameter of the assignment action,
 or <code>null</code> if it has not been created.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedTargetParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">getOwnedTargetParameter</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the owned target parameter of the assignment action, or <code>null</code>
 if it has not been created.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getReferentMembership(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">getReferentMembership</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the referent membership of the assignment action, excluding
 feature memberships.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferent(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setReferent</a><wbr/>(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage,
 <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the referent of the assignment action.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="TARGET_PARAMETER_INDEX">
<h3>TARGET_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TARGET_PARAMETER_INDEX</span></div>
<div class="block">Index of the target input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AssignmentActions.TARGET_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REPLACEMENT_VALUES_PARAMETER_INDEX">
<h3>REPLACEMENT_VALUES_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">REPLACEMENT_VALUES_PARAMETER_INDEX</span></div>
<div class="block">Index of the replacement-values input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.AssignmentActions.REPLACEMENT_VALUES_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>AssignmentActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AssignmentActions</span>()</div>
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
<section class="detail" id="getOwnedTargetParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">
<h3>getOwnedTargetParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedTargetParameter</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the owned target parameter of the assignment action, or <code>null</code>
 if it has not been created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the assignment action usage</dd>
<dt>Returns:</dt>
<dd>the owned target parameter, or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateTargetParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">
<h3>getOrCreateTargetParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateTargetParameter</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the target parameter of the assignment action, creating it if necessary.
 When created, the parameter is initialized with a nested reference structure
 representing the “startingAt → accessedFeature” pattern.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the assignment action usage</dd>
<dt>Returns:</dt>
<dd>the existing or newly created target parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTargetParameterStartingAt(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>createTargetParameterStartingAt</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createTargetParameterStartingAt</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> targetParameter)</span></div>
<div class="block">Initializes a newly created target parameter with a nested reference structure:
 <pre>
 targetParameter
   └─ startingAt : ReferenceUsage
        └─ accessedFeature : ReferenceUsage
 </pre>
 This mirrors the typical structure of assignment target expressions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetParameter</code> - the target parameter to initialize</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedReplacementValuesParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">
<h3>getOwnedReplacementValuesParameter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOwnedReplacementValuesParameter</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the owned replacement-values parameter of the assignment action,
 or <code>null</code> if it has not been created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the assignment action usage</dd>
<dt>Returns:</dt>
<dd>the owned replacement-values parameter, or <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateReplacementValuesParameter(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">
<h3>getOrCreateReplacementValuesParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateReplacementValuesParameter</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the replacement-values parameter of the assignment action,
 creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the assignment action usage</dd>
<dt>Returns:</dt>
<dd>the existing or newly created replacement-values parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReferent(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setReferent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setReferent</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage,
 <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> referent)</span></div>
<div class="block">Sets the referent of the assignment action. The referent membership is
 inserted immediately after the target parameter.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the assignment action usage</dd>
<dd><code>referent</code> - the feature to set as the referent</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferentMembership(com.dassault_systemes.modeler.sysml.model.sysml.AssignmentActionUsage)">
<h3>getReferentMembership</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Membership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Membership</a></span> <span class="element-name">getReferentMembership</span><wbr/><span class="parameters">(<a href="sysml/AssignmentActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">AssignmentActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the referent membership of the assignment action, excluding
 feature memberships. This identifies the membership that holds the
 referent feature for the assignment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the assignment action usage</dd>
<dt>Returns:</dt>
<dd>the referent membership, or <code>null</code></dd>
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
