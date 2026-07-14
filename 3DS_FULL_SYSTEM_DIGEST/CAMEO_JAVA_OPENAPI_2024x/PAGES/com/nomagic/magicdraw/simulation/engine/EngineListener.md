# JAVA OPENAPI: EngineListener (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/simulation/engine/EngineListener.html
- source_path: `com/nomagic/magicdraw/simulation/engine/EngineListener.html`
- source_sha256: `fed1422a589de4ef6ce667b8587916069bac48fe3b1a4cc9738653592d60350e`
- captured_utc: `2026-07-14T16:51:29.819321+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation.engine](package-summary.html)

## Interface EngineListener

@OpenApiAllpublic interfaceEngineListener
A listener interface for element id in the simulation model.
 Element id should be the id of [`Element`](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[elementActivated](#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)`
Handle when the element is activated.
`void`
`[elementDeactivated](#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)`
Handle when the element is deactivated.
`void`
`[eventTriggered](#eventTriggered(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) eventID)`
Handle when the event id is triggered.
`void`
`[executionTerminated](#executionTerminated())()`
Handle the termination.

============ METHOD DETAIL ========== 
Method Details
elementActivated
void elementActivated([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)
Handle when the element is activated.
Parameters:
`element` - the activated element
`values` - the values that passed with this element activation
elementDeactivated
void elementDeactivated([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> values)
Handle when the element is deactivated.
Parameters:
`element` - the deactivated element
`values` - the values that passed with this element deactivation
eventTriggered
void eventTriggered([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) eventID)
Handle when the event id is triggered.
Parameters:
`eventID` - the triggered event id
executionTerminated
void executionTerminated()
Handle the termination.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation.engine</a></div>
<h1 class="title" title="Interface EngineListener">Interface EngineListener</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EngineListener</span></div>
<div class="block">A listener interface for element id in the simulation model.
 Element id should be the id of <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">elementActivated</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handle when the element is activated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">elementDeactivated</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handle when the element is deactivated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#eventTriggered(java.lang.String)">eventTriggered</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> eventID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handle when the event id is triggered.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#executionTerminated()">executionTerminated</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Handle the termination.</div>
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
<section class="detail" id="elementActivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>elementActivated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">elementActivated</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</span></div>
<div class="block">Handle when the element is activated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the activated element</dd>
<dd><code>values</code> - the values that passed with this element activation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="elementDeactivated(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">
<h3>elementDeactivated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">elementDeactivated</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; values)</span></div>
<div class="block">Handle when the element is deactivated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the deactivated element</dd>
<dd><code>values</code> - the values that passed with this element deactivation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eventTriggered(java.lang.String)">
<h3>eventTriggered</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">eventTriggered</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> eventID)</span></div>
<div class="block">Handle when the event id is triggered.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eventID</code> - the triggered event id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executionTerminated()">
<h3>executionTerminated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">executionTerminated</span>()</div>
<div class="block">Handle the termination.</div>
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
