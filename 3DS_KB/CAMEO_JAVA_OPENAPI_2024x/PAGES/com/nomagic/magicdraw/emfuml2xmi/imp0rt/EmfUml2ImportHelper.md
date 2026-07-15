# JAVA OPENAPI: EmfUml2ImportHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/emfuml2xmi/imp0rt/EmfUml2ImportHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/imp0rt/EmfUml2ImportHelper.html`
- source_sha256: `e7e23bada73b94286beae304893e3d420adb3a686bfd8dc25c5311b141a97c08`
- captured_utc: `2026-07-14T16:51:18.846173+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.imp0rt](package-summary.html)

## Interface EmfUml2ImportHelper

All Superinterfaces:
`[BaseEElementNameRetriever](../helpers/BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](../helpers/BaseEmfUml2Helper.html)`, `[EmfUml2Helper](../helpers/EmfUml2Helper.html)`

@OpenApipublic interfaceEmfUml2ImportHelperextends [EmfUml2Helper](../helpers/EmfUml2Helper.html)

Eclipse UML2 model conversion to MagicDraw UML2 model helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`org.eclipse.uml2.uml.Package`
`[getRootPackage](#getRootPackage())()`
Return Eclipse UML2 model root package.
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[BaseEmfUml2Helper](../helpers/BaseEmfUml2Helper.html)
`[getEElementName](../helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getLogger](../helpers/BaseEmfUml2Helper.html#getLogger()), [getProject](../helpers/BaseEmfUml2Helper.html#getProject()), [isMappedElement](../helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](../helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](../helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](../helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markSkippedElement](../helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[EmfUml2Helper](../helpers/EmfUml2Helper.html)
`[getElementClass](../helpers/EmfUml2Helper.html#getElementClass()), [getStringPrimitiveType](../helpers/EmfUml2Helper.html#getStringPrimitiveType()), [getUml2JavaPrimitiveTypesLibrary](../helpers/EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()), [getUml2MetaModel](../helpers/EmfUml2Helper.html#getUml2MetaModel()), [getUml2PrimitiveTypesLibrary](../helpers/EmfUml2Helper.html#getUml2PrimitiveTypesLibrary())`

============ METHOD DETAIL ========== 
Method Details
getRootPackage
@OpenApiorg.eclipse.uml2.uml.Package getRootPackage()
Return Eclipse UML2 model root package.
Returns:
root package

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.imp0rt</a></div>
<h1 class="title" title="Interface EmfUml2ImportHelper">Interface EmfUml2ImportHelper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="../helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code>, <code><a href="../helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2ImportHelper</span><span class="extends-implements">
extends <a href="../helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a></span></div>
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
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>org.eclipse.uml2.uml.Package</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRootPackage()">getRootPackage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return Eclipse UML2 model root package.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></h3>
<code><a href="../helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="../helpers/BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="../helpers/BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="../helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="../helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="../helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="../helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="../helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="../helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a></h3>
<code><a href="../helpers/EmfUml2Helper.html#getElementClass()">getElementClass</a>, <a href="../helpers/EmfUml2Helper.html#getStringPrimitiveType()">getStringPrimitiveType</a>, <a href="../helpers/EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()">getUml2JavaPrimitiveTypesLibrary</a>, <a href="../helpers/EmfUml2Helper.html#getUml2MetaModel()">getUml2MetaModel</a>, <a href="../helpers/EmfUml2Helper.html#getUml2PrimitiveTypesLibrary()">getUml2PrimitiveTypesLibrary</a></code></div>
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
</span><span class="return-type">org.eclipse.uml2.uml.Package</span> <span class="element-name">getRootPackage</span>()</div>
<div class="block">Return Eclipse UML2 model root package.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>root package</dd>
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
