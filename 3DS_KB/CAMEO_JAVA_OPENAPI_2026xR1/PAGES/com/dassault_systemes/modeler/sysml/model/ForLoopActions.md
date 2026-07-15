# JAVA OPENAPI: ForLoopActions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/ForLoopActions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/ForLoopActions.html`
- source_sha256: `eb374cc86ec76cb0b0ffd4f16f7fd6b38d146e6c4d98eeeb467d3c1d55759c0b`
- captured_utc: `2026-07-14T16:45:02.374035+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class ForLoopActions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.ForLoopActions

@OpenApiAllpublic classForLoopActions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for accessing and creating
 input parameters and loop‑variable elements of a [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html).
 A for‑loop action typically includes:
 a sequence expression supplying iteration values,
a body action executed for each value, and
a loop variable referencing the current iteration element.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[BODY_ARGUMENT_PARAMETER_INDEX](#BODY_ARGUMENT_PARAMETER_INDEX)`
Index of the loop body action input parameter.
`static final int`
`[SEQ_ARGUMENT_PARAMETER_INDEX](#SEQ_ARGUMENT_PARAMETER_INDEX)`
Index of the sequence (iteration source) input parameter.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ForLoopActions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ActionUsage](sysml/ActionUsage.html)`
`[getOrCreateBodyAction](#getOrCreateBodyAction(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,java.util.function.Supplier))([ForLoopActionUsage](sysml/ForLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)`
Returns the loop body action of the [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html), creating it
 if necessary using the supplied factory.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreateLoopVariable](#getOrCreateLoopVariable(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage))([ForLoopActionUsage](sysml/ForLoopActionUsage.html) actionUsage)`
Returns the loop variable of the [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html), creating it
 if necessary.
`static [Feature](../../kerml/model/kerml/Feature.html)`
`[getOrCreateSeqArgumentParameter](#getOrCreateSeqArgumentParameter(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage))([ForLoopActionUsage](sysml/ForLoopActionUsage.html) actionUsage)`
Returns the sequence argument of the [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html), creating it
 if necessary.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SEQ_ARGUMENT_PARAMETER_INDEX
public static final int SEQ_ARGUMENT_PARAMETER_INDEX
Index of the sequence (iteration source) input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.ForLoopActions.SEQ_ARGUMENT_PARAMETER_INDEX)
BODY_ARGUMENT_PARAMETER_INDEX
public static final int BODY_ARGUMENT_PARAMETER_INDEX
Index of the loop body action input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.ForLoopActions.BODY_ARGUMENT_PARAMETER_INDEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ForLoopActions
public ForLoopActions()
 ============ METHOD DETAIL ========== 
Method Details
getOrCreateSeqArgumentParameter
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreateSeqArgumentParameter([ForLoopActionUsage](sysml/ForLoopActionUsage.html) actionUsage)
Returns the sequence argument of the [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html), creating it
 if necessary. The returned feature represents the iteration source.
Parameters:
`actionUsage` - the for‑loop action usage whose sequence argument is requested
Returns:
existing or newly created sequence argument feature
getOrCreateBodyAction
public static [ActionUsage](sysml/ActionUsage.html) getOrCreateBodyAction([ForLoopActionUsage](sysml/ForLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)
Returns the loop body action of the [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html), creating it
 if necessary using the supplied factory.
Parameters:
`actionUsage` - the for‑loop action usage whose body action is requested
`parameterFactory` - factory used to create the action if missing
Returns:
existing or newly created body action
getOrCreateLoopVariable
public static [Feature](../../kerml/model/kerml/Feature.html) getOrCreateLoopVariable([ForLoopActionUsage](sysml/ForLoopActionUsage.html) actionUsage)
Returns the loop variable of the [`ForLoopActionUsage`](sysml/ForLoopActionUsage.html), creating it
 if necessary. The loop variable is a [`ReferenceUsage`](sysml/ReferenceUsage.html) owned by the
 action and represents the current iteration element.
Parameters:
`actionUsage` - the for‑loop action usage whose loop variable is requested
Returns:
existing or newly created loop variable feature

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class ForLoopActions">Class ForLoopActions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.ForLoopActions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ForLoopActions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for accessing and creating
 input parameters and loop‑variable elements of a <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>.
 <p>
 A for‑loop action typically includes:
 <ul>
<li>a sequence expression supplying iteration values,</li>
<li>a body action executed for each value, and</li>
<li>a loop variable referencing the current iteration element.</li>
</ul></p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BODY_ARGUMENT_PARAMETER_INDEX">BODY_ARGUMENT_PARAMETER_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the loop body action input parameter.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SEQ_ARGUMENT_PARAMETER_INDEX">SEQ_ARGUMENT_PARAMETER_INDEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Index of the sequence (iteration source) input parameter.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ForLoopActions</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateBodyAction(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,java.util.function.Supplier)">getOrCreateBodyAction</a><wbr/>(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the loop body action of the <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateLoopVariable(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage)">getOrCreateLoopVariable</a><wbr/>(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> actionUsage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the loop variable of the <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>, creating it
 if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateSeqArgumentParameter(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage)">getOrCreateSeqArgumentParameter</a><wbr/>(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> actionUsage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the sequence argument of the <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>, creating it
 if necessary.</div>
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
<section class="detail" id="SEQ_ARGUMENT_PARAMETER_INDEX">
<h3>SEQ_ARGUMENT_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SEQ_ARGUMENT_PARAMETER_INDEX</span></div>
<div class="block">Index of the sequence (iteration source) input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.ForLoopActions.SEQ_ARGUMENT_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BODY_ARGUMENT_PARAMETER_INDEX">
<h3>BODY_ARGUMENT_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">BODY_ARGUMENT_PARAMETER_INDEX</span></div>
<div class="block">Index of the loop body action input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.ForLoopActions.BODY_ARGUMENT_PARAMETER_INDEX">Constant Field Values</a></li>
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
<h3>ForLoopActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ForLoopActions</span>()</div>
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
<section class="detail" id="getOrCreateSeqArgumentParameter(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage)">
<h3>getOrCreateSeqArgumentParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateSeqArgumentParameter</span><wbr/><span class="parameters">(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the sequence argument of the <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>, creating it
 if necessary. The returned feature represents the iteration source.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the for‑loop action usage whose sequence argument is requested</dd>
<dt>Returns:</dt>
<dd>existing or newly created sequence argument feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateBodyAction(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage,java.util.function.Supplier)">
<h3>getOrCreateBodyAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></span> <span class="element-name">getOrCreateBodyAction</span><wbr/><span class="parameters">(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</span></div>
<div class="block">Returns the loop body action of the <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the for‑loop action usage whose body action is requested</dd>
<dd><code>parameterFactory</code> - factory used to create the action if missing</dd>
<dt>Returns:</dt>
<dd>existing or newly created body action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateLoopVariable(com.dassault_systemes.modeler.sysml.model.sysml.ForLoopActionUsage)">
<h3>getOrCreateLoopVariable</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getOrCreateLoopVariable</span><wbr/><span class="parameters">(<a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ForLoopActionUsage</a> actionUsage)</span></div>
<div class="block">Returns the loop variable of the <a href="sysml/ForLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ForLoopActionUsage</code></a>, creating it
 if necessary. The loop variable is a <a href="sysml/ReferenceUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ReferenceUsage</code></a> owned by the
 action and represents the current iteration element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the for‑loop action usage whose loop variable is requested</dd>
<dt>Returns:</dt>
<dd>existing or newly created loop variable feature</dd>
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
