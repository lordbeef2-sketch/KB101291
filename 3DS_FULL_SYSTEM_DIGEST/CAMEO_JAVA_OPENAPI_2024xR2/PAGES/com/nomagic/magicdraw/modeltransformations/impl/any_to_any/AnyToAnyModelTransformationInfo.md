# JAVA OPENAPI: AnyToAnyModelTransformationInfo (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/modeltransformations/impl/any_to_any/AnyToAnyModelTransformationInfo.html
- source_path: `com/nomagic/magicdraw/modeltransformations/impl/any_to_any/AnyToAnyModelTransformationInfo.html`
- source_sha256: `149b78293a734a7e29458b19130c8af9fa1c07f170ee2a40ccb6d99346fd79eb`
- captured_utc: `2026-07-14T16:55:24.223107+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations.impl.any_to_any](package-summary.html)

## Class AnyToAnyModelTransformationInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.modeltransformations.AbstractModelTransformationInfo](../../AbstractModelTransformationInfo.html)
com.nomagic.magicdraw.modeltransformations.impl.any_to_any.AnyToAnyModelTransformationInfo

All Implemented Interfaces:
`[ModelTransformationInfo](../../ModelTransformationInfo.html)`

@OpenApiAllpublic classAnyToAnyModelTransformationInfo
extends [AbstractModelTransformationInfo](../../AbstractModelTransformationInfo.html)

See Also:
[`ModelTransformation`](../../ModelTransformation.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT](#MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AnyToAnyModelTransformationInfo](#%3Cinit%3E())()`

`[AnyToAnyModelTransformationInfo](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationDescription,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) iconName)`

`[AnyToAnyModelTransformationInfo](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationDescription,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) iconName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] requiredProfiles)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [PropertyManager](../../../properties/PropertyManager.html)`
`[createPropertyManager](#createPropertyManager())()`

`[PropertyManager](../../../properties/PropertyManager.html)`
`[getDefaultPropertyManager](#getDefaultPropertyManager())()`
Returns property manager with default properties for transformation
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDefaulTypeMapProfileName](#getDefaulTypeMapProfileName())()`
Returns name of default type map profile
`[TypeMapProfile](../../TypeMapProfile.html)`
`[getSpecificTypeMap](#getSpecificTypeMap())()`
In case there is no user selected option to select type map specific type map can be provided.
`[ModelTransformation](../../ModelTransformation.html)`
`[getTransformation](#getTransformation())()`
Returns model transformation for this info
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)>`
`[getVisibleClasses](#getVisibleClasses())()`
Visible classes that will be displayed in transformation source selection
`boolean`
`[isOnlyInPlace](#isOnlyInPlace())()`

`boolean`
`[isSupportsLeaveIntactModel](#isSupportsLeaveIntactModel())()`

`boolean`
`[isTypeMappingSupported](#isTypeMappingSupported())()`
Getter for type mapping support
`boolean`
`[isVisibleInBrowser](#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../uml/BaseElement.html) e)`
Is element visible in source selection tree.
`protected boolean`
`[loadProfiles](#loadProfiles(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`

`boolean`
`[prepareTransformation](#prepareTransformation(com.nomagic.magicdraw.core.Project))([Project](../../../core/Project.html) project)`
Prepares transformation
Methods inherited from class com.nomagic.magicdraw.modeltransformations.[AbstractModelTransformationInfo](../../AbstractModelTransformationInfo.html)
`[getDescriptionAsStream](../../AbstractModelTransformationInfo.html#getDescriptionAsStream()), [getIcon](../../AbstractModelTransformationInfo.html#getIcon()), [getTransformationName](../../AbstractModelTransformationInfo.html#getTransformationName()), [isDefaulTypeMapProfileMappingOrderForward](../../AbstractModelTransformationInfo.html#isDefaulTypeMapProfileMappingOrderForward())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.modeltransformations.[ModelTransformationInfo](../../ModelTransformationInfo.html)
`[canCreateNewElements](../../ModelTransformationInfo.html#canCreateNewElements()), [shouldPreloadDiagram](../../ModelTransformationInfo.html#shouldPreloadDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.util.Collection))`

============ FIELD DETAIL =========== 
Field Details
MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.modeltransformations.impl.any_to_any.AnyToAnyModelTransformationInfo.MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AnyToAnyModelTransformationInfo
public AnyToAnyModelTransformationInfo()
AnyToAnyModelTransformationInfo
public AnyToAnyModelTransformationInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationDescription,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) iconName)
AnyToAnyModelTransformationInfo
public AnyToAnyModelTransformationInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationDescription,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) iconName,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] requiredProfiles)
 ============ METHOD DETAIL ========== 
