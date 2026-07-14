# JAVA OPENAPI: EmfUml2PersistenceManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/emfuml2xmi/helpers/EmfUml2PersistenceManager.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/helpers/EmfUml2PersistenceManager.html`
- source_sha256: `662fbfea358a18d896705c105e00d086264de42eb682f9b478c54e3a5fd10abb`
- captured_utc: `2026-07-14T16:51:19.067175+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.helpers](package-summary.html)

## Interface EmfUml2PersistenceManager

All Known Implementing Classes:
`[EmfUml2PersistenceManager](../v3/helpers/EmfUml2PersistenceManager.html)`, `com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl`

@OpenApiAllpublic interfaceEmfUml2PersistenceManager

Stores save and load options.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addLoadOptionsProvider](#addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)`
Sets load options provider.
`void`
`[addResourceSetInitializer](#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Register resource set initializer.
`void`
`[addSaveOptionsProvider](#addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)`
Sets save options provider.
`void`
`[removeLoadOptionsProvider](#removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)`
Remove load options provider.
`void`
`[removeResourceSetInitializer](#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer))([ResourceSetInitializer](ResourceSetInitializer.html) initializer)`
Remove resource set initializer.
`void`
`[removeSaveOptionsProvider](#removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider))([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)`
Remove save options provider.

============ METHOD DETAIL ========== 
Method Details
addSaveOptionsProvider
void addSaveOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)
Sets save options provider.
removeSaveOptionsProvider
void removeSaveOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) saveOptionsProvider)
Remove save options provider.
addLoadOptionsProvider
void addLoadOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)
Sets load options provider.
removeLoadOptionsProvider
void removeLoadOptionsProvider([PersistenceOptionsProvider](PersistenceOptionsProvider.html) loadOptionsProvider)
Remove load options provider.
addResourceSetInitializer
void addResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Register resource set initializer.
Parameters:
`initializer` - resource set initializer to add.
removeResourceSetInitializer
void removeResourceSetInitializer([ResourceSetInitializer](ResourceSetInitializer.html) initializer)
Remove resource set initializer.
Parameters:
`initializer` - resource set initializer to remove.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.helpers</a></div>
<h1 class="title" title="Interface EmfUml2PersistenceManager">Interface EmfUml2PersistenceManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../v3/helpers/EmfUml2PersistenceManager.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v3.helpers">EmfUml2PersistenceManager</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2PersistenceManagerImpl</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2PersistenceManager</span></div>
<div class="block">Stores save and load options.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">addLoadOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets load options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)">addResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Register resource set initializer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">addSaveOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets save options provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">removeLoadOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Remove load options provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)">removeResourceSetInitializer</a><wbr/>(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">ResourceSetInitializer</a> initializer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Remove resource set initializer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">removeSaveOptionsProvider</a><wbr/>(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Remove save options provider.</div>
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
<section class="detail" id="addSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">
<h3>addSaveOptionsProvider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addSaveOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</span></div>
<div class="block">Sets save options provider.</div>
</section>
</li>
<li>
<section class="detail" id="removeSaveOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">
<h3>removeSaveOptionsProvider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeSaveOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> saveOptionsProvider)</span></div>
<div class="block">Remove save options provider.</div>
</section>
</li>
<li>
<section class="detail" id="addLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">
<h3>addLoadOptionsProvider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addLoadOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</span></div>
<div class="block">Sets load options provider.</div>
</section>
</li>
<li>
<section class="detail" id="removeLoadOptionsProvider(com.nomagic.magicdraw.emfuml2xmi.helpers.PersistenceOptionsProvider)">
<h3>removeLoadOptionsProvider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeLoadOptionsProvider</span><wbr/><span class="parameters">(<a href="PersistenceOptionsProvider.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">PersistenceOptionsProvider</a> loadOptionsProvider)</span></div>
<div class="block">Remove load options provider.</div>
</section>
</li>
<li>
<section class="detail" id="addResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)">
<h3>addResourceSetInitializer</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Register resource set initializer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>initializer</code> - resource set initializer to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeResourceSetInitializer(com.nomagic.magicdraw.emfuml2xmi.helpers.ResourceSetInitializer)">
<h3>removeResourceSetInitializer</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeResourceSetInitializer</span><wbr/><span class="parameters">(<a href="ResourceSetInitializer.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">ResourceSetInitializer</a> initializer)</span></div>
<div class="block">Remove resource set initializer.</div>
<dl class="notes">
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
