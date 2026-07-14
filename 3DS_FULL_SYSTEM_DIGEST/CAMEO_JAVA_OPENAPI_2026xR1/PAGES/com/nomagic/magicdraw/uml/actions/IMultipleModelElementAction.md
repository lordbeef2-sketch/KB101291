# JAVA OPENAPI: IMultipleModelElementAction (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/actions/IMultipleModelElementAction.html
- source_path: `com/nomagic/magicdraw/uml/actions/IMultipleModelElementAction.html`
- source_sha256: `f8f6afb00a47888f69f3f13d0bbee73315cc815427c7d43d38fc983222aa07a5`
- captured_utc: `2026-07-14T16:46:05.514874+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.actions](package-summary.html)

## Interface IMultipleModelElementAction

All Known Implementing Classes:
`[MultipleModelElementAction](MultipleModelElementAction.html)`

@OpenApiAllpublic interfaceIMultipleModelElementAction

Actions should implement this interface, so correct element provider is set when action used in browser and diagram.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ModelElementsProvider](../core/ModelElementsProvider.html)`
`[getElementsProvider](#getElementsProvider())()`
Gets the provider.
`void`
`[setElementsProvider](#setElementsProvider(com.nomagic.magicdraw.uml.core.ModelElementsProvider))([ModelElementsProvider](../core/ModelElementsProvider.html) provider)`
Sets the provider.

============ METHOD DETAIL ========== 
Method Details
setElementsProvider
void setElementsProvider(@CheckForNull
 [ModelElementsProvider](../core/ModelElementsProvider.html) provider)
Sets the provider.
Parameters:
`provider` - The provider to set
getElementsProvider
@CheckForNull[ModelElementsProvider](../core/ModelElementsProvider.html) getElementsProvider()
Gets the provider.
Returns:
Returns a ModelElementProvider

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.actions</a></div>
<h1 class="title" title="Interface IMultipleModelElementAction">Interface IMultipleModelElementAction</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="MultipleModelElementAction.html" title="class in com.nomagic.magicdraw.uml.actions">MultipleModelElementAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IMultipleModelElementAction</span></div>
<div class="block">Actions should implement this interface, so correct element provider is set when action used in browser and diagram.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../core/ModelElementsProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementsProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementsProvider()">getElementsProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setElementsProvider(com.nomagic.magicdraw.uml.core.ModelElementsProvider)">setElementsProvider</a><wbr/>(<a href="../core/ModelElementsProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementsProvider</a> provider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the provider.</div>
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
<section class="detail" id="setElementsProvider(com.nomagic.magicdraw.uml.core.ModelElementsProvider)">
<h3>setElementsProvider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setElementsProvider</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/ModelElementsProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementsProvider</a> provider)</span></div>
<div class="block">Sets the provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The provider to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsProvider()">
<h3>getElementsProvider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../core/ModelElementsProvider.html" title="interface in com.nomagic.magicdraw.uml.core">ModelElementsProvider</a></span> <span class="element-name">getElementsProvider</span>()</div>
<div class="block">Gets the provider.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns a ModelElementProvider</dd>
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
