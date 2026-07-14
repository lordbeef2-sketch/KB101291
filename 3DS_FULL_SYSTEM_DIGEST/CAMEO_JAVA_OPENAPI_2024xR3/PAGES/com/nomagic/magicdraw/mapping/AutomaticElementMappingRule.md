# JAVA OPENAPI: AutomaticElementMappingRule (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/mapping/AutomaticElementMappingRule.html
- source_path: `com/nomagic/magicdraw/mapping/AutomaticElementMappingRule.html`
- source_sha256: `668aec2bef1f775cb3f29926c670dbd778c753fcbe7ed8d7269c262ecf2b52b2`
- captured_utc: `2026-07-14T16:55:24.287109+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.mapping](package-summary.html)

## Interface AutomaticElementMappingRule

@OpenApiAllpublic interfaceAutomaticElementMappingRule
Rule for describing when source element can be mapped to target element without user input

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`boolean`
`[accept](#accept(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement))([TypedElement](../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) sourceElement)`
Gets if mapping rule can be applied to source element
`[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElementToMap](#getElementToMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) sourceElement,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> targetElements)`
Get target element to be automatically mapped to the source element.
`default boolean`
`[isOneToOneMapping](#isOneToOneMapping())()`
Allow one to one or many to one mapping.

============ METHOD DETAIL ========== 
Method Details
getElementToMap
@CheckForNull[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElementToMap([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) sourceElement,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> targetElements)
Get target element to be automatically mapped to the source element.
 If this method returns an element, provided elements will be mapped at once
 If this method returns null, user still can pair elements later manually
Parameters:
`sourceElement` - source element
`targetElements` - list of candidate target elements. Target elements are always in the same nesting depth as the source element
Returns:
element that can be mapped automatically, without user input, to the source element
accept
boolean accept([TypedElement](../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html) sourceElement)
Gets if mapping rule can be applied to source element
Parameters:
`sourceElement` - source element (property)
Returns:
true if rule can be used, else false
isOneToOneMapping
default boolean isOneToOneMapping()
Allow one to one or many to one mapping.
Returns:
true if only one to one mapping is allowed, false - many to one

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.mapping</a></div>
<h1 class="title" title="Interface AutomaticElementMappingRule">Interface AutomaticElementMappingRule</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">AutomaticElementMappingRule</span></div>
<div class="block">Rule for describing when source element can be mapped to target element without user input</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#accept(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)">accept</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> sourceElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets if mapping rule can be applied to source element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementToMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List)">getElementToMap</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> sourceElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; targetElements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get target element to be automatically mapped to the source element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isOneToOneMapping()">isOneToOneMapping</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Allow one to one or many to one mapping.</div>
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
<section class="detail" id="getElementToMap(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.List)">
<h3>getElementToMap</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElementToMap</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> sourceElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; targetElements)</span></div>
<div class="block">Get target element to be automatically mapped to the source element.
 If this method returns an element, provided elements will be mapped at once
 If this method returns null, user still can pair elements later manually</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceElement</code> - source element</dd>
<dd><code>targetElements</code> - list of candidate target elements. Target elements are always in the same nesting depth as the source element</dd>
<dt>Returns:</dt>
<dd>element that can be mapped automatically, without user input, to the source element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="accept(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.TypedElement)">
<h3>accept</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/TypedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">TypedElement</a> sourceElement)</span></div>
<div class="block">Gets if mapping rule can be applied to source element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceElement</code> - source element (property)</dd>
<dt>Returns:</dt>
<dd>true if rule can be used, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOneToOneMapping()">
<h3>isOneToOneMapping</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isOneToOneMapping</span>()</div>
<div class="block">Allow one to one or many to one mapping.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if only one to one mapping is allowed, false - many to one</dd>
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
