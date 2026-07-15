# JAVA OPENAPI: VariantsModelTransformationWizardConfigurator (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/variants/ui/modeltransformation/VariantsModelTransformationWizardConfigurator.html
- source_path: `com/nomagic/magicdraw/variants/ui/modeltransformation/VariantsModelTransformationWizardConfigurator.html`
- source_sha256: `3f9130ba827a8d9513f1e1360a94bec321a827189614d9fdceb2e05f481a1708`
- captured_utc: `2026-07-14T16:58:35.652265+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.ui.modeltransformation](package-summary.html)

## Interface VariantsModelTransformationWizardConfigurator

@OpenApiAllpublic interfaceVariantsModelTransformationWizardConfigurator

Used to provide properties related to variation points provider

See Also:
[`VariationPointsProvider`](../../variationpoints/VariationPointsProvider.html)
[`VariantsModelTransformationWizardRegistry`](VariantsModelTransformationWizardRegistry.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[PropertyManager](../../../properties/PropertyManager.html)`
`[getInvisibleProperties](#getInvisibleProperties(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Properties are saved in project options as invisible properties
`[VariationPointsProvider](../../variationpoints/VariationPointsProvider.html)`
`[getVariationPointsProvider](#getVariationPointsProvider())()`

`[PropertyManager](../../../properties/PropertyManager.html)`
`[getVisibleProperties](#getVisibleProperties(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Properties are saved in project options as invisible properties
`boolean`
`[isVariationPointsProviderVisible](#isVariationPointsProviderVisible(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Checks if @see VariationPointsProvider should be visible in model transformation wizard dialog
 for given project

============ METHOD DETAIL ========== 
Method Details
getVariationPointsProvider
[VariationPointsProvider](../../variationpoints/VariationPointsProvider.html) getVariationPointsProvider()
Returns:
VariationPointsProvider
See Also:
[`VariationPointsProvider`](../../variationpoints/VariationPointsProvider.html)
getVisibleProperties
@CheckForNull[PropertyManager](../../../properties/PropertyManager.html) getVisibleProperties([Project](../../../core/Project.html) project)
Properties are saved in project options as invisible properties
Parameters:
`project` - currently active project
Returns:
properties that will be visible and may be edited in model transformation wizard transformation details panel
See Also:
[`VariationPointsProvider`](../../variationpoints/VariationPointsProvider.html)
getInvisibleProperties
@CheckForNull[PropertyManager](../../../properties/PropertyManager.html) getInvisibleProperties([Project](../../../core/Project.html) project)
Properties are saved in project options as invisible properties
Parameters:
`project` - currently active project
Returns:
properties that wont be visible in any GUI
See Also:
[`VariationPointsProvider`](../../variationpoints/VariationPointsProvider.html)
isVariationPointsProviderVisible
boolean isVariationPointsProviderVisible([Project](../../../core/Project.html) project)
Checks if @see VariationPointsProvider should be visible in model transformation wizard dialog
 for given project
Parameters:
`project` - currently active project
Returns:
true if [`VariationPointsProvider`](../../variationpoints/VariationPointsProvider.html) should be visible in th dialog, false otherwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.ui.modeltransformation</a></div>
<h1 class="title" title="Interface VariantsModelTransformationWizardConfigurator">Interface VariantsModelTransformationWizardConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">VariantsModelTransformationWizardConfigurator</span></div>
<div class="block">Used to provide properties related to variation points provider</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints"><code>VariationPointsProvider</code></a></li>
<li><a href="VariantsModelTransformationWizardRegistry.html" title="class in com.nomagic.magicdraw.variants.ui.modeltransformation"><code>VariantsModelTransformationWizardRegistry</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getInvisibleProperties(com.nomagic.magicdraw.core.Project)">getInvisibleProperties</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Properties are saved in project options as invisible properties</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVariationPointsProvider()">getVariationPointsProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getVisibleProperties(com.nomagic.magicdraw.core.Project)">getVisibleProperties</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Properties are saved in project options as invisible properties</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isVariationPointsProviderVisible(com.nomagic.magicdraw.core.Project)">isVariationPointsProviderVisible</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if @see VariationPointsProvider should be visible in model transformation wizard dialog
 for given project</div>
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
<section class="detail" id="getVariationPointsProvider()">
<h3>getVariationPointsProvider</h3>
<div class="member-signature"><span class="return-type"><a href="../../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a></span> <span class="element-name">getVariationPointsProvider</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>VariationPointsProvider</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints"><code>VariationPointsProvider</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleProperties(com.nomagic.magicdraw.core.Project)">
<h3>getVisibleProperties</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getVisibleProperties</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Properties are saved in project options as invisible properties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - currently active project</dd>
<dt>Returns:</dt>
<dd>properties that will be visible and may be edited in model transformation wizard transformation details panel</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints"><code>VariationPointsProvider</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInvisibleProperties(com.nomagic.magicdraw.core.Project)">
<h3>getInvisibleProperties</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getInvisibleProperties</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Properties are saved in project options as invisible properties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - currently active project</dd>
<dt>Returns:</dt>
<dd>properties that wont be visible in any GUI</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints"><code>VariationPointsProvider</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVariationPointsProviderVisible(com.nomagic.magicdraw.core.Project)">
<h3>isVariationPointsProviderVisible</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isVariationPointsProviderVisible</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Checks if @see VariationPointsProvider should be visible in model transformation wizard dialog
 for given project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - currently active project</dd>
<dt>Returns:</dt>
<dd>true if <a href="../../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints"><code>VariationPointsProvider</code></a> should be visible in th dialog, false otherwise</dd>
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