Method Details
getDefaulTypeMapProfileName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDefaulTypeMapProfileName()
Description copied from interface: `[ModelTransformationInfo](../../ModelTransformationInfo.html#getDefaulTypeMapProfileName())`
Returns name of default type map profile
Returns:
name of default type map
prepareTransformation
public boolean prepareTransformation([Project](../../../core/Project.html) project)
Description copied from interface: `[ModelTransformationInfo](../../ModelTransformationInfo.html#prepareTransformation(com.nomagic.magicdraw.core.Project))`
Prepares transformation
Parameters:
`project` - project
Returns:
true if preparation was successful, false in other case
loadProfiles
protected boolean loadProfiles([Project](../../../core/Project.html) project)
getTransformation
public [ModelTransformation](../../ModelTransformation.html) getTransformation()
Description copied from interface: `[ModelTransformationInfo](../../ModelTransformationInfo.html#getTransformation())`
Returns model transformation for this info
Returns:
model transformation
isVisibleInBrowser
public boolean isVisibleInBrowser([BaseElement](../../../uml/BaseElement.html) e)
Description copied from interface: `[ModelTransformationInfo](../../ModelTransformationInfo.html#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement))`
Is element visible in source selection tree.
Parameters:
`e` - element to check
Returns:
true if visible
getVisibleClasses
@CheckForNullpublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)> getVisibleClasses()
Visible classes that will be displayed in transformation source selection
Returns:
visible class types to show in transformation source selection
createPropertyManager
protected [PropertyManager](../../../properties/PropertyManager.html) createPropertyManager()
getDefaultPropertyManager
public [PropertyManager](../../../properties/PropertyManager.html) getDefaultPropertyManager()
Description copied from interface: `[ModelTransformationInfo](../../ModelTransformationInfo.html#getDefaultPropertyManager())`
Returns property manager with default properties for transformation
Returns:
property manager
isTypeMappingSupported
public boolean isTypeMappingSupported()
Description copied from interface: `[ModelTransformationInfo](../../ModelTransformationInfo.html#isTypeMappingSupported())`
Getter for type mapping support
Returns:
true if type mapping is supported by transformation
isSupportsLeaveIntactModel
public boolean isSupportsLeaveIntactModel()
isOnlyInPlace
public boolean isOnlyInPlace()
Returns:
true if transformation supports only in place transformation.
getSpecificTypeMap
public [TypeMapProfile](../../TypeMapProfile.html) getSpecificTypeMap()
Description copied from interface: `[ModelTransformationInfo](../../ModelTransformationInfo.html#getSpecificTypeMap())`
In case there is no user selected option to select type map specific type map can be provided.
Returns:
[`TypeMapProfile`](../../TypeMapProfile.html) which should be used in this transformation.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations.impl.any_to_any</a></div>
<h1 class="title" title="Class AnyToAnyModelTransformationInfo">Class AnyToAnyModelTransformationInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../AbstractModelTransformationInfo.html" title="class in com.nomagic.magicdraw.modeltransformations">com.nomagic.magicdraw.modeltransformations.AbstractModelTransformationInfo</a>
<div class="inheritance">com.nomagic.magicdraw.modeltransformations.impl.any_to_any.AnyToAnyModelTransformationInfo</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">AnyToAnyModelTransformationInfo</span>
<span class="extends-implements">extends <a href="../../AbstractModelTransformationInfo.html" title="class in com.nomagic.magicdraw.modeltransformations">AbstractModelTransformationInfo</a></span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations"><code>ModelTransformation</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT">MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AnyToAnyModelTransformationInfo</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String)">AnyToAnyModelTransformationInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> iconName)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String,java.lang.String%5B%5D)">AnyToAnyModelTransformationInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> iconName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] requiredProfiles)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyManager()">createPropertyManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaultPropertyManager()">getDefaultPropertyManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns property manager with default properties for transformation</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDefaulTypeMapProfileName()">getDefaulTypeMapProfileName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns name of default type map profile</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSpecificTypeMap()">getSpecificTypeMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">In case there is no user selected option to select type map specific type map can be provided.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformation()">getTransformation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model transformation for this info</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibleClasses()">getVisibleClasses</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Visible classes that will be displayed in transformation source selection</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOnlyInPlace()">isOnlyInPlace</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSupportsLeaveIntactModel()">isSupportsLeaveIntactModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTypeMappingSupported()">isTypeMappingSupported</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for type mapping support</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement)">isVisibleInBrowser</a><wbr/>(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Is element visible in source selection tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadProfiles(com.nomagic.magicdraw.core.Project)">loadProfiles</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#prepareTransformation(com.nomagic.magicdraw.core.Project)">prepareTransformation</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prepares transformation</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.modeltransformations.AbstractModelTransformationInfo">Methods inherited from class com.nomagic.magicdraw.modeltransformations.<a href="../../AbstractModelTransformationInfo.html" title="class in com.nomagic.magicdraw.modeltransformations">AbstractModelTransformationInfo</a></h3>
<code><a href="../../AbstractModelTransformationInfo.html#getDescriptionAsStream()">getDescriptionAsStream</a>, <a href="../../AbstractModelTransformationInfo.html#getIcon()">getIcon</a>, <a href="../../AbstractModelTransformationInfo.html#getTransformationName()">getTransformationName</a>, <a href="../../AbstractModelTransformationInfo.html#isDefaulTypeMapProfileMappingOrderForward()">isDefaulTypeMapProfileMappingOrderForward</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo">Methods inherited from interface com.nomagic.magicdraw.modeltransformations.<a href="../../ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></h3>
<code><a href="../../ModelTransformationInfo.html#canCreateNewElements()">canCreateNewElements</a>, <a href="../../ModelTransformationInfo.html#shouldPreloadDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.util.Collection)">shouldPreloadDiagram</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT">
<h3>MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.modeltransformations.impl.any_to_any.AnyToAnyModelTransformationInfo.MT_RESET_SYMBOL_PROPERTIES_TO_DEFAULT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>AnyToAnyModelTransformationInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AnyToAnyModelTransformationInfo</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String)">
<h3>AnyToAnyModelTransformationInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AnyToAnyModelTransformationInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> iconName)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String,java.lang.String[])">
<h3>AnyToAnyModelTransformationInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AnyToAnyModelTransformationInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> iconName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] requiredProfiles)</span></div>
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
<section class="detail" id="getDefaulTypeMapProfileName()">
<h3>getDefaulTypeMapProfileName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDefaulTypeMapProfileName</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformationInfo.html#getDefaulTypeMapProfileName()">ModelTransformationInfo</a></code></span></div>
<div class="block">Returns name of default type map profile</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of default type map</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prepareTransformation(com.nomagic.magicdraw.core.Project)">
<h3>prepareTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">prepareTransformation</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformationInfo.html#prepareTransformation(com.nomagic.magicdraw.core.Project)">ModelTransformationInfo</a></code></span></div>
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
<section class="detail" id="loadProfiles(com.nomagic.magicdraw.core.Project)">
<h3>loadProfiles</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">loadProfiles</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="getTransformation()">
<h3>getTransformation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformation</a></span> <span class="element-name">getTransformation</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformationInfo.html#getTransformation()">ModelTransformationInfo</a></code></span></div>
<div class="block">Returns model transformation for this info</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>model transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isVisibleInBrowser</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVisibleInBrowser</span><wbr/><span class="parameters">(<a href="../../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> e)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformationInfo.html#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement)">ModelTransformationInfo</a></code></span></div>
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
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&gt;</span> <span class="element-name">getVisibleClasses</span>()</div>
<div class="block">Visible classes that will be displayed in transformation source selection</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>visible class types to show in transformation source selection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyManager()">
<h3>createPropertyManager</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">createPropertyManager</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getDefaultPropertyManager()">
<h3>getDefaultPropertyManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../../properties/PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></span> <span class="element-name">getDefaultPropertyManager</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformationInfo.html#getDefaultPropertyManager()">ModelTransformationInfo</a></code></span></div>
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
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTypeMappingSupported</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformationInfo.html#isTypeMappingSupported()">ModelTransformationInfo</a></code></span></div>
<div class="block">Getter for type mapping support</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if type mapping is supported by transformation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSupportsLeaveIntactModel()">
<h3>isSupportsLeaveIntactModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSupportsLeaveIntactModel</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isOnlyInPlace()">
<h3>isOnlyInPlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOnlyInPlace</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if transformation supports only in place transformation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecificTypeMap()">
<h3>getSpecificTypeMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations">TypeMapProfile</a></span> <span class="element-name">getSpecificTypeMap</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="../../ModelTransformationInfo.html#getSpecificTypeMap()">ModelTransformationInfo</a></code></span></div>
<div class="block">In case there is no user selected option to select type map specific type map can be provided.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><a href="../../TypeMapProfile.html" title="class in com.nomagic.magicdraw.modeltransformations"><code>TypeMapProfile</code></a> which should be used in this transformation.</dd>
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
