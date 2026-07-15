# JAVA OPENAPI: EmfUml2Helper (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2Helper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2Helper.html`
- source_sha256: `eea0cc0b0e933d2bbcdf857ce60d3e382773cde52ab7b61d79abcb7f2115cb98`
- captured_utc: `2026-07-14T16:51:19.011176+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v2](package-summary.html)

## Class EmfUml2Helper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper](../BaseEmfUml2Helper.html)
com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2Helper

All Implemented Interfaces:
`[BaseEElementNameRetriever](../helpers/BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](../helpers/BaseEmfUml2Helper.html)`

Direct Known Subclasses:
`[EmfUml2ExportHelper](export/EmfUml2ExportHelper.html)`, `[EmfUml2ImportHelper](imp0rt/EmfUml2ImportHelper.html)`

@OpenApipublic abstract classEmfUml2Helper
extends [BaseEmfUml2Helper](../BaseEmfUml2Helper.html)

Eclipse UML2 XMI helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`org.eclipse.uml2_2_0_4.uml.Type`
`[getElementClass](#getElementClass())()`
Returns Element type of Eclipse UML2 metamodel.
`org.eclipse.uml2_2_0_4.uml.Type`
`[getStringPrimitiveType](#getStringPrimitiveType())()`
Returns String type of Eclipse UML2 metamodel.
`org.eclipse.uml2_2_0_4.uml.Model`
`[getUml2JavaPrimitiveTypesLibrary](#getUml2JavaPrimitiveTypesLibrary())()`
Returns Eclipse UML2 model Java primitive type library
`org.eclipse.uml2_2_0_4.uml.Model`
`[getUml2MetaModel](#getUml2MetaModel())()`
Returns model of Eclipse UML2 metamodel.
`org.eclipse.uml2_2_0_4.uml.Model`
`[getUml2PrimitiveTypesLibrary](#getUml2PrimitiveTypesLibrary())()`
Returns Eclipse UML2 model primitive type library
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)
`[getEElementName](../BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getElementName](../BaseEmfUml2Helper.html#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getLogger](../BaseEmfUml2Helper.html#getLogger()), [getProject](../BaseEmfUml2Helper.html#getProject()), [isMappedElement](../BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](../BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](../BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](../BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markSkippedElement](../BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getUml2MetaModel
@OpenApipublic org.eclipse.uml2_2_0_4.uml.Model getUml2MetaModel()
Returns model of Eclipse UML2 metamodel.
Returns:
Eclipse UML2 metamodel model
getUml2PrimitiveTypesLibrary
@OpenApipublic org.eclipse.uml2_2_0_4.uml.Model getUml2PrimitiveTypesLibrary()
Returns Eclipse UML2 model primitive type library
Returns:
Eclipse UML2 model primitive type library
getUml2JavaPrimitiveTypesLibrary
@OpenApipublic org.eclipse.uml2_2_0_4.uml.Model getUml2JavaPrimitiveTypesLibrary()
Returns Eclipse UML2 model Java primitive type library
Returns:
Eclipse UML2 model primitive type library
getElementClass
@OpenApipublic org.eclipse.uml2_2_0_4.uml.Type getElementClass()
Returns Element type of Eclipse UML2 metamodel.
Returns:
Element type
getStringPrimitiveType
@OpenApipublic org.eclipse.uml2_2_0_4.uml.Type getStringPrimitiveType()
Returns String type of Eclipse UML2 metamodel.
Returns:
String type

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v2</a></div>
<h1 class="title" title="Class EmfUml2Helper">Class EmfUml2Helper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2Helper</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="export/EmfUml2ExportHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export">EmfUml2ExportHelper</a></code>, <code><a href="imp0rt/EmfUml2ImportHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.imp0rt">EmfUml2ImportHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">EmfUml2Helper</span>
<span class="extends-implements">extends <a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></span></div>
<div class="block">Eclipse UML2 XMI helper.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Type</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementClass()">getElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Element type of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Type</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringPrimitiveType()">getStringPrimitiveType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns String type of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Model</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUml2JavaPrimitiveTypesLibrary()">getUml2JavaPrimitiveTypesLibrary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Eclipse UML2 model Java primitive type library</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Model</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUml2MetaModel()">getUml2MetaModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns model of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Model</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUml2PrimitiveTypesLibrary()">getUml2PrimitiveTypesLibrary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Eclipse UML2 model primitive type library</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.<a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></h3>
<code><a href="../BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="../BaseEmfUml2Helper.html#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementName</a>, <a href="../BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="../BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="../BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="../BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="../BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="../BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="../BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="getUml2MetaModel()">
<h3>getUml2MetaModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Model</span> <span class="element-name">getUml2MetaModel</span>()</div>
<div class="block">Returns model of Eclipse UML2 metamodel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Eclipse UML2 metamodel model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUml2PrimitiveTypesLibrary()">
<h3>getUml2PrimitiveTypesLibrary</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Model</span> <span class="element-name">getUml2PrimitiveTypesLibrary</span>()</div>
<div class="block">Returns Eclipse UML2 model primitive type library</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Eclipse UML2 model primitive type library</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUml2JavaPrimitiveTypesLibrary()">
<h3>getUml2JavaPrimitiveTypesLibrary</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Model</span> <span class="element-name">getUml2JavaPrimitiveTypesLibrary</span>()</div>
<div class="block">Returns Eclipse UML2 model Java primitive type library</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Eclipse UML2 model primitive type library</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementClass()">
<h3>getElementClass</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Type</span> <span class="element-name">getElementClass</span>()</div>
<div class="block">Returns Element type of Eclipse UML2 metamodel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Element type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStringPrimitiveType()">
<h3>getStringPrimitiveType</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Type</span> <span class="element-name">getStringPrimitiveType</span>()</div>
<div class="block">Returns String type of Eclipse UML2 metamodel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String type</dd>
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
