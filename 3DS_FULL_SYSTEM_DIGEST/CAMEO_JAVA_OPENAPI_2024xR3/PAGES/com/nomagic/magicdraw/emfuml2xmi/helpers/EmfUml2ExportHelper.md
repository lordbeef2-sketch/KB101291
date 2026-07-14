# JAVA OPENAPI: EmfUml2ExportHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/helpers/EmfUml2ExportHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/helpers/EmfUml2ExportHelper.html`
- source_sha256: `d34165d54759cec3c0c6d5f30ade464c0d486555c49905561506db299433640c`
- captured_utc: `2026-07-14T16:55:18.060040+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.helpers](package-summary.html)

## Interface EmfUml2ExportHelper

All Superinterfaces:
`[BaseEElementNameRetriever](BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](BaseEmfUml2Helper.html)`, `[EmfUml2Helper](EmfUml2Helper.html)`, `com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider`

@OpenApipublic interfaceEmfUml2ExportHelperextends [EmfUml2Helper](EmfUml2Helper.html), com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider

MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[importDataTypePackages](#importDataTypePackages(org.eclipse.uml2.uml.Package))(org.eclipse.uml2.uml.Package ePackage)`

`void`
`[importPackage](#importPackage(org.eclipse.uml2.uml.Package,org.eclipse.uml2.uml.Package,java.lang.String))(org.eclipse.uml2.uml.Package ePackage,
 org.eclipse.uml2.uml.Package eImport,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)`
Imports package
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[BaseEmfUml2Helper](BaseEmfUml2Helper.html)
`[addCreatedElementIDData](BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)), [addFinalizeActivity](BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)), [clearCreatedElementsIDData](BaseEmfUml2Helper.html#clearCreatedElementsIDData()), [getCreatedElementsIDData](BaseEmfUml2Helper.html#getCreatedElementsIDData()), [getEElementName](BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getFinalizeActivities](BaseEmfUml2Helper.html#getFinalizeActivities()), [getLogger](BaseEmfUml2Helper.html#getLogger()), [getMDProjectBuiltinProfiles](BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()), [getPersistenceHelper](BaseEmfUml2Helper.html#getPersistenceHelper()), [getProject](BaseEmfUml2Helper.html#getProject()), [getUml2DataTypeMap](BaseEmfUml2Helper.html#getUml2DataTypeMap()), [isMappedElement](BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markRemovableElement](BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)), [markSkippedElement](BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)), [setMDElementID](BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.[EmfUml2Helper](EmfUml2Helper.html)
`[getElementClass](EmfUml2Helper.html#getElementClass()), [getEmfUml2StandardProfiles](EmfUml2Helper.html#getEmfUml2StandardProfiles()), [getMagicDrawAnnotationDetails](EmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)), [getOptions](EmfUml2Helper.html#getOptions()), [getStringPrimitiveType](EmfUml2Helper.html#getStringPrimitiveType()), [getTemplateParameterHelper](EmfUml2Helper.html#getTemplateParameterHelper()), [getUml2JavaPrimitiveTypesLibrary](EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()), [getUml2MetaModel](EmfUml2Helper.html#getUml2MetaModel()), [getUml2PrimitiveTypesLibrary](EmfUml2Helper.html#getUml2PrimitiveTypesLibrary())`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider
`getInteractionExportHelper`

============ METHOD DETAIL ========== 
Method Details
importPackage
void importPackage(org.eclipse.uml2.uml.Package ePackage,
 org.eclipse.uml2.uml.Package eImport,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)
Imports package
Parameters:
`ePackage` - package which imports package.
`eImport` - package which is imported
`extra` - extra info which is used to construct package import id
importDataTypePackages
void importDataTypePackages(org.eclipse.uml2.uml.Package ePackage)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.helpers</a></div>
<h1 class="title" title="Interface EmfUml2ExportHelper">Interface EmfUml2ExportHelper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code>, <code><a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a></code>, <code>com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">EmfUml2ExportHelper</span><span class="extends-implements">
extends <a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a>, com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</span></div>
<div class="block">MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#importDataTypePackages(org.eclipse.uml2.uml.Package)">importDataTypePackages</a><wbr/>(org.eclipse.uml2.uml.Package ePackage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#importPackage(org.eclipse.uml2.uml.Package,org.eclipse.uml2.uml.Package,java.lang.String)">importPackage</a><wbr/>(org.eclipse.uml2.uml.Package ePackage,
 org.eclipse.uml2.uml.Package eImport,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extra)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Imports package</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></h3>
<code><a href="BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a>, <a href="BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a>, <a href="BaseEmfUml2Helper.html#clearCreatedElementsIDData()">clearCreatedElementsIDData</a>, <a href="BaseEmfUml2Helper.html#getCreatedElementsIDData()">getCreatedElementsIDData</a>, <a href="BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="BaseEmfUml2Helper.html#getFinalizeActivities()">getFinalizeActivities</a>, <a href="BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a>, <a href="BaseEmfUml2Helper.html#getPersistenceHelper()">getPersistenceHelper</a>, <a href="BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="BaseEmfUml2Helper.html#getUml2DataTypeMap()">getUml2DataTypeMap</a>, <a href="BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)">markRemovableElement</a>, <a href="BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a>, <a href="BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.helpers.EmfUml2Helper">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.helpers.<a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a></h3>
<code><a href="EmfUml2Helper.html#getElementClass()">getElementClass</a>, <a href="EmfUml2Helper.html#getEmfUml2StandardProfiles()">getEmfUml2StandardProfiles</a>, <a href="EmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a>, <a href="EmfUml2Helper.html#getOptions()">getOptions</a>, <a href="EmfUml2Helper.html#getStringPrimitiveType()">getStringPrimitiveType</a>, <a href="EmfUml2Helper.html#getTemplateParameterHelper()">getTemplateParameterHelper</a>, <a href="EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()">getUml2JavaPrimitiveTypesLibrary</a>, <a href="EmfUml2Helper.html#getUml2MetaModel()">getUml2MetaModel</a>, <a href="EmfUml2Helper.html#getUml2PrimitiveTypesLibrary()">getUml2PrimitiveTypesLibrary</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</h3>
<code>getInteractionExportHelper</code></div>
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
<section class="detail" id="importPackage(org.eclipse.uml2.uml.Package,org.eclipse.uml2.uml.Package,java.lang.String)">
<h3>importPackage</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">importPackage</span><wbr/><span class="parameters">(org.eclipse.uml2.uml.Package ePackage,
 org.eclipse.uml2.uml.Package eImport,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extra)</span></div>
<div class="block">Imports package</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ePackage</code> - package which imports package.</dd>
<dd><code>eImport</code> - package which is imported</dd>
<dd><code>extra</code> - extra info which is used to construct package import id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importDataTypePackages(org.eclipse.uml2.uml.Package)">
<h3>importDataTypePackages</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">importDataTypePackages</span><wbr/><span class="parameters">(org.eclipse.uml2.uml.Package ePackage)</span></div>
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
