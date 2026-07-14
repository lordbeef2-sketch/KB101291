# JAVA OPENAPI: WhileLoopActions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/WhileLoopActions.html
- source_path: `com/dassault_systemes/modeler/sysml/model/WhileLoopActions.html`
- source_sha256: `4ad7b91ba6c501e66b89ef9ff138475b7168d9d40f13375e509ff6952b8c9a81`
- captured_utc: `2026-07-14T16:45:02.765046+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class WhileLoopActions

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.WhileLoopActions

@OpenApiAllpublic classWhileLoopActions
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for [`WhileLoopActionUsage`](sysml/WhileLoopActionUsage.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[BODY_ARGUMENT_PARAMETER_INDEX](#BODY_ARGUMENT_PARAMETER_INDEX)`
Index of the loop body argument.
`static final int`
`[UNTIL_ARGUMENT_PARAMETER_INDEX](#UNTIL_ARGUMENT_PARAMETER_INDEX)`
Index of the "until" condition argument.
`static final int`
`[WHILE_ARGUMENT_PARAMETER_INDEX](#WHILE_ARGUMENT_PARAMETER_INDEX)`
Index of the "while" condition argument.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[WhileLoopActions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [ActionUsage](sysml/ActionUsage.html)`
`[getOrCreateBodyAction](#getOrCreateBodyAction(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier))([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)`
Returns the loop body action of the action usage,
 creating it if necessary.
`static [Expression](../../kerml/model/kerml/Expression.html)`
`[getOrCreateUntilArgument](#getOrCreateUntilArgument(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier))([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Expression](../../kerml/model/kerml/Expression.html)> parameterFactory)`
Returns the "until" condition expression of the action usage,
 creating it if necessary.
`static [Expression](../../kerml/model/kerml/Expression.html)`
`[getOrCreateWhileArgument](#getOrCreateWhileArgument(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier))([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Expression](../../kerml/model/kerml/Expression.html)> parameterFactory)`
Returns the "while" condition expression of the action usage,
 creating it if necessary.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
WHILE_ARGUMENT_PARAMETER_INDEX
public static final int WHILE_ARGUMENT_PARAMETER_INDEX
Index of the "while" condition argument.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.WhileLoopActions.WHILE_ARGUMENT_PARAMETER_INDEX)
BODY_ARGUMENT_PARAMETER_INDEX
public static final int BODY_ARGUMENT_PARAMETER_INDEX
Index of the loop body argument.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.WhileLoopActions.BODY_ARGUMENT_PARAMETER_INDEX)
UNTIL_ARGUMENT_PARAMETER_INDEX
public static final int UNTIL_ARGUMENT_PARAMETER_INDEX
Index of the "until" condition argument.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.WhileLoopActions.UNTIL_ARGUMENT_PARAMETER_INDEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
WhileLoopActions
public WhileLoopActions()
 ============ METHOD DETAIL ========== 
Method Details
getOrCreateWhileArgument
public static [Expression](../../kerml/model/kerml/Expression.html) getOrCreateWhileArgument([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Expression](../../kerml/model/kerml/Expression.html)> parameterFactory)
Returns the "while" condition expression of the action usage,
 creating it if necessary.
