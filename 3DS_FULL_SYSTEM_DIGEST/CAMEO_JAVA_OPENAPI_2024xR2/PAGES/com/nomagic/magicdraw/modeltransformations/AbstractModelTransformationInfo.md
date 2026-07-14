# JAVA OPENAPI: AbstractModelTransformationInfo (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/modeltransformations/AbstractModelTransformationInfo.html
- source_path: `com/nomagic/magicdraw/modeltransformations/AbstractModelTransformationInfo.html`
- source_sha256: `8a8777334d1db5adb2ae0e5476a2c689c511866c4cb484d8ce8dd793273dfa06`
- captured_utc: `2026-07-14T16:55:23.555100+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modeltransformations](package-summary.html)

## Class AbstractModelTransformationInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.modeltransformations.AbstractModelTransformationInfo

All Implemented Interfaces:
`[ModelTransformationInfo](ModelTransformationInfo.html)`

Direct Known Subclasses:
`[AnyToAnyModelTransformationInfo](impl/any_to_any/AnyToAnyModelTransformationInfo.html)`

@OpenApiAllpublic abstract classAbstractModelTransformationInfo
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [ModelTransformationInfo](ModelTransformationInfo.html)

Abstract class for model transformation info.

See Also:
[`ModelTransformation`](ModelTransformation.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractModelTransformationInfo](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationDescription,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) iconNameWithPath)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html)`
`[getDescriptionAsStream](#getDescriptionAsStream())()`
Returns model transformation description as stream
`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getIcon](#getIcon())()`
Returns model transformation icon
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTransformationName](#getTransformationName())()`
Getter for model transformation name
`boolean`
`[isDefaulTypeMapProfileMappingOrderForward](#isDefaulTypeMapProfileMappingOrderForward())()`
Returns mapping order of default type map profile
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.modeltransformations.[ModelTransformationInfo](ModelTransformationInfo.html)
`[canCreateNewElements](ModelTransformationInfo.html#canCreateNewElements()), [getDefaultPropertyManager](ModelTransformationInfo.html#getDefaultPropertyManager()), [getDefaulTypeMapProfileName](ModelTransformationInfo.html#getDefaulTypeMapProfileName()), [getSpecificTypeMap](ModelTransformationInfo.html#getSpecificTypeMap()), [getTransformation](ModelTransformationInfo.html#getTransformation()), [getVisibleClasses](ModelTransformationInfo.html#getVisibleClasses()), [isOnlyInPlace](ModelTransformationInfo.html#isOnlyInPlace()), [isSupportsLeaveIntactModel](ModelTransformationInfo.html#isSupportsLeaveIntactModel()), [isTypeMappingSupported](ModelTransformationInfo.html#isTypeMappingSupported()), [isVisibleInBrowser](ModelTransformationInfo.html#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement)), [prepareTransformation](ModelTransformationInfo.html#prepareTransformation(com.nomagic.magicdraw.core.Project)), [shouldPreloadDiagram](ModelTransformationInfo.html#shouldPreloadDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.util.Collection))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractModelTransformationInfo
public AbstractModelTransformationInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) transformationDescription,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) iconNameWithPath)
Constructor
Parameters:
`transformationName` - Model transformation name
`transformationDescription` - Model transformation description
`iconNameWithPath` - Icon name with resourse path
 ============ METHOD DETAIL ========== 
Method Details
getDescriptionAsStream
@CheckForNullpublic [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) getDescriptionAsStream()
Returns model transformation description as stream
Specified by:
`[getDescriptionAsStream](ModelTransformationInfo.html#getDescriptionAsStream())` in interface `[ModelTransformationInfo](ModelTransformationInfo.html)`
Returns:
input stream of model transformation description.
getTransformationName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTransformationName()
Getter for model transformation name
Specified by:
`[getTransformationName](ModelTransformationInfo.html#getTransformationName())` in interface `[ModelTransformationInfo](ModelTransformationInfo.html)`
Returns:
model transformation name
isDefaulTypeMapProfileMappingOrderForward
public boolean isDefaulTypeMapProfileMappingOrderForward()
Description copied from interface: `[ModelTransformationInfo](ModelTransformationInfo.html#isDefaulTypeMapProfileMappingOrderForward())`
Returns mapping order of default type map profile
Specified by:
`[isDefaulTypeMapProfileMappingOrderForward](ModelTransformationInfo.html#isDefaulTypeMapProfileMappingOrderForward())` in interface `[ModelTransformationInfo](ModelTransformationInfo.html)`
Returns:
return true for forward mapping
getIcon
public [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getIcon()
Returns model transformation icon
Specified by:
`[getIcon](ModelTransformationInfo.html#getIcon())` in interface `[ModelTransformationInfo](ModelTransformationInfo.html)`
Returns:
model transformation icon

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modeltransformations</a></div>
<h1 class="title" title="Class AbstractModelTransformationInfo">Class AbstractModelTransformationInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.modeltransformations.AbstractModelTransformationInfo</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="impl/any_to_any/AnyToAnyModelTransformationInfo.html" title="class in com.nomagic.magicdraw.modeltransformations.impl.any_to_any">AnyToAnyModelTransformationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractModelTransformationInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></span></div>
<div class="block">Abstract class for model transformation info.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ModelTransformation.html" title="interface in com.nomagic.magicdraw.modeltransformations"><code>ModelTransformation</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String)">AbstractModelTransformationInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> iconNameWithPath)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDescriptionAsStream()">getDescriptionAsStream</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model transformation description as stream</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model transformation icon</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTransformationName()">getTransformationName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Getter for model transformation name</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDefaulTypeMapProfileMappingOrderForward()">isDefaulTypeMapProfileMappingOrderForward</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns mapping order of default type map profile</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.modeltransformations.ModelTransformationInfo">Methods inherited from interface com.nomagic.magicdraw.modeltransformations.<a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></h3>
<code><a href="ModelTransformationInfo.html#canCreateNewElements()">canCreateNewElements</a>, <a href="ModelTransformationInfo.html#getDefaultPropertyManager()">getDefaultPropertyManager</a>, <a href="ModelTransformationInfo.html#getDefaulTypeMapProfileName()">getDefaulTypeMapProfileName</a>, <a href="ModelTransformationInfo.html#getSpecificTypeMap()">getSpecificTypeMap</a>, <a href="ModelTransformationInfo.html#getTransformation()">getTransformation</a>, <a href="ModelTransformationInfo.html#getVisibleClasses()">getVisibleClasses</a>, <a href="ModelTransformationInfo.html#isOnlyInPlace()">isOnlyInPlace</a>, <a href="ModelTransformationInfo.html#isSupportsLeaveIntactModel()">isSupportsLeaveIntactModel</a>, <a href="ModelTransformationInfo.html#isTypeMappingSupported()">isTypeMappingSupported</a>, <a href="ModelTransformationInfo.html#isVisibleInBrowser(com.nomagic.magicdraw.uml.BaseElement)">isVisibleInBrowser</a>, <a href="ModelTransformationInfo.html#prepareTransformation(com.nomagic.magicdraw.core.Project)">prepareTransformation</a>, <a href="ModelTransformationInfo.html#shouldPreloadDiagram(com.nomagic.magicdraw.uml.symbols.DiagramPresentationElement,java.util.Collection)">shouldPreloadDiagram</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String)">
<h3>AbstractModelTransformationInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractModelTransformationInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> transformationDescription,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> iconNameWithPath)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transformationName</code> - Model transformation name</dd>
<dd><code>transformationDescription</code> - Model transformation description</dd>
<dd><code>iconNameWithPath</code> - Icon name with resourse path</dd>
</dl>
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
<section class="detail" id="getDescriptionAsStream()">
<h3>getDescriptionAsStream</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></span> <span class="element-name">getDescriptionAsStream</span>()</div>
<div class="block">Returns model transformation description as stream</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ModelTransformationInfo.html#getDescriptionAsStream()">getDescriptionAsStream</a></code> in interface <code><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></dd>
<dt>Returns:</dt>
<dd>input stream of model transformation description.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTransformationName()">
<h3>getTransformationName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTransformationName</span>()</div>
<div class="block">Getter for model transformation name</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ModelTransformationInfo.html#getTransformationName()">getTransformationName</a></code> in interface <code><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></dd>
<dt>Returns:</dt>
<dd>model transformation name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDefaulTypeMapProfileMappingOrderForward()">
<h3>isDefaulTypeMapProfileMappingOrderForward</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDefaulTypeMapProfileMappingOrderForward</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ModelTransformationInfo.html#isDefaulTypeMapProfileMappingOrderForward()">ModelTransformationInfo</a></code></span></div>
<div class="block">Returns mapping order of default type map profile</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ModelTransformationInfo.html#isDefaulTypeMapProfileMappingOrderForward()">isDefaulTypeMapProfileMappingOrderForward</a></code> in interface <code><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></dd>
<dt>Returns:</dt>
<dd>return true for forward mapping</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="block">Returns model transformation icon</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ModelTransformationInfo.html#getIcon()">getIcon</a></code> in interface <code><a href="ModelTransformationInfo.html" title="interface in com.nomagic.magicdraw.modeltransformations">ModelTransformationInfo</a></code></dd>
<dt>Returns:</dt>
<dd>model transformation icon</dd>
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
