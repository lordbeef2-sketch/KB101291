# JAVA OPENAPI: Constraints (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Constraints.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Constraints.html`
- source_sha256: `fd79117d4e390898c292cbba4805d6b2671af1c12e3e3ad9fe3da11fd17b9213`
- captured_utc: `2026-07-14T16:45:02.276033+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Constraints

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Constraints

@OpenApiAllpublic classConstraints
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Constraints](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Expression](../../kerml/model/kerml/Expression.html)>`
`[getOwnedExpressions](#getOwnedExpressions(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage))([ConstraintUsage](sysml/ConstraintUsage.html) constraintUsage)`
Returns a stream of all [`Expression`](../../kerml/model/kerml/Expression.html) elements owned by the given
 [`ConstraintUsage`](sysml/ConstraintUsage.html).
`static boolean`
`[isAssumeConstraint](#isAssumeConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) constraint)`
Returns whether the given constraint is an assumption constraint.
`static boolean`
`[isConstraintUsageOrDefinition](#isConstraintUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Returns whether the given element is a [`ConstraintUsage`](sysml/ConstraintUsage.html) or
 [`ConstraintDefinition`](sysml/ConstraintDefinition.html).
`static boolean`
`[isConstraintUsageOrDefinition](#isConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a constraint usage
 or constraint definition.
`static boolean`
`[isPureConstraintUsageOrDefinition](#isPureConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` is exactly the pure
 [`ConstraintUsage`](sysml/ConstraintUsage.html) or [`ConstraintDefinition`](sysml/ConstraintDefinition.html) type.
`static boolean`
`[isRequireConstraint](#isRequireConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) constraint)`
Returns whether the given constraint is a requirement constraint.
`static boolean`
`[isRequirementAssumeOrRequire](#isRequirementAssumeOrRequire(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) constraint)`
Returns whether the given element is a [`ConstraintUsage`](sysml/ConstraintUsage.html) that is
 either an assumption or a requirement constraint.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Constraints
public Constraints()
 ============ METHOD DETAIL ========== 
Method Details
isConstraintUsageOrDefinition
public static boolean isConstraintUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Returns whether the given element is a [`ConstraintUsage`](sysml/ConstraintUsage.html) or
 [`ConstraintDefinition`](sysml/ConstraintDefinition.html).
Parameters:
`element` - the element to test
Returns:
`true` if the element is a constraint usage or definition
isConstraintUsageOrDefinition
public static boolean isConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a constraint usage
 or constraint definition.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a constraint usage or definition
isPureConstraintUsageOrDefinition
public static boolean isPureConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` is exactly the pure
 [`ConstraintUsage`](sysml/ConstraintUsage.html) or [`ConstraintDefinition`](sysml/ConstraintDefinition.html) type.
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is the pure constraint usage or definition type
getOwnedExpressions
public static [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Expression](../../kerml/model/kerml/Expression.html)> getOwnedExpressions([ConstraintUsage](sysml/ConstraintUsage.html) constraintUsage)
Returns a stream of all [`Expression`](../../kerml/model/kerml/Expression.html) elements owned by the given
 [`ConstraintUsage`](sysml/ConstraintUsage.html). Includes expressions owned by the constraint
 definition and the usage itself.
 Special handling is applied for [`AssertConstraintUsage`](sysml/AssertConstraintUsage.html), which
 delegates to its asserted constraint.
Parameters:
`constraintUsage` - the constraint usage whose expressions are requested
Returns:
a stream of owned expressions
isAssumeConstraint
public static boolean isAssumeConstraint([Element](../../kerml/model/kerml/Element.html) constraint)
Returns whether the given constraint is an assumption constraint.
 Assumption constraints are identified through their
 [`RequirementConstraintMembership`](sysml/RequirementConstraintMembership.html) kind.
Parameters:
`constraint` - the constraint element to test
Returns:
`true` if the constraint is an assumption
isRequireConstraint
public static boolean isRequireConstraint([Element](../../kerml/model/kerml/Element.html) constraint)
Returns whether the given constraint is a requirement constraint.
 Requirement constraints are identified through their
 [`RequirementConstraintMembership`](sysml/RequirementConstraintMembership.html) kind.
Parameters:
`constraint` - the constraint element to test
Returns:
`true` if the constraint is a requirement
isRequirementAssumeOrRequire
public static boolean isRequirementAssumeOrRequire(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) constraint)
Returns whether the given element is a [`ConstraintUsage`](sysml/ConstraintUsage.html) that is
 either an assumption or a requirement constraint.
Parameters:
`constraint` - the element to test
Returns:
`true` if the element is an assume or require constraint

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Constraints">Class Constraints</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Constraints</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Constraints</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Constraints</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOwnedExpressions(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage)">getOwnedExpressions</a><wbr/>(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> constraintUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a stream of all <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a> elements owned by the given
 <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAssumeConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isAssumeConstraint</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given constraint is an assumption constraint.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isConstraintUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isConstraintUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is a <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a> or
 <a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isConstraintUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a constraint usage
 or constraint definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPureConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isPureConstraintUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> is exactly the pure
 <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a> or <a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintDefinition</code></a> type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequireConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isRequireConstraint</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> constraint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given constraint is a requirement constraint.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRequirementAssumeOrRequire(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isRequirementAssumeOrRequire</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> constraint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given element is a <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a> that is
 either an assumption or a requirement constraint.</div>
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
<h3>Constraints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Constraints</span>()</div>
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
<section class="detail" id="isConstraintUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isConstraintUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isConstraintUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Returns whether the given element is a <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a> or
 <a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is a constraint usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isConstraintUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isConstraintUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a constraint usage
 or constraint definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a constraint usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPureConstraintUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isPureConstraintUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPureConstraintUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> is exactly the pure
 <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a> or <a href="sysml/ConstraintDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintDefinition</code></a> type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is the pure constraint usage or definition type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOwnedExpressions(com.dassault_systemes.modeler.sysml.model.sysml.ConstraintUsage)">
<h3>getOwnedExpressions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</span> <span class="element-name">getOwnedExpressions</span><wbr/><span class="parameters">(<a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConstraintUsage</a> constraintUsage)</span></div>
<div class="block">Returns a stream of all <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Expression</code></a> elements owned by the given
 <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a>. Includes expressions owned by the constraint
 definition and the usage itself.
 <p>
 Special handling is applied for <a href="sysml/AssertConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>AssertConstraintUsage</code></a>, which
 delegates to its asserted constraint.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraintUsage</code> - the constraint usage whose expressions are requested</dd>
<dt>Returns:</dt>
<dd>a stream of owned expressions</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAssumeConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isAssumeConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAssumeConstraint</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> constraint)</span></div>
<div class="block">Returns whether the given constraint is an assumption constraint.
 Assumption constraints are identified through their
 <a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementConstraintMembership</code></a> kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - the constraint element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the constraint is an assumption</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequireConstraint(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isRequireConstraint</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequireConstraint</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> constraint)</span></div>
<div class="block">Returns whether the given constraint is a requirement constraint.
 Requirement constraints are identified through their
 <a href="sysml/RequirementConstraintMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RequirementConstraintMembership</code></a> kind.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - the constraint element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the constraint is a requirement</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequirementAssumeOrRequire(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isRequirementAssumeOrRequire</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequirementAssumeOrRequire</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> constraint)</span></div>
<div class="block">Returns whether the given element is a <a href="sysml/ConstraintUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ConstraintUsage</code></a> that is
 either an assumption or a requirement constraint.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraint</code> - the element to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the element is an assume or require constraint</dd>
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
