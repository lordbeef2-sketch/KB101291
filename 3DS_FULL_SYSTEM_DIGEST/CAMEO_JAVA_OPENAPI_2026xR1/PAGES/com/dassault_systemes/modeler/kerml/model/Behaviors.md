# JAVA OPENAPI: Behaviors (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Behaviors.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Behaviors.html`
- source_sha256: `7872d7876f690f3c3beb6a9252ea2da1b665018e67f643f99e8f17d08c9797f2`
- captured_utc: `2026-07-14T16:44:47.267837+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Behaviors

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Behaviors

@OpenApiAllpublic classBehaviors
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Behavior`](kerml/Behavior.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Behaviors](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[isStepOrBehavior](#isStepOrBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns whether the given type is a [`Step`](kerml/Step.html) or [`Behavior`](kerml/Behavior.html).
`static boolean`
`[isStepOrBehavior](#isStepOrBehavior(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Returns whether the given `EClass` represents a [`Step`](kerml/Step.html)
 or a [`Behavior`](kerml/Behavior.html).
`static boolean`
`[isStepOrBehaviorResolving](#isStepOrBehaviorResolving(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](kerml/Type.html) type)`
Returns whether the given type resolves to a [`Step`](kerml/Step.html) or [`Behavior`](kerml/Behavior.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Behaviors
public Behaviors()
 ============ METHOD DETAIL ========== 
Method Details
isStepOrBehaviorResolving
public static boolean isStepOrBehaviorResolving(@CheckForNull
 [Type](kerml/Type.html) type)
Returns whether the given type resolves to a [`Step`](kerml/Step.html) or [`Behavior`](kerml/Behavior.html).
 Type resolution is performed before the check.
Parameters:
`type` - the type to test
Returns:
`true` if the resolved type is a step or behavior
isStepOrBehavior
public static boolean isStepOrBehavior(@CheckForNull
 [Type](kerml/Type.html) type)
Returns whether the given type is a [`Step`](kerml/Step.html) or [`Behavior`](kerml/Behavior.html).
Parameters:
`type` - the type to test
Returns:
`true` if the type is a step or behavior
isStepOrBehavior
public static boolean isStepOrBehavior(org.eclipse.emf.ecore.EClass eClass)
Returns whether the given `EClass` represents a [`Step`](kerml/Step.html)
 or a [`Behavior`](kerml/Behavior.html).
Parameters:
`eClass` - the class to test
Returns:
`true` if the class is a step or behavior

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Behaviors">Class Behaviors</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Behaviors</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Behaviors</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Behaviors</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStepOrBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isStepOrBehavior</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given type is a <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a> or <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStepOrBehavior(org.eclipse.emf.ecore.EClass)">isStepOrBehavior</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given <code>EClass</code> represents a <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a>
 or a <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStepOrBehaviorResolving(com.dassault_systemes.modeler.kerml.model.kerml.Type)">isStepOrBehaviorResolving</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns whether the given type resolves to a <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a> or <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.</div>
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
<h3>Behaviors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Behaviors</span>()</div>
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
<section class="detail" id="isStepOrBehaviorResolving(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isStepOrBehaviorResolving</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStepOrBehaviorResolving</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns whether the given type resolves to a <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a> or <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.
 Type resolution is performed before the check.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the resolved type is a step or behavior</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStepOrBehavior(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>isStepOrBehavior</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStepOrBehavior</span><wbr/><span class="parameters">(@CheckForNull
 <a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns whether the given type is a <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a> or <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the type is a step or behavior</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStepOrBehavior(org.eclipse.emf.ecore.EClass)">
<h3>isStepOrBehavior</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStepOrBehavior</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Returns whether the given <code>EClass</code> represents a <a href="kerml/Step.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Step</code></a>
 or a <a href="kerml/Behavior.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Behavior</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to test</dd>
<dt>Returns:</dt>
<dd><code>true</code> if the class is a step or behavior</dd>
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
