# JAVA OPENAPI: VariationPointsProvider (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/variants/variationpoints/VariationPointsProvider.html
- source_path: `com/nomagic/magicdraw/variants/variationpoints/VariationPointsProvider.html`
- source_sha256: `7c1524bd9faf7ef861a548fe77a7e4e01ba1fd2b795a91a7af9db1e095d46c09`
- captured_utc: `2026-07-14T16:52:28.289097+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.variationpoints](package-summary.html)

## Interface VariationPointsProvider

@OpenApiAllpublic interfaceVariationPointsProvider
Implementations are used by [`VariantRealizationTransformation`](../transformation/VariantRealizationTransformation.html) to perform model transformation

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getVariabilityElements](#getVariabilityElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)`
Collects elements to be transformed in given scope
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[VariationPoint](VariationPoint.html)>`
`[getVariationPoints](#getVariationPoints(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Creates VariationPoint for given element
`void`
`[setUp](#setUp(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.properties.PropertyManager))([Project](../../core/Project.html) project,
 [PropertyManager](../../properties/PropertyManager.html) propertyManager)`
Should be called before the transformation.
`void`
`[tearDown](#tearDown(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[VariationPoint](VariationPoint.html)> failed)`
Automatically called after transformation of all variation points is finished

============ METHOD DETAIL ========== 
Method Details
getName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns:
name of this VariationPointsProvider
setUp
void setUp([Project](../../core/Project.html) project,
 @CheckForNull
 [PropertyManager](../../properties/PropertyManager.html) propertyManager)
Should be called before the transformation. Resources required for other methods should be initialized here
Parameters:
`project` - currently open project that will be transformed
`propertyManager` - may contain custom properties specific for this transformation
getVariabilityElements
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getVariabilityElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)
Collects elements to be transformed in given scope
Parameters:
`scope` - scope to collect elements from
Returns:
elements to be transformed
getVariationPoints
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[VariationPoint](VariationPoint.html)> getVariationPoints([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Creates VariationPoint for given element
Parameters:
`element` - given element
Returns:
VariationPoint for given element, [`VariationPointsFactory`](VariationPointsFactory.html)
tearDown
void tearDown([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[VariationPoint](VariationPoint.html)> failed)
Automatically called after transformation of all variation points is finished
Parameters:
`failed` - list of variation points that could not be successfully transformed

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.variationpoints</a></div>
<h1 class="title" title="Interface VariationPointsProvider">Interface VariationPointsProvider</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">VariationPointsProvider</span></div>
<div class="block">Implementations are used by <a href="../transformation/VariantRealizationTransformation.html" title="class in com.nomagic.magicdraw.variants.transformation"><code>VariantRealizationTransformation</code></a> to perform model transformation</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariabilityElements(java.util.Collection)">getVariabilityElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Collects elements to be transformed in given scope</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariationPoints(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getVariationPoints</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates VariationPoint for given element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUp(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.properties.PropertyManager)">setUp</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Should be called before the transformation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#tearDown(java.util.Collection)">tearDown</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&gt; failed)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Automatically called after transformation of all variation points is finished</div>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of this VariationPointsProvider</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUp(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.properties.PropertyManager)">
<h3>setUp</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setUp</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a href="../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager)</span></div>
<div class="block">Should be called before the transformation. Resources required for other methods should be initialized here</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - currently open project that will be transformed</dd>
<dd><code>propertyManager</code> - may contain custom properties specific for this transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariabilityElements(java.util.Collection)">
<h3>getVariabilityElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getVariabilityElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</span></div>
<div class="block">Collects elements to be transformed in given scope</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scope</code> - scope to collect elements from</dd>
<dt>Returns:</dt>
<dd>elements to be transformed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariationPoints(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getVariationPoints</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&gt;</span> <span class="element-name">getVariationPoints</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Creates VariationPoint for given element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>VariationPoint for given element, <a href="VariationPointsFactory.html" title="class in com.nomagic.magicdraw.variants.variationpoints"><code>VariationPointsFactory</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="tearDown(java.util.Collection)">
<h3>tearDown</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">tearDown</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="VariationPoint.html" title="class in com.nomagic.magicdraw.variants.variationpoints">VariationPoint</a>&gt; failed)</span></div>
<div class="block">Automatically called after transformation of all variation points is finished</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>failed</code> - list of variation points that could not be successfully transformed</dd>
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
