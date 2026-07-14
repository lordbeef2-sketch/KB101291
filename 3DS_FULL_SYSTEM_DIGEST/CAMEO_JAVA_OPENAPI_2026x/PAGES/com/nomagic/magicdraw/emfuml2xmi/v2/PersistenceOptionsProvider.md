# JAVA OPENAPI: PersistenceOptionsProvider (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/emfuml2xmi/v2/PersistenceOptionsProvider.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/PersistenceOptionsProvider.html`
- source_sha256: `3cdaa7e2d5fa9f98e5c8682084b2e84087e4b108ccbe278e0561f7bd624eff2d`
- captured_utc: `2026-07-14T16:57:56.466517+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v2](package-summary.html)

## Interface PersistenceOptionsProvider

@OpenApiAllpublic interfacePersistenceOptionsProvider

Eclipse UML2 persistence options provider - provides options used to load/save the Eclipse UML2 model.

See Also:
`XMLResource`

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)`
`[getOptions](#getOptions(org.eclipse.emf_2_2_3.ecore.resource.ResourceSet,java.lang.String))(org.eclipse.emf_2_2_3.ecore.resource.ResourceSet resourceSet,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) optionsDir)`
Returns options used to load/save the Eclipse UML2 model.

============ METHOD DETAIL ========== 
Method Details
getOptions
[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html) getOptions(org.eclipse.emf_2_2_3.ecore.resource.ResourceSet resourceSet,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) optionsDir)
Returns options used to load/save the Eclipse UML2 model.
Parameters:
`resourceSet` -
`optionsDir` -
Returns:
options map

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v2</a></div>
<h1 class="title" title="Interface PersistenceOptionsProvider">Interface PersistenceOptionsProvider</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PersistenceOptionsProvider</span></div>
<div class="block">Eclipse UML2 persistence options provider - provides options used to load/save the Eclipse UML2 model.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><code>XMLResource</code></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOptions(org.eclipse.emf_2_2_3.ecore.resource.ResourceSet,java.lang.String)">getOptions</a><wbr/>(org.eclipse.emf_2_2_3.ecore.resource.ResourceSet resourceSet,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsDir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns options used to load/save the Eclipse UML2 model.</div>
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
<section class="detail" id="getOptions(org.eclipse.emf_2_2_3.ecore.resource.ResourceSet,java.lang.String)">
<h3>getOptions</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getOptions</span><wbr/><span class="parameters">(org.eclipse.emf_2_2_3.ecore.resource.ResourceSet resourceSet,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsDir)</span></div>
<div class="block">Returns options used to load/save the Eclipse UML2 model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resourceSet</code> - </dd>
<dd><code>optionsDir</code> - </dd>
<dt>Returns:</dt>
<dd>options map</dd>
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
