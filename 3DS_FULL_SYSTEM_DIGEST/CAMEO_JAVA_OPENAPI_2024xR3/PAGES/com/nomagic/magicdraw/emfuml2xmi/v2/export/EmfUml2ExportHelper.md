# JAVA OPENAPI: EmfUml2ExportHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v2/export/EmfUml2ExportHelper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/export/EmfUml2ExportHelper.html`
- source_sha256: `d6d90fb0c73e4c56c24ddb7ab1cad1ec1fa2ed25f699be9981c63810077865ce`
- captured_utc: `2026-07-14T16:55:18.529045+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v2.export](package-summary.html)

## Class EmfUml2ExportHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper](../../BaseEmfUml2Helper.html)
[com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2Helper](../EmfUml2Helper.html)
com.nomagic.magicdraw.emfuml2xmi.v2.export.EmfUml2ExportHelper

All Implemented Interfaces:
`com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider`, `[BaseEElementNameRetriever](../../helpers/BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](../../helpers/BaseEmfUml2Helper.html)`

@OpenApipublic classEmfUml2ExportHelper
extends [EmfUml2Helper](../EmfUml2Helper.html)
implements com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider

MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.[BaseEmfUml2Helper](../../BaseEmfUml2Helper.html)
`[MAGICDRAW_SOURCE](../../BaseEmfUml2Helper.html#MAGICDRAW_SOURCE), [MD_ID](../../BaseEmfUml2Helper.html#MD_ID), [MD_PROPERTY_NAME](../../BaseEmfUml2Helper.html#MD_PROPERTY_NAME)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EmfUml2ExportHelper](#%3Cinit%3E(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger))([Project](../../../core/Project.html) project,
 [EmfUml2PersistenceHelper](../EmfUml2PersistenceHelper.html) persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 [BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html) emfOptionsGroup,
 [EmfUml2Logger](../../EmfUml2Logger.html) logger)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`com.nomagic.magicdraw.emfuml2xmi.helpers.BaseInteractionExportHelper`
`[getInteractionExportHelper](#getInteractionExportHelper())()`

`void`
`[importDataTypePackages](#importDataTypePackages(org.eclipse.uml2_2_0_4.uml.Package))(org.eclipse.uml2_2_0_4.uml.Package ePackage)`

`void`
`[importPackage](#importPackage(org.eclipse.uml2_2_0_4.uml.Package,org.eclipse.uml2_2_0_4.uml.Package,java.lang.String))(org.eclipse.uml2_2_0_4.uml.Package ePackage,
 org.eclipse.uml2_2_0_4.uml.Package eImport,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)`
