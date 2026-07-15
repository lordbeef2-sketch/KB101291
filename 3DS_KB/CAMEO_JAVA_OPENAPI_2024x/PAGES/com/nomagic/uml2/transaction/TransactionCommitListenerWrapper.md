# JAVA OPENAPI: TransactionCommitListenerWrapper (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/uml2/transaction/TransactionCommitListenerWrapper.html
- source_path: `com/nomagic/uml2/transaction/TransactionCommitListenerWrapper.html`
- source_sha256: `86c0bf945e6077e7101250e440df916b0689f25ae53e21fa1c32a39b7abf283f`
- captured_utc: `2026-07-14T16:53:16.333676+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.transaction](package-summary.html)

## Class TransactionCommitListenerWrapper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.transaction.TransactionCommitListenerWrapper

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.transaction.TransactionListener`

public classTransactionCommitListenerWrapper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements com.dassault_systemes.modeler.foundation.transaction.TransactionListener

A wrapper of @[`TransactionCommitListener`](TransactionCommitListener.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[TransactionCommitListenerWrapper](#%3Cinit%3E(com.nomagic.uml2.transaction.TransactionCommitListener))([TransactionCommitListener](TransactionCommitListener.html) listener)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[allTransactionsCompleted](#allTransactionsCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)`
Invoked when all transactions (master and nested) are completed.
`[TransactionCommitListener](TransactionCommitListener.html)`
`[getListener](#getListener())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`

`void`
`[transactionCompleted](#transactionCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> events,
 com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)`
Notifies that transaction is completed and provides changes done in the transaction.
`void`
`[transactionStarted](#transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions))(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)`
Invoked when transaction is started.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
TransactionCommitListenerWrapper
public TransactionCommitListenerWrapper([TransactionCommitListener](TransactionCommitListener.html) listener)
 ============ METHOD DETAIL ========== 
Method Details
transactionStarted
public void transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)
Description copied from interface: `com.dassault_systemes.modeler.foundation.transaction.TransactionListener`
Invoked when transaction is started.
Specified by:
`transactionStarted` in interface `com.dassault_systemes.modeler.foundation.transaction.TransactionListener`
transactionCompleted
public void transactionCompleted([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html)> events,
 com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)
Description copied from interface: `com.dassault_systemes.modeler.foundation.transaction.TransactionListener`
Notifies that transaction is completed and provides changes done in the transaction.
 Listener can modify model.
Specified by:
`transactionCompleted` in interface `com.dassault_systemes.modeler.foundation.transaction.TransactionListener`
Parameters:
`events` - events recorded during transaction.
allTransactionsCompleted
public void allTransactionsCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)
Description copied from interface: `com.dassault_systemes.modeler.foundation.transaction.TransactionListener`
Invoked when all transactions (master and nested) are completed.
Specified by:
`allTransactionsCompleted` in interface `com.dassault_systemes.modeler.foundation.transaction.TransactionListener`
getListener
public [TransactionCommitListener](TransactionCommitListener.html) getListener()
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.transaction</a></div>
<h1 class="title" title="Class TransactionCommitListenerWrapper">Class TransactionCommitListenerWrapper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.transaction.TransactionCommitListenerWrapper</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.transaction.TransactionListener</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">TransactionCommitListenerWrapper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements com.dassault_systemes.modeler.foundation.transaction.TransactionListener</span></div>
<div class="block">A wrapper of @<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction"><code>TransactionCommitListener</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.transaction.TransactionCommitListener)">TransactionCommitListenerWrapper</a><wbr/>(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#allTransactionsCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">allTransactionsCompleted</a><wbr/>(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoked when all transactions (master and nested) are completed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getListener()">getListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#transactionCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">transactionCompleted</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; events,
 com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies that transaction is completed and provides changes done in the transaction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">transactionStarted</a><wbr/>(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoked when transaction is started.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.transaction.TransactionCommitListener)">
<h3>TransactionCommitListenerWrapper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">TransactionCommitListenerWrapper</span><wbr/><span class="parameters">(<a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a> listener)</span></div>
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
<section class="detail" id="transactionStarted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">
<h3>transactionStarted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">transactionStarted</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.transaction.TransactionListener</code></span></div>
<div class="block">Invoked when transaction is started.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>transactionStarted</code> in interface <code>com.dassault_systemes.modeler.foundation.transaction.TransactionListener</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transactionCompleted(java.util.Collection,com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">
<h3>transactionCompleted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">transactionCompleted</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a>&gt; events,
 com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.transaction.TransactionListener</code></span></div>
<div class="block">Notifies that transaction is completed and provides changes done in the transaction.
 Listener can modify model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>transactionCompleted</code> in interface <code>com.dassault_systemes.modeler.foundation.transaction.TransactionListener</code></dd>
<dt>Parameters:</dt>
<dd><code>events</code> - events recorded during transaction.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="allTransactionsCompleted(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions)">
<h3>allTransactionsCompleted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">allTransactionsCompleted</span><wbr/><span class="parameters">(com.dassault_systemes.modeler.foundation.transaction.TransactionOptions options)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.transaction.TransactionListener</code></span></div>
<div class="block">Invoked when all transactions (master and nested) are completed.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>allTransactionsCompleted</code> in interface <code>com.dassault_systemes.modeler.foundation.transaction.TransactionListener</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getListener()">
<h3>getListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TransactionCommitListener.html" title="interface in com.nomagic.uml2.transaction">TransactionCommitListener</a></span> <span class="element-name">getListener</span>()</div>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
