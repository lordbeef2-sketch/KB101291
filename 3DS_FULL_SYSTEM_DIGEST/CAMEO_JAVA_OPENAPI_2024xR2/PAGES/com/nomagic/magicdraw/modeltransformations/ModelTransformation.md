# JAVA OPENAPI: ModelTransformation (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/modeltransformations/ModelTransformation.html
- source_path: `com/nomagic/magicdraw/modeltransformations/ModelTransformation.html`
- source_sha256: `8bc02265b703de190a187951341455ff7dbd2c8f575ec558b71eab6c477f5c30`
- captured_utc: `2026-07-14T16:55:23.567103+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations](package-summary.html)

## Interface ModelTransformation

All Known Implementing Classes:
`[AnyToAnyModelTransformation](impl/any_to_any/AnyToAnyModelTransformation.html)`

@OpenApiAllpublic interfaceModelTransformation

Interface for model transformation.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[setTask](#setTask(com.nomagic.task.Task))([Task](../../task/Task.html) task)`
Sets task for transformation.
`[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[transform](#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) objects,
 [ModelTransformationInfo](ModelTransformationInfo.html) info,
 [TypeMapProfile](TypeMapProfile.html) typeMap,
 [PropertyManager](../properties/PropertyManager.html) propertyManager,
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) destination)`
Performs transformation on specific set of objects
`void`
`[updateTransform](#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformationPackage,
 [TypeMapProfile](TypeMapProfile.html) typeMap,
 [PropertyManager](../properties/PropertyManager.html) propertyManager,
 boolean syncDestination)`
Updates transformation on specific set of objects

============ METHOD DETAIL ========== 
Method Details
transform
[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transform(@CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) objects,
 @CheckForNull
 [ModelTransformationInfo](ModelTransformationInfo.html) info,
 @CheckForNull
 [TypeMapProfile](TypeMapProfile.html) typeMap,
 [PropertyManager](../properties/PropertyManager.html) propertyManager,
 @CheckForNull
 [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) destination)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Performs transformation on specific set of objects
Parameters:
`objects` - set of objects to transform
`info` - model transformation info
`typeMap` - type map profile to use for transformation, null for none
`propertyManager` - transformation properties
`destination` - destination model packages, null for transformation in place
Returns:
transformation model package (where transformation links are stored)
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - in case target model elements are read-only
updateTransform
void updateTransform([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) transformationPackage,
 @CheckForNull
 [TypeMapProfile](TypeMapProfile.html) typeMap,
 [PropertyManager](../properties/PropertyManager.html) propertyManager,
 boolean syncDestination)
 throws [ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)
Updates transformation on specific set of objects
Parameters:
`transformationPackage` - package containing transformation links
`typeMap` - type map profile to use for transformation, null for none
`propertyManager` - transformation properties
`syncDestination` - true for destination overwrite
Throws:
`[ReadOnlyElementException](../openapi/uml/ReadOnlyElementException.html)` - in case target model elements are read-only
setTask
void setTask([Task](../../task/Task.html) task)
Sets task for transformation. Transformation can use Task for accesing progress status and etc.
Parameters:
`task` - transformation task

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations</a></div>
<h1 class="title" title="Interface ModelTransformation">Interface ModelTransformation</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="impl/any_to_any/AnyToAnyModelTransformation.html" title="class in com.nomagic.magicdraw.modeltransformations.impl.any_to_any">AnyToAnyModelTransformation</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModelTransformation</span></div>
<div class="block">Interface for model transformation.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTask(com.nomagic.task.Task)">setTask</a><wbr/>(<a href="../../task/Task.html" title="class in com.nomagic.task">Task</a> task)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets task for transformation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">transform</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> objects,
 <a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info,
 <a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> destination)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs transformation on specific set of objects</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean)">updateTransform</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformationPackage,
 <a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 boolean syncDestination)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Updates transformation on specific set of objects</div>
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
<section class="detail" id="transform(java.util.Collection,com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>transform</h3>
<div class="member-signature"><span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">transform</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> objects,
 @CheckForNull
 <a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a> info,
 @CheckForNull
 <a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> destination)</span>
           throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Performs transformation on specific set of objects</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>objects</code> - set of objects to transform</dd>
<dd><code>info</code> - model transformation info</dd>
<dd><code>typeMap</code> - type map profile to use for transformation, null for none</dd>
<dd><code>propertyManager</code> - transformation properties</dd>
<dd><code>destination</code> - destination model packages, null for transformation in place</dd>
<dt>Returns:</dt>
<dd>transformation model package (where transformation links are stored)</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - in case target model elements are read-only</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateTransform(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.modeltransformations.TypeMapProfile,com.nomagic.magicdraw.properties.PropertyManager,boolean)">
<h3>updateTransform</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">updateTransform</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> transformationPackage,
 @CheckForNull
 <a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a> typeMap,
 <a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> propertyManager,
 boolean syncDestination)</span>
              throws <span class="exceptions"><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Updates transformation on specific set of objects</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformationPackage</code> - package containing transformation links</dd>
<dd><code>typeMap</code> - type map profile to use for transformation, null for none</dd>
<dd><code>propertyManager</code> - transformation properties</dd>
<dd><code>syncDestination</code> - true for destination overwrite</dd>
<dt>Throws:</dt>
<dd><code><a href="../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - in case target model elements are read-only</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTask(com.nomagic.task.Task)">
<h3>setTask</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTask</span><wbr/><span class="parameters">(<a href="../../task/Task.html" title="class in com.nomagic.task">Task</a> task)</span></div>
<div class="block">Sets task for transformation. Transformation can use Task for accesing progress status and etc.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>task</code> - transformation task</dd>
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
