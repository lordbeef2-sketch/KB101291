# JAVA OPENAPI: ModelTransformationInfo (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/modeltransformations/ModelTransformationInfo.html
- source_path: `com/nomagic/magicdraw/modeltransformations/ModelTransformationInfo.html`
- source_sha256: `95f8e408e9a79d1ac57df3bcf2d3c1d7701083d861ffe19bf977aae73a8f583a`
- captured_utc: `2026-07-14T16:55:25.787126+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations](package-summary.html)

## Interface ModelTransformationInfo

All Known Implementing Classes:
`[AbstractModelTransformationInfo](AbstractModelTransformationInfo.html)`, `[AnyToAnyModelTransformationInfo](impl/any_to_any/AnyToAnyModelTransformationInfo.html)`

@OpenApiAllpublic interfaceModelTransformationInfo

Interface for model transformation info

See Also:
[`AbstractModelTransformationInfo`](AbstractModelTransformationInfo.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default boolean`
`[canCreateNewElements](#canCreateNewElements())()`
If true, new elements can be created as the result of transformation.
`[PropertyManager](../properties/PropertyManager.html)`
`[getDefaultPropertyManager](#getDefaultPropertyManager())()`
Returns property manager with default properties for transformation
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDefaulTypeMapProfileName](#getDefaulTypeMapProfileName())()`
Returns name of default type map profile
`[InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html)`
`[getDescriptionAsStream](#getDescriptionAsStream())()`
Returns model transformation description as stream
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Returns model transformation icon
`[TypeMapProfile](TypeMapProfile.html)`
`[getSpecificTypeMap](#getSpecificTypeMap())()`
In case there is no user selected option to select type map specific type map can be provided.
`[ModelTransformation](ModelTransformation.html)`
`[getTransformation](#getTransformation())()`
Returns model transformation for this info
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTransformationName](#getTransformationName())()`
Getter for model transformation name
`default [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[getVisibleClasses](#getVisibleClasses())()`
Visible classes that will be displayed in transformation source selection
`boolean`
`[isDefaulTypeMapProfileMappingOrderForward](#isDefaulTypeMapProfileMappingOrderForward())()`
Returns mapping order of default type map profile
`boolean`
`[isOnlyInPlace](#isOnlyInPlace())()`

`boolean`
`[isSupportsLeaveIntactModel](#isSupportsLeaveIntactModel())()`

`boolean`
`[isTypeMappingSupported](#isTypeMappingSupported())()`
Getter for type mapping support
`boolean`
`[isVisibleInBrowser](#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) e)`
Is element visible in source selection tree.
`boolean`
`[prepareTransformation](#prepareTransformation(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Prepares transformation
`default boolean`
`[shouldPreloadDiagram](#shouldPreloadDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.util.Collection))([DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)> elementsInScope)`

============ METHOD DETAIL ========== 
Method Details
getTransformationName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTransformationName()
Getter for model transformation name
Returns:
model transformation name
getIcon
[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Returns model transformation icon
Returns:
model transformation icon
getTransformation
[ModelTransformation](ModelTransformation.html) getTransformation()
Returns model transformation for this info
Returns:
model transformation
getDefaultPropertyManager
[PropertyManager](../properties/PropertyManager.html) getDefaultPropertyManager()
Returns property manager with default properties for transformation
Returns:
property manager
isTypeMappingSupported
boolean isTypeMappingSupported()
Getter for type mapping support
Returns:
true if type mapping is supported by transformation
getDefaulTypeMapProfileName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDefaulTypeMapProfileName()
Returns name of default type map profile
Returns:
name of default type map
isDefaulTypeMapProfileMappingOrderForward
boolean isDefaulTypeMapProfileMappingOrderForward()
Returns mapping order of default type map profile
Returns:
return true for forward mapping
prepareTransformation
boolean prepareTransformation([Project](../core/Project.html) project)
Prepares transformation
Parameters:
`project` - project
Returns:
true if preparation was successful, false in other case
isVisibleInBrowser
boolean isVisibleInBrowser([BaseElement](../uml/BaseElement.html) e)
Is element visible in source selection tree.
Parameters:
`e` - element to check
Returns:
true if visible
getVisibleClasses
@CheckForNulldefault [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> getVisibleClasses()
Visible classes that will be displayed in transformation source selection
Returns:
visible class types to show in transformation source selection, if null all classes can be visible
getDescriptionAsStream
[InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) getDescriptionAsStream()
Returns model transformation description as stream
Returns:
input stream of model transformation description.
isSupportsLeaveIntactModel
boolean isSupportsLeaveIntactModel()
isOnlyInPlace
boolean isOnlyInPlace()
Returns:
true if transformation supports only in place transformation.
getSpecificTypeMap
@CheckForNull[TypeMapProfile](TypeMapProfile.html) getSpecificTypeMap()
In case there is no user selected option to select type map specific type map can be provided.
Returns:
[`TypeMapProfile`](TypeMapProfile.html) which should be used in this transformation.
canCreateNewElements
default boolean canCreateNewElements()
If true, new elements can be created as the result of transformation. This might cause auto-numbers update to be called which can be time consuming
 Returning false indicates that the transformation only modifies existing elements and updating auto-numbers can be skipped
shouldPreloadDiagram
default boolean shouldPreloadDiagram([DiagramPresentationElement](../uml/symbols/DiagramPresentationElement.html) diagram,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)> elementsInScope)
Parameters:
`diagram` - any not loaded diagram in the project
`elementsInScope` - all elements in scope of this transformation
Returns:
true if the given diagram should be loaded before executing the transformation

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations</a></div>
<h1 class="title" title="Interface ModelTransformationInfo">Interface ModelTransformationInfo</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="AbstractModelTransformationInfo.html" title="class in com.nomagic.magicdraw.modeltransformations">AbstractModelTransformationInfo</a></code>, <code><a href="impl/any_to_any/AnyToAnyModelTransformationInfo.html" title="class in com.nomagic.magicdraw.modeltransformations.impl.any_to_any">AnyToAnyModelTransformationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ModelTransformationInfo</span></div>
<div class="block">Interface for model transformation info</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="AbstractModelTransformationInfo.html" title="class in com.nomagic.magicdraw.modeltransformations"><code>AbstractModelTransformationInfo</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#canCreateNewElements()">canCreateNewElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">If true, new elements can be created as the result of transformation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaultPropertyManager()">getDefaultPropertyManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns property manager with default properties for transformation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDefaulTypeMapProfileName()">getDefaulTypeMapProfileName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns name of default type map profile</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDescriptionAsStream()">getDescriptionAsStream</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns model transformation description as stream</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns model transformation icon</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSpecificTypeMap()">getSpecificTypeMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">In case there is no user selected option to select type map specific type map can be provided.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTransformation()">getTransformation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns model transformation for this info</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTransformationName()">getTransformationName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Getter for model transformation name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getVisibleClasses()">getVisibleClasses</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Visible classes that will be displayed in transformation source selection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDefaulTypeMapProfileMappingOrderForward()">isDefaulTypeMapProfileMappingOrderForward</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns mapping order of default type map profile</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isOnlyInPlace()">isOnlyInPlace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSupportsLeaveIntactModel()">isSupportsLeaveIntactModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isTypeMappingSupported()">isTypeMappingSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Getter for type mapping support</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement)">isVisibleInBrowser</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Is element visible in source selection tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#prepareTransformation(com.nomagic.magicdraw.core.Project)">prepareTransformation</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Prepares transformation</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#shouldPreloadDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.util.Collection)">shouldPreloadDiagram</a><wbr/>(<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementsInScope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"> </div>
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
<section class="detail" id="getTransformationName()">
<h3>getTransformationName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTransformationName</span>()</div>
<div class="block">Getter for model transformation name</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model transformation name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">Returns model transformation icon</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model transformation icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransformation()">
<h3>getTransformation</h3>
<div class="member-signature"><span class="return-type"><a href="ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></span> <span class="element-name">getTransformation</span>()</div>
<div class="block">Returns model transformation for this info</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaultPropertyManager()">
<h3>getDefaultPropertyManager</h3>
<div class="member-signature"><span class="return-type"><a href="../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getDefaultPropertyManager</span>()</div>
<div class="block">Returns property manager with default properties for transformation</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>property manager</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTypeMappingSupported()">
<h3>isTypeMappingSupported</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isTypeMappingSupported</span>()</div>
<div class="block">Getter for type mapping support</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if type mapping is supported by transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefaulTypeMapProfileName()">
<h3>getDefaulTypeMapProfileName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDefaulTypeMapProfileName</span>()</div>
<div class="block">Returns name of default type map profile</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of default type map</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDefaulTypeMapProfileMappingOrderForward()">
<h3>isDefaulTypeMapProfileMappingOrderForward</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isDefaulTypeMapProfileMappingOrderForward</span>()</div>
<div class="block">Returns mapping order of default type map profile</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>return true for forward mapping</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepareTransformation(com.nomagic.magicdraw.core.Project)">
<h3>prepareTransformation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">prepareTransformation</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Prepares transformation</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true if preparation was successful, false in other case</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isVisibleInBrowser</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isVisibleInBrowser</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> e)</span></div>
<div class="block">Is element visible in source selection tree.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - element to check</dd>
<dt>Returns:</dt>
<dd>true if visible</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibleClasses()">
<h3>getVisibleClasses</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">getVisibleClasses</span>()</div>
<div class="block">Visible classes that will be displayed in transformation source selection</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>visible class types to show in transformation source selection, if null all classes can be visible</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDescriptionAsStream()">
<h3>getDescriptionAsStream</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></span> <span class="element-name">getDescriptionAsStream</span>()</div>
<div class="block">Returns model transformation description as stream</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>input stream of model transformation description.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupportsLeaveIntactModel()">
<h3>isSupportsLeaveIntactModel</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isSupportsLeaveIntactModel</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isOnlyInPlace()">
<h3>isOnlyInPlace</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isOnlyInPlace</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if transformation supports only in place transformation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecificTypeMap()">
<h3>getSpecificTypeMap</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a></span> <span class="element-name">getSpecificTypeMap</span>()</div>
<div class="block">In case there is no user selected option to select type map specific type map can be provided.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><a href="TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations"><code>TypeMapProfile</code></a> which should be used in this transformation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canCreateNewElements()">
<h3>canCreateNewElements</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">canCreateNewElements</span>()</div>
<div class="block">If true, new elements can be created as the result of transformation. This might cause auto-numbers update to be called which can be time consuming
 Returning false indicates that the transformation only modifies existing elements and updating auto-numbers can be skipped</div>
</section>
</li>
<li>
<section class="detail" id="shouldPreloadDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.util.Collection)">
<h3>shouldPreloadDiagram</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">shouldPreloadDiagram</span><wbr/><span class="parameters">(<a href="../uml/symbols/DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">DiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; elementsInScope)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - any not loaded diagram in the project</dd>
<dd><code>elementsInScope</code> - all elements in scope of this transformation</dd>
<dt>Returns:</dt>
<dd>true if the given diagram should be loaded before executing the transformation</dd>
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
