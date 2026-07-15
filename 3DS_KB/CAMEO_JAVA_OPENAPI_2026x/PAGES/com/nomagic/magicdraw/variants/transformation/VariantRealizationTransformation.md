# JAVA OPENAPI: VariantRealizationTransformation (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/variants/transformation/VariantRealizationTransformation.html
- source_path: `com/nomagic/magicdraw/variants/transformation/VariantRealizationTransformation.html`
- source_sha256: `53a159ac1d6779f5a852dd6ebdd46353eff80c595b9863a4b3e3295454974f67`
- captured_utc: `2026-07-14T16:58:35.539264+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.variants.transformation](package-summary.html)

## Class VariantRealizationTransformation

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.variants.transformation.VariantRealizationTransformation

@OpenApiAllpublic classVariantRealizationTransformation
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Performs model transformation in scope using given [`VariationPointsProvider`](../variationpoints/VariationPointsProvider.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[VariantRealizationTransformation](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[transform](#transform(com.nomagic.magicdraw.variants.transformation.VariantTransformation,com.nomagic.task.ProgressStatus,java.util.Collection))(com.nomagic.magicdraw.variants.transformation.VariantTransformation<? extends [VariationPointsProvider](../variationpoints/VariationPointsProvider.html)> variantTransformation,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)`

`static void`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection))([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)`

`static void`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier))([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 [Notifier](../ui/Notifier.html) notifier)`

`static void`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier,boolean))([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 [Notifier](../ui/Notifier.html) notifier,
 boolean ignoreElementPermissions)`

`static void`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier,com.nomagic.magicdraw.variants.transformation.TransformationParameters))([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 [Notifier](../ui/Notifier.html) notifier,
 [TransformationParameters](TransformationParameters.html) transformationParameters)`

`static void`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,java.util.Collection))([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)`

`static void`
`[transform](#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,java.util.Collection,boolean))([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 boolean ignoreElementPermissions)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
VariantRealizationTransformation
public VariantRealizationTransformation()
 ============ METHOD DETAIL ========== 
Method Details
transform
public static void transform([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)
Parameters:
`provider` - defines which model elements are transformable
`scope` - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.
transform
public static void transform([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 boolean ignoreElementPermissions)
Parameters:
`provider` - defines which model elements are transformable
`scope` - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.
`ignoreElementPermissions` - if true, even read only elements be transformed (except for elements from read-only used projects).
 Doing so is only recommended if the transformation result will not be committed/saved to the edited (current) branch/file.
transform
public static void transform([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)
Parameters:
`provider` - defines which model elements are transformable
`status` - progress status of the transformation
`scope` - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.
 Doing so is only recommended if the transformation result will not be committed to the edited (current) branch.
transform
public static void transform([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 [Notifier](../ui/Notifier.html) notifier)
Parameters:
`provider` - defines which model elements are transformable
`status` - progress status of the transformation
`scope` - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.
`notifier` - notifies users about various abnormal situations when transforming.
transform
public static void transform([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 [Notifier](../ui/Notifier.html) notifier,
 boolean ignoreElementPermissions)
Parameters:
`provider` - defines which model elements are transformable
`status` - progress status of the transformation
`scope` - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.
`notifier` - notifies users about various abnormal situations when transforming.
`ignoreElementPermissions` - if true, even read only elements be transformed (except for elements from read-only used projects).
 Doing so is only recommended if the transformation result will not be committed/saved to the edited (current) branch/file.
transform
public static void transform([VariationPointsProvider](../variationpoints/VariationPointsProvider.html) provider,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope,
 [Notifier](../ui/Notifier.html) notifier,
 [TransformationParameters](TransformationParameters.html) transformationParameters)
Parameters:
`provider` - defines which model elements are transformable
`status` - progress status of the transformation
`scope` - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.
`notifier` - notifies users about various abnormal situations when transforming.
`transformationParameters` - transformation parameters
transform
public static void transform(com.nomagic.magicdraw.variants.transformation.VariantTransformation<? extends [VariationPointsProvider](../variationpoints/VariationPointsProvider.html)> variantTransformation,
 @CheckForNull
 [ProgressStatus](../../../task/ProgressStatus.html) status,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> scope)
Parameters:
`variantTransformation` - the transformation engine that performs the transform
`status` - progress status of the transformation
`scope` - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.variants.transformation</a></div>
<h1 class="title" title="Class VariantRealizationTransformation">Class VariantRealizationTransformation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.variants.transformation.VariantRealizationTransformation</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">VariantRealizationTransformation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Performs model transformation in scope using given <a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints"><code>VariationPointsProvider</code></a></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">VariantRealizationTransformation</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.transformation.VariantTransformation,com.nomagic.task.ProgressStatus,java.util.Collection)">transform</a><wbr/>(com.nomagic.magicdraw.variants.transformation.VariantTransformation&lt;? extends <a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a>&gt; variantTransformation,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection)">transform</a><wbr/>(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier)">transform</a><wbr/>(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 <a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier,boolean)">transform</a><wbr/>(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 <a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier,
 boolean ignoreElementPermissions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier,com.nomagic.magicdraw.variants.transformation.TransformationParameters)">transform</a><wbr/>(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 <a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier,
 <a href="TransformationParameters.html" title="class in com.nomagic.magicdraw.variants.transformation">TransformationParameters</a> transformationParameters)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,java.util.Collection)">transform</a><wbr/>(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,java.util.Collection,boolean)">transform</a><wbr/>(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 boolean ignoreElementPermissions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>VariantRealizationTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VariantRealizationTransformation</span>()</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,java.util.Collection)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - defines which model elements are transformable</dd>
<dd><code>scope</code> - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,java.util.Collection,boolean)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 boolean ignoreElementPermissions)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - defines which model elements are transformable</dd>
<dd><code>scope</code> - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.</dd>
<dd><code>ignoreElementPermissions</code> - if true, even read only elements be transformed (except for elements from read-only used projects).
                                 Doing so is only recommended if the transformation result will not be committed/saved to the edited (current) branch/file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - defines which model elements are transformable</dd>
<dd><code>status</code> - progress status of the transformation</dd>
<dd><code>scope</code> - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.
                 Doing so is only recommended if the transformation result will not be committed to the edited (current) branch.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 <a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - defines which model elements are transformable</dd>
<dd><code>status</code> - progress status of the transformation</dd>
<dd><code>scope</code> - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.</dd>
<dd><code>notifier</code> - notifies users about various abnormal situations when transforming.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier,boolean)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 <a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier,
 boolean ignoreElementPermissions)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - defines which model elements are transformable</dd>
