# JAVA OPENAPI: ExtractSource (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/refactor/extract/ExtractSource.html
- source_path: `com/nomagic/magicdraw/uml/refactor/extract/ExtractSource.html`
- source_sha256: `37eeaab574312004879d3868c2af60d14b3d2ddb511685d02b7ce021ae02c8e3`
- captured_utc: `2026-07-14T16:55:54.405447+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.refactor.extract](package-summary.html)

## Interface ExtractSource

@OpenApiAllpublic interfaceExtractSource

Represents the source model end of the extract refactoring.

See Also:
[`ExtractManager`](ExtractManager.html)
[`ExtractTarget`](ExtractTarget.html)
[`Refactoring.Extracting`](../../Refactoring.Extracting.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Gets element which was created in the extract refactor source after refactoring.
`void`
`[setElementName](#setElementName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)`
Sets name of the element which will be created in the extract refactor source.

============ METHOD DETAIL ========== 
Method Details
setElementName
void setElementName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) elementName)
Sets name of the element which will be created in the extract refactor source.
Parameters:
`elementName` - name of the extract refactor source.
getElement
[Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Gets element which was created in the extract refactor source after refactoring.
Returns:
refactored element in the source if called after refactoring, null if called before refactoring.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.refactor.extract</a></div>
<h1 class="title" title="Interface ExtractSource">Interface ExtractSource</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ExtractSource</span></div>
<div class="block">Represents the source model end of the extract refactoring.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ExtractManager.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractManager</code></a></li>
<li><a href="ExtractTarget.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractTarget</code></a></li>
<li><a href="../../Refactoring.Extracting.html" title="class in com.nomagic.magicdraw.uml"><code>Refactoring.Extracting</code></a></li>
</ul>
</dd>
</dl>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets element which was created in the extract refactor source after refactoring.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setElementName(java.lang.String)">setElementName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets name of the element which will be created in the extract refactor source.</div>
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
<section class="detail" id="setElementName(java.lang.String)">
<h3>setElementName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setElementName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementName)</span></div>
<div class="block">Sets name of the element which will be created in the extract refactor source.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementName</code> - name of the extract refactor source.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="return-type"><a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Gets element which was created in the extract refactor source after refactoring.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>refactored element in the source if called after refactoring, null if called before refactoring.</dd>
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
