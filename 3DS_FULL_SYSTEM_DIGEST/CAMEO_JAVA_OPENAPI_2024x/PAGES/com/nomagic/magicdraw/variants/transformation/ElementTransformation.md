# JAVA OPENAPI: ElementTransformation (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/variants/transformation/ElementTransformation.html
- source_path: `com/nomagic/magicdraw/variants/transformation/ElementTransformation.html`
- source_sha256: `782df376455d96bad314d9dd35b595b576945c9da7aae539e93cb6a2b983292b`
- captured_utc: `2026-07-14T16:52:27.730088+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.transformation](package-summary.html)

## Interface ElementTransformation

@OpenApiAllpublic interfaceElementTransformation
Performs transformation for given model element using the provided VariationPoint to know how to transform

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`boolean`
`[canTransform](#canTransform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint))([VariationPoint](../variationpoints/VariationPoint.html) variationPoint)`

`default boolean`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint))([VariationPoint](../variationpoints/VariationPoint.html) variationPoint)`
Deprecated.
use com.nomagic.magicdraw.variants.transformation.ElementTransformation#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint, com.nomagic.magicdraw.variants.transformation.TransformationParameters)
`default boolean`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint,com.nomagic.magicdraw.variants.transformation.TransformationParameters))([VariationPoint](../variationpoints/VariationPoint.html) variationPoint,
 [TransformationParameters](TransformationParameters.html) parameters)`
Changes the model element.

============ METHOD DETAIL ========== 
Method Details
canTransform
boolean canTransform([VariationPoint](../variationpoints/VariationPoint.html) variationPoint)
Parameters:
`variationPoint` - defines element and its feature that is being transformed
Returns:
true if this transformation object should be used to transform the given variationPoint
transform
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default boolean transform([VariationPoint](../variationpoints/VariationPoint.html) variationPoint)
Deprecated.
use com.nomagic.magicdraw.variants.transformation.ElementTransformation#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint, com.nomagic.magicdraw.variants.transformation.TransformationParameters)
Changes the model element. Change and element are described by the provided variation point.
 This method is always called in an open session.
Parameters:
`variationPoint` - defines feature of the element that is being transformed
Returns:
true if variation point was transformed, false if transformation failed for any reason.
 Failure details should be at least printed to MDLog
transform
default boolean transform([VariationPoint](../variationpoints/VariationPoint.html) variationPoint,
 @CheckForNull
 [TransformationParameters](TransformationParameters.html) parameters)
Changes the model element. Change and element are described by the provided variation point.
 This method is always called in an open session.
Parameters:
`variationPoint` - defines feature of the element that is being transformed
`parameters` - additional transformation parameters
Returns:
true if variation point was transformed, false if transformation failed for any reason.
 Failure details should be at least printed to MDLog

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.transformation</a></div>
<h1 class="title" title="Interface ElementTransformation">Interface ElementTransformation</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ElementTransformation</span></div>
<div class="block">Performs transformation for given model element using the provided VariationPoint to know how to transform</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#canTransform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint)">canTransform</a><wbr/>(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint)">transform</a><wbr/>(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use com.nomagic.magicdraw.variants.transformation.ElementTransformation#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint, com.nomagic.magicdraw.variants.transformation.TransformationParameters)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint,com.nomagic.magicdraw.variants.transformation.TransformationParameters)">transform</a><wbr/>(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint,
 <a href="TransformationParameters.html" title="class in com.nomagic.magicdraw.variants.transformation">TransformationParameters</a> parameters)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Changes the model element.</div>
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
<section class="detail" id="canTransform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint)">
<h3>canTransform</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">canTransform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variationPoint</code> - defines element and its feature that is being transformed</dd>
<dt>Returns:</dt>
<dd>true if this transformation object should be used to transform the given variationPoint</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint)">
<h3>transform</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use com.nomagic.magicdraw.variants.transformation.ElementTransformation#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint, com.nomagic.magicdraw.variants.transformation.TransformationParameters)</div>
</div>
<div class="block">Changes the model element. Change and element are described by the provided variation point.
 This method is always called in an open session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variationPoint</code> - defines feature of the element that is being transformed</dd>
<dt>Returns:</dt>
<dd>true if variation point was transformed, false if transformation failed for any reason.
 Failure details should be at least printed to MDLog</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPoint,com.nomagic.magicdraw.variants.transformation.TransformationParameters)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a> variationPoint,
 @CheckForNull
 <a href="TransformationParameters.html" title="class in com.nomagic.magicdraw.variants.transformation">TransformationParameters</a> parameters)</span></div>
<div class="block">Changes the model element. Change and element are described by the provided variation point.
 This method is always called in an open session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variationPoint</code> - defines feature of the element that is being transformed</dd>
<dd><code>parameters</code> - additional transformation parameters</dd>
<dt>Returns:</dt>
<dd>true if variation point was transformed, false if transformation failed for any reason.
 Failure details should be at least printed to MDLog</dd>
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