Parameters:
`actionUsage` - the while-loop action usage
`parameterFactory` - factory used to create the expression if missing
Returns:
existing or newly created while-condition expression
getOrCreateBodyAction
public static [ActionUsage](sysml/ActionUsage.html) getOrCreateBodyAction([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[ActionUsage](sysml/ActionUsage.html)> parameterFactory)
Returns the loop body action of the action usage,
 creating it if necessary.
Parameters:
`actionUsage` - the while-loop action usage
`parameterFactory` - factory used to create the body action if missing
Returns:
existing or newly created body action
getOrCreateUntilArgument
public static [Expression](../../kerml/model/kerml/Expression.html) getOrCreateUntilArgument([WhileLoopActionUsage](sysml/WhileLoopActionUsage.html) actionUsage,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<[Expression](../../kerml/model/kerml/Expression.html)> parameterFactory)
Returns the "until" condition expression of the action usage,
 creating it if necessary.
Parameters:
`actionUsage` - the while-loop action usage
`parameterFactory` - factory used to create the expression if missing
Returns:
existing or newly created until-condition expression

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class WhileLoopActions">Class WhileLoopActions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.WhileLoopActions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">WhileLoopActions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for <a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>WhileLoopActionUsage</code></a></div>
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
<div class="block">Index of the loop body argument.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#UNTIL_ARGUMENT_PARAMETER_INDEX">UNTIL_ARGUMENT_PARAMETER_INDEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Index of the "until" condition argument.</div>
</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#WHILE_ARGUMENT_PARAMETER_INDEX">WHILE_ARGUMENT_PARAMETER_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the "while" condition argument.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">WhileLoopActions</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateBodyAction(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier)">getOrCreateBodyAction</a><wbr/>(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the loop body action of the action usage,
 creating it if necessary.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateUntilArgument(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier)">getOrCreateUntilArgument</a><wbr/>(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; parameterFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the "until" condition expression of the action usage,
 creating it if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateWhileArgument(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier)">getOrCreateWhileArgument</a><wbr/>(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; parameterFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the "while" condition expression of the action usage,
 creating it if necessary.</div>
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
<section class="detail" id="WHILE_ARGUMENT_PARAMETER_INDEX">
<h3>WHILE_ARGUMENT_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">WHILE_ARGUMENT_PARAMETER_INDEX</span></div>
<div class="block">Index of the "while" condition argument.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.WhileLoopActions.WHILE_ARGUMENT_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BODY_ARGUMENT_PARAMETER_INDEX">
<h3>BODY_ARGUMENT_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">BODY_ARGUMENT_PARAMETER_INDEX</span></div>
<div class="block">Index of the loop body argument.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.WhileLoopActions.BODY_ARGUMENT_PARAMETER_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="UNTIL_ARGUMENT_PARAMETER_INDEX">
<h3>UNTIL_ARGUMENT_PARAMETER_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">UNTIL_ARGUMENT_PARAMETER_INDEX</span></div>
<div class="block">Index of the "until" condition argument.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.sysml.model.WhileLoopActions.UNTIL_ARGUMENT_PARAMETER_INDEX">Constant Field Values</a></li>
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
<h3>WhileLoopActions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">WhileLoopActions</span>()</div>
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
<section class="detail" id="getOrCreateWhileArgument(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier)">
<h3>getOrCreateWhileArgument</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getOrCreateWhileArgument</span><wbr/><span class="parameters">(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; parameterFactory)</span></div>
<div class="block">Returns the "while" condition expression of the action usage,
 creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the while-loop action usage</dd>
<dd><code>parameterFactory</code> - factory used to create the expression if missing</dd>
<dt>Returns:</dt>
<dd>existing or newly created while-condition expression</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateBodyAction(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier)">
<h3>getOrCreateBodyAction</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a></span> <span class="element-name">getOrCreateBodyAction</span><wbr/><span class="parameters">(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="sysml/ActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ActionUsage</a>&gt; parameterFactory)</span></div>
<div class="block">Returns the loop body action of the action usage,
 creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the while-loop action usage</dd>
<dd><code>parameterFactory</code> - factory used to create the body action if missing</dd>
<dt>Returns:</dt>
<dd>existing or newly created body action</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateUntilArgument(com.dassault_systemes.modeler.sysml.model.sysml.WhileLoopActionUsage,java.util.function.Supplier)">
<h3>getOrCreateUntilArgument</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a></span> <span class="element-name">getOrCreateUntilArgument</span><wbr/><span class="parameters">(<a href="sysml/WhileLoopActionUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">WhileLoopActionUsage</a> actionUsage,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt; parameterFactory)</span></div>
<div class="block">Returns the "until" condition expression of the action usage,
 creating it if necessary.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>actionUsage</code> - the while-loop action usage</dd>
<dd><code>parameterFactory</code> - factory used to create the expression if missing</dd>
<dt>Returns:</dt>
<dd>existing or newly created until-condition expression</dd>
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
