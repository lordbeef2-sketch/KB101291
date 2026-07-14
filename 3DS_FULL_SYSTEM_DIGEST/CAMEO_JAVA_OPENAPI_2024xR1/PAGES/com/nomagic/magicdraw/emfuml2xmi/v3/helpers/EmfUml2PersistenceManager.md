# JAVA OPENAPI: EmfUml2PersistenceManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/emfuml2xmi/v3/helpers/EmfUml2PersistenceManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v3/helpers/EmfUml2PersistenceManager.html`
- source_sha256: `42d40c7dccd7f6cc72911519b78f45d07e7f6c831c4456f50900c5868bf7e9ca`
- captured_utc: `2026-07-14T16:51:19.862184+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v3.helpers](package-summary.html)

## Class EmfUml2PersistenceManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl
com.nomagic.magicdraw.emfuml2xmi.v3.helpers.EmfUml2PersistenceManager

All Implemented Interfaces:
`[EmfUml2PersistenceManager](../../helpers/EmfUml2PersistenceManager.html)`

@OpenApipublic final classEmfUml2PersistenceManager
extends com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl
implements [EmfUml2PersistenceManager](../../helpers/EmfUml2PersistenceManager.html)

Stores save and load options.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [EmfUml2PersistenceManager](EmfUml2PersistenceManager.html)`
`[getInstance](#getInstance())()`
Get singleton instance of the manager.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl
`addLoadOptionsProvider, addResourceSetInitializer, addSaveOptionsProvider, clean, getLoadOptionsProvider, getResourceSetInitializers, getSaveOptionsProvider, removeLoadOptionsProvider, removeResourceSetInitializer, removeSaveOptionsProvider`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[EmfUml2PersistenceManager](../../helpers/EmfUml2PersistenceManager.html)
`[addLoadOptionsProvider](../../helpers/EmfUml2PersistenceManager.html#addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)), [addResourceSetInitializer](../../helpers/EmfUml2PersistenceManager.html#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)), [addSaveOptionsProvider](../../helpers/EmfUml2PersistenceManager.html#addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)), [removeLoadOptionsProvider](../../helpers/EmfUml2PersistenceManager.html#removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)), [removeResourceSetInitializer](../../helpers/EmfUml2PersistenceManager.html#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)), [removeSaveOptionsProvider](../../helpers/EmfUml2PersistenceManager.html#removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider))`

============ METHOD DETAIL ========== 
Method Details
getInstance
@OpenApipublic static [EmfUml2PersistenceManager](EmfUml2PersistenceManager.html) getInstance()
Get singleton instance of the manager.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v3.helpers</a></div>
<h1 class="title" title="Class EmfUml2PersistenceManager">Class EmfUml2PersistenceManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v3.helpers.EmfUml2PersistenceManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../helpers/EmfUml2PersistenceManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2PersistenceManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">EmfUml2PersistenceManager</span>
<span class="extends-implements">extends com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl
implements <a href="../../helpers/EmfUml2PersistenceManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2PersistenceManager</a></span></div>
<div class="block">Stores save and load options.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="EmfUml2PersistenceManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.helpers">EmfUml2PersistenceManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get singleton instance of the manager.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl</h3>
<code>addLoadOptionsProvider, addResourceSetInitializer, addSaveOptionsProvider, clean, getLoadOptionsProvider, getResourceSetInitializers, getSaveOptionsProvider, removeLoadOptionsProvider, removeResourceSetInitializer, removeSaveOptionsProvider</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManager">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="../../helpers/EmfUml2PersistenceManager.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2PersistenceManager</a></h3>
<code><a href="../../helpers/EmfUml2PersistenceManager.html#addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">addLoadOptionsProvider</a>, <a href="../../helpers/EmfUml2PersistenceManager.html#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)">addResourceSetInitializer</a>, <a href="../../helpers/EmfUml2PersistenceManager.html#addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">addSaveOptionsProvider</a>, <a href="../../helpers/EmfUml2PersistenceManager.html#removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">removeLoadOptionsProvider</a>, <a href="../../helpers/EmfUml2PersistenceManager.html#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)">removeResourceSetInitializer</a>, <a href="../../helpers/EmfUml2PersistenceManager.html#removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">removeSaveOptionsProvider</a></code></div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="EmfUml2PersistenceManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.helpers">EmfUml2PersistenceManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Get singleton instance of the manager.</div>
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
