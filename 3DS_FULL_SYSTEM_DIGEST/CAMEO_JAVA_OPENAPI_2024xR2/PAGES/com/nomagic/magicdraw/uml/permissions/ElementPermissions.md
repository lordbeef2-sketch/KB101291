# JAVA OPENAPI: ElementPermissions (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/permissions/ElementPermissions.html
- source_path: `com/nomagic/magicdraw/uml/permissions/ElementPermissions.html`
- source_sha256: `5e47363051ab4592f309aac3ee221071df72e8ca1bb40f42ce6391ee788d5f23`
- captured_utc: `2026-07-14T16:55:54.400447+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.permissions](package-summary.html)

## Interface ElementPermissions

@OpenApiAllpublic interfaceElementPermissions
Interface for elements permissions handler.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[canAddChild](#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) parent,
 [BaseElement](../BaseElement.html) child)`
Checks if there is permissions to add given child to given parent.
`boolean`
`[canCreateChildIn](#canCreateChildIn(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Return true if children can be created in given element
`boolean`
`[canDelete](#canDelete(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Checks if element can be deleted
`boolean`
`[isElementEditable](#isElementEditable(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../BaseElement.html) element)`
Return true if elements properties can be changed.

============ METHOD DETAIL ========== 
Method Details
isElementEditable
boolean isElementEditable([BaseElement](../BaseElement.html) element)
Return true if elements properties can be changed.
Parameters:
`element` - element to check.
Returns:
true if elements properties can be changed.
canCreateChildIn
boolean canCreateChildIn([BaseElement](../BaseElement.html) element)
Return true if children can be created in given element
Parameters:
`element` - element to check
Returns:
true if children can be created in given element
canAddChild
boolean canAddChild([BaseElement](../BaseElement.html) parent,
 [BaseElement](../BaseElement.html) child)
Checks if there is permissions to add given child to given parent.
Parameters:
`parent` - parent to check.
`child` - child to check
Returns:
true if there is permissions to add given child to given parent.
canDelete
boolean canDelete([BaseElement](../BaseElement.html) element)
Checks if element can be deleted
Parameters:
`element` - element to check
Returns:
if element can be deleted.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.permissions</a></div>
<h1 class="title" title="Interface ElementPermissions">Interface ElementPermissions</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementPermissions</span></div>
<div class="block">Interface for elements permissions handler.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">canAddChild</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> parent,
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if there is permissions to add given child to given parent.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canCreateChildIn(com.nomagic.magicdraw.uml.BaseElement)">canCreateChildIn</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return true if children can be created in given element</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canDelete(com.nomagic.magicdraw.uml.BaseElement)">canDelete</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if element can be deleted</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isElementEditable(com.nomagic.magicdraw.uml.BaseElement)">isElementEditable</a><wbr/>(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return true if elements properties can be changed.</div>
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
<section class="detail" id="isElementEditable(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isElementEditable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isElementEditable</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Return true if elements properties can be changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check.</dd>
<dt>Returns:</dt>
<dd>true if elements properties can be changed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canCreateChildIn(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canCreateChildIn</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canCreateChildIn</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Return true if children can be created in given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true if children can be created in given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canAddChild(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">
<h3>canAddChild</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canAddChild</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> parent,
 <a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> child)</span></div>
<div class="block">Checks if there is permissions to add given child to given parent.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - parent to check.</dd>
<dd><code>child</code> - child to check</dd>
<dt>Returns:</dt>
<dd>true if there is permissions to add given child to given parent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canDelete(com.nomagic.magicdraw.uml.BaseElement)">
<h3>canDelete</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canDelete</span><wbr/><span class="parameters">(<a href="../BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Checks if element can be deleted</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to check</dd>
<dt>Returns:</dt>
<dd>if element can be deleted.</dd>
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
