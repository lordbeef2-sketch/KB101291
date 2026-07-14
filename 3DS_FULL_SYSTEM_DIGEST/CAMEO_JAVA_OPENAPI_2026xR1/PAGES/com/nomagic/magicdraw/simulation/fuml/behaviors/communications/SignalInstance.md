# JAVA OPENAPI: SignalInstance (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/simulation/fuml/behaviors/communications/SignalInstance.html
- source_path: `com/nomagic/magicdraw/simulation/fuml/behaviors/communications/SignalInstance.html`
- source_sha256: `d46e92c6b450c21216be4fec07dea13daee3599a18bf2944bbd56649f9699b70`
- captured_utc: `2026-07-14T16:45:43.040574+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.fuml.behaviors.communications](package-summary.html)

## Class SignalInstance

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
[com.nomagic.magicdraw.simulation.fuml.classes.Value](../../classes/Value.html)
[com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue](../../classes/StructuredValue.html)
[com.nomagic.magicdraw.simulation.fuml.classes.CompoundValue](../../classes/CompoundValue.html)
com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance

All Implemented Interfaces:
`com.nomagic.magicdraw.simulation.listener.SimulationListenerable`

@OpenApipublic classSignalInstance
extends [CompoundValue](../../classes/CompoundValue.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
`listenerInfoSupport`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SignalInstance](#%3Cinit%3E())()`
Instantiates a new signal instance.
`[SignalInstance](#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecution](../../../execution/SimulationExecution.html) execution)`
Instantiates a new signal instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Signal](../../../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)`
`[getSignal](#getSignal())()`
Methods inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
`_beginIsolation, _endIsolation, firePropertyChange, getListeners, register, register, unregister`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SignalInstance
@OpenApipublic SignalInstance()
Instantiates a new signal instance.
SignalInstance
@OpenApipublic SignalInstance([SimulationExecution](../../../execution/SimulationExecution.html) execution)
Instantiates a new signal instance.
Parameters:
`execution` - the execution
 ============ METHOD DETAIL ========== 
Method Details
getSignal
@OpenApi
@CheckForNullpublic [Signal](../../../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html) getSignal()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.fuml.behaviors.communications</a></div>
<h1 class="title" title="Class SignalInstance">Class SignalInstance</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
<div class="inheritance"><a href="../../classes/Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">com.nomagic.magicdraw.simulation.fuml.classes.Value</a>
<div class="inheritance"><a href="../../classes/StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue</a>
<div class="inheritance"><a href="../../classes/CompoundValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">com.nomagic.magicdraw.simulation.fuml.classes.CompoundValue</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.behaviors.communications.SignalInstance</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.simulation.listener.SimulationListenerable</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SignalInstance</span>
<span class="extends-implements">extends <a href="../../classes/CompoundValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">CompoundValue</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor">Fields inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor</h3>
<code>listenerInfoSupport</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SignalInstance</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Instantiates a new signal instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">SignalInstance</a><wbr/>(<a href="../../../execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last odd-row-color">
<div class="block">Instantiates a new signal instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSignal()">getSignal</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor">Methods inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor</h3>
<code>_beginIsolation, _endIsolation, firePropertyChange, getListeners, register, register, unregister</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>SignalInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">SignalInstance</span>()</div>
<div class="block">Instantiates a new signal instance.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>SignalInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">SignalInstance</span><wbr/><span class="parameters">(<a href="../../../execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Instantiates a new signal instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - the execution</dd>
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
<section class="detail" id="getSignal()">
<h3>getSignal</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a></span> <span class="element-name">getSignal</span>()</div>
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
