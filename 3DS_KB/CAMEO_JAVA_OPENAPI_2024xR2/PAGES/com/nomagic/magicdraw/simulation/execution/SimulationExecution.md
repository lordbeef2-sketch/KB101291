# JAVA OPENAPI: SimulationExecution (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/simulation/execution/SimulationExecution.html
- source_path: `com/nomagic/magicdraw/simulation/execution/SimulationExecution.html`
- source_sha256: `980452a1971b2d01b66e3c42549e32b94649a1a0330f2cd441c88f6a18928778`
- captured_utc: `2026-07-14T16:55:30.274176+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.execution](package-summary.html)

## Class SimulationExecution

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.execution.SimulationExecution

All Implemented Interfaces:
`com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport`

@OpenApiAllpublic abstract classSimulationExecution
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport

The SimulationExecution class.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected final [CopyOnWriteArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CopyOnWriteArrayList.html)<[SimulationExecutionListener](SimulationExecutionListener.html)>`
`[simulationListeners](#simulationListeners)`
Simulation Execution Listener.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimulationExecution](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`boolean`
`[addSimulationListener](#addSimulationListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener))([SimulationExecutionListener](SimulationExecutionListener.html) listener)`
Add the specified simulation execution listener.
`void`
`[addSimulationListeners](#addSimulationListeners(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SimulationExecutionListener](SimulationExecutionListener.html)> listeners)`
Add all simulation execution listeners, if not already registered.
`abstract fUML.Semantics.Loci.LociL1.Locus`
`[getExecutionLocus](#getExecutionLocus())()`
Get the execution `Locus`.
`abstract [SimulationSession](session/SimulationSession.html)`
`[getMainSession](#getMainSession())()`
get main session.
`abstract [SimulationOptions](SimulationOptions.html)`
`[getOptions](#getOptions())()`

`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[SimulationExecutionListener](SimulationExecutionListener.html)>`
`[getSimulationExecutionListeners](#getSimulationExecutionListeners())()`
get the registered SimulationExecutionListener.
`[SimulationOptions](SimulationOptions.html)`
`[getSimulationOptions](#getSimulationOptions())()`
Deprecated.
renamed to [`getOptions()`](#getOptions())
`boolean`
`[removeSimulationListener](#removeSimulationListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener))([SimulationExecutionListener](SimulationExecutionListener.html) listener)`
Removes the specified simulation execution listener.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport
`getProject, getServiceProvider`

============ FIELD DETAIL =========== 
Field Details
simulationListeners
protected final [CopyOnWriteArrayList](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CopyOnWriteArrayList.html)<[SimulationExecutionListener](SimulationExecutionListener.html)> simulationListeners
Simulation Execution Listener.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationExecution
public SimulationExecution()
 ============ METHOD DETAIL ========== 
Method Details
getExecutionLocus
public abstract fUML.Semantics.Loci.LociL1.Locus getExecutionLocus()
Get the execution `Locus`.
Returns:
`Locus`
getMainSession
public abstract [SimulationSession](session/SimulationSession.html) getMainSession()
get main session.
Returns:
main session
addSimulationListener
public boolean addSimulationListener([SimulationExecutionListener](SimulationExecutionListener.html) listener)
Add the specified simulation execution listener.
Parameters:
`listener` - the specified simulation execution listener
Returns:
true if this listener was not already registered
addSimulationListeners
public void addSimulationListeners([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SimulationExecutionListener](SimulationExecutionListener.html)> listeners)
Add all simulation execution listeners, if not already registered.
Parameters:
`listeners` - simulation execution listeners
removeSimulationListener
public boolean removeSimulationListener([SimulationExecutionListener](SimulationExecutionListener.html) listener)
Removes the specified simulation execution listener.
Parameters:
`listener` - the specified simulation execution listener
Returns:
true if this set contained the specified element
getSimulationExecutionListeners
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[SimulationExecutionListener](SimulationExecutionListener.html)> getSimulationExecutionListeners()
get the registered SimulationExecutionListener.
Returns:
Set of registered SimulationExecutionListener
getSimulationOptions
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [SimulationOptions](SimulationOptions.html) getSimulationOptions()
Deprecated.
renamed to [`getOptions()`](#getOptions())
getOptions
public abstract [SimulationOptions](SimulationOptions.html) getOptions()
Specified by:
`getOptions` in interface `com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport`
Returns:
SimulationOptions of this execution

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.execution</a></div>
<h1 class="title" title="Class SimulationExecution">Class SimulationExecution</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.execution.SimulationExecution</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">SimulationExecution</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport</span></div>
<div class="block">The SimulationExecution class.</div>
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
<div class="col-first even-row-color"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CopyOnWriteArrayList.html" title="class or interface in java.util.concurrent">CopyOnWriteArrayList</a>&lt;<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#simulationListeners">simulationListeners</a></code></div>
<div class="col-last even-row-color">
<div class="block">Simulation Execution Listener.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SimulationExecution</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSimulationListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">addSimulationListener</a><wbr/>(<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add the specified simulation execution listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSimulationListeners(java.util.Collection)">addSimulationListeners</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a>&gt; listeners)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add all simulation execution listeners, if not already registered.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract fUML.Semantics.Loci.LociL1.Locus</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExecutionLocus()">getExecutionLocus</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get the execution <code>Locus</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMainSession()">getMainSession</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">get main session.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract <a href="SimulationOptions.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSimulationExecutionListeners()">getSimulationExecutionListeners</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">get the registered SimulationExecutionListener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="SimulationOptions.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSimulationOptions()">getSimulationOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">renamed to <a href="#getOptions()"><code>getOptions()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSimulationListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">removeSimulationListener</a><wbr/>(<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the specified simulation execution listener.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport">Methods inherited from interface com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport</h3>
<code>getProject, getServiceProvider</code></div>
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
<section class="detail" id="simulationListeners">
<h3>simulationListeners</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/CopyOnWriteArrayList.html" title="class or interface in java.util.concurrent">CopyOnWriteArrayList</a>&lt;<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a>&gt;</span> <span class="element-name">simulationListeners</span></div>
<div class="block">Simulation Execution Listener.</div>
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
<h3>SimulationExecution</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimulationExecution</span>()</div>
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
<section class="detail" id="getExecutionLocus()">
<h3>getExecutionLocus</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type">fUML.Semantics.Loci.LociL1.Locus</span> <span class="element-name">getExecutionLocus</span>()</div>
<div class="block">Get the execution <code>Locus</code>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>Locus</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainSession()">
<h3>getMainSession</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a href="session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">getMainSession</span>()</div>
<div class="block">get main session.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>main session</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSimulationListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">
<h3>addSimulationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">addSimulationListener</span><wbr/><span class="parameters">(<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</span></div>
<div class="block">Add the specified simulation execution listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified simulation execution listener</dd>
<dt>Returns:</dt>
<dd><tt>true</tt> if this listener was not already registered</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addSimulationListeners(java.util.Collection)">
<h3>addSimulationListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSimulationListeners</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a>&gt; listeners)</span></div>
<div class="block">Add all simulation execution listeners, if not already registered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listeners</code> - simulation execution listeners</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSimulationListener(com.nomagic.magicdraw.simulation.execution.SimulationExecutionListener)">
<h3>removeSimulationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">removeSimulationListener</span><wbr/><span class="parameters">(<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a> listener)</span></div>
<div class="block">Removes the specified simulation execution listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the specified simulation execution listener</dd>
<dt>Returns:</dt>
<dd>true if this set contained the specified element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSimulationExecutionListeners()">
<h3>getSimulationExecutionListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="SimulationExecutionListener.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecutionListener</a>&gt;</span> <span class="element-name">getSimulationExecutionListeners</span>()</div>
<div class="block">get the registered SimulationExecutionListener.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Set of registered SimulationExecutionListener</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSimulationOptions()">
<h3>getSimulationOptions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="SimulationOptions.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationOptions</a></span> <span class="element-name">getSimulationOptions</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">renamed to <a href="#getOptions()"><code>getOptions()</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="modifiers">public abstract</span> <span class="return-type"><a href="SimulationOptions.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationOptions</a></span> <span class="element-name">getOptions</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getOptions</code> in interface <code>com.nomagic.magicdraw.simulation.execution.service.ExecutionWithServiceSupport</code></dd>
<dt>Returns:</dt>
<dd>SimulationOptions of this execution</dd>
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
