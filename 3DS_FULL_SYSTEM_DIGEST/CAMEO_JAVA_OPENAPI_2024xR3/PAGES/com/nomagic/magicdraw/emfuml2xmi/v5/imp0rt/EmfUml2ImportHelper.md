# JAVA OPENAPI: EmfUml2ImportHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v5/imp0rt/EmfUml2ImportHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v5/imp0rt/EmfUml2ImportHelper.html`
- source_sha256: `b8f707bd4650e850092a5501fafe5d62e129d5892af6b840063c42394c531ba0`
- captured_utc: `2026-07-14T16:55:20.133062+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt](package-summary.html)

## Interface EmfUml2ImportHelper

All Superinterfaces:
`[BaseEElementNameRetriever](../../helpers/BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](../../helpers/BaseEmfUml2Helper.html)`, `[EmfUml2Helper](../helpers/EmfUml2Helper.html)`

@OpenApipublic interfaceEmfUml2ImportHelperextends [EmfUml2Helper](../helpers/EmfUml2Helper.html)

Eclipse UML2 model conversion to MagicDraw UML2 model helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<org.eclipse.uml2_5_0_2.uml.Element>`
`[getImportedElements](#getImportedElements())()`

`org.eclipse.uml2_5_0_2.uml.Package`
`[getRootPackage](#getRootPackage())()`
Return Eclipse UML2 model root package.
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[BaseEmfUml2Helper](../../helpers/BaseEmfUml2Helper.html)
`[addCreatedElementIDData](../../helpers/BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)), [addFinalizeActivity](../../helpers/BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)), [clearCreatedElementsIDData](../../helpers/BaseEmfUml2Helper.html#clearCreatedElementsIDData()), [getCreatedElementsIDData](../../helpers/BaseEmfUml2Helper.html#getCreatedElementsIDData()), [getEElementName](../../helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getFinalizeActivities](../../helpers/BaseEmfUml2Helper.html#getFinalizeActivities()), [getLogger](../../helpers/BaseEmfUml2Helper.html#getLogger()), [getMDProjectBuiltinProfiles](../../helpers/BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()), [getOptions](../../helpers/BaseEmfUml2Helper.html#getOptions()), [getPersistenceHelper](../../helpers/BaseEmfUml2Helper.html#getPersistenceHelper()), [getProject](../../helpers/BaseEmfUml2Helper.html#getProject()), [getUml2DataTypeMap](../../helpers/BaseEmfUml2Helper.html#getUml2DataTypeMap()), [isMappedElement](../../helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](../../helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](../../helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](../../helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markRemovableElement](../../helpers/BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)), [markSkippedElement](../../helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)), [setMDElementID](../../helpers/BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.v5.helpers.[EmfUml2Helper](../helpers/EmfUml2Helper.html)
`[getElementClass](../helpers/EmfUml2Helper.html#getElementClass()), [getEmfUml2StandardProfiles](../helpers/EmfUml2Helper.html#getEmfUml2StandardProfiles()), [getMagicDrawAnnotationDetails](../helpers/EmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)), [getStringPrimitiveType](../helpers/EmfUml2Helper.html#getStringPrimitiveType()), [getTemplateParameterHelper](../helpers/EmfUml2Helper.html#getTemplateParameterHelper()), [getUml2JavaPrimitiveTypesLibrary](../helpers/EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()), [getUml2MetaModel](../helpers/EmfUml2Helper.html#getUml2MetaModel()), [getUml2PrimitiveTypesLibrary](../helpers/EmfUml2Helper.html#getUml2PrimitiveTypesLibrary())`

============ METHOD DETAIL ========== 
Method Details
getRootPackage
@OpenApiorg.eclipse.uml2_5_0_2.uml.Package getRootPackage()
Return Eclipse UML2 model root package.
Returns:
root package
getImportedElements
[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<org.eclipse.uml2_5_0_2.uml.Element> getImportedElements()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt</a></div>
<h1 class="title" title="Interface EmfUml2ImportHelper">Interface EmfUml2ImportHelper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../../helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="../../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code>, <code><a href="../helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2Helper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2ImportHelper</span><span class="extends-implements">
extends <a href="../helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2Helper</a></span></div>
<div class="block">Eclipse UML2 model conversion to MagicDraw UML2 model helper.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.uml2_5_0_2.uml.Element&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getImportedElements()">getImportedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2_5_0_2.uml.Package</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRootPackage()">getRootPackage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return Eclipse UML2 model root package.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="../../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></h3>
<code><a href="../../helpers/BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a>, <a href="../../helpers/BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a>, <a href="../../helpers/BaseEmfUml2Helper.html#clearCreatedElementsIDData()">clearCreatedElementsIDData</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getCreatedElementsIDData()">getCreatedElementsIDData</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getFinalizeActivities()">getFinalizeActivities</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getOptions()">getOptions</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getPersistenceHelper()">getPersistenceHelper</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="../../helpers/BaseEmfUml2Helper.html#getUml2DataTypeMap()">getUml2DataTypeMap</a>, <a href="../../helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)">markRemovableElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a>, <a href="../../helpers/BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.v5.helpers.EmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.v5.helpers.<a href="../helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2Helper</a></h3>
<code><a href="../helpers/EmfUml2Helper.html#getElementClass()">getElementClass</a>, <a href="../helpers/EmfUml2Helper.html#getEmfUml2StandardProfiles()">getEmfUml2StandardProfiles</a>, <a href="../helpers/EmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a>, <a href="../helpers/EmfUml2Helper.html#getStringPrimitiveType()">getStringPrimitiveType</a>, <a href="../helpers/EmfUml2Helper.html#getTemplateParameterHelper()">getTemplateParameterHelper</a>, <a href="../helpers/EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()">getUml2JavaPrimitiveTypesLibrary</a>, <a href="../helpers/EmfUml2Helper.html#getUml2MetaModel()">getUml2MetaModel</a>, <a href="../helpers/EmfUml2Helper.html#getUml2PrimitiveTypesLibrary()">getUml2PrimitiveTypesLibrary</a></code></div>
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
<section class="detail" id="getRootPackage()">
<h3>getRootPackage</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">org.eclipse.uml2_5_0_2.uml.Package</span> <span class="element-name">getRootPackage</span>()</div>
<div class="block">Return Eclipse UML2 model root package.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root package</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImportedElements()">
<h3>getImportedElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.uml2_5_0_2.uml.Element&gt;</span> <span class="element-name">getImportedElements</span>()</div>
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
