# JAVA OPENAPI: BrowserContextAMConfigurator (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/actions/BrowserContextAMConfigurator.html
- source_path: `com/nomagic/magicdraw/actions/BrowserContextAMConfigurator.html`
- source_sha256: `bc6339b35b3fa11e0af6a8268a478440f56d9cbe3c86c7aabef92393f19c7992`
- captured_utc: `2026-07-14T16:55:02.903871+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Interface BrowserContextAMConfigurator

All Superinterfaces:
`[ConfiguratorWithPriority](ConfiguratorWithPriority.html)`, `[PriorityProvider](../utils/PriorityProvider.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`

@OpenApiAllpublic interfaceBrowserContextAMConfiguratorextends [ConfiguratorWithPriority](ConfiguratorWithPriority.html)

Configurator for configuring managers for browser pop up menu.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.utils.[PriorityProvider](../../utils/PriorityProvider.html)
`[HIGH_PRIORITY](../../utils/PriorityProvider.html#HIGH_PRIORITY), [LOW_PRIORITY](../../utils/PriorityProvider.html#LOW_PRIORITY), [MEDIUM_PRIORITY](../../utils/PriorityProvider.html#MEDIUM_PRIORITY)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[configure](#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Tree))([ActionsManager](../../actions/ActionsManager.html) mngr,
 [Tree](../ui/browser/Tree.html) tree)`
Method should add or remove actions for given browser context menu.
Methods inherited from interface com.nomagic.magicdraw.actions.[ConfiguratorWithPriority](ConfiguratorWithPriority.html)
`[getPriority](ConfiguratorWithPriority.html#getPriority())`

============ METHOD DETAIL ========== 
Method Details
configure
void configure([ActionsManager](../../actions/ActionsManager.html) mngr,
 [Tree](../ui/browser/Tree.html) tree)
Method should add or remove actions for given browser context menu.
Parameters:
`mngr` - manager to be configured.
`tree` - tree for which context menu actions will be configured.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Interface BrowserContextAMConfigurator">Interface BrowserContextAMConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BrowserContextAMConfigurator</span><span class="extends-implements">
extends <a href="ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></span></div>
<div class="block">Configurator for configuring managers for browser pop up menu.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.utils.PriorityProvider">Fields inherited from interface com.nomagic.utils.<a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></h3>
<code><a href="../../utils/PriorityProvider.html#HIGH_PRIORITY">HIGH_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#LOW_PRIORITY">LOW_PRIORITY</a>, <a href="../../utils/PriorityProvider.html#MEDIUM_PRIORITY">MEDIUM_PRIORITY</a></code></div>
</section>
</li>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Tree)">configure</a><wbr/>(<a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> mngr,
 <a href="../ui/browser/Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method should add or remove actions for given browser context menu.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.actions.ConfiguratorWithPriority">Methods inherited from interface com.nomagic.magicdraw.actions.<a href="ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></h3>
<code><a href="ConfiguratorWithPriority.html#getPriority()">getPriority</a></code></div>
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
<section class="detail" id="configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.ui.browser.Tree)">
<h3>configure</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> mngr,
 <a href="../ui/browser/Tree.html" title="class in com.nomagic.magicdraw.ui.browser">Tree</a> tree)</span></div>
<div class="block">Method should add or remove actions for given browser context menu.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mngr</code> - manager to be configured.</dd>
<dd><code>tree</code> - tree for which context menu actions will be configured.</dd>
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
