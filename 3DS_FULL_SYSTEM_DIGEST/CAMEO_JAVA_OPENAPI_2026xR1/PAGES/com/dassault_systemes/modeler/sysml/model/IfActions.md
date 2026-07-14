# JAVA OPENAPI: IfActions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/IfActions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/IfActions.html`
- source_sha256: `49001df15d896d9c3f94a7268405d3e5e69c58bf39797bab3b6d614723c69612`
- captured_utc: `2026-07-14T16:45:02.393035+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class IfActions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.IfActions

@OpenApiAllpublic classIfActions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for accessing and creating
 input parameters of an [`IfActionUsage`](sysml/IfActionUsage.html). These parameters correspond
 to the condition expression, the “then” action, and the “else” action.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[ELSE_ACTION_PARAMETER_INDEX](#ELSE_ACTION_PARAMETER_INDEX)`
Index of the “else” action input parameter.
`static final int`
`[IF_ARGUMENT_PARAMETER_INDEX](#IF_ARGUMENT_PARAMETER_INDEX)`
Index of the condition (if‑argument) input parameter.
`static final int`
`[THEN_ACTION_PARAMETER_INDEX](#THEN_ACTION_PARAMETER_INDEX)`
Index of the “then” action input parameter.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[IfActions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ActionUsage](sysml/ActionUsage.html)`
`[getOrCreateElseAction](#getOrCreateElseAction(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier))([IfActionUsage](sysml/IfActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)`
Returns the “else” action of the [`IfActionUsage`](sysml/IfActionUsage.html), creating it
 if necessary using the supplied factory.
`static [Expression](../../kerml/model/kerml/Expression.html)`
`[getOrCreateIfArgument](#getOrCreateIfArgument(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier))([IfActionUsage](sysml/IfActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Expression](../../kerml/model/kerml/Expression.html)> parameterFactory)`
Returns the condition expression of the [`IfActionUsage`](sysml/IfActionUsage.html), creating it
 if necessary using the supplied factory.
`static [ActionUsage](sysml/ActionUsage.html)`
`[getOrCreateThenAction](#getOrCreateThenAction(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier))([IfActionUsage](sysml/IfActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)`
Returns the “then” action of the [`IfActionUsage`](sysml/IfActionUsage.html), creating it
 if necessary using the supplied factory.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
IF_ARGUMENT_PARAMETER_INDEX
public static final int IF_ARGUMENT_PARAMETER_INDEX
Index of the condition (if‑argument) input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.IfActions.IF_ARGUMENT_PARAMETER_INDEX)
THEN_ACTION_PARAMETER_INDEX
public static final int THEN_ACTION_PARAMETER_INDEX
Index of the “then” action input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.IfActions.THEN_ACTION_PARAMETER_INDEX)
ELSE_ACTION_PARAMETER_INDEX
public static final int ELSE_ACTION_PARAMETER_INDEX
Index of the “else” action input parameter.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.IfActions.ELSE_ACTION_PARAMETER_INDEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
IfActions
public IfActions()
 ============ METHOD DETAIL ========== 
Method Details
getOrCreateIfArgument
public static [Expression](../../kerml/model/kerml/Expression.html) getOrCreateIfArgument([IfActionUsage](sysml/IfActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Expression](../../kerml/model/kerml/Expression.html)> parameterFactory)
Returns the condition expression of the [`IfActionUsage`](sysml/IfActionUsage.html), creating it
 if necessary using the supplied factory.
