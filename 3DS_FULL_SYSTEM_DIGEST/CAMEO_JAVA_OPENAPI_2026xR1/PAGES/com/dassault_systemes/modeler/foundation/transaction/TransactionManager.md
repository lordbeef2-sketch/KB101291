# JAVA OPENAPI: TransactionManager (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/transaction/TransactionManager.html
- source_path: `com/dassault_systemes/modeler/foundation/transaction/TransactionManager.html`
- source_sha256: `aaa5d87f1698112a6fbe604c5db5c2bce0220ea57d1de371c3930ce2e48f6cb7`
- captured_utc: `2026-07-14T16:44:44.604798+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.transaction](package-summary.html)

## Interface TransactionManager

@OpenApipublic interfaceTransactionManager
Provides access to transaction lifecycle events and allows reacting to model changes.

 `TransactionManager` is used to register [`TransactionListener`](TransactionListener.html)s
 that are invoked during write transactions. Listeners can observe changes,
 perform validation, or modify the model using nested transactions.
Listeners may be filtered by [`OperationKind`](OperationKind.html) to react only to specific
 types of operations.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addListener](#addListener(com.dassault_systemes.modeler.foundation.transaction.TransactionListener,com.dassault_systemes.modeler.foundation.transaction.OperationKind...))([TransactionListener](TransactionListener.html) listener,
 [OperationKind](OperationKind.html)... kind)`
Registers a transaction listener.
`void`
`[removeListener](#removeListener(com.dassault_systemes.modeler.foundation.transaction.TransactionListener))([TransactionListener](TransactionListener.html) listener)`
Unregisters a transaction listener.

============ METHOD DETAIL ========== 
Method Details
addListener
@OpenApivoid addListener([TransactionListener](TransactionListener.html) listener,
 [OperationKind](OperationKind.html)... kind)
Registers a transaction listener.

 If operation kinds are specified, the listener is invoked only for those kinds.
 Otherwise, it is invoked for [`OperationKind.OTHER`](OperationKind.html#OTHER) transactions.
Parameters:
`listener` - listener to add
`kind` - operation kinds to listen to
removeListener
@OpenApivoid removeListener([TransactionListener](TransactionListener.html) listener)
Unregisters a transaction listener.
Parameters:
`listener` - listener to remove

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.transaction</a></div>
<h1 class="title" title="Interface TransactionManager">Interface TransactionManager</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">TransactionManager</span></div>
<div class="block">Provides access to transaction lifecycle events and allows reacting to model changes.

 <p><code>TransactionManager</code> is used to register <a href="TransactionListener.html" title="interface in com.dassault_systemes.modeler.foundation.transaction"><code>TransactionListener</code></a>s
 that are invoked during write transactions. Listeners can observe changes,
 perform validation, or modify the model using nested transactions.</p>
<p>Listeners may be filtered by <a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction"><code>OperationKind</code></a> to react only to specific
 types of operations.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addListener(com.dassault_systemes.modeler.foundation.transaction.TransactionListener,com.dassault_systemes.modeler.foundation.transaction.OperationKind...)">addListener</a><wbr/>(<a href="TransactionListener.html" title="interface in com.dassault_systemes.modeler.foundation.transaction">TransactionListener</a> listener,
 <a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a>... kind)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Registers a transaction listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeListener(com.dassault_systemes.modeler.foundation.transaction.TransactionListener)">removeListener</a><wbr/>(<a href="TransactionListener.html" title="interface in com.dassault_systemes.modeler.foundation.transaction">TransactionListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Unregisters a transaction listener.</div>
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
<section class="detail" id="addListener(com.dassault_systemes.modeler.foundation.transaction.TransactionListener,com.dassault_systemes.modeler.foundation.transaction.OperationKind...)">
<h3>addListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">addListener</span><wbr/><span class="parameters">(<a href="TransactionListener.html" title="interface in com.dassault_systemes.modeler.foundation.transaction">TransactionListener</a> listener,
 <a href="OperationKind.html" title="enum class in com.dassault_systemes.modeler.foundation.transaction">OperationKind</a>... kind)</span></div>
<div class="block">Registers a transaction listener.

 <p>If operation kinds are specified, the listener is invoked only for those kinds.
 Otherwise, it is invoked for <a href="OperationKind.html#OTHER"><code>OperationKind.OTHER</code></a> transactions.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to add</dd>
<dd><code>kind</code> - operation kinds to listen to</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeListener(com.dassault_systemes.modeler.foundation.transaction.TransactionListener)">
<h3>removeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">removeListener</span><wbr/><span class="parameters">(<a href="TransactionListener.html" title="interface in com.dassault_systemes.modeler.foundation.transaction">TransactionListener</a> listener)</span></div>
<div class="block">Unregisters a transaction listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to remove</dd>
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
