# JAVA OPENAPI: EmfUml2Helper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2Helper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/EmfUml2Helper.html`
- source_sha256: `69841e41351eec8add665daa7a0142fa82d592c4d750aab7cb1bbcf1d724fde7`
- captured_utc: `2026-07-14T16:55:18.801048+00:00`

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

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)
`[MAGICDRAW_SOURCE](../BaseEmfUml2Helper.html#MAGICDRAW_SOURCE), [MD_ID](../BaseEmfUml2Helper.html#MD_ID), [MD_PROPERTY_NAME](../BaseEmfUml2Helper.html#MD_PROPERTY_NAME)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EmfUml2Helper](#%3Cinit%3E(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger))([Project](../../core/Project.html) project,
 [EmfUml2PersistenceHelper](EmfUml2PersistenceHelper.html) persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 [BaseEmfOptionsGroup](../envoptions/BaseEmfOptionsGroup.html) emfOptionsGroup,
 [EmfUml2Logger](../EmfUml2Logger.html) logger)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap`
`[createDataTypeMap](#createDataTypeMap())()`

`protected [BaseEElementNameRetriever](../helpers/BaseEElementNameRetriever.html)`
`[createEElementNameRetriever](#createEElementNameRetriever())()`

`org.eclipse.uml2_2_0_4.uml.Type`
`[getElementClass](#getElementClass())()`
Returns Element type of Eclipse UML2 metamodel.
`[EmfOptionsGroup](envoptions/EmfOptionsGroup.html)`
`[getEmfOptionsGroup](#getEmfOptionsGroup())()`

`org.eclipse.uml2_2_0_4.uml.Profile`
`[getEmfUml2StandardProfiles](#getEmfUml2StandardProfiles())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[getMagicDrawAnnotationDetails](#getMagicDrawAnnotationDetails(java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getNameStereotypeMap](#getNameStereotypeMap())()`
Get standard Eclipse UML2 stereotypes names map.
`[Options](envoptions/Options.html)`
`[getOptions](#getOptions())()`