Parameters:
`actionUsage` - the if‑action usage whose condition is requested
`parameterFactory` - factory used to create the expression if missing
Returns:
existing or newly created condition expression
getOrCreateThenAction
public static [ActionUsage](sysml/ActionUsage.html) getOrCreateThenAction([IfActionUsage](sysml/IfActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)
Returns the “then” action of the [`IfActionUsage`](sysml/IfActionUsage.html), creating it
 if necessary using the supplied factory.
Parameters:
`actionUsage` - the if‑action usage whose then‑action is requested
`parameterFactory` - factory used to create the action if missing
Returns:
existing or newly created then‑action
getOrCreateElseAction
public static [ActionUsage](sysml/ActionUsage.html) getOrCreateElseAction([IfActionUsage](sysml/IfActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)
Returns the “else” action of the [`IfActionUsage`](sysml/IfActionUsage.html), creating it
 if necessary using the supplied factory.
Parameters:
`actionUsage` - the if‑action usage whose else‑action is requested
`parameterFactory` - factory used to create the action if missing
Returns:
existing or newly created else‑action

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class IfActions">Class IfActions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.IfActions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">IfActions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for accessing and creating
 input parameters of an <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>. These parameters correspond
 to the condition expression, the “then” action, and the “else” action.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ELSE_ACTION_PARAMETER_INDEX">ELSE_ACTION_PARAMETER_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the “else” action input parameter.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IF_ARGUMENT_PARAMETER_INDEX">IF_ARGUMENT_PARAMETER_INDEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Index of the condition (if‑argument) input parameter.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#THEN_ACTION_PARAMETER_INDEX">THEN_ACTION_PARAMETER_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the “then” action input parameter.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">IfActions</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateElseAction(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier)">getOrCreateElseAction</a><wbr/>(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the “else” action of the <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateIfArgument(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier)">getOrCreateIfArgument</a><wbr/>(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; parameterFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the condition expression of the <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateThenAction(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier)">getOrCreateThenAction</a><wbr/>(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the “then” action of the <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
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
<section class="detail" id="IF_ARGUMENT_PARAMETER_INDEX">
<h3>IF_ARGUMENT_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">IF_ARGUMENT_PARAMETER_INDEX</span></div>
<div class="block">Index of the condition (if‑argument) input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.IfActions.IF_ARGUMENT_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="THEN_ACTION_PARAMETER_INDEX">
<h3>THEN_ACTION_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">THEN_ACTION_PARAMETER_INDEX</span></div>
<div class="block">Index of the “then” action input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.IfActions.THEN_ACTION_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ELSE_ACTION_PARAMETER_INDEX">
<h3>ELSE_ACTION_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ELSE_ACTION_PARAMETER_INDEX</span></div>
<div class="block">Index of the “else” action input parameter.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.IfActions.ELSE_ACTION_PARAMETER_INDEX">Constant Field Values</a></li>
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
<h3>IfActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IfActions</span>()</div>
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
<section class="detail" id="getOrCreateIfArgument(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier)">
<h3>getOrCreateIfArgument</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getOrCreateIfArgument</span><wbr/><span class="parameters">(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; parameterFactory)</span></div>
<div class="block">Returns the condition expression of the <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the if‑action usage whose condition is requested</dd>
<dd><code>parameterFactory</code> - factory used to create the expression if missing</dd>
<dt>Returns:</dt>
<dd>existing or newly created condition expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateThenAction(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier)">
<h3>getOrCreateThenAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></span> <span class="element-name">getOrCreateThenAction</span><wbr/><span class="parameters">(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</span></div>
<div class="block">Returns the “then” action of the <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the if‑action usage whose then‑action is requested</dd>
<dd><code>parameterFactory</code> - factory used to create the action if missing</dd>
<dt>Returns:</dt>
<dd>existing or newly created then‑action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateElseAction(com.dassault_systemes.modeler.sysml.model.sysml.IfActionUsage,java.util.function.Supplier)">
<h3>getOrCreateElseAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></span> <span class="element-name">getOrCreateElseAction</span><wbr/><span class="parameters">(<a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">IfActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</span></div>
<div class="block">Returns the “else” action of the <a href="sysml/IfActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>IfActionUsage</code></a>, creating it
 if necessary using the supplied factory.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the if‑action usage whose else‑action is requested</dd>
<dd><code>parameterFactory</code> - factory used to create the action if missing</dd>
<dt>Returns:</dt>
<dd>existing or newly created else‑action</dd>
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
