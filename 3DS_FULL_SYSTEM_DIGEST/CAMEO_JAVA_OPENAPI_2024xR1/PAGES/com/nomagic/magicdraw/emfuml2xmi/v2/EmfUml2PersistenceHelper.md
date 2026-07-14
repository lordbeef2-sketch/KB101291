# JAVA OPENAPI: EmfUml2PersistenceHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2PersistenceHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2PersistenceHelper.html`
- source_sha256: `151214e42e50d086cbddaf1e6a45306c4cc10bb5dd882bf6ebeecf70b467b7ea`
- captured_utc: `2026-07-14T16:51:19.358179+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v2](package-summary.html)

## Class EmfUml2PersistenceHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper

@OpenApipublic final classEmfUml2PersistenceHelper
extends com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
Stores save and load options.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addResourceSetInitializer](#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Register resource set initializer.
`static void`
`[clean](#clean(java.util.Collection,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)`
Disposes given Eclipse UML2 elements.
`static [PersistenceOptionsProvider](PersistenceOptionsProvider.html)`
`[getLoadOptionsProvider](#getLoadOptionsProvider())()`
Returns load options provider.
`static [PersistenceOptionsProvider](PersistenceOptionsProvider.html)`
`[getSaveOptionsProvider](#getSaveOptionsProvider())()`
Returns save options provider
`static void`
`[removeResourceSetInitializer](#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Remove resource set initializer.
`static void`
`[setLoadOptionsProvider](#setLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)`
Sets load options provider.
`static void`
`[setSaveOptionsProvider](#setSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)`
Sets save options provider.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
`getOptionsDir, registerPackage, removeIllegalCharacters`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getSaveOptionsProvider
@OpenApipublic static [PersistenceOptionsProvider](PersistenceOptionsProvider.html) getSaveOptionsProvider()
Returns save options provider
Returns:
persistence options provider
setSaveOptionsProvider
@OpenApipublic static void setSaveOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)
Sets save options provider.
getLoadOptionsProvider
@OpenApipublic static [PersistenceOptionsProvider](PersistenceOptionsProvider.html) getLoadOptionsProvider()
Returns load options provider.
Returns:
persistence options provider
addResourceSetInitializer
@OpenApipublic static void addResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Register resource set initializer.
Parameters:
`initializer` - resource set initializer to add.
removeResourceSetInitializer
@OpenApipublic static void removeResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Remove resource set initializer.
Parameters:
`initializer` - resource set initializer to remove.
setLoadOptionsProvider
@OpenApipublic static void setLoadOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)
Sets load options provider.
clean
@OpenApipublic static void clean([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) elements,
 [ProgressStatus](../../../task/ProgressStatus.html) progress)
Disposes given Eclipse UML2 elements.
Parameters:
`elements` - Eclipse UML2 elements.
`progress` - progress

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v2</a></div>
<h1 class="title" title="Class EmfUml2PersistenceHelper">Class EmfUml2PersistenceHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">EmfUml2PersistenceHelper</span>
<span class="extends-implements">extends com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</span></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">addResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Register resource set initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clean(java.util.Collection,com.nomagic.task.ProgressStatus)">clean</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Disposes given Eclipse UML2 elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoadOptionsProvider()">getLoadOptionsProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns load options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSaveOptionsProvider()">getSaveOptionsProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns save options provider</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">removeResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Remove resource set initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">setLoadOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> loadOptionsProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets load options provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">setSaveOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> saveOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets save options provider.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</h3>
<code>getOptionsDir, registerPackage, removeIllegalCharacters</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getSaveOptionsProvider()">
<h3>getSaveOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></span> <span class="element-name">getSaveOptionsProvider</span>()</div>
<div class="block">Returns save options provider</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>persistence options provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">
<h3>setSaveOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setSaveOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> saveOptionsProvider)</span></div>
<div class="block">Sets save options provider.</div>
</section>
</li>
<li>
<section class="detail" id="getLoadOptionsProvider()">
<h3>getLoadOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a></span> <span class="element-name">getLoadOptionsProvider</span>()</div>
<div class="block">Returns load options provider.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>persistence options provider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">
<h3>addResourceSetInitializer</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Register resource set initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - resource set initializer to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.v2.ResourceSetInitializer)">
<h3>removeResourceSetInitializer</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Remove resource set initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - resource set initializer to remove.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.v2.PersistenceOptionsProvider)">
<h3>setLoadOptionsProvider</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setLoadOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2">PersistenceOptionsProvider</a> loadOptionsProvider)</span></div>
<div class="block">Sets load options provider.</div>
</section>
</li>
<li>
<section class="detail" id="clean(java.util.Collection,com.nomagic.task.ProgressStatus)">
<h3>clean</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">clean</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> elements,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> progress)</span></div>
<div class="block">Disposes given Eclipse UML2 elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - Eclipse UML2 elements.</dd>
<dd><code>progress</code> - progress</dd>
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
