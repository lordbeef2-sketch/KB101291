# JAVA OPENAPI: Object_ (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/simulation/fuml/classes/Object_.html
- source_path: `com/nomagic/magicdraw/simulation/fuml/classes/Object_.html`
- source_sha256: `9cb3c53da56ec86bb0539a3372e1695093ab83aed1912fa9e4c0f85dfb1a9935`
- captured_utc: `2026-07-14T16:58:02.712588+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.fuml.classes](package-summary.html)

## Class Object_

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
[com.nomagic.magicdraw.simulation.fuml.classes.Value](Value.html)
[com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue](StructuredValue.html)
[com.nomagic.magicdraw.simulation.fuml.classes.CompoundValue](CompoundValue.html)
com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue
com.nomagic.magicdraw.simulation.fuml.classes.Object_

All Implemented Interfaces:
`com.nomagic.magicdraw.simulation.listener.SimulationListenerable`

Direct Known Subclasses:
`[Execution](../behaviors/Execution.html)`

@OpenApipublic classObject_
extends com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue
`identifier, locus`
Fields inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
`listenerInfoSupport`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Execution](../behaviors/Execution.html)>`
`[getExecutions](#getExecutions())()`

`[SimulationSession](../../execution/session/SimulationSession.html)`
`[getRefSession](#getRefSession())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)>`
`[getTypes](#getTypes())()`
Gets the types.
Methods inherited from class com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue
`getLocus`
Methods inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
`_beginIsolation, _endIsolation, firePropertyChange, getListeners, register, register, unregister`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getTypes
@OpenApipublic [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Classifier](../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html)> getTypes()
Description copied from class: `[Value](Value.html#getTypes())`
Gets the types.
Specified by:
`[getTypes](Value.html#getTypes())` in class `[Value](Value.html)`
Returns:
the types
getRefSession
@OpenApi
@CheckForNullpublic [SimulationSession](../../execution/session/SimulationSession.html) getRefSession()
getExecutions
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Execution](../behaviors/Execution.html)> getExecutions()
Returns:
the executions which depend on this object.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.fuml.classes</a></div>
<h1 class="title" title="Class Object_">Class Object_</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor
<div class="inheritance"><a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">com.nomagic.magicdraw.simulation.fuml.classes.Value</a>
<div class="inheritance"><a href="StructuredValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">com.nomagic.magicdraw.simulation.fuml.classes.StructuredValue</a>
<div class="inheritance"><a href="CompoundValue.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">com.nomagic.magicdraw.simulation.fuml.classes.CompoundValue</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue
<div class="inheritance">com.nomagic.magicdraw.simulation.fuml.classes.Object_</div>
</div>
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
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../behaviors/Execution.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors">Execution</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Object_</span>
<span class="extends-implements">extends com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue</span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue">Fields inherited from class com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue</h3>
<code>identifier, locus</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor">Fields inherited from class com.nomagic.magicdraw.simulation.fuml.loci.SemanticVisitor</h3>
<code>listenerInfoSupport</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../behaviors/Execution.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors">Execution</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExecutions()">getExecutions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRefSession()">getRefSession</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypes()">getTypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the types.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue">Methods inherited from class com.nomagic.magicdraw.simulation.fuml.classes.ExtensionalValue</h3>
<code>getLocus</code></div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getTypes()">
<h3>getTypes</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Classifier.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Classifier</a>&gt;</span> <span class="element-name">getTypes</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="Value.html#getTypes()">Value</a></code></span></div>
<div class="block">Gets the types.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Value.html#getTypes()">getTypes</a></code> in class <code><a href="Value.html" title="class in com.nomagic.magicdraw.simulation.fuml.classes">Value</a></code></dd>
<dt>Returns:</dt>
<dd>the types</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRefSession()">
<h3>getRefSession</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../execution/session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">getRefSession</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExecutions()">
<h3>getExecutions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../behaviors/Execution.html" title="class in com.nomagic.magicdraw.simulation.fuml.behaviors">Execution</a>&gt;</span> <span class="element-name">getExecutions</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the executions which depend on this object.</dd>
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
