# JAVA OPENAPI: TimeTracker (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml2/util/TimeTracker.html
- source_path: `com/nomagic/magicdraw/uml2/util/TimeTracker.html`
- source_sha256: `ed61f98a9106a8591f4ae84b1e3f8181afdc067e6599a4624e87c99680ef1154`
- captured_utc: `2026-07-14T16:52:32.131146+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml2.util](package-summary.html)

## Interface TimeTracker

All Superinterfaces:
`com.dassault_systemes.modeler.foundation.util.TimeTracker`

public interfaceTimeTrackerextends com.dassault_systemes.modeler.foundation.util.TimeTracker

Collect times of operations and dump longest of them.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static interface`
`[TimeTracker.TrackedOperation](TimeTracker.TrackedOperation.html)`
Operation to track
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[TimeTracker.TrackedOperation](TimeTracker.TrackedOperation.html)`
`[start](#start(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) operationName)`
Start operation
`[TimeTracker.TrackedOperation](TimeTracker.TrackedOperation.html)`
`[start](#start(java.util.function.Supplier))([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> operationName)`
Start operation
Methods inherited from interface com.dassault_systemes.modeler.foundation.util.TimeTracker
`dumpLongest, getAllTimePassedMillis`

============ METHOD DETAIL ========== 
Method Details
start
[TimeTracker.TrackedOperation](TimeTracker.TrackedOperation.html) start([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) operationName)
Start operation
Specified by:
`start` in interface `com.dassault_systemes.modeler.foundation.util.TimeTracker`
Parameters:
`operationName` - operation identifier
Returns:
operation
start
[TimeTracker.TrackedOperation](TimeTracker.TrackedOperation.html) start([Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> operationName)
Start operation
Specified by:
`start` in interface `com.dassault_systemes.modeler.foundation.util.TimeTracker`
Parameters:
`operationName` - operation identifier
Returns:
operation

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml2.util</a></div>
<h1 class="title" title="Interface TimeTracker">Interface TimeTracker</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.util.TimeTracker</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TimeTracker</span><span class="extends-implements">
extends com.dassault_systemes.modeler.foundation.util.TimeTracker</span></div>
<div class="block">Collect times of operations and dump longest of them.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="TimeTracker.TrackedOperation.html" title="interface in com.nomagic.magicdraw.uml2.util">TimeTracker.TrackedOperation</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operation to track</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TimeTracker.TrackedOperation.html" title="interface in com.nomagic.magicdraw.uml2.util">TimeTracker.TrackedOperation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#start(java.lang.Object)">start</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> operationName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Start operation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TimeTracker.TrackedOperation.html" title="interface in com.nomagic.magicdraw.uml2.util">TimeTracker.TrackedOperation</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#start(java.util.function.Supplier)">start</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; operationName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Start operation</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.util.TimeTracker">Methods inherited from interface com.dassault_systemes.modeler.foundation.util.TimeTracker</h3>
<code>dumpLongest, getAllTimePassedMillis</code></div>
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
<section class="detail" id="start(java.lang.Object)">
<h3>start</h3>
<div class="member-signature"><span class="return-type"><a href="TimeTracker.TrackedOperation.html" title="interface in com.nomagic.magicdraw.uml2.util">TimeTracker.TrackedOperation</a></span> <span class="element-name">start</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> operationName)</span></div>
<div class="block">Start operation</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>start</code> in interface <code>com.dassault_systemes.modeler.foundation.util.TimeTracker</code></dd>
<dt>Parameters:</dt>
<dd><code>operationName</code> - operation identifier</dd>
<dt>Returns:</dt>
<dd>operation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(java.util.function.Supplier)">
<h3>start</h3>
<div class="member-signature"><span class="return-type"><a href="TimeTracker.TrackedOperation.html" title="interface in com.nomagic.magicdraw.uml2.util">TimeTracker.TrackedOperation</a></span> <span class="element-name">start</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; operationName)</span></div>
<div class="block">Start operation</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>start</code> in interface <code>com.dassault_systemes.modeler.foundation.util.TimeTracker</code></dd>
<dt>Parameters:</dt>
<dd><code>operationName</code> - operation identifier</dd>
<dt>Returns:</dt>
<dd>operation</dd>
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