`org.eclipse.uml2_2_0_4.uml.Type`
`[getStringPrimitiveType](#getStringPrimitiveType())()`
Returns String type of Eclipse UML2 metamodel.
`com.nomagic.magicdraw.emfuml2xmi.v2.helpers.TemplateParameterHelper`
`[getTemplateParameterHelper](#getTemplateParameterHelper())()`

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
`[addCreatedElementIDData](../BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)), [addFinalizeActivity](../BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)), [clearCreatedElementsIDData](../BaseEmfUml2Helper.html#clearCreatedElementsIDData()), [getCreatedElementsIDData](../BaseEmfUml2Helper.html#getCreatedElementsIDData()), [getEElementName](../BaseEmfUml2Helper.html#getEElementName(java.lang.Object)), [getElementName](../BaseEmfUml2Helper.html#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)), [getFinalizeActivities](../BaseEmfUml2Helper.html#getFinalizeActivities()), [getLogger](../BaseEmfUml2Helper.html#getLogger()), [getMDProjectBuiltinProfiles](../BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()), [getMDStandardProfiles](../BaseEmfUml2Helper.html#getMDStandardProfiles()), [getPersistenceHelper](../BaseEmfUml2Helper.html#getPersistenceHelper()), [getProject](../BaseEmfUml2Helper.html#getProject()), [getUml2DataTypeMap](../BaseEmfUml2Helper.html#getUml2DataTypeMap()), [initProgressStatus](../BaseEmfUml2Helper.html#initProgressStatus(com.nomagic.task.ProgressStatus,java.lang.String,boolean)), [isMappedElement](../BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)), [isRemovableElement](../BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)), [isSkippedElement](../BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)), [markMappedElement](../BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)), [markRemovableElement](../BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)), [markSkippedElement](../BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)), [removeElement](../BaseEmfUml2Helper.html#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)), [setMDElementID](../BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EmfUml2Helper
public EmfUml2Helper([Project](../../core/Project.html) project,
 [EmfUml2PersistenceHelper](EmfUml2PersistenceHelper.html) persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 [BaseEmfOptionsGroup](../envoptions/BaseEmfOptionsGroup.html) emfOptionsGroup,
 [EmfUml2Logger](../EmfUml2Logger.html) logger)
 ============ METHOD DETAIL ========== 
Method Details
createDataTypeMap
protected com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap createDataTypeMap()
Specified by:
`[createDataTypeMap](../BaseEmfUml2Helper.html#createDataTypeMap())` in class `[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`
getMagicDrawAnnotationDetails
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) getMagicDrawAnnotationDetails([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)
Specified by:
`[getMagicDrawAnnotationDetails](../helpers/BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean))` in interface `[BaseEmfUml2Helper](../helpers/BaseEmfUml2Helper.html)`
Specified by:
`[getMagicDrawAnnotationDetails](../BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean))` in class `[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`
getUml2MetaModel
@OpenApipublic org.eclipse.uml2_2_0_4.uml.Model getUml2MetaModel()
Returns model of Eclipse UML2 metamodel.
Specified by:
`[getUml2MetaModel](../BaseEmfUml2Helper.html#getUml2MetaModel())` in class `[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`
Returns:
Eclipse UML2 metamodel model
getEmfUml2StandardProfiles
public org.eclipse.uml2_2_0_4.uml.Profile getEmfUml2StandardProfiles()
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
getEmfOptionsGroup
public [EmfOptionsGroup](envoptions/EmfOptionsGroup.html) getEmfOptionsGroup()
Overrides:
`[getEmfOptionsGroup](../BaseEmfUml2Helper.html#getEmfOptionsGroup())` in class `[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`
Returns:
getOptions
public [Options](envoptions/Options.html) getOptions()
Specified by:
`[getOptions](../helpers/BaseEmfUml2Helper.html#getOptions())` in interface `[BaseEmfUml2Helper](../helpers/BaseEmfUml2Helper.html)`
Overrides:
`[getOptions](../BaseEmfUml2Helper.html#getOptions())` in class `[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`
createEElementNameRetriever
protected [BaseEElementNameRetriever](../helpers/BaseEElementNameRetriever.html) createEElementNameRetriever()
Specified by:
`[createEElementNameRetriever](../BaseEmfUml2Helper.html#createEElementNameRetriever())` in class `[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`
getTemplateParameterHelper
public com.nomagic.magicdraw.emfuml2xmi.v2.helpers.TemplateParameterHelper getTemplateParameterHelper()
getNameStereotypeMap
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getNameStereotypeMap()
Get standard Eclipse UML2 stereotypes names map.
Returns:
name->Stereotype map.

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
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper">Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.<a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></h3>
<code><a href="../BaseEmfUml2Helper.html#MAGICDRAW_SOURCE">MAGICDRAW_SOURCE</a>, <a href="../BaseEmfUml2Helper.html#MD_ID">MD_ID</a>, <a href="../BaseEmfUml2Helper.html#MD_PROPERTY_NAME">MD_PROPERTY_NAME</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.emfuml2xmi.v2.EmfUml2PersistenceHelper,com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager,com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup,com.nomagic.magicdraw.emfuml2xmi.EmfUml2Logger)">EmfUml2Helper</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="EmfUml2PersistenceHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2PersistenceHelper</a> persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 <a href="../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> emfOptionsGroup,
 <a href="../EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a> logger)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDataTypeMap()">createDataTypeMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createEElementNameRetriever()">createEElementNameRetriever</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Type</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementClass()">getElementClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns Element type of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="envoptions/EmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">EmfOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEmfOptionsGroup()">getEmfOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Profile</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEmfUml2StandardProfiles()">getEmfUml2StandardProfiles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNameStereotypeMap()">getNameStereotypeMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get standard Eclipse UML2 stereotypes names map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="envoptions/Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.eclipse.uml2_2_0_4.uml.Type</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStringPrimitiveType()">getStringPrimitiveType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns String type of Eclipse UML2 metamodel.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.emfuml2xmi.v2.helpers.TemplateParameterHelper</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateParameterHelper()">getTemplateParameterHelper</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<code><a href="../BaseEmfUml2Helper.html#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a>, <a href="../BaseEmfUml2Helper.html#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a>, <a href="../BaseEmfUml2Helper.html#clearCreatedElementsIDData()">clearCreatedElementsIDData</a>, <a href="../BaseEmfUml2Helper.html#getCreatedElementsIDData()">getCreatedElementsIDData</a>, <a href="../BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a>, <a href="../BaseEmfUml2Helper.html#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementName</a>, <a href="../BaseEmfUml2Helper.html#getFinalizeActivities()">getFinalizeActivities</a>, <a href="../BaseEmfUml2Helper.html#getLogger()">getLogger</a>, <a href="../BaseEmfUml2Helper.html#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a>, <a href="../BaseEmfUml2Helper.html#getMDStandardProfiles()">getMDStandardProfiles</a>, <a href="../BaseEmfUml2Helper.html#getPersistenceHelper()">getPersistenceHelper</a>, <a href="../BaseEmfUml2Helper.html#getProject()">getProject</a>, <a href="../BaseEmfUml2Helper.html#getUml2DataTypeMap()">getUml2DataTypeMap</a>, <a href="../BaseEmfUml2Helper.html#initProgressStatus(com.nomagic.task.ProgressStatus,java.lang.String,boolean)">initProgressStatus</a>, <a href="../BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a>, <a href="../BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a>, <a href="../BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a>, <a href="../BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a>, <a href="../BaseEmfUml2Helper.html#markRemovableElement(java.lang.Object)">markRemovableElement</a>, <a href="../BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a>, <a href="../BaseEmfUml2Helper.html#removeElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Collection)">removeElement</a>, <a href="../BaseEmfUml2Helper.html#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a></code></div>
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
<h3>EmfUml2Helper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EmfUml2Helper</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="EmfUml2PersistenceHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2PersistenceHelper</a> persistenceHelper,
 com.nomagic.magicdraw.emfuml2xmi.export.BaseEmfUml2IDManager idManager,
 <a href="../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> emfOptionsGroup,
 <a href="../EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a> logger)</span></div>
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
<section class="detail" id="createDataTypeMap()">
<h3>createDataTypeMap</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</span> <span class="element-name">createDataTypeMap</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html#createDataTypeMap()">createDataTypeMap</a></code> in class <code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMagicDrawAnnotationDetails(java.lang.Object,boolean)">
<h3>getMagicDrawAnnotationDetails</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getMagicDrawAnnotationDetails</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../helpers/BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a></code> in interface <code><a href="../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a></code> in class <code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUml2MetaModel()">
<h3>getUml2MetaModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Model</span> <span class="element-name">getUml2MetaModel</span>()</div>
<div class="block">Returns model of Eclipse UML2 metamodel.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html#getUml2MetaModel()">getUml2MetaModel</a></code> in class <code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
<dd>Eclipse UML2 metamodel model</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEmfUml2StandardProfiles()">
<h3>getEmfUml2StandardProfiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.eclipse.uml2_2_0_4.uml.Profile</span> <span class="element-name">getEmfUml2StandardProfiles</span>()</div>
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
<li>
<section class="detail" id="getEmfOptionsGroup()">
<h3>getEmfOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="envoptions/EmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">EmfOptionsGroup</a></span> <span class="element-name">getEmfOptionsGroup</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html#getEmfOptionsGroup()">getEmfOptionsGroup</a></code> in class <code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="envoptions/Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></span> <span class="element-name">getOptions</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../helpers/BaseEmfUml2Helper.html#getOptions()">getOptions</a></code> in interface <code><a href="../helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html#getOptions()">getOptions</a></code> in class <code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createEElementNameRetriever()">
<h3>createEElementNameRetriever</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></span> <span class="element-name">createEElementNameRetriever</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html#createEElementNameRetriever()">createEElementNameRetriever</a></code> in class <code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateParameterHelper()">
<h3>getTemplateParameterHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.v2.helpers.TemplateParameterHelper</span> <span class="element-name">getTemplateParameterHelper</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNameStereotypeMap()">
<h3>getNameStereotypeMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getNameStereotypeMap</span>()</div>
<div class="block">Get standard Eclipse UML2 stereotypes names map.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name-&gt;Stereotype map.</dd>
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
