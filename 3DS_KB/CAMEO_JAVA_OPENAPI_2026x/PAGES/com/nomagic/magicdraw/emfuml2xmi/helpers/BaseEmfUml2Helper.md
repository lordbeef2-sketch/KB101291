# JAVA OPENAPI: BaseEmfUml2Helper (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/emfuml2xmi/helpers/BaseEmfUml2Helper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/helpers/BaseEmfUml2Helper.html`
- source_sha256: `734d5d6e33910f23eaa90baa94da1819185ad9598d4f4314790cb148d3d9b194`
- captured_utc: `2026-07-14T16:57:56.132514+00:00`

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
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getEElementName](#getEElementName(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eElement)`
Returns element human name.
`[EmfUml2Logger](../EmfUml2Logger.html)`
`[getLogger](#getLogger())()`
Returns logger.
`[Project](../../core/Project.html)`
`[getProject](#getProject())()`
Returns current project
`boolean`
`[isMappedElement](#isMappedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)`
Checks if given element is mapped.
`boolean`
`[isRemovableElement](#isRemovableElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)`
Checks if element will be removed or already disposed.
`boolean`
`[isSkippedElement](#isSkippedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)`
Checks if given element is skipped.
`void`
`[markMappedElement](#markMappedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)`
Marks that element is mapped.
`void`
`[markSkippedElement](#markSkippedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)`
Mark skipped element.

============ METHOD DETAIL ========== 
Method Details
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
@OpenApivoid markMappedElement([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)
Marks that element is mapped.
 Mapped element - element is not created, but used in UML2 model.
Parameters:
`element` -
isMappedElement
@OpenApiboolean isMappedElement([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is mapped.
Parameters:
`element` -
Returns:
true - if mapped.
markSkippedElement
@OpenApivoid markSkippedElement([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)
Mark skipped element.
Parameters:
`element` -
isRemovableElement
@OpenApiboolean isRemovableElement([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)
Checks if element will be removed or already disposed.
 Element can be disposed if during export/import differs composite reference multiplicity (* to 1)
Parameters:
`element` -
Returns:
true - if will element should be removed or are alredy removed.
isSkippedElement
@OpenApiboolean isSkippedElement([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is skipped.
Parameters:
`element` -
getEElementName
@OpenApi[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getEElementName([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eElement)
Returns element human name.
Specified by:
`[getEElementName](BaseEElementNameRetriever.html#getEElementName(java.lang.Object))` in interface `[BaseEElementNameRetriever](BaseEElementNameRetriever.html)`
Parameters:
`eElement` -
Returns:
element type + qualified name

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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEElementName(java.lang.Object)">getEElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns element human name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLogger()">getLogger</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns logger.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns current project</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isMappedElement(java.lang.Object)">isMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if given element is mapped.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isRemovableElement(java.lang.Object)">isRemovableElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if element will be removed or already disposed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isSkippedElement(java.lang.Object)">isSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if given element is skipped.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#markMappedElement(java.lang.Object)">markMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Marks that element is mapped.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#markSkippedElement(java.lang.Object)">markSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Mark skipped element.</div>
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
</span><span class="return-type">void</span> <span class="element-name">markMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
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
</span><span class="return-type">boolean</span> <span class="element-name">isMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
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
</span><span class="return-type">void</span> <span class="element-name">markSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
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
</span><span class="return-type">boolean</span> <span class="element-name">isRemovableElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
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
<section class="detail" id="isSkippedElement(java.lang.Object)">
<h3>isSkippedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if given element is skipped.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEElementName(java.lang.Object)">
<h3>getEElementName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</span></div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
