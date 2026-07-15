# JAVA OPENAPI: TransactionListener (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/transaction/TransactionListener.html
- source_path: `com/dassault_systemes/modeler/foundation/transaction/TransactionListener.html`
- source_sha256: `b00361aaa530b5965a270fa036e882b6202669e71bc7103fc413c2764426a4ad`
- captured_utc: `2026-07-14T16:44:44.677798+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.transaction](package-summary.html)

## Interface TransactionListener

@OpenApiAllpublic interfaceTransactionListener
Listener for observing and reacting to the transaction lifecycle.

 A `TransactionListener` allows you to hook into different stages
 of a transaction and inspect or react to model changes. It is commonly used
 for validation, synchronization, auditing, or enforcing modeling rules.
The transaction lifecycle consists of three phases:
[`transactionStarted(TransactionOptions)`](#transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)) – called once when the transaction begins
[`transactionPreCompleted(Collection, TransactionOptions)`](#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)) – called before completion,
 possibly multiple times
[`transactionCompleted(TransactionOptions)`](#transactionCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)) – called once when the transaction is finalized
**Important:** `transactionPreCompleted` may be invoked multiple times
 within a single transaction if listeners modify the model. In such cases,
 previously notified listeners are invoked again with the updated set of changes.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[transactionCompleted](#transactionCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))([TransactionOptions](TransactionOptions.html) options)`
Invoked once when the transaction is about to complete,
 after all [`transactionPreCompleted(Collection, TransactionOptions)`](#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))
 calls have stabilized (i.e., no further model changes are made).
`void`
`[transactionPreCompleted](#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> events,
 [TransactionOptions](TransactionOptions.html) options)`
Invoked when transaction completion is initiated.
`default void`
`[transactionStarted](#transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))([TransactionOptions](TransactionOptions.html) options)`
Invoked once when a transaction is started.

============ METHOD DETAIL ========== 
Method Details
transactionStarted
default void transactionStarted([TransactionOptions](TransactionOptions.html) options)
Invoked once when a transaction is started.

 This is typically used for initialization or preparing
 context for the upcoming changes.
Parameters:
`options` - transaction configuration and metadata
transactionPreCompleted
void transactionPreCompleted([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> events,
 [TransactionOptions](TransactionOptions.html) options)
Invoked when transaction completion is initiated.

 This method provides access to all model changes recorded so far
 as a collection of [`PropertyChangeEvent`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) instances.
Listeners are allowed to modify the model in this phase.
 If any listener performs additional modifications, the transaction
 enters another pre-completion cycle and all listeners are invoked again
 with the updated set of events.
This makes the method **re-entrant** within a single transaction.
Parameters:
`events` - model modification events recorded during the transaction
`options` - transaction configuration and metadata
transactionCompleted
default void transactionCompleted([TransactionOptions](TransactionOptions.html) options)
Invoked once when the transaction is about to complete,
 after all [`transactionPreCompleted(Collection, TransactionOptions)`](#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))
 calls have stabilized (i.e., no further model changes are made).

 At this stage, the transaction is finalized and the model must not be modified.
This method is typically used for post-processing, logging,
 or triggering external actions based on the completed changes.
Parameters:
`options` - transaction configuration and metadata

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.transaction</a></div>
<h1 class="title" title="Interface TransactionListener">Interface TransactionListener</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">TransactionListener</span></div>
<div class="block">Listener for observing and reacting to the transaction lifecycle.

 <p>A <code>TransactionListener</code> allows you to hook into different stages
 of a transaction and inspect or react to model changes. It is commonly used
 for validation, synchronization, auditing, or enforcing modeling rules.</p>
<p>The transaction lifecycle consists of three phases:</p>
<ul>
<li><a href="#transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)"><code>transactionStarted(TransactionOptions)</code></a> – called once when the transaction begins</li>
<li><a href="#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)"><code>transactionPreCompleted(Collection, TransactionOptions)</code></a> – called before completion,
       possibly multiple times</li>
<li><a href="#transactionCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)"><code>transactionCompleted(TransactionOptions)</code></a> – called once when the transaction is finalized</li>
</ul>
<p><b>Important:</b> <code>transactionPreCompleted</code> may be invoked multiple times
 within a single transaction if listeners modify the model. In such cases,
 previously notified listeners are invoked again with the updated set of changes.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#transactionCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">transactionCompleted</a><wbr/>(<a href="TransactionOptions.html" title="class in com.dassault_systemes.modeler.foundation.transaction">TransactionOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Invoked once when the transaction is about to complete,
 after all <a href="#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)"><code>transactionPreCompleted(Collection, TransactionOptions)</code></a>
 calls have stabilized (i.e., no further model changes are made).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">transactionPreCompleted</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; events,
 <a href="TransactionOptions.html" title="class in com.dassault_systemes.modeler.foundation.transaction">TransactionOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Invoked when transaction completion is initiated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">transactionStarted</a><wbr/>(<a href="TransactionOptions.html" title="class in com.dassault_systemes.modeler.foundation.transaction">TransactionOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Invoked once when a transaction is started.</div>
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
<section class="detail" id="transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">
<h3>transactionStarted</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">transactionStarted</span><wbr/><span class="parameters">(<a href="TransactionOptions.html" title="class in com.dassault_systemes.modeler.foundation.transaction">TransactionOptions</a> options)</span></div>
<div class="block">Invoked once when a transaction is started.

 <p>This is typically used for initialization or preparing
 context for the upcoming changes.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - transaction configuration and metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">
<h3>transactionPreCompleted</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">transactionPreCompleted</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; events,
 <a href="TransactionOptions.html" title="class in com.dassault_systemes.modeler.foundation.transaction">TransactionOptions</a> options)</span></div>
<div class="block">Invoked when transaction completion is initiated.

 <p>This method provides access to all model changes recorded so far
 as a collection of <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans"><code>PropertyChangeEvent</code></a> instances.</p>
<p>Listeners are allowed to modify the model in this phase.
 If any listener performs additional modifications, the transaction
 enters another pre-completion cycle and all listeners are invoked again
 with the updated set of events.</p>
<p>This makes the method <b>re-entrant</b> within a single transaction.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>events</code> - model modification events recorded during the transaction</dd>
<dd><code>options</code> - transaction configuration and metadata</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transactionCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">
<h3>transactionCompleted</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">transactionCompleted</span><wbr/><span class="parameters">(<a href="TransactionOptions.html" title="class in com.dassault_systemes.modeler.foundation.transaction">TransactionOptions</a> options)</span></div>
<div class="block">Invoked once when the transaction is about to complete,
 after all <a href="#transactionPreCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)"><code>transactionPreCompleted(Collection, TransactionOptions)</code></a>
 calls have stabilized (i.e., no further model changes are made).

 <p>At this stage, the transaction is finalized and the model must not be modified.</p>
<p>This method is typically used for post-processing, logging,
 or triggering external actions based on the completed changes.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - transaction configuration and metadata</dd>
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
