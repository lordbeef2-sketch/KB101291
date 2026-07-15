# JAVA OPENAPI: EmfUml2Helper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/helpers/EmfUml2Helper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/helpers/EmfUml2Helper.html`
- source_sha256: `c4cce16e609a538c8e23682b24bd2cee488abda5286ab9a652a4ccda2234c711`
- captured_utc: `2026-07-14T16:55:18.084039+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.helpers](package-summary.html)

## Interface EmfUml2Helper

All Superinterfaces:
`[BaseEElementNameRetriever](BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](BaseEmfUml2Helper.html)`

All Known Subinterfaces:
`[EmfUml2ExportHelper](EmfUml2ExportHelper.html)`, `[EmfUml2ImportHelper](../imp0rt/EmfUml2ImportHelper.html)`

@OpenApipublic interfaceEmfUml2Helperextends [BaseEmfUml2Helper](BaseEmfUml2Helper.html), [BaseEElementNameRetriever](BaseEElementNameRetriever.html)

Eclipse UML2 XMI helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.uml2.uml.Type`
`[getElementClass](#getElementClass())()`
Returns Element type of Eclipse UML2 metamodel.
`org.eclipse.uml2.uml.Profile`
`[getEmfUml2StandardProfiles](#getEmfUml2StandardProfiles())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[getMagicDrawAnnotationDetails](#getMagicDrawAnnotationDetails(java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)`

`[Options](../envoptions/Options.html)`
`[getOptions](#getOptions())()`

`org.eclipse.uml2.uml.Type`
`[getStringPrimitiveType](#getStringPrimitiveType())()`
Returns String type of Eclipse UML2 metamodel.
`com.nomagic.magicdraw.emfuml2xmi.helpers.TemplateParameterHelper`
`[getTemplateParameterHelper](#getTemplateParameterHelper())()`

`org.eclipse.uml2.uml.Model`
`[getUml2JavaPrimitiveTypesLibrary](#getUml2JavaPrimitiveTypesLibrary())()`
Returns Eclipse UML2 model Java primitive type library
`org.eclipse.uml2.uml.Model`
`[getUml2MetaModel](#getUml2MetaModel())()`
Returns model of Eclipse UML2 metamodel.
`org.eclipse.uml2.uml.Model`
`[getUml2PrimitiveTypesLibrary](#getUml2PrimitiveTypesLibrary())()`
Returns Eclipse UML2 model primitive type library
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[BaseEmfUml2Helper](BaseEmfUml2Helper.html)
`[addCreatedElementIDData](BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)), [addFinalizeActivity](BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)), [clearCreatedElementsIDData](BaseEmfUml2Helper.html#clearCreatedElementsIDData()), [getCreatedElementsIDData](BaseEmfUml2Helper.html#getCreatedElementsIDData()), [getEElementName](BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getFinalizeActivities](BaseEmfUml2Helper.html#getFinalizeActivities()), [getLogger](BaseEmfUml2Helper.html#getLogger()), [getMDProjectBuiltinProfiles](BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()), [getPersistenceHelper](BaseEmfUml2Helper.html#getPersistenceHelper()), [getProject](BaseEmfUml2Helper.html#getProject()), [getUml2DataTypeMap](BaseEmfUml2Helper.html#getUml2DataTypeMap()), [isMappedElement](BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markRemovableElement](BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)), [markSkippedElement](BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)), [setMDElementID](BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))`

