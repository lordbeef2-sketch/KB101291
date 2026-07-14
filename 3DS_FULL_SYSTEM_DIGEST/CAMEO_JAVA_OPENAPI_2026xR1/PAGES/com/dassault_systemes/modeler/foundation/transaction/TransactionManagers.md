# JAVA OPENAPI: TransactionManagers (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/foundation/transaction/TransactionManagers.html
- source_path: `com/dassault_systemes/modeler/foundation/transaction/TransactionManagers.html`
- source_sha256: `22d04f97a98575913f6083b95011d3c5e161a59fc1e28f88b5f135708892cb69`
- captured_utc: `2026-07-14T16:44:44.647797+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.foundation.transaction](package-summary.html)

## Class TransactionManagers

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.transaction.TransactionManagers

@OpenApiAllpublic final classTransactionManagers
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for obtaining [`transaction managers`](TransactionManager.html).

 This class provides Open API access to the transaction manager associated
 with a [`ModelElementProject`](../project/ModelElementProject.html).
**Example:**
`TransactionManager transactionManager = TransactionManagers.getTransactionManager(project);`

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [TransactionManager](TransactionManager.html)`
`[getTransactionManager](#getTransactionManager(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../project/ModelElementProject.html) project)`
Returns the transaction manager associated with the given project.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getTransactionManager
public static [TransactionManager](TransactionManager.html) getTransactionManager([ModelElementProject](../project/ModelElementProject.html) project)
Returns the transaction manager associated with the given project.
Parameters:
`project` - the project for which to obtain the transaction manager
Returns:
the transaction manager associated with the project
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if the model element repository cannot be found in the project
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if the transaction manager cannot be found for the project repository

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.foundation.transaction</a></div>
<h1 class="title" title="Class TransactionManagers">Class TransactionManagers</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.transaction.TransactionManagers</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">TransactionManagers</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for obtaining <a href="TransactionManager.html" title="interface in com.dassault_systemes.modeler.foundation.transaction"><code>transaction managers</code></a>.

 <p>This class provides Open API access to the transaction manager associated
 with a <a href="../project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project"><code>ModelElementProject</code></a>.</p>
<p><b>Example:</b></p>
<pre><code>
 TransactionManager transactionManager = TransactionManagers.getTransactionManager(project);
 </code></pre></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="TransactionManager.html" title="interface in com.dassault_systemes.modeler.foundation.transaction">TransactionManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransactionManager(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getTransactionManager</a><wbr/>(<a href="../project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the transaction manager associated with the given project.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getTransactionManager(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getTransactionManager</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="TransactionManager.html" title="interface in com.dassault_systemes.modeler.foundation.transaction">TransactionManager</a></span> <span class="element-name">getTransactionManager</span><wbr/><span class="parameters">(<a href="../project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the transaction manager associated with the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project for which to obtain the transaction manager</dd>
<dt>Returns:</dt>
<dd>the transaction manager associated with the project</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if the model element repository cannot be found in the project</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if the transaction manager cannot be found for the project repository</dd>
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
