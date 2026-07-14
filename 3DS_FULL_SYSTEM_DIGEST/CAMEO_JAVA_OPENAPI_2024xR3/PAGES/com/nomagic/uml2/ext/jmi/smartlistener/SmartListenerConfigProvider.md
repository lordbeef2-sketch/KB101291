# JAVA OPENAPI: SmartListenerConfigProvider (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html
- source_path: `com/nomagic/uml2/ext/jmi/smartlistener/SmartListenerConfigProvider.html`
- source_sha256: `355d081bdabf7e399b001c32c36a4f1101f0267c424cd2df8ec1f5ab091ebd04`
- captured_utc: `2026-07-14T16:56:16.406693+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.smartlistener](package-summary.html)

## Interface SmartListenerConfigProvider

All Known Subinterfaces:
`[DependencyExtractor](../../../../magicdraw/dependencymatrix/datamodel/cell/DependencyExtractor.html)`, `[SmartListenerConfigurationProvider](../../../../magicdraw/validation/SmartListenerConfigurationProvider.html)`

All Known Implementing Classes:
`[DefaultValidationRuleImpl](../../../../magicdraw/validation/DefaultValidationRuleImpl.html)`

@OpenApiAllpublic interfaceSmartListenerConfigProvider

Defines interface for smart listeners configuration providers by element class type.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)>,[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)>>`
`[getListenerConfigurations](#getListenerConfigurations())()`
Implementation of the method should return a map of classes derived from [`Element`](../../magicdraw/classes/mdkernel/Element.html) class and [`SmartListenerConfig`](SmartListenerConfig.html)
 objects.

============ METHOD DETAIL ========== 
Method Details
getListenerConfigurations
@CheckForNull[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)>,[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)>> getListenerConfigurations()
Implementation of the method should return a map of classes derived from [`Element`](../../magicdraw/classes/mdkernel/Element.html) class and [`SmartListenerConfig`](SmartListenerConfig.html)
 objects.
Returns:
map of listener configurations by element class type

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.smartlistener</a></div>
<h1 class="title" title="Interface SmartListenerConfigProvider">Interface SmartListenerConfigProvider</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="../../../../magicdraw/dependencymatrix/datamodel/cell/DependencyExtractor.html" title="interface in com.nomagic.magicdraw.dependencymatrix.datamodel.cell">DependencyExtractor</a></code>, <code><a href="../../../../magicdraw/validation/SmartListenerConfigurationProvider.html" title="interface in com.nomagic.magicdraw.validation">SmartListenerConfigurationProvider</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../../../../magicdraw/validation/DefaultValidationRuleImpl.html" title="class in com.nomagic.magicdraw.validation">DefaultValidationRuleImpl</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SmartListenerConfigProvider</span></div>
<div class="block">Defines interface for smart listeners configuration providers by element class type.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getListenerConfigurations()">getListenerConfigurations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Implementation of the method should return a map of classes derived from <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a> class and <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a>
 objects.</div>
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
<section class="detail" id="getListenerConfigurations()">
<h3>getListenerConfigurations</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;&gt;</span> <span class="element-name">getListenerConfigurations</span>()</div>
<div class="block">Implementation of the method should return a map of classes derived from <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a> class and <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a>
 objects.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of listener configurations by element class type</dd>
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
