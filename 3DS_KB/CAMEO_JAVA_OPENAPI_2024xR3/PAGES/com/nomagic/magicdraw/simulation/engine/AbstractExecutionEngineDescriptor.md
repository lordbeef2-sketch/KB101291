# JAVA OPENAPI: AbstractExecutionEngineDescriptor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/simulation/engine/AbstractExecutionEngineDescriptor.html
- source_path: `com/nomagic/magicdraw/simulation/engine/AbstractExecutionEngineDescriptor.html`
- source_sha256: `67a97882bef0786b11f370507b071cdb7bb72b488bc6460371ba90eab410fb4d`
- captured_utc: `2026-07-14T16:55:33.333211+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.engine](package-summary.html)

## Class AbstractExecutionEngineDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.engine.AbstractExecutionEngineDescriptor

All Implemented Interfaces:
`[ExecutionEngineDescriptor](ExecutionEngineDescriptor.html)`

@OpenApipublic abstract classAbstractExecutionEngineDescriptor
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ExecutionEngineDescriptor](ExecutionEngineDescriptor.html)

The abstract implementation class of `ExecutionEngineDescriptor`.
 It provides some default value to the extended engine descriptor.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractExecutionEngineDescriptor](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`com.nomagic.magicdraw.simulation.listener.DurationListener`
`[createDurationListener](#createDurationListener(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))([SimulationSession](../execution/session/SimulationSession.html) session)`
Deprecated.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.simulation.engine.[ExecutionEngineDescriptor](ExecutionEngineDescriptor.html)
`[canExecute](ExecutionEngineDescriptor.html#canExecute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [createEngine](ExecutionEngineDescriptor.html#createEngine()), [getEngineName](ExecutionEngineDescriptor.html#getEngineName())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractExecutionEngineDescriptor
public AbstractExecutionEngineDescriptor()
 ============ METHOD DETAIL ========== 
Method Details
createDurationListener
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public com.nomagic.magicdraw.simulation.listener.DurationListener createDurationListener([SimulationSession](../execution/session/SimulationSession.html) session)
Deprecated.
Description copied from interface: `[ExecutionEngineDescriptor](ExecutionEngineDescriptor.html#createDurationListener(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))`
Return specific DurationListener of an engine created from this descriptor.
Specified by:
`[createDurationListener](ExecutionEngineDescriptor.html#createDurationListener(com.nomagic.magicdraw.simulation.execution.session.SimulationSession))` in interface `[ExecutionEngineDescriptor](ExecutionEngineDescriptor.html)`
Parameters:
`session` - `SimulationSession` that this duration listener registered to its engine
Returns:
durationListener DurationListener

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.engine</a></div>
<h1 class="title" title="Class AbstractExecutionEngineDescriptor">Class AbstractExecutionEngineDescriptor</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.engine.AbstractExecutionEngineDescriptor</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractExecutionEngineDescriptor</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a></span></div>
<div class="block">The abstract implementation class of <code>ExecutionEngineDescriptor</code>.
 It provides some default value to the extended engine descriptor.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractExecutionEngineDescriptor</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>com.nomagic.magicdraw.simulation.listener.DurationListener</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createDurationListener(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">createDurationListener</a><wbr/>(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.simulation.engine.ExecutionEngineDescriptor">Methods inherited from interface com.nomagic.magicdraw.simulation.engine.<a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a></h3>
<code><a href="ExecutionEngineDescriptor.html#canExecute(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">canExecute</a>, <a href="ExecutionEngineDescriptor.html#createEngine()">createEngine</a>, <a href="ExecutionEngineDescriptor.html#getEngineName()">getEngineName</a></code></div>
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
<h3>AbstractExecutionEngineDescriptor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractExecutionEngineDescriptor</span>()</div>
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
<section class="detail" id="createDurationListener(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">
<h3>createDurationListener</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.simulation.listener.DurationListener</span> <span class="element-name">createDurationListener</span><wbr/><span class="parameters">(<a href="../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a> session)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ExecutionEngineDescriptor.html#createDurationListener(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">ExecutionEngineDescriptor</a></code></span></div>
<div class="block">Return specific DurationListener of an engine created from this descriptor.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ExecutionEngineDescriptor.html#createDurationListener(com.nomagic.magicdraw.simulation.execution.session.SimulationSession)">createDurationListener</a></code> in interface <code><a href="ExecutionEngineDescriptor.html" title="interface in com.nomagic.magicdraw.simulation.engine">ExecutionEngineDescriptor</a></code></dd>
<dt>Parameters:</dt>
<dd><code>session</code> - <code>SimulationSession</code> that this duration listener registered to its engine</dd>
<dt>Returns:</dt>
<dd>durationListener DurationListener</dd>
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
