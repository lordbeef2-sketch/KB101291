# JAVA OPENAPI: BaseEmfUml2Helper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/helpers/BaseEmfUml2Helper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/helpers/BaseEmfUml2Helper.html`
- source_sha256: `2d0e8da5cfda0dacdcf5f3dd7dfab6891a68e5fde991f4cbf3b95a4d38cfaac0`
- captured_utc: `2026-07-14T16:55:18.183039+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.helpers](package-summary.html)

## Interface BaseEmfUml2Helper

All Superinterfaces:
`[BaseEElementNameRetriever](BaseEElementNameRetriever.html)`

All Known Subinterfaces:
`[EmfUml2ExportHelper](EmfUml2ExportHelper.html)`, `[EmfUml2ExportHelper](../v4/helpers/EmfUml2ExportHelper.html)`, `[EmfUml2ExportHelper](../v5/helpers/EmfUml2ExportHelper.html)`, `[EmfUml2Helper](EmfUml2Helper.html)`, `[EmfUml2Helper](../v4/helpers/EmfUml2Helper.html)`, `[EmfUml2Helper](../v5/helpers/EmfUml2Helper.html)`, `[EmfUml2ImportHelper](../imp0rt/EmfUml2ImportHelper.html)`, `[EmfUml2ImportHelper](../v4/imp0rt/EmfUml2ImportHelper.html)`, `[EmfUml2ImportHelper](../v5/imp0rt/EmfUml2ImportHelper.html)`

All Known Implementing Classes:
`[BaseEmfUml2Helper](../BaseEmfUml2Helper.html)`, `[EmfUml2ExportHelper](../v2/export/EmfUml2ExportHelper.html)`, `[EmfUml2Helper](../v2/EmfUml2Helper.html)`, `[EmfUml2ImportHelper](../v2/imp0rt/EmfUml2ImportHelper.html)`

@OpenApipublic interfaceBaseEmfUml2Helperextends [BaseEElementNameRetriever](BaseEElementNameRetriever.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[addCreatedElementIDData](#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) createdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) relatedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)`

`void`
`[addFinalizeActivity](#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity))([FinalizeActivity](../FinalizeActivity.html) activity)`