Imports package
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.v2.[EmfUml2Helper](../EmfUml2Helper.html)
`[createDataTypeMap](../EmfUml2Helper.html#createDataTypeMap()), [createEElementNameRetriever](../EmfUml2Helper.html#createEElementNameRetriever()), [getElementClass](../EmfUml2Helper.html#getElementClass()), [getEmfOptionsGroup](../EmfUml2Helper.html#getEmfOptionsGroup()), [getEmfUml2StandardProfiles](../EmfUml2Helper.html#getEmfUml2StandardProfiles()), [getMagicDrawAnnotationDetails](../EmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)), [getNameStereotypeMap](../EmfUml2Helper.html#getNameStereotypeMap()), [getOptions](../EmfUml2Helper.html#getOptions()), [getStringPrimitiveType](../EmfUml2Helper.html#getStringPrimitiveType()), [getTemplateParameterHelper](../EmfUml2Helper.html#getTemplateParameterHelper()), [getUml2JavaPrimitiveTypesLibrary](../EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()), [getUml2MetaModel](../EmfUml2Helper.html#getUml2MetaModel()), [getUml2PrimitiveTypesLibrary](../EmfUml2Helper.html#getUml2PrimitiveTypesLibrary())`
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.[BaseEmfUml2Helper](../../BaseEmfUml2Helper.html)
`[addCreatedElementIDData](../../BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)), [addFinalizeActivity](../../BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)), [clearCreatedElementsIDData](../../BaseEmfUml2Helper.html#clearCreatedElementsIDData()), [getCreatedElementsIDData](../../BaseEmfUml2Helper.html#getCreatedElementsIDData()), [getEElementName](../../BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getElementName](../../BaseEmfUml2Helper.html#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFinalizeActivities](../../BaseEmfUml2Helper.html#getFinalizeActivities()), [getLogger](../../BaseEmfUml2Helper.html#getLogger()), [getMDProjectBuiltinProfiles](../../BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()), [getMDStandardProfiles](../../BaseEmfUml2Helper.html#getMDStandardProfiles()), [getPersistenceHelper](../../BaseEmfUml2Helper.html#getPersistenceHelper()), [getProject](../../BaseEmfUml2Helper.html#getProject()), [getUml2DataTypeMap](../../BaseEmfUml2Helper.html#getUml2DataTypeMap()), [initProgressStatus](../../BaseEmfUml2Helper.html#initProgressStatus(com.nomagic.task.ProgressStatus,java.lang.String,boolean)), [isMappedElement](../../BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](../../BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](../../BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](../../BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markRemovableElement](../../BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)), [markSkippedElement](../../BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)), [removeElement](../../BaseEmfUml2Helper.html#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)), [setMDElementID](../../BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EmfUml2ExportHelper
public EmfUml2ExportHelper([Project](../../../core/Project.html) project,
 [EmfUml2PersistenceHelper](../EmfUml2PersistenceHelper.html) persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 [BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html) emfOptionsGroup,
 [EmfUml2Logger](../../EmfUml2Logger.html) logger)
 ============ METHOD DETAIL ========== 
Method Details
getInteractionExportHelper
public com.nomagic.magicdraw.emfuml2xmi.helpers.BaseInteractionExportHelper getInteractionExportHelper()
Specified by:
`getInteractionExportHelper` in interface `com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider`
importPackage
public void importPackage(org.eclipse.uml2_2_0_4.uml.Package ePackage,
 org.eclipse.uml2_2_0_4.uml.Package eImport,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)
Imports package
Parameters:
`ePackage` - package which imports package.
`eImport` - package which is imported
`extra` - extra info which is used to construct package import id
importDataTypePackages
public void importDataTypePackages(org.eclipse.uml2_2_0_4.uml.Package ePackage)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v2.export</a></div>
<h1 class="title" title="Class EmfUml2ExportHelper">Class EmfUml2ExportHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper</a>
<div class="inheritance"><a href="../EmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2Helper</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v2.export.EmfUml2ExportHelper</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</code>, <code><a href="../../helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="../../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">EmfUml2ExportHelper</span>
<span class="extends-implements">extends <a href="../EmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2Helper</a>
implements com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</span></div>
<div class="block">MagicDraw UML2 model conversion to Eclipse UML2 XMI helper.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper">Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.<a href="../../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></h3>
<code><a href="../../BaseEmfUml2Helper.html#MAGICDRAW_SOURCE">MAGICDRAW_SOURCE</a>, <a href="../../BaseEmfUml2Helper.html#MD_ID">MD_ID</a>, <a href="../../BaseEmfUml2Helper.html#MD_PROPERTY_NAME">MD_PROPERTY_NAME</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger)">EmfUml2ExportHelper</a><wbr/>(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../EmfUml2PersistenceHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2PersistenceHelper</a> persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 <a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> emfOptionsGroup,
 <a href="../../EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a> logger)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseInteractionExportHelper</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInteractionExportHelper()">getInteractionExportHelper</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importDataTypePackages(org.eclipse.uml2_2_0_4.uml.Package)">importDataTypePackages</a><wbr/>(org.eclipse.uml2_2_0_4.uml.Package ePackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importPackage(org.eclipse.uml2_2_0_4.uml.Package,org.eclipse.uml2_2_0_4.uml.Package,java.lang.String)">importPackage</a><wbr/>(org.eclipse.uml2_2_0_4.uml.Package ePackage,
 org.eclipse.uml2_2_0_4.uml.Package eImport,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extra)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Imports package</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2Helper">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.v2.<a href="../EmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2Helper</a></h3>
<code><a href="../EmfUml2Helper.html#createDataTypeMap()">createDataTypeMap</a>, <a href="../EmfUml2Helper.html#createEElementNameRetriever()">createEElementNameRetriever</a>, <a href="../EmfUml2Helper.html#getElementClass()">getElementClass</a>, <a href="../EmfUml2Helper.html#getEmfOptionsGroup()">getEmfOptionsGroup</a>, <a href="../EmfUml2Helper.html#getEmfUml2StandardProfiles()">getEmfUml2StandardProfiles</a>, <a href="../EmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a>, <a href="../EmfUml2Helper.html#getNameStereotypeMap()">getNameStereotypeMap</a>, <a href="../EmfUml2Helper.html#getOptions()">getOptions</a>, <a href="../EmfUml2Helper.html#getStringPrimitiveType()">getStringPrimitiveType</a>, <a href="../EmfUml2Helper.html#getTemplateParameterHelper()">getTemplateParameterHelper</a>, <a href="../EmfUml2Helper.html#getUml2JavaPrimitiveTypesLibrary()">getUml2JavaPrimitiveTypesLibrary</a>, <a href="../EmfUml2Helper.html#getUml2MetaModel()">getUml2MetaModel</a>, <a href="../EmfUml2Helper.html#getUml2PrimitiveTypesLibrary()">getUml2PrimitiveTypesLibrary</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.<a href="../../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></h3>
<code><a href="../../BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a>, <a href="../../BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a>, <a href="../../BaseEmfUml2Helper.html#clearCreatedElementsIDData()">clearCreatedElementsIDData</a>, <a href="../../BaseEmfUml2Helper.html#getCreatedElementsIDData()">getCreatedElementsIDData</a>, <a href="../../BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="../../BaseEmfUml2Helper.html#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementName</a>, <a href="../../BaseEmfUml2Helper.html#getFinalizeActivities()">getFinalizeActivities</a>, <a href="../../BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="../../BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a>, <a href="../../BaseEmfUml2Helper.html#getMDStandardProfiles()">getMDStandardProfiles</a>, <a href="../../BaseEmfUml2Helper.html#getPersistenceHelper()">getPersistenceHelper</a>, <a href="../../BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="../../BaseEmfUml2Helper.html#getUml2DataTypeMap()">getUml2DataTypeMap</a>, <a href="../../BaseEmfUml2Helper.html#initProgressStatus(com.nomagic.task.ProgressStatus,java.lang.String,boolean)">initProgressStatus</a>, <a href="../../BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="../../BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="../../BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="../../BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="../../BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)">markRemovableElement</a>, <a href="../../BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a>, <a href="../../BaseEmfUml2Helper.html#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">removeElement</a>, <a href="../../BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger)">
<h3>EmfUml2ExportHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EmfUml2ExportHelper</span><wbr/><span class="parameters">(<a href="../../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="../EmfUml2PersistenceHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2PersistenceHelper</a> persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 <a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> emfOptionsGroup,
 <a href="../../EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a> logger)</span></div>
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
<section class="detail" id="getInteractionExportHelper()">
<h3>getInteractionExportHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseInteractionExportHelper</span> <span class="element-name">getInteractionExportHelper</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getInteractionExportHelper</code> in interface <code>com.nomagic.magicdraw.emfuml2xmi.export.InteractionExportHelperProvider</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importPackage(org.eclipse.uml2_2_0_4.uml.Package,org.eclipse.uml2_2_0_4.uml.Package,java.lang.String)">
<h3>importPackage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">importPackage</span><wbr/><span class="parameters">(org.eclipse.uml2_2_0_4.uml.Package ePackage,
 org.eclipse.uml2_2_0_4.uml.Package eImport,
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
<section class="detail" id="importDataTypePackages(org.eclipse.uml2_2_0_4.uml.Package)">
<h3>importDataTypePackages</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">importDataTypePackages</span><wbr/><span class="parameters">(org.eclipse.uml2_2_0_4.uml.Package ePackage)</span></div>
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
