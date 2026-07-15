# JAVA OPENAPI: ISingleModelElementAction (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/actions/ISingleModelElementAction.html
- source_path: `com/nomagic/magicdraw/uml/actions/ISingleModelElementAction.html`
- source_sha256: `ddfb9c4f11fa38b7b2ac1dc6f44e56fa995ae25983f17276c4fc8f06d5465271`
- captured_utc: `2026-07-14T16:52:10.345856+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.actions](package-summary.html)

## Interface ISingleModelElementAction

All Known Implementing Classes:
`[MultipleModelElementAction](MultipleModelElementAction.html)`, `[SingleModelElementAction](SingleModelElementAction.html)`

@OpenApiAllpublic interfaceISingleModelElementAction

Base class for actions to work with one model element.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[ModelElementProvider](../ModelElementProvider.html)`
`[getProvider](#getProvider())()`
Gets the provider.
`void`
`[setProvider](#setProvider(com.nomagic.magicdraw.uml.ModelElementProvider))([ModelElementProvider](../ModelElementProvider.html) provider)`
Sets the provider.

============ METHOD DETAIL ========== 
Method Details
getProvider
@CheckForNull[ModelElementProvider](../ModelElementProvider.html) getProvider()
Gets the provider.
Returns:
Returns a ModelElementProvider
setProvider
void setProvider(@CheckForNull
 [ModelElementProvider](../ModelElementProvider.html) provider)
Sets the provider.
Parameters:
`provider` - The provider to set

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.actions</a></div>
<h1 class="title" title="Interface ISingleModelElementAction">Interface ISingleModelElementAction</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="MultipleModelElementAction.html" title="class in com.nomagic.magicdraw.uml.actions">MultipleModelElementAction</a></code>, <code><a href="SingleModelElementAction.html" title="class in com.nomagic.magicdraw.uml.actions">SingleModelElementAction</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ISingleModelElementAction</span></div>
<div class="block">Base class for actions to work with one model element.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProvider()">getProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setProvider(com.nomagic.magicdraw.uml.ModelElementProvider)">setProvider</a><wbr/>(<a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> provider)</code></div>
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
<section class="detail" id="getProvider()">
<h3>getProvider</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a></span> <span class="element-name">getProvider</span>()</div>
<div class="block">Gets the provider.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Returns a ModelElementProvider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProvider(com.nomagic.magicdraw.uml.ModelElementProvider)">
<h3>setProvider</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setProvider</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../ModelElementProvider.html" title="interface in com.nomagic.magicdraw.uml">ModelElementProvider</a> provider)</span></div>
<div class="block">Sets the provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - The provider to set</dd>
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
