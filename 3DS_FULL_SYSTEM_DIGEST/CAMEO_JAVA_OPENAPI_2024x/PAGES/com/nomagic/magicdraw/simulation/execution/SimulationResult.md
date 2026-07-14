# JAVA OPENAPI: SimulationResult (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/simulation/execution/SimulationResult.html
- source_path: `com/nomagic/magicdraw/simulation/execution/SimulationResult.html`
- source_sha256: `c059626951cdd86d0a9c5334d63d961db7ebe7340f3a0dc0a4f7d0eafedf9c68`
- captured_utc: `2026-07-14T16:51:31.514342+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.execution](package-summary.html)

## Interface SimulationResult

@OpenApiAllpublic interfaceSimulationResult
The SimulationResult class.
 Contains simulation execution information.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Get the executed element.
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
`[getException](#getException())()`
Get simulation exception if it occurred starting or during execution.
`[SimulationSession](session/SimulationSession.html)`
`[getMainSession](#getMainSession())()`
Get main simulation session if not multiple execution was started.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getOutputValues](#getOutputValues())()`
Gets simulation output values if simulation execution finished successfully.

============ METHOD DETAIL ========== 
Method Details
getMainSession
@CheckForNull[SimulationSession](session/SimulationSession.html) getMainSession()
Get main simulation session if not multiple execution was started.
Returns:
mainSession
getElement
[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Get the executed element.
Returns:
element
getException
@CheckForNull[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html) getException()
Get simulation exception if it occurred starting or during execution.
Returns:
exception
getOutputValues
[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getOutputValues()
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Gets simulation output values if simulation execution finished successfully.
 If simulation session is still running it waits for simulation execution termination.
Returns:
Key value map of outputs
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)` - if some exception occurred by running simulation.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.execution</a></div>
<h1 class="title" title="Interface SimulationResult">Interface SimulationResult</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SimulationResult</span></div>
<div class="block">The SimulationResult class.
 Contains simulation execution information.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get the executed element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getException()">getException</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get simulation exception if it occurred starting or during execution.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMainSession()">getMainSession</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get main simulation session if not multiple execution was started.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOutputValues()">getOutputValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets simulation output values if simulation execution finished successfully.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="getMainSession()">
<h3>getMainSession</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="session/SimulationSession.html" title="class in com.nomagic.magicdraw.simulation.execution.session">SimulationSession</a></span> <span class="element-name">getMainSession</span>()</div>
<div class="block">Get main simulation session if not multiple execution was started.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>mainSession</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Get the executed element.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getException()">
<h3>getException</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span> <span class="element-name">getException</span>()</div>
<div class="block">Get simulation exception if it occurred starting or during execution.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutputValues()">
<h3>getOutputValues</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getOutputValues</span>()
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Gets simulation output values if simulation execution finished successfully.
 If simulation session is still running it waits for simulation execution termination.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Key value map of outputs</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - if some exception occurred by running simulation.</dd>
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
