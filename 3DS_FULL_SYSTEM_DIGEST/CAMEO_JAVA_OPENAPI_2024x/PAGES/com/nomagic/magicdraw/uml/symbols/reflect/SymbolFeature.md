# JAVA OPENAPI: SymbolFeature (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/symbols/reflect/SymbolFeature.html
- source_path: `com/nomagic/magicdraw/uml/symbols/reflect/SymbolFeature.html`
- source_sha256: `a43840bde09f2fd45cde84d7451ebf2fcd70577c8abaad8b5d95bf10f41c2ffb`
- captured_utc: `2026-07-14T16:52:14.350911+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.reflect](package-summary.html)

## Interface SymbolFeature<T>

@OpenApiAllpublic interfaceSymbolFeature<T>
Meta information about persistent symbol feature.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default [T](SymbolFeature.html)`
`[getDefaultValue](#getDefaultValue())()`
Get default value.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`

`[SymbolFeatureTypes](SymbolFeatureTypes.html)`
`[getType](#getType())()`

`default boolean`
`[isMultiple](#isMultiple())()`

`default boolean`
`[isOrdered](#isOrdered())()`

============ METHOD DETAIL ========== 
Method Details
getName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns:
name of feature. Each symbol can have only one feature with given name.
getType
[SymbolFeatureTypes](SymbolFeatureTypes.html) getType()
Returns:
type of feature.
isMultiple
default boolean isMultiple()
Returns:
true if feature is multiple value.
isOrdered
default boolean isOrdered()
Returns:
true if feature is ordered value. In case feature is not multiple method may return
 any value.
getDefaultValue
@CheckForNulldefault [T](SymbolFeature.html) getDefaultValue()
Get default value.
Returns:
default value.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.reflect</a></div>
<h1 class="title" title="Interface SymbolFeature">Interface SymbolFeature&lt;T&gt;</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SymbolFeature&lt;T&gt;</span></div>
<div class="block">Meta information about persistent symbol feature.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a href="SymbolFeature.html" title="type parameter in SymbolFeature">T</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getDefaultValue()">getDefaultValue</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Get default value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="SymbolFeatureTypes.html" title="enum class in com.nomagic.magicdraw.uml.symbols.reflect">SymbolFeatureTypes</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getType()">getType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isMultiple()">isMultiple</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isOrdered()">isOrdered</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of feature. Each symbol can have only one feature with given name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="return-type"><a href="SymbolFeatureTypes.html" title="enum class in com.nomagic.magicdraw.uml.symbols.reflect">SymbolFeatureTypes</a></span> <span class="element-name">getType</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>type of feature.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMultiple()">
<h3>isMultiple</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isMultiple</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if feature is multiple value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOrdered()">
<h3>isOrdered</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isOrdered</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if feature is ordered value. In case feature is not multiple method may return
 any value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultValue()">
<h3>getDefaultValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">default</span> <span class="return-type"><a href="SymbolFeature.html" title="type parameter in SymbolFeature">T</a></span> <span class="element-name">getDefaultValue</span>()</div>
<div class="block">Get default value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>default value.</dd>
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
