# JAVA OPENAPI: EmfUml2PersistenceManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/emfuml2xmi/v4/helpers/EmfUml2PersistenceManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v4/helpers/EmfUml2PersistenceManager.html`
- source_sha256: `b233aac2f8dde523bc16d7dfea5e2fdf08b15ca5bdd3d1b046b155d2be54e812`
- captured_utc: `2026-07-14T16:57:56.897523+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v4.helpers](package-summary.html)

## Class EmfUml2PersistenceManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl
com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManager

@OpenApiAllpublic final classEmfUml2PersistenceManager
extends com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl
Stores save and load options.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addLoadOptionsProvider](#addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)`
Sets load options provider.
`void`
`[addResourceSetInitializer](#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Register resource set initializer.
`void`
`[addSaveOptionsProvider](#addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)`
Sets save options provider.
`static [EmfUml2PersistenceManager](EmfUml2PersistenceManager.html)`
`[getInstance](#getInstance())()`
Get singleton instance of the manager.
`void`
`[removeLoadOptionsProvider](#removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)`
Remove load options provider.
`void`
`[removeResourceSetInitializer](#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Remove resource set initializer.
`void`
`[removeSaveOptionsProvider](#removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)`
Remove save options provider.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl
`clean, getLoadOptionsProvider, getResourceSetInitializers, getSaveOptionsProvider`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [EmfUml2PersistenceManager](EmfUml2PersistenceManager.html) getInstance()
Get singleton instance of the manager.
addSaveOptionsProvider
public void addSaveOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)
Sets save options provider.
Overrides:
`addSaveOptionsProvider` in class `com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl`
removeSaveOptionsProvider
public void removeSaveOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)
Remove save options provider.
Overrides:
`removeSaveOptionsProvider` in class `com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl`
addLoadOptionsProvider
public void addLoadOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)
Sets load options provider.
Overrides:
`addLoadOptionsProvider` in class `com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl`
removeLoadOptionsProvider
public void removeLoadOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)
Remove load options provider.
Overrides:
`removeLoadOptionsProvider` in class `com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl`
addResourceSetInitializer
public void addResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Register resource set initializer.
Overrides:
`addResourceSetInitializer` in class `com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl`
Parameters:
`initializer` - resource set initializer to add.
removeResourceSetInitializer
public void removeResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Remove resource set initializer.
Overrides:
`removeResourceSetInitializer` in class `com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl`
Parameters:
`initializer` - resource set initializer to remove.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v4.helpers</a></div>
<h1 class="title" title="Class EmfUml2PersistenceManager">Class EmfUml2PersistenceManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">EmfUml2PersistenceManager</span>
<span class="extends-implements">extends com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</span></div>
<div class="block">Stores save and load options.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">addLoadOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets load options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.ResourceSetInitializer)">addResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register resource set initializer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">addSaveOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets save options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="EmfUml2PersistenceManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2PersistenceManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get singleton instance of the manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">removeLoadOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove load options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.ResourceSetInitializer)">removeResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove resource set initializer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">removeSaveOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove save options provider.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</h3>
<code>clean, getLoadOptionsProvider, getResourceSetInitializers, getSaveOptionsProvider</code></div>
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
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="EmfUml2PersistenceManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2PersistenceManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Get singleton instance of the manager.</div>
</section>
</li>
<li>
<section class="detail" id="addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">
<h3>addSaveOptionsProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addSaveOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</span></div>
<div class="block">Sets save options provider.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addSaveOptionsProvider</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">
<h3>removeSaveOptionsProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeSaveOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</span></div>
<div class="block">Remove save options provider.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removeSaveOptionsProvider</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">
<h3>addLoadOptionsProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLoadOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</span></div>
<div class="block">Sets load options provider.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addLoadOptionsProvider</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.PersistenceOptionsProvider)">
<h3>removeLoadOptionsProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLoadOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</span></div>
<div class="block">Remove load options provider.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removeLoadOptionsProvider</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.ResourceSetInitializer)">
<h3>addResourceSetInitializer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Register resource set initializer.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>addResourceSetInitializer</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>initializer</code> - resource set initializer to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v4.helpers.ResourceSetInitializer)">
<h3>removeResourceSetInitializer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Remove resource set initializer.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>removeResourceSetInitializer</code> in class <code>com.nomagic.magicdraw.emfuml2xmi.v4.helpers.EmfUml2PersistenceManagerImpl</code></dd>
<dt>Parameters:</dt>
<dd><code>initializer</code> - resource set initializer to remove.</dd>
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
