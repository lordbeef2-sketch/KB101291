# JAVA OPENAPI: Views (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Views.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Views.html`
- source_sha256: `a5c9f22df6361f03f573966797a2625ffd1e9106d7629af7f826cc6128a07cf5`
- captured_utc: `2026-07-14T16:45:02.753039+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Views

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Views

@OpenApiAllpublic classViews
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class providing helper methods for working with Views

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Views](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expression](../../kerml/model/kerml/Expression.html)>`
`[getViewCondition](#getViewCondition(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the view condition expressions associated with the given type.
`static [RenderingUsage](sysml/RenderingUsage.html)`
`[getViewRendering](#getViewRendering(com.dassault_systemes.modeler.kerml.model.kerml.Type))([Type](../../kerml/model/kerml/Type.html) type)`
Returns the view rendering associated with the given type.
`static boolean`
`[isOwningTypeRenderingUsageOrDefinition](#isOwningTypeRenderingUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the owning type of the feature is a rendering usage or definition.
`static boolean`
`[isOwningTypeViewUsageOrDefinition](#isOwningTypeViewUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](../../kerml/model/kerml/Feature.html) feature)`
Checks whether the owning type of the feature is a view usage or definition.
`static boolean`
`[isRenderingUsageOrDefinition](#isRenderingUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the element is a [`RenderingUsage`](sysml/RenderingUsage.html) or [`RenderingDefinition`](sysml/RenderingDefinition.html).
`static boolean`
`[isViewpointUsageOrDefinition](#isViewpointUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the element is a [`ViewpointUsage`](sysml/ViewpointUsage.html) or [`ViewpointDefinition`](sysml/ViewpointDefinition.html).
`static boolean`
`[isViewRendering](#isViewRendering(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership))([FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)`
Checks whether the membership represents a view rendering.
`static boolean`
`[isViewUsageOrDefinition](#isViewUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](../../kerml/model/kerml/Element.html) element)`
Checks whether the element is a [`ViewUsage`](sysml/ViewUsage.html) or [`ViewDefinition`](sysml/ViewDefinition.html).
`static boolean`
`[isViewUsageOrDefinition](#isViewUsageOrDefinition(org.eclipse.emf.ecore.EClass))(org.eclipse.emf.ecore.EClass eClass)`
Checks whether the given EClass represents a [`ViewUsage`](sysml/ViewUsage.html)
 or [`ViewDefinition`](sysml/ViewDefinition.html).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Views
public Views()
 ============ METHOD DETAIL ========== 
Method Details
isViewUsageOrDefinition
public static boolean isViewUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the element is a [`ViewUsage`](sysml/ViewUsage.html) or [`ViewDefinition`](sysml/ViewDefinition.html).
Parameters:
`element` - the element to check
Returns:
true if the element is a view usage or definition
isViewUsageOrDefinition
public static boolean isViewUsageOrDefinition(org.eclipse.emf.ecore.EClass eClass)
Checks whether the given EClass represents a [`ViewUsage`](sysml/ViewUsage.html)
 or [`ViewDefinition`](sysml/ViewDefinition.html).
Parameters:
`eClass` - the class to check
Returns:
true if the class is a view usage or definition
isOwningTypeViewUsageOrDefinition
public static boolean isOwningTypeViewUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the owning type of the feature is a view usage or definition.
Parameters:
`feature` - the feature
Returns:
true if the owning type is a view usage or definition
isViewpointUsageOrDefinition
public static boolean isViewpointUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the element is a [`ViewpointUsage`](sysml/ViewpointUsage.html) or [`ViewpointDefinition`](sysml/ViewpointDefinition.html).
Parameters:
`element` - the element to check
Returns:
true if the element is a viewpoint usage or definition
isRenderingUsageOrDefinition
public static boolean isRenderingUsageOrDefinition(@CheckForNull
 [Element](../../kerml/model/kerml/Element.html) element)
Checks whether the element is a [`RenderingUsage`](sysml/RenderingUsage.html) or [`RenderingDefinition`](sysml/RenderingDefinition.html).
Parameters:
`element` - the element to check
Returns:
true if the element is a rendering usage or definition
isOwningTypeRenderingUsageOrDefinition
public static boolean isOwningTypeRenderingUsageOrDefinition([Feature](../../kerml/model/kerml/Feature.html) feature)
Checks whether the owning type of the feature is a rendering usage or definition.
Parameters:
`feature` - the feature
Returns:
true if the owning type is a rendering usage or definition
getViewRendering
@CheckForNullpublic static [RenderingUsage](sysml/RenderingUsage.html) getViewRendering([Type](../../kerml/model/kerml/Type.html) type)
Returns the view rendering associated with the given type.
Parameters:
`type` - the type
Returns:
rendering usage, or null if none exists
isViewRendering
public static boolean isViewRendering(@CheckForNull
 [FeatureMembership](../../kerml/model/kerml/FeatureMembership.html) membership)
Checks whether the membership represents a view rendering.
Parameters:
`membership` - the membership to check
Returns:
true if the membership is a [`ViewRenderingMembership`](sysml/ViewRenderingMembership.html)
getViewCondition
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Expression](../../kerml/model/kerml/Expression.html)> getViewCondition([Type](../../kerml/model/kerml/Type.html) type)
Returns the view condition expressions associated with the given type.
 View conditions may be defined on both view usages and view definitions.
Parameters:
`type` - the type
Returns:
list of view condition expressions, or an empty list if none exist

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Views">Class Views</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Views</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Views</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class providing helper methods for working with Views</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Views</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getViewCondition(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getViewCondition</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the view condition expressions associated with the given type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getViewRendering(com.dassault_systemes.modeler.kerml.model.kerml.Type)">getViewRendering</a><wbr/>(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the view rendering associated with the given type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypeRenderingUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypeRenderingUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the owning type of the feature is a rendering usage or definition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isOwningTypeViewUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isOwningTypeViewUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the owning type of the feature is a view usage or definition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isRenderingUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isRenderingUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a <a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingUsage</code></a> or <a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingDefinition</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isViewpointUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isViewpointUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a <a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointUsage</code></a> or <a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isViewRendering(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">isViewRendering</a><wbr/>(<a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the membership represents a view rendering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isViewUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isViewUsageOrDefinition</a><wbr/>(<a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a <a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewUsage</code></a> or <a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewDefinition</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isViewUsageOrDefinition(org.eclipse.emf.ecore.EClass)">isViewUsageOrDefinition</a><wbr/>(org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given EClass represents a <a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewUsage</code></a>
 or <a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewDefinition</code></a>.</div>
</div>
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
<h3>Views</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Views</span>()</div>
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
<section class="detail" id="isViewUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isViewUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isViewUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a <a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewUsage</code></a> or <a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is a view usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isViewUsageOrDefinition(org.eclipse.emf.ecore.EClass)">
<h3>isViewUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isViewUsageOrDefinition</span><wbr/><span class="parameters">(org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Checks whether the given EClass represents a <a href="sysml/ViewUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewUsage</code></a>
 or <a href="sysml/ViewDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>eClass</code> - the class to check</dd>
<dt>Returns:</dt>
<dd>true if the class is a view usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwningTypeViewUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypeViewUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypeViewUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the owning type of the feature is a view usage or definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the owning type is a view usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isViewpointUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isViewpointUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isViewpointUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a <a href="sysml/ViewpointUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointUsage</code></a> or <a href="sysml/ViewpointDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewpointDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is a viewpoint usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRenderingUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isRenderingUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRenderingUsageOrDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a <a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingUsage</code></a> or <a href="sysml/RenderingDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>RenderingDefinition</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element to check</dd>
<dt>Returns:</dt>
<dd>true if the element is a rendering usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOwningTypeRenderingUsageOrDefinition(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isOwningTypeRenderingUsageOrDefinition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isOwningTypeRenderingUsageOrDefinition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the owning type of the feature is a rendering usage or definition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the owning type is a rendering usage or definition</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getViewRendering(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getViewRendering</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/RenderingUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">RenderingUsage</a></span> <span class="element-name">getViewRendering</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the view rendering associated with the given type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>rendering usage, or null if none exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isViewRendering(com.dassault_systemes.modeler.kerml.model.kerml.FeatureMembership)">
<h3>isViewRendering</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isViewRendering</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../kerml/model/kerml/FeatureMembership.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">FeatureMembership</a> membership)</span></div>
<div class="block">Checks whether the membership represents a view rendering.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>membership</code> - the membership to check</dd>
<dt>Returns:</dt>
<dd>true if the membership is a <a href="sysml/ViewRenderingMembership.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml"><code>ViewRenderingMembership</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getViewCondition(com.dassault_systemes.modeler.kerml.model.kerml.Type)">
<h3>getViewCondition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../kerml/model/kerml/Expression.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Expression</a>&gt;</span> <span class="element-name">getViewCondition</span><wbr/><span class="parameters">(<a href="../../kerml/model/kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type)</span></div>
<div class="block">Returns the view condition expressions associated with the given type.
 View conditions may be defined on both view usages and view definitions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dt>Returns:</dt>
<dd>list of view condition expressions, or an empty list if none exist</dd>
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
