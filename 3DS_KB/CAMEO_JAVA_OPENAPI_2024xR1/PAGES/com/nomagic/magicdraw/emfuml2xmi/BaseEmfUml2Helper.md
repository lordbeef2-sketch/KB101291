# JAVA OPENAPI: BaseEmfUml2Helper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2Helper.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/BaseEmfUml2Helper.html`
- source_sha256: `2645fdf69ea7aa66df8c8f3f2c1afc373401be231d91b69dd67d5ef8f9ad18c6`
- captured_utc: `2026-07-14T16:51:18.699171+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi](package-summary.html)

## Class BaseEmfUml2Helper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper

All Implemented Interfaces:
`[BaseEElementNameRetriever](helpers/BaseEElementNameRetriever.html)`, `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`

Direct Known Subclasses:
`[EmfUml2Helper](v2/EmfUml2Helper.html)`

@OpenApipublic abstract classBaseEmfUml2Helper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)

Eclipse UML2 XMI helper.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getEElementName](#getEElementName(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)`
Returns element human name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getElementName](#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 boolean qualifiedName)`
Returns element human name.
`[EmfUml2Logger](EmfUml2Logger.html)`
`[getLogger](#getLogger())()`
Returns logger.
`[Project](../core/Project.html)`
`[getProject](#getProject())()`
Returns current project
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
`[markSkippedElement](#markSkippedElement(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)`
Mark skipped element.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getProject
@OpenApipublic [Project](../core/Project.html) getProject()
Returns current project
Specified by:
`[getProject](helpers/BaseEmfUml2Helper.html#getProject())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Returns:
project
getLogger
@OpenApipublic [EmfUml2Logger](EmfUml2Logger.html) getLogger()
Returns logger.
Specified by:
`[getLogger](helpers/BaseEmfUml2Helper.html#getLogger())` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Returns:
logger
markMappedElement
@OpenApipublic void markMappedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Marks that element is mapped.
 Mapped element - element is not created, but used in UML2 model.
Specified by:
`[markMappedElement](helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
isMappedElement
@OpenApipublic boolean isMappedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is mapped.
Specified by:
`[isMappedElement](helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
Returns:
true - if mapped.
markSkippedElement
@OpenApipublic void markSkippedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Mark skipped element.
Specified by:
`[markSkippedElement](helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
isRemovableElement
@OpenApipublic boolean isRemovableElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if element will be removed or already disposed.
 Element can be disposed if during export/import differs composite reference multiplicity (* to 1)
Specified by:
`[isRemovableElement](helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
Returns:
true - if will element should be removed or are alredy removed.
isSkippedElement
@OpenApipublic boolean isSkippedElement([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) element)
Checks if given element is skipped.
Specified by:
`[isSkippedElement](helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
Parameters:
`element` -
getElementName
@OpenApipublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getElementName([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) mdElement,
 boolean qualifiedName)
Returns element human name.
Parameters:
`mdElement` -
`qualifiedName` -
Returns:
element type + [qualified] name
getEElementName
@OpenApipublic final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getEElementName([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) eElement)
Returns element human name.
Specified by:
`[getEElementName](helpers/BaseEElementNameRetriever.html#getEElementName(java.lang.Object))` in interface `[BaseEElementNameRetriever](helpers/BaseEElementNameRetriever.html)`
Specified by:
`[getEElementName](helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object))` in interface `[BaseEmfUml2Helper](helpers/BaseEmfUml2Helper.html)`
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi</a></div>
<h1 class="title" title="Class BaseEmfUml2Helper">Class BaseEmfUml2Helper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.BaseEmfUml2Helper</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code>, <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="v2/EmfUml2Helper.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2">EmfUml2Helper</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">BaseEmfUml2Helper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></span></div>
<div class="block">Eclipse UML2 XMI helper.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEElementName(java.lang.Object)">getEElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns element human name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">getElementName</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 boolean qualifiedName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns element human name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLogger()">getLogger</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns logger.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns current project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMappedElement(java.lang.Object)">isMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element is mapped.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isRemovableElement(java.lang.Object)">isRemovableElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if element will be removed or already disposed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSkippedElement(java.lang.Object)">isSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if given element is skipped.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#markMappedElement(java.lang.Object)">markMappedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks that element is mapped.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#markSkippedElement(java.lang.Object)">markSkippedElement</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Mark skipped element.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Returns current project</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getProject()">getProject</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
<dd>project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLogger()">
<h3>getLogger</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="EmfUml2Logger.html" title="interface in com.nomagic.magicdraw.emfuml2xmi">EmfUml2Logger</a></span> <span class="element-name">getLogger</span>()</div>
<div class="block">Returns logger.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getLogger()">getLogger</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Returns:</dt>
<dd>logger</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="markMappedElement(java.lang.Object)">
<h3>markMappedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">markMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Marks that element is mapped.
 Mapped element - element is not created, but used in UML2 model.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#markMappedElement(java.lang.Object)">markMappedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMappedElement(java.lang.Object)">
<h3>isMappedElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMappedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if given element is mapped.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#isMappedElement(java.lang.Object)">isMappedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">markSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Mark skipped element.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#markSkippedElement(java.lang.Object)">markSkippedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRemovableElement(java.lang.Object)">
<h3>isRemovableElement</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRemovableElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if element will be removed or already disposed.
 Element can be disposed if during export/import differs composite reference multiplicity (* to 1)</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#isRemovableElement(java.lang.Object)">isRemovableElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
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
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSkippedElement</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> element)</span></div>
<div class="block">Checks if given element is skipped.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#isSkippedElement(java.lang.Object)">isSkippedElement</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
<dt>Parameters:</dt>
<dd><code>element</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementName(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>getElementName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getElementName</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> mdElement,
 boolean qualifiedName)</span></div>
<div class="block">Returns element human name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mdElement</code> - </dd>
<dd><code>qualifiedName</code> - </dd>
<dt>Returns:</dt>
<dd>element type + [qualified] name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEElementName(java.lang.Object)">
<h3>getEElementName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> eElement)</span></div>
<div class="block">Returns element human name.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEElementNameRetriever.html#getEElementName(java.lang.Object)">getEElementName</a></code> in interface <code><a href="helpers/BaseEElementNameRetriever.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEElementNameRetriever</a></code></dd>
<dt>Specified by:</dt>
<dd><code><a href="helpers/BaseEmfUml2Helper.html#getEElementName(java.lang.Object)">getEElementName</a></code> in interface <code><a href="helpers/BaseEmfUml2Helper.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.helpers">BaseEmfUml2Helper</a></code></dd>
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