============ METHOD DETAIL ========== 
Method Details
getMagicDrawAnnotationDetails
[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) getMagicDrawAnnotationDetails([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)
Specified by:
`[getMagicDrawAnnotationDetails](BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean))` in interface `[BaseEmfUml2Helper](BaseEmfUml2Helper.html)`
getUml2MetaModel
@OpenApiorg.eclipse.uml2.uml.Model getUml2MetaModel()
Returns model of Eclipse UML2 metamodel.
Returns:
Eclipse UML2 metamodel model
getEmfUml2StandardProfiles
org.eclipse.uml2.uml.Profile getEmfUml2StandardProfiles()
getUml2PrimitiveTypesLibrary
@OpenApiorg.eclipse.uml2.uml.Model getUml2PrimitiveTypesLibrary()
Returns Eclipse UML2 model primitive type library
Returns:
Eclipse UML2 model primitive type library
getUml2JavaPrimitiveTypesLibrary
@OpenApiorg.eclipse.uml2.uml.Model getUml2JavaPrimitiveTypesLibrary()
Returns Eclipse UML2 model Java primitive type library
Returns:
Eclipse UML2 model primitive type library
getElementClass
@OpenApiorg.eclipse.uml2.uml.Type getElementClass()
Returns Element type of Eclipse UML2 metamodel.
Returns:
Element type
getStringPrimitiveType
@OpenApiorg.eclipse.uml2.uml.Type getStringPrimitiveType()
Returns String type of Eclipse UML2 metamodel.
Returns:
String type
getOptions
[Options](../envoptions/Options.html) getOptions()
Specified by:
`[getOptions](BaseEmfUml2Helper.html#getOptions())` in interface `[BaseEmfUml2Helper](BaseEmfUml2Helper.html)`
getTemplateParameterHelper
com.nomagic.magicdraw.emfuml2xmi.helpers.TemplateParameterHelper getTemplateParameterHelper()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.helpers</a></div>
<h1 class="title" title="Interface EmfUml2Helper">Interface EmfUml2Helper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2ExportHelper</a></code>, <code><a href="../imp0rt/EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt">EmfUml2ImportHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2Helper</span><span class="extends-implements">
extends <a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a>, <a href="BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></span></div>
<div class="block">Eclipse UML2 XMI helper.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2.uml.Type</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElementClass()">getElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns Element type of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2.uml.Profile</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEmfUml2StandardProfiles()">getEmfUml2StandardProfiles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../envoptions/Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">Options</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2.uml.Type</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStringPrimitiveType()">getStringPrimitiveType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns String type of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.magicdraw.emfuml2xmi.helpers.TemplateParameterHelper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTemplateParameterHelper()">getTemplateParameterHelper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2.uml.Model</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUml2JavaPrimitiveTypesLibrary()">getUml2JavaPrimitiveTypesLibrary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns Eclipse UML2 model Java primitive type library</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2.uml.Model</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUml2MetaModel()">getUml2MetaModel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns model of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2.uml.Model</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUml2PrimitiveTypesLibrary()">getUml2PrimitiveTypesLibrary</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns Eclipse UML2 model primitive type library</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></h3>
<code><a href="BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a>, <a href="BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a>, <a href="BaseEmfUml2Helper.html#clearCreatedElementsIDData()">clearCreatedElementsIDData</a>, <a href="BaseEmfUml2Helper.html#getCreatedElementsIDData()">getCreatedElementsIDData</a>, <a href="BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="BaseEmfUml2Helper.html#getFinalizeActivities()">getFinalizeActivities</a>, <a href="BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a>, <a href="BaseEmfUml2Helper.html#getPersistenceHelper()">getPersistenceHelper</a>, <a href="BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="BaseEmfUml2Helper.html#getUml2DataTypeMap()">getUml2DataTypeMap</a>, <a href="BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)">markRemovableElement</a>, <a href="BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a>, <a href="BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a></code></div>
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
<section class="detail" id="getMagicDrawAnnotationDetails(java.lang.Object,boolean)">
<h3>getMagicDrawAnnotationDetails</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getMagicDrawAnnotationDetails</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a></code> in interface <code><a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUml2MetaModel()">
<h3>getUml2MetaModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">org.eclipse.uml2.uml.Model</span> <span class="element-name">getUml2MetaModel</span>()</div>
<div class="block">Returns model of Eclipse UML2 metamodel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Eclipse UML2 metamodel model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEmfUml2StandardProfiles()">
<h3>getEmfUml2StandardProfiles</h3>
<div class="member-signature"><span class="return-type">org.eclipse.uml2.uml.Profile</span> <span class="element-name">getEmfUml2StandardProfiles</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getUml2PrimitiveTypesLibrary()">
<h3>getUml2PrimitiveTypesLibrary</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">org.eclipse.uml2.uml.Model</span> <span class="element-name">getUml2PrimitiveTypesLibrary</span>()</div>
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
</span><span class="return-type">org.eclipse.uml2.uml.Model</span> <span class="element-name">getUml2JavaPrimitiveTypesLibrary</span>()</div>
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
</span><span class="return-type">org.eclipse.uml2.uml.Type</span> <span class="element-name">getElementClass</span>()</div>
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
</span><span class="return-type">org.eclipse.uml2.uml.Type</span> <span class="element-name">getStringPrimitiveType</span>()</div>
<div class="block">Returns String type of Eclipse UML2 metamodel.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>String type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="return-type"><a href="../envoptions/Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">Options</a></span> <span class="element-name">getOptions</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseEmfUml2Helper.html#getOptions()">getOptions</a></code> in interface <code><a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateParameterHelper()">
<h3>getTemplateParameterHelper</h3>
<div class="member-signature"><span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.TemplateParameterHelper</span> <span class="element-name">getTemplateParameterHelper</span>()</div>
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