`void`
`[clearCreatedElementsIDData](#clearCreatedElementsIDData())()`

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[getCreatedElementsIDData](#getCreatedElementsIDData())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEElementName](#getEElementName(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)`
Returns element human name.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FinalizeActivity](../FinalizeActivity.html)>`
`[getFinalizeActivities](#getFinalizeActivities())()`

`[EmfUml2Logger](../EmfUml2Logger.html)`
`[getLogger](#getLogger())()`
Returns logger.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`
`[getMagicDrawAnnotationDetails](#getMagicDrawAnnotationDetails(java.lang.Object,boolean))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getMDProjectBuiltinProfiles](#getMDProjectBuiltinProfiles())()`
Returns profiles that are "built-in" in MagicDraw project
`[BaseOptions](../envoptions/BaseOptions.html)`
`[getOptions](#getOptions())()`

`com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper`
`[getPersistenceHelper](#getPersistenceHelper())()`

`[Project](../../core/Project.html)`
`[getProject](#getProject())()`
Returns current project
`com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap`
`[getUml2DataTypeMap](#getUml2DataTypeMap())()`
Returns datatype map
`boolean`
`[isMappedElement](#isMappedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Checks if given element is mapped.
`boolean`
`[isRemovableElement](#isRemovableElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Checks if element will be removed or already disposed.
`boolean`
`[isSkippedElement](#isSkippedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Checks if given element is skipped.
`void`
`[markMappedElement](#markMappedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Marks that element is mapped.
`void`
`[markRemovableElement](#markRemovableElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Mark element that will be removed or already disposed
`void`
`[markSkippedElement](#markSkippedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Mark skipped element.
`void`
`[setMDElementID](#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object))([BaseElement](../../uml/BaseElement.html) mdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)`
Set MD element id according given EMF element id.

============ METHOD DETAIL ========== 
Method Details
getUml2DataTypeMap
com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap getUml2DataTypeMap()
Returns datatype map
Returns:
datatypes map
getMagicDrawAnnotationDetails
[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) getMagicDrawAnnotationDetails([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement,
 boolean create)
getProject
@OpenApi[Project](../../core/Project.html) getProject()
Returns current project
Returns:
project
getLogger
@OpenApi[EmfUml2Logger](../EmfUml2Logger.html) getLogger()
Returns logger.
Returns:
logger
markMappedElement
@OpenApivoid markMappedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Marks that element is mapped.
 Mapped element - element is not created, but used in UML2 model.
Parameters:
`element` -
isMappedElement
@OpenApiboolean isMappedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is mapped.
Parameters:
`element` -
Returns:
true - if mapped.
markSkippedElement
@OpenApivoid markSkippedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Mark skipped element.
Parameters:
`element` -
isRemovableElement
@OpenApiboolean isRemovableElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if element will be removed or already disposed.
 Element can be disposed if during export/import differs composite reference multiplicity (* to 1)
Parameters:
`element` -
Returns:
true - if will element should be removed or are alredy removed.
markRemovableElement
void markRemovableElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Mark element that will be removed or already disposed
Parameters:
`element` -
getFinalizeActivities
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[FinalizeActivity](../FinalizeActivity.html)> getFinalizeActivities()
isSkippedElement
@OpenApiboolean isSkippedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is skipped.
Parameters:
`element` -
getPersistenceHelper
com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper getPersistenceHelper()
addCreatedElementIDData
void addCreatedElementIDData([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) createdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) relatedElement,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extra)
getCreatedElementsIDData
[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html) getCreatedElementsIDData()
clearCreatedElementsIDData
void clearCreatedElementsIDData()
setMDElementID
void setMDElementID([BaseElement](../../uml/BaseElement.html) mdElement,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)
Set MD element id according given EMF element id. If there is id's conflict id is not changed.
Parameters:
`mdElement` - MD element
`eElement` - EMF element
getOptions
[BaseOptions](../envoptions/BaseOptions.html) getOptions()
getEElementName
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEElementName([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)
Returns element human name.
Specified by:
`[getEElementName](BaseEElementNameRetriever.html#getEElementName(java.lang.Object))` in interface `[BaseEElementNameRetriever](BaseEElementNameRetriever.html)`
Parameters:
`eElement` -
Returns:
element type + qualified name
getMDProjectBuiltinProfiles
[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getMDProjectBuiltinProfiles()
Returns profiles that are "built-in" in MagicDraw project
Returns:
addFinalizeActivity
void addFinalizeActivity([FinalizeActivity](../FinalizeActivity.html) activity)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.helpers</a></div>
<h1 class="title" title="Interface BaseEmfUml2Helper">Interface BaseEmfUml2Helper</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2ExportHelper</a></code>, <code><a href="../v4/helpers/EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2ExportHelper</a></code>, <code><a href="../v5/helpers/EmfUml2ExportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2ExportHelper</a></code>, <code><a href="EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">EmfUml2Helper</a></code>, <code><a href="../v4/helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.helpers">EmfUml2Helper</a></code>, <code><a href="../v5/helpers/EmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.helpers">EmfUml2Helper</a></code>, <code><a href="../imp0rt/EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.imp0rt">EmfUml2ImportHelper</a></code>, <code><a href="../v4/imp0rt/EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v4.imp0rt">EmfUml2ImportHelper</a></code>, <code><a href="../v5/imp0rt/EmfUml2ImportHelper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v5.imp0rt">EmfUml2ImportHelper</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="../BaseEmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi">BaseEmfUml2Helper</a></code>, <code><a href="../v2/export/EmfUml2ExportHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.export">EmfUml2ExportHelper</a></code>, <code><a href="../v2/EmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2Helper</a></code>, <code><a href="../v2/imp0rt/EmfUml2ImportHelper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.imp0rt">EmfUml2ImportHelper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BaseEmfUml2Helper</span><span class="extends-implements">
extends <a href="BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></span></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">addCreatedElementIDData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> createdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> relatedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extra)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">addFinalizeActivity</a><wbr/>(<a href="../FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#clearCreatedElementsIDData()">clearCreatedElementsIDData</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCreatedElementsIDData()">getCreatedElementsIDData</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEElementName(java.lang.Object)">getEElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns element human name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getFinalizeActivities()">getFinalizeActivities</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLogger()">getLogger</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns logger.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMagicDrawAnnotationDetails(java.lang.Object,boolean)">getMagicDrawAnnotationDetails</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMDProjectBuiltinProfiles()">getMDProjectBuiltinProfiles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns profiles that are "built-in" in MagicDraw project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOptions()">getOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPersistenceHelper()">getPersistenceHelper</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns current project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getUml2DataTypeMap()">getUml2DataTypeMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns datatype map</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isMappedElement(java.lang.Object)">isMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if given element is mapped.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isRemovableElement(java.lang.Object)">isRemovableElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if element will be removed or already disposed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSkippedElement(java.lang.Object)">isSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if given element is skipped.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#markMappedElement(java.lang.Object)">markMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Marks that element is mapped.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#markRemovableElement(java.lang.Object)">markRemovableElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Mark element that will be removed or already disposed</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#markSkippedElement(java.lang.Object)">markSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Mark skipped element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">setMDElementID</a><wbr/>(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> mdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set MD element id according given EMF element id.</div>
</div>
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
<section class="detail" id="getUml2DataTypeMap()">
<h3>getUml2DataTypeMap</h3>
<div class="member-signature"><span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2DataTypeMap</span> <span class="element-name">getUml2DataTypeMap</span>()</div>
<div class="block">Returns datatype map</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>datatypes map</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMagicDrawAnnotationDetails(java.lang.Object,boolean)">
<h3>getMagicDrawAnnotationDetails</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getMagicDrawAnnotationDetails</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement,
 boolean create)</span></div>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Returns current project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLogger()">
<h3>getLogger</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a href="../EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a></span> <span class="element-name">getLogger</span>()</div>
<div class="block">Returns logger.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>logger</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markMappedElement(java.lang.Object)">
<h3>markMappedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">markMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Marks that element is mapped.
 Mapped element - element is not created, but used in UML2 model.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMappedElement(java.lang.Object)">
<h3>isMappedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if given element is mapped.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
<dt>Returns:</dt>
<dd>true - if mapped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markSkippedElement(java.lang.Object)">
<h3>markSkippedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">markSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Mark skipped element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemovableElement(java.lang.Object)">
<h3>isRemovableElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isRemovableElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if element will be removed or already disposed.
 Element can be disposed if during export/import differs composite reference multiplicity (* to 1)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
<dt>Returns:</dt>
<dd>true - if will element should be removed or are alredy removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markRemovableElement(java.lang.Object)">
<h3>markRemovableElement</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">markRemovableElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Mark element that will be removed or already disposed</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFinalizeActivities()">
<h3>getFinalizeActivities</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a>&gt;</span> <span class="element-name">getFinalizeActivities</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isSkippedElement(java.lang.Object)">
<h3>isSkippedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if given element is skipped.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPersistenceHelper()">
<h3>getPersistenceHelper</h3>
<div class="member-signature"><span class="return-type">com.nomagic.magicdraw.emfuml2xmi.helpers.BaseEmfUml2PersistenceHelper</span> <span class="element-name">getPersistenceHelper</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addCreatedElementIDData(java.lang.Object,java.lang.Object,java.lang.String)">
<h3>addCreatedElementIDData</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addCreatedElementIDData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> createdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> relatedElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extra)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCreatedElementsIDData()">
<h3>getCreatedElementsIDData</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a></span> <span class="element-name">getCreatedElementsIDData</span>()</div>
</section>
</li>
<li>
<section class="detail" id="clearCreatedElementsIDData()">
<h3>clearCreatedElementsIDData</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">clearCreatedElementsIDData</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setMDElementID(com.nomagic.magicdraw.uml.BaseElement,java.lang.Object)">
<h3>setMDElementID</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMDElementID</span><wbr/><span class="parameters">(<a href="../../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> mdElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</span></div>
<div class="block">Set MD element id according given EMF element id. If there is id's conflict id is not changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdElement</code> - MD element</dd>
<dd><code>eElement</code> - EMF element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptions()">
<h3>getOptions</h3>
<div class="member-signature"><span class="return-type"><a href="../envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></span> <span class="element-name">getOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getEElementName(java.lang.Object)">
<h3>getEElementName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</span></div>
<div class="block">Returns element human name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseEElementNameRetriever.html#getEElementName(java.lang.Object)">getEElementName</a></code> in interface <code><a href="BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code></dd>
<dt>Parameters:</dt>
<dd><code>eElement</code> - </dd>
<dt>Returns:</dt>
<dd>element type + qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMDProjectBuiltinProfiles()">
<h3>getMDProjectBuiltinProfiles</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getMDProjectBuiltinProfiles</span>()</div>
<div class="block">Returns profiles that are "built-in" in MagicDraw project</div>
<dl class="notes">
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFinalizeActivity(com.nomagic.magicdraw.emfuml2xmi.FinalizeActivity)">
<h3>addFinalizeActivity</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addFinalizeActivity</span><wbr/><span class="parameters">(<a href="../FinalizeActivity.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">FinalizeActivity</a> activity)</span></div>
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
