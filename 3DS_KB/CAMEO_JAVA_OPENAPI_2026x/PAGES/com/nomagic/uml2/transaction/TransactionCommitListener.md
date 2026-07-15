# JAVA OPENAPI: TransactionCommitListener (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/transaction/TransactionCommitListener.html
- source_path: `com/nomagic/uml2/transaction/TransactionCommitListener.html`
- source_sha256: `2e5e5975be43926c6707a3230e132c8ae7a2b539d524a557e55ad75fcfba0606`
- captured_utc: `2026-07-14T16:59:00.483544+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.transaction](package-summary.html)

## Interface TransactionCommitListener

public interfaceTransactionCommitListener
Listener to listen transactions commits.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[allTransactionsCommitted](#allTransactionsCommitted())()`
Invoked when all transactions are already committed.
`static [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)`
`[toRunnable](#toRunnable(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)> runnable)`
Merges given Runnables to a single composite Runnable
`static <T> [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)`
`[toRunnable](#toRunnable(java.util.Collection,java.util.function.Consumer))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> elements,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<T> consumer)`
Creates consumer which consumes all elements from given collection
`static [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)`
`[toRunnable](#toRunnable(java.util.stream.Stream))([Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)> runnableStream)`
Merges given Runnables to a single composite Runnable
`[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)`
`[transactionCommited](#transactionCommited(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> events)`
Notifies listener that transaction is committed and provides changes done in transaction.

============ METHOD DETAIL ========== 
Method Details
transactionCommited
@CheckForNull[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) transactionCommited([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> events)
Notifies listener that transaction is committed and provides changes done in transaction.
 Listener can return [`Runnable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) which modifies model after all listeners are notified.
Parameters:
`events` - events recorded during transaction.
Returns:
[`Runnable`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) which will be run to modify model after all listeners are notified.
 Can be null.
allTransactionsCommitted
default void allTransactionsCommitted()
Invoked when all transactions are already committed.
toRunnable
@CheckForNullstatic [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) toRunnable(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)> runnable)
Merges given Runnables to a single composite Runnable
Parameters:
`runnable` - runnables
Returns:
composite Runnable or null if given runnables are empty
toRunnable
@CheckForNullstatic [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) toRunnable([Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<[Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html)> runnableStream)
Merges given Runnables to a single composite Runnable
Parameters:
`runnableStream` - stream of Runnable
Returns:
composite Runnable or null if given stream is empty
toRunnable
@CheckForNullstatic <T> [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) toRunnable(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> elements,
 [Consumer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html)<T> consumer)
Creates consumer which consumes all elements from given collection
Parameters:
`elements` - elements to be consumed
`consumer` - consumer
Returns:
runnable or null if elements collection is null or empty

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.transaction</a></div>
<h1 class="title" title="Interface TransactionCommitListener">Interface TransactionCommitListener</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TransactionCommitListener</span></div>
<div class="block">Listener to listen transactions commits.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#allTransactionsCommitted()">allTransactionsCommitted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Invoked when all transactions are already committed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#toRunnable(java.util.Collection)">toRunnable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; runnable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Merges given Runnables to a single composite Runnable</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#toRunnable(java.util.Collection,java.util.function.Consumer)">toRunnable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;T&gt; consumer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1">
<div class="block">Creates consumer which consumes all elements from given collection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1"><code><a class="member-name-link" href="#toRunnable(java.util.stream.Stream)">toRunnable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; runnableStream)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1">
<div class="block">Merges given Runnables to a single composite Runnable</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#transactionCommited(java.util.Collection)">transactionCommited</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; events)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Notifies listener that transaction is committed and provides changes done in transaction.</div>
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
<section class="detail" id="transactionCommited(java.util.Collection)">
<h3>transactionCommited</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></span> <span class="element-name">transactionCommited</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; events)</span></div>
<div class="block">Notifies listener that transaction is committed and provides changes done in transaction.
 Listener can return <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> which modifies model after all listeners are notified.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>events</code> - events recorded during transaction.</dd>
<dt>Returns:</dt>
<dd><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang"><code>Runnable</code></a> which will be run to modify model after all listeners are notified.
 Can be null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="allTransactionsCommitted()">
<h3>allTransactionsCommitted</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">allTransactionsCommitted</span>()</div>
<div class="block">Invoked when all transactions are already committed.</div>
</section>
</li>
<li>
<section class="detail" id="toRunnable(java.util.Collection)">
<h3>toRunnable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></span> <span class="element-name">toRunnable</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; runnable)</span></div>
<div class="block">Merges given Runnables to a single composite Runnable</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - runnables</dd>
<dt>Returns:</dt>
<dd>composite Runnable or null if given runnables are empty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toRunnable(java.util.stream.Stream)">
<h3>toRunnable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></span> <span class="element-name">toRunnable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a>&gt; runnableStream)</span></div>
<div class="block">Merges given Runnables to a single composite Runnable</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnableStream</code> - stream of Runnable</dd>
<dt>Returns:</dt>
<dd>composite Runnable or null if given stream is empty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toRunnable(java.util.Collection,java.util.function.Consumer)">
<h3>toRunnable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a></span> <span class="element-name">toRunnable</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Consumer.html" title="class or interface in java.util.function">Consumer</a>&lt;T&gt; consumer)</span></div>
<div class="block">Creates consumer which consumes all elements from given collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements to be consumed</dd>
<dd><code>consumer</code> - consumer</dd>
<dt>Returns:</dt>
<dd>runnable or null if elements collection is null or empty</dd>
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
