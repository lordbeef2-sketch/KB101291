# JAVA OPENAPI: DiagramContextToolbarAMConfigurator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/actions/DiagramContextToolbarAMConfigurator.html
- source_path: `com/nomagic/magicdraw/actions/DiagramContextToolbarAMConfigurator.html`
- source_sha256: `4751c11408e5c3bbece1041018e64b9b3af015ee33abef6ab5d38051a9060d0c`
- captured_utc: `2026-07-14T16:55:02.505865+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Interface DiagramContextToolbarAMConfigurator

All Superinterfaces:
`[ConfiguratorWithPriority](ConfiguratorWithPriority.html)`, `[PriorityProvider](../utils/PriorityProvider.html)`, `[PriorityProvider](../../utils/PriorityProvider.html)`

All Known Implementing Classes:
`[BaseDiagramContextToolbarAMConfigurator](../ui/actions/BaseDiagramContextToolbarAMConfigurator.html)`

@OpenApiAllpublic interfaceDiagramContextToolbarAMConfiguratorextends [ConfiguratorWithPriority](ConfiguratorWithPriority.html)

The interface for all diagram context toolbar action configurators.
 This configurator is used for configuring context bar for element in diagram.

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
`[configure](#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.PresentationElement))([ActionsManager](../../actions/ActionsManager.html) manager,
 [PresentationElement](../uml/symbols/PresentationElement.html) requestor)`
Configure given actions manager for given diagram.
Methods inherited from interface com.nomagic.magicdraw.actions.[ConfiguratorWithPriority](ConfiguratorWithPriority.html)
`[getPriority](ConfiguratorWithPriority.html#getPriority())`

============ METHOD DETAIL ========== 
Method Details
configure
void configure([ActionsManager](../../actions/ActionsManager.html) manager,
 [PresentationElement](../uml/symbols/PresentationElement.html) requestor)
Configure given actions manager for given diagram.
Parameters:
`manager` - the given manager
`requestor` - the selected symbol in the diagram

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Interface DiagramContextToolbarAMConfigurator">Interface DiagramContextToolbarAMConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></code>, <code><a href="../utils/PriorityProvider.html" title="interface in com.nomagic.magicdraw.utils">PriorityProvider</a></code>, <code><a href="../../utils/PriorityProvider.html" title="interface in com.nomagic.utils">PriorityProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../ui/actions/BaseDiagramContextToolbarAMConfigurator.html" title="class in com.nomagic.magicdraw.ui.actions">BaseDiagramContextToolbarAMConfigurator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">DiagramContextToolbarAMConfigurator</span><span class="extends-implements">
extends <a href="ConfiguratorWithPriority.html" title="interface in com.nomagic.magicdraw.actions">ConfiguratorWithPriority</a></span></div>
<div class="block">The interface for all diagram context toolbar action configurators.
 This configurator is used for configuring context bar for element in diagram.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.PresentationElement)">configure</a><wbr/>(<a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requestor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Configure given actions manager for given diagram.</div>
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
<section class="detail" id="configure(com.nomagic.actions.ActionsManager,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>configure</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../../actions/ActionsManager.html" title="class in com.nomagic.actions">ActionsManager</a> manager,
 <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> requestor)</span></div>
<div class="block">Configure given actions manager for given diagram.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>manager</code> - the given manager</dd>
<dd><code>requestor</code> - the selected symbol in the diagram</dd>
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