<dd><code>status</code> - progress status of the transformation</dd>
<dd><code>scope</code> - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.</dd>
<dd><code>notifier</code> - notifies users about various abnormal situations when transforming.</dd>
<dd><code>ignoreElementPermissions</code> - if true, even read only elements be transformed (except for elements from read-only used projects).
                                 Doing so is only recommended if the transformation result will not be committed/saved to the edited (current) branch/file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.variationpoints.VariationPointsProvider,com.nomagic.task.ProgressStatus,java.util.Collection,com.nomagic.magicdraw.variants.ui.Notifier,com.nomagic.magicdraw.variants.transformation.TransformationParameters)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">transform</span><wbr/><span class="parameters">(<a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a> provider,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope,
 <a href="../ui/Notifier.html" title="interface in com.nomagic.magicdraw.variants.ui">Notifier</a> notifier,
 <a href="TransformationParameters.html" title="class in com.nomagic.magicdraw.variants.transformation">TransformationParameters</a> transformationParameters)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - defines which model elements are transformable</dd>
<dd><code>status</code> - progress status of the transformation</dd>
<dd><code>scope</code> - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.</dd>
<dd><code>notifier</code> - notifies users about various abnormal situations when transforming.</dd>
<dd><code>transformationParameters</code> - transformation parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="transform(com.nomagic.magicdraw.variants.transformation.VariantTransformation,com.nomagic.task.ProgressStatus,java.util.Collection)">
<h3>transform</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">transform</span><wbr/><span class="parameters">(com.nomagic.magicdraw.variants.transformation.VariantTransformation&lt;? extends <a href="../variationpoints/VariationPointsProvider.html" title="interface in com.nomagic.magicdraw.variants.variationpoints">VariationPointsProvider</a>&gt; variantTransformation,
 @CheckForNull
 <a href="../../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> status,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; scope)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>variantTransformation</code> - the transformation engine that performs the transform</dd>
<dd><code>status</code> - progress status of the transformation</dd>
<dd><code>scope</code> - root elements(s) that defines the part of the model to transform. Provide primary model(s) to transform the complete project.</dd>
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
